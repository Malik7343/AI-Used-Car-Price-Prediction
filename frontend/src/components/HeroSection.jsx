import { Box, Typography, Chip } from "@mui/material";
import DirectionsCarFilledIcon from "@mui/icons-material/DirectionsCarFilled";
import AutoAwesomeIcon from "@mui/icons-material/AutoAwesome";
import { motion } from "framer-motion";

function HeroSection() {
  return (
    <motion.div
      initial={{ opacity: 0, y: -40 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.8 }}
    >
      <Box textAlign="center" mb={5}>
        <DirectionsCarFilledIcon
          sx={{
            fontSize: 90,
            color: "#3b82f6",
            mb: 2,
          }}
        />

        <Typography
          variant="h2"
          className="titleGradient"
        >
          AI Used Car
        </Typography>

        <Typography
          variant="h3"
          fontWeight="bold"
        >
          Price Prediction
        </Typography>

        <Typography
          sx={{
            mt: 2,
            color: "text.secondary",
            fontSize: 20,
          }}
        >
          Predict accurate used car prices using Machine Learning
        </Typography>

        <Chip
          icon={<AutoAwesomeIcon />}
          label="Powered by FastAPI + React + Random Forest"
          color="primary"
          sx={{
            mt: 3,
            fontSize: 16,
            padding: 2,
          }}
        />
      </Box>
    </motion.div>
  );
}

export default HeroSection;