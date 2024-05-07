import NavBar from "./components/NavBar";
import Leftbar from "./components/Leftbar";
import Main from "./components/Main";
import Rightbar from "./components/Rightbar";

import { Box, Stack } from "@mui/material";

function App() {
  return (
    <Box>
      <NavBar />
      <Stack sx={{ flexDirection: "row", gap: 2, justifyContent: "space-between" }}>
        <Leftbar />
        <Main />
        <Rightbar />
      </Stack>
    </Box>
  );
}

export default App;
