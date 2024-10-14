import React, { useState } from "react";
import useFetchData from "./hooks/useFetchData";
import ChartComponent from "./components/ChartComponent";
import Loading from "./components/Loading";
import ErrorAlert from "./components/ErrorAlert";
import Button from "./components/Button";
import Container from "./components/Container";
import Title from "./components/Title";
import Dropdown from "./components/Dropdown";

function App() {
  const [selectedYear, setSelectedYear] = useState("");
  const [selectedMonth, setSelectedMonth] = useState("");

  const { data, years, months, loading, error, fetchData, nextPage } =
    useFetchData(selectedYear, selectedMonth);

  const handleYearChange = (event) => {
    const newYear = event.target.value;
    setSelectedYear(newYear);
    fetchData(newYear, selectedMonth);
  };

  const handleMonthChange = (event) => {
    const newMonth = event.target.value;
    setSelectedMonth(newMonth);
    fetchData(selectedYear, newMonth);
  };

  const loadMore = () => {
    if (nextPage) {
      fetchData(selectedYear, selectedMonth, nextPage);
    }
  };

  return (
    <Container>
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
        }}
      >
        <Title text="Timestamped Values Visualization" />
        <div>
          <Dropdown
            label="Year"
            options={["", ...years]}
            value={selectedYear}
            onChange={handleYearChange}
          />
          <Dropdown
            label="Month"
            options={["", ...months]}
            value={selectedMonth}
            onChange={handleMonthChange}
          />
        </div>
      </div>
      {error && <ErrorAlert message={error} />}
      {loading && <Loading />}
      {data && !loading ? (
        <>
          <ChartComponent data={data.results} />
          {nextPage && <Button onClick={loadMore} text="Load More" />}
        </>
      ) : !loading ? (
        <p>No data available</p>
      ) : null}
    </Container>
  );
}

export default App;
