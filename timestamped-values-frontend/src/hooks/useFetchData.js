import { useState, useEffect, useCallback } from "react";
import axios from "axios";

const useFetchData = (initialYear, initialMonth) => {
  const [data, setData] = useState(null);
  const [years, setYears] = useState([]);
  const [nextPage, setNextPage] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const months = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
  ];

  // Get the API URL from environment variable
  const apiUrl =
    process.env.REACT_APP_API_URL ||
    "http://localhost:8000/candidate_test/fronted/";

  // Function to fetch data
  const fetchData = useCallback(
    async (
      selectedYear = "",
      selectedMonth = "",
      url = apiUrl
  ) => {
    setLoading(true);
    setError(null);

    let apiUrlWithParams = url;
    const params = new URLSearchParams();

    if (selectedYear) {
      params.append("year", selectedYear);
    }
    if (selectedMonth) {
      params.append("month", selectedMonth);
    }

    const queryString = params.toString();
    apiUrlWithParams = queryString ? `${url}?${queryString}` : url;

    try {
      const response = await axios.get(apiUrlWithParams);
      setData(response.data);
      setNextPage(response.data.next);
    } catch (err) {
      setError("Failed to fetch data. Please try again later.");
    } finally {
      setLoading(false);
      }
    },
    [apiUrl]
  );

  const fetchYears = useCallback(
    async () => {
    try {
      const response = await axios.get(apiUrl);
      const availableYears = new Set();
      response.data.results.forEach((item) => {
        const year = Object.keys(item)[0];
        availableYears.add(year);
      });

      setYears(Array.from(availableYears).sort());
    } catch (err) {
      setError("Failed to fetch available years.");
      }
    },
    [apiUrl]
  );

  useEffect(() => {
    fetchYears();
    fetchData(initialYear, initialMonth);
  }, [initialYear, initialMonth, fetchData, fetchYears]);

  return { data, years, loading, error, fetchData, nextPage, months };
};

export default useFetchData;
