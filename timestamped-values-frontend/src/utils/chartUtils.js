export const processChartData = (results) => {
    const processedData = {
      labels: [],
      values: [],
    };
  
    results.forEach(item => {
      const year = Object.keys(item)[0];
      const months = item[year];
  
      months.forEach(monthObj => {
        const month = Object.keys(monthObj)[0];
        const entries = monthObj[month];
  
        entries.forEach(entry => {
          const timestamp = Object.keys(entry)[0];
          const value = entry[timestamp];
  
          processedData.labels.push(timestamp);
          processedData.values.push(value);
        });
      });
    });
  
    return processedData;
  };
  