import React, { useState } from "react";

const Filters = ({ onFilterChange }) => {
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");

  const applyFilters = () => {
    onFilterChange({
      startDate,
      endDate
    });
  };

  return (
    <div style={{ marginBottom: "20px" }}>
      <h4>Filters</h4>

      <label>Start Date:</label>

      <input
        type="date"
        value={startDate}
        onChange={(e) => setStartDate(e.target.value)}
      />

      <label style={{ marginLeft: "10px" }}>End Date:</label>

      <input
        type="date"
        value={endDate}
        onChange={(e) => setEndDate(e.target.value)}
      />

      <button
        onClick={applyFilters}
        style={{ marginLeft: "10px" }}
      >
        Apply
      </button>
    </div>
  );
};

export default Filters;