import NavBar from "./components/NavBar";
import LeftBar from "./components/LeftBar";
import Main from "./components/Main";
import RightBar from "./components/RightBar";

import { Box, Stack } from "@mui/material";

function App() {
  return (
    <Box>
      <NavBar />
      <Stack sx={{ flexDirection: "row", gap: 2, justifyContent: "space-between" }}>
        <LeftBar />
        <Main />
        <RightBar />
      </Stack>
    </Box>
  );
}

export default App;
