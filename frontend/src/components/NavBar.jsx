import {
  AppBar,
  Avatar,
  Badge,
  Box,
  Menu,
  MenuItem,
  Toolbar,
  Typography,
} from "@mui/material";
import { IconBar, IconBarMobile } from "../themes/NavBarTheme";
import ChairIcon from "@mui/icons-material/Chair";
import MailIcon from "@mui/icons-material/Mail";
import NotificationsIcon from "@mui/icons-material/Notifications";
import avatarImg from "../static/avatarDog.jpeg";

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
        <IconBar>
          <Badge color="secondary" badgeContent={0} showZero>
            <MailIcon />
          </Badge>
          <Badge color="secondary" badgeContent={0} showZero>
            <NotificationsIcon />
          </Badge>
          <Avatar src={avatarImg} />
        </IconBar>
        <IconBarMobile>
          <Typography>Basil</Typography>
          <Avatar src={avatarImg} />
        </IconBarMobile>
      </Toolbar>
      <Menu
        id="demo-positioned-menu"
        aria-labelledby="demo-positioned-button"
        open={true}
        onClose={false}
        anchorOrigin={{
          vertical: "top",
          horizontal: "right",
        }}
        transformOrigin={{
          vertical: "top",
          horizontal: "left",
        }}
      >
        <MenuItem>Profile</MenuItem>
        <MenuItem>Admin</MenuItem>
        <MenuItem>Logout</MenuItem>
      </Menu>
    </AppBar>
  );
};

export default NavBar;
