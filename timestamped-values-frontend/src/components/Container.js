import React from 'react';

const Container = ({ children }) => {
  const containerStyle = {
    width: '80%',
    margin: '0 auto',
    padding: '20px',
    textAlign: 'center',
    backgroundColor: '#f8f8f8',
    borderRadius: '10px',
    boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
  };

  return <div style={containerStyle}>{children}</div>;
};

export default Container;
