import { StrictMode, useMemo, useState } from "react";
import { createRoot } from "react-dom/client";

import {
  ThemeProvider,
  CssBaseline,
} from "@mui/material";

import getTheme from "./theme";

import App from "./App";

function Root() {
  const [darkMode, setDarkMode] = useState(false);

  const theme = useMemo(
    () => getTheme(darkMode),
    [darkMode]
  );

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />

      <App
        darkMode={darkMode}
        setDarkMode={setDarkMode}
      />
    </ThemeProvider>
  );
}

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <Root />
  </StrictMode>
);