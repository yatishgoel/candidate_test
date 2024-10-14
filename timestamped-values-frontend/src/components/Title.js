
import React from 'react';

const Title = ({ text }) => {
  const titleStyle = {
    fontSize: '24px',
    fontWeight: 'bold',
    marginBottom: '20px',
  };

  return <h1 style={titleStyle}>{text}</h1>;
};

export default Title;
