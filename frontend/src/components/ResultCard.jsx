import { Alert, Typography } from "@mui/material";

function ResultCard({ price }) {

  if (!price) return null;

  return (
    <Alert
      severity="success"
      sx={{
        mt: 4,
        borderRadius: 3,
        padding: 2,
      }}
    >
      <Typography variant="h5" fontWeight="bold">
        💰 Estimated Price
      </Typography>

      <Typography
        variant="h4"
        color="success.main"
        fontWeight="bold"
        sx={{ mt: 1 }}
      >
        Rs. {Number(price).toLocaleString()}
      </Typography>
    </Alert>
  );
}

export default ResultCard;