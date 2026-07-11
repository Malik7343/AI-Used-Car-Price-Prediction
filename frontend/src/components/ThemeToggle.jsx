import { IconButton } from "@mui/material";
import { LightMode, DarkMode } from "@mui/icons-material";

function ThemeToggle({ darkMode, setDarkMode }) {
  return (
    <IconButton
      onClick={() => setDarkMode(!darkMode)}
      sx={{
        position: "fixed",
        top: 20,
        right: 20,
        bgcolor: "white",
        boxShadow: 3,
      }}
    >
      {darkMode ? <LightMode /> : <DarkMode />}
    </IconButton>
  );
}

export default ThemeToggle;