import { AppBar, Box, Toolbar, Typography } from "@mui/material";
import ChairIcon from "@mui/icons-material/Chair";

const NavBar = () => {
  return (
    <AppBar sx={{ position: "sticky" }}>
      <Toolbar sx={{ display: "flex", justifyContent: "space-between" }}>
        <Box sx={{ display: { xs: "none", sm: "block" } }}>
          <Typography
            variant="h6"
            sx={{ display: "flex", alignItems: "center" }}
          >
            <ChairIcon sx={{ display: "flex", p: 1 }} />
            HAF MINI
          </Typography>
        </Box>
        <ChairIcon sx={{ display: { xs: "block", sm: "none" } }} />
      </Toolbar>
    </AppBar>
  );
};

export default NavBar;
