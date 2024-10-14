import axios from 'axios';

export const fetchData = async (url) => {
  try {
    const response = await axios.get(url);
    return response;
  } catch (error) {
    throw new Error('Error fetching data');
  }
};