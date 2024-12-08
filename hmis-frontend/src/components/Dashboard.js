import React from "react";
import { useNavigate } from "react-router-dom";

function Dashboard() {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/");
  };

  return (
    <div>
      <h1>Welcome to the HMIS Dashboard</h1>
      <p>Select an option:</p>
      <ul>
        <li><a href="/patients">View Patients</a></li>
        <li><a href="/doctors">View Doctors</a></li>
        <li><a href="/records">Manage Records</a></li>
      </ul>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
}

export default Dashboard;
