import { useState } from "react";
import axios from "axios";

import { Container, Paper } from "@mui/material";

import HeroSection from "./components/HeroSection";
import StatsCards from "./components/StatsCards";
import PredictionForm from "./components/PredictionForm";
import ResultCard from "./components/ResultCard";
import ThemeToggle from "./components/ThemeToggle";

function App({ darkMode, setDarkMode }) {
  const [formData, setFormData] = useState({
    car_name: "",
    brand: "",
    model: "",
    vehicle_age: "",
    km_driven: "",
    seller_type: "Individual",
    fuel_type: "Petrol",
    transmission_type: "Manual",
    mileage: "",
    engine: "",
    max_power: "",
    seats: "",
  });

  const [price, setPrice] = useState("");
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const predictPrice = async () => {
    try {
      setLoading(true);

      const response = await axios.post(
        "http://127.0.0.1:8000/predict",
        {
          car_name: formData.car_name,
          brand: formData.brand,
          model: formData.model,
          vehicle_age: Number(formData.vehicle_age),
          km_driven: Number(formData.km_driven),
          seller_type: formData.seller_type,
          fuel_type: formData.fuel_type,
          transmission_type: formData.transmission_type,
          mileage: Number(formData.mileage),
          engine: Number(formData.engine),
          max_power: Number(formData.max_power),
          seats: Number(formData.seats),
        }
      );

      setPrice(response.data.predicted_price);
    } catch (error) {
      console.error(error);
      alert("Prediction Failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <ThemeToggle
        darkMode={darkMode}
        setDarkMode={setDarkMode}
      />

      <Container maxWidth="lg" sx={{ mt: 5, mb: 5 }}>
        <HeroSection />

        <StatsCards />

        <Paper
          elevation={8}
          sx={{
            mt: 4,
            p: 4,
            borderRadius: 4,
          }}
        >
          <PredictionForm
            formData={formData}
            handleChange={handleChange}
            predictPrice={predictPrice}
            loading={loading}
          />

          <ResultCard price={price} />
        </Paper>
      </Container>
    </>
  );
}

export default App;