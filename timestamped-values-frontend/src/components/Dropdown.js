import React from 'react';

const Dropdown = ({ label, options, value, onChange }) => {
  const dropdownStyle = {
    marginLeft: '10px',
    padding: '5px 10px',
    borderRadius: '5px',
    border: '1px solid #ccc',
  };

  const labelStyle = {
    marginRight: '10px',
    fontWeight: 'bold',
  };

  return (
    <div style={{ display: 'inline-block', marginRight: '15px' }}>
      <label style={labelStyle}>{label}:</label>
      <select value={value} onChange={onChange} style={dropdownStyle}>
        {options.map((option, index) => (
          <option key={index} value={option}>
            {option}
          </option>
        ))}
      </select>
    </div>
  );
};

export default Dropdown;
