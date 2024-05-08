import { Link } from "react-router-dom";
import { Box, Stack, Typography } from "@mui/material";

const Error = () => {
  return (
    <Box sx={{ margin: 10 }}>
      <Stack sx={{ flexDirection: "column", gap: 1, justifyContent: "center" }}>
        <Typography variant="h6" sx={{ fontWeight: "500" }}>
          404 Not Found
        </Typography>
        <Link to="/">Return to Dashboard</Link>
      </Stack>
    </Box>
  );
};

export default Error;
