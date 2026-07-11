import { createTheme } from "@mui/material/styles";

const getTheme = (darkMode) =>
  createTheme({
    palette: {
      mode: darkMode ? "dark" : "light",

      primary: {
        main: "#1976d2",
      },

      secondary: {
        main: "#7c4dff",
      },
    },

    typography: {
      fontFamily: "'Poppins', sans-serif",
    },

    shape: {
      borderRadius: 14,
    },
  });

export default getTheme;