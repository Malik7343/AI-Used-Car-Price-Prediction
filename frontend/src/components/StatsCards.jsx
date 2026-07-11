import {
  Grid,
  Card,
  CardContent,
  Typography,
} from "@mui/material";

import SpeedIcon from "@mui/icons-material/Speed";
import MemoryIcon from "@mui/icons-material/Memory";
import BoltIcon from "@mui/icons-material/Bolt";

import { motion } from "framer-motion";

const cards = [
  {
    icon: <SpeedIcon fontSize="large" />,
    title: "Accuracy",
    value: "89.4%",
  },
  {
    icon: <MemoryIcon fontSize="large" />,
    title: "Model",
    value: "Random Forest",
  },
  {
    icon: <BoltIcon fontSize="large" />,
    title: "Backend",
    value: "FastAPI",
  },
];

function StatsCards() {
  return (
    <Grid container spacing={3} mb={5}>
      {cards.map((card, index) => (
        <Grid item xs={12} md={4} key={index}>
          <motion.div
            whileHover={{
              scale: 1.05,
            }}
          >
            <Card
              className="glass cardHover"
              sx={{
                textAlign: "center",
                p: 2,
              }}
            >
              <CardContent>
                {card.icon}

                <Typography
                  variant="h6"
                  mt={2}
                >
                  {card.title}
                </Typography>

                <Typography
                  variant="h5"
                  fontWeight="bold"
                  color="primary"
                >
                  {card.value}
                </Typography>
              </CardContent>
            </Card>
          </motion.div>
        </Grid>
      ))}
    </Grid>
  );
}

export default StatsCards;