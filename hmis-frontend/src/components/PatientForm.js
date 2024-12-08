import React, { useState } from "react";
import axios from "../services/api";

function PatientForm() {
  const [formData, setFormData] = useState({
    name: "",
    address: "",
    contact: "",
    medical_history: "",
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("/patients", formData);
      alert("Patient record saved successfully!");
      console.log(response.data);
      setFormData({
        name: "",
        address: "",
        contact: "",
        medical_history: "",
      });
    } catch (error) {
      alert("Error saving patient record.");
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Patient Information</h2>
      <label>Name:</label>
      <input
        type="text"
        name="name"
        value={formData.name}
        onChange={handleChange}
        required
      />
      <br />
      <label>Address:</label>
      <input
        type="text"
        name="address"
        value={formData.address}
        onChange={handleChange}
        required
      />
      <br />
      <label>Contact:</label>
      <input
        type="text"
        name="contact"
        value={formData.contact}
        onChange={handleChange}
        required
      />
      <br />
      <label>Medical History:</label>
      <textarea
        name="medical_history"
        value={formData.medical_history}
        onChange={handleChange}
        required
      />
      <br />
      <button type="submit">Submit</button>
    </form>
  );
}

export default PatientForm;
