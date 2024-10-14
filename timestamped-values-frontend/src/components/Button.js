import React from "react";

const Button = ({ onClick, text }) => {
  const buttonStyle = {
    padding: "10px 20px",
    backgroundColor: "#4CAF50",
    color: "white",
    border: "none",
    borderRadius: "5px",
    cursor: "pointer",
    marginTop: "20px",
  };

  const handleMouseOver = (event) => {
    event.target.style.backgroundColor = "#45a049";
  };

  const handleMouseOut = (event) => {
    event.target.style.backgroundColor = "#4CAF50";
  };

  return (
    <button
      onClick={onClick}
      onMouseOver={handleMouseOver}
      onMouseOut={handleMouseOut}
      style={buttonStyle}
    >
      {text}
    </button>
  );
};

export default Button;
