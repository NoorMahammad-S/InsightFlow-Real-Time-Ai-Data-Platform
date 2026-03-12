import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav
      style={{
        background: "#1e293b",
        padding: "10px",
        color: "white",
        display: "flex",
        justifyContent: "space-between"
      }}
    >
      <h2>InsightFlow</h2>

      <div>
        <Link
          to="/dashboard"
          style={{ color: "white", marginRight: "15px" }}
        >
          Dashboard
        </Link>

        <Link
          to="/upload"
          style={{ color: "white" }}
        >
          Upload
        </Link>
      </div>
    </nav>
  );
};

export default Navbar;