import React from 'react';

const ErrorAlert = ({ message }) => {
  const alertStyle = {
    padding: '15px',
    backgroundColor: '#f44336',
    color: 'white',
    marginBottom: '20px',
    borderRadius: '5px',
  };

  return (
    <div style={alertStyle}>
      <strong>Error: </strong> {message}
    </div>
  );
};

export default ErrorAlert;