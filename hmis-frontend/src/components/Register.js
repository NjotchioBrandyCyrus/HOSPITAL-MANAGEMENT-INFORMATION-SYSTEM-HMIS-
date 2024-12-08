import React, { useState } from "react";
import { register } from "../services/api";

function Register() {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: "",
    role: "patient", // Default role is patient
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await register(formData);
      alert("Registration successful!");
      console.log(response.data);
      setFormData({
        name: "",
        email: "",
        password: "",
        role: "patient",
      });
    } catch (error) {
      alert("Registration failed.");
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Register</h2>
      <label>Name:</label>
      <input
        type="text"
        name="name"
        value={formData.name}
        onChange={handleChange}
        required
      />
      <br />
      <label>Email:</label>
      <input
        type="email"
        name="email"
        value={formData.email}
        onChange={handleChange}
        required
      />
      <br />
      <label>Password:</label>
      <input
        type="password"
        name="password"
        value={formData.password}
        onChange={handleChange}
        required
      />
      <br />
      <label>Role:</label>
      <select
        name="role"
        value={formData.role}
        onChange={handleChange}
        required
      >
        <option value="patient">Patient</option>
        <option value="doctor">Doctor</option>
        <option value="admin">Admin</option>
      </select>
      <br />
      <button type="submit">Register</button>
    </form>
  );
}

export default Register;
