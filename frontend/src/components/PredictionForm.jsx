import {
  Grid,
  TextField,
  MenuItem,
  Button,
  InputAdornment,
  CircularProgress,
} from "@mui/material";

import DirectionsCarIcon from "@mui/icons-material/DirectionsCar";
import BrandingWatermarkIcon from "@mui/icons-material/BrandingWatermark";
import SpeedIcon from "@mui/icons-material/Speed";
import LocalGasStationIcon from "@mui/icons-material/LocalGasStation";
import SettingsIcon from "@mui/icons-material/Settings";
import EventIcon from "@mui/icons-material/Event";
import AirlineSeatReclineNormalIcon from "@mui/icons-material/AirlineSeatReclineNormal";
import MemoryIcon from "@mui/icons-material/Memory";
import FlashOnIcon from "@mui/icons-material/FlashOn";

function PredictionForm({
  formData,
  handleChange,
  predictPrice,
  loading,
}) {
  return (
    <>
      <Grid container spacing={3}>
        <Grid item xs={12}>
          <TextField
            fullWidth
            label="Car Name"
            name="car_name"
            value={formData.car_name}
            onChange={handleChange}
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  <DirectionsCarIcon />
                </InputAdornment>
              ),
            }}
          />
        </Grid>

        <Grid item xs={12} md={6}>
          <TextField
            fullWidth
            label="Brand"
            name="brand"
            value={formData.brand}
            onChange={handleChange}
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  <BrandingWatermarkIcon />
                </InputAdornment>
              ),
            }}
          />
        </Grid>

        <Grid item xs={12} md={6}>
          <TextField
            fullWidth
            label="Model"
            name="model"
            value={formData.model}
            onChange={handleChange}
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  <MemoryIcon />
                </InputAdornment>
              ),
            }}
          />
        </Grid>

        <Grid item xs={12} md={6}>
          <TextField
            fullWidth
            type="number"
            label="Vehicle Age"
            name="vehicle_age"
            value={formData.vehicle_age}
            onChange={handleChange}
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  <EventIcon />
                </InputAdornment>
              ),
            }}
          />
        </Grid>

        <Grid item xs={12} md={6}>
          <TextField
            fullWidth
            type="number"
            label="KM Driven"
            name="km_driven"
            value={formData.km_driven}
            onChange={handleChange}
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  <SpeedIcon />
                </InputAdornment>
              ),
            }}
          />
        </Grid>

        <Grid item xs={12} md={6}>
          <TextField
            select
            fullWidth
            label="Seller Type"
            name="seller_type"
            value={formData.seller_type}
            onChange={handleChange}
          >
            <MenuItem value="Individual">Individual</MenuItem>
            <MenuItem value="Dealer">Dealer</MenuItem>
            <MenuItem value="Trustmark Dealer">
              Trustmark Dealer
            </MenuItem>
          </TextField>
        </Grid>

        <Grid item xs={12} md={6}>
          <TextField
            select
            fullWidth
            label="Fuel Type"
            name="fuel_type"
            value={formData.fuel_type}
            onChange={handleChange}
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  <LocalGasStationIcon />
                </InputAdornment>
              ),
            }}
          >
            <MenuItem value="Petrol">Petrol</MenuItem>
            <MenuItem value="Diesel">Diesel</MenuItem>
            <MenuItem value="CNG">CNG</MenuItem>
            <MenuItem value="LPG">LPG</MenuItem>
            <MenuItem value="Electric">Electric</MenuItem>
          </TextField>
        </Grid>

        <Grid item xs={12} md={6}>
          <TextField
            select
            fullWidth
            label="Transmission"
            name="transmission_type"
            value={formData.transmission_type}
            onChange={handleChange}
          >
            <MenuItem value="Manual">Manual</MenuItem>
            <MenuItem value="Automatic">Automatic</MenuItem>
          </TextField>
        </Grid>

        <Grid item xs={12} md={6}>
          <TextField
            fullWidth
            type="number"
            label="Mileage"
            name="mileage"
            value={formData.mileage}
            onChange={handleChange}
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  <SpeedIcon />
                </InputAdornment>
              ),
            }}
          />
        </Grid>

        <Grid item xs={12} md={4}>
          <TextField
            fullWidth
            type="number"
            label="Engine (CC)"
            name="engine"
            value={formData.engine}
            onChange={handleChange}
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  <SettingsIcon />
                </InputAdornment>
              ),
            }}
          />
        </Grid>

        <Grid item xs={12} md={4}>
          <TextField
            fullWidth
            type="number"
            label="Max Power"
            name="max_power"
            value={formData.max_power}
            onChange={handleChange}
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  <FlashOnIcon />
                </InputAdornment>
              ),
            }}
          />
        </Grid>

        <Grid item xs={12} md={4}>
          <TextField
            fullWidth
            type="number"
            label="Seats"
            name="seats"
            value={formData.seats}
            onChange={handleChange}
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  <AirlineSeatReclineNormalIcon />
                </InputAdornment>
              ),
            }}
          />
        </Grid>
      </Grid>

      <Button
        fullWidth
        variant="contained"
        size="large"
        sx={{
          mt: 4,
          py: 1.8,
          borderRadius: 3,
          fontSize: "18px",
          fontWeight: "bold",
          textTransform: "none",
        }}
        onClick={predictPrice}
        disabled={loading}
      >
        {loading ? (
          <>
            <CircularProgress
              size={22}
              color="inherit"
              sx={{ mr: 2 }}
            />
            Predicting...
          </>
        ) : (
          "🚗 Predict Price"
        )}
      </Button>
    </>
  );
}

export default PredictionForm;