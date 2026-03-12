import React, { useEffect, useState } from "react";
import axios from "axios";

import Navbar from "../components/Navbar";
import Chart from "../components/Chart";
import Filters from "../components/Filters";

const Dashboard = () => {

  const [data, setData] = useState([]);

  const fetchData = async (filters = {}) => {

    try {

      const response = await axios.get(
        "http://localhost:8000/api/dashboard",
        { params: filters }
      );

      setData(response.data);

    } catch (error) {

      console.error("Error fetching dashboard data");

    }

  };

  useEffect(() => {

    fetchData();

  }, []);

  const handleFilterChange = (filters) => {

    fetchData(filters);

  };

  return (

    <div>

      <Navbar />

      <div style={{ padding: "20px" }}>

        <h2>Analytics Dashboard</h2>

        <Filters onFilterChange={handleFilterChange} />

        <Chart
          data={data}
          dataKey="sales_value"
          title="Sales Trend"
        />

      </div>

    </div>

  );

};

export default Dashboard;