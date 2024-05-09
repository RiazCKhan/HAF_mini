import NavBar from "../components/navbars/NavBar";
import LeftBar from "../components/navbars/LeftBar";
import RightBar from "../components/navbars/RightBar";

import { Outlet } from "react-router-dom";
import { Box, Stack } from "@mui/material";

const Homepage = () => {
  return (
    <Box>
      <NavBar />
      <Stack
        sx={{ flexDirection: "row", gap: 2, justifyContent: "space-between" }}
      >
        <LeftBar />
        <Outlet />
        <RightBar />
      </Stack>
    </Box>
  );
};

export default Homepage;
