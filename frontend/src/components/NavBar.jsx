import {
  AppBar,
  Avatar,
  Badge,
  Box,
  styled,
  Toolbar,
  Typography,
} from "@mui/material";
import ChairIcon from "@mui/icons-material/Chair";
import MailIcon from "@mui/icons-material/Mail";
import NotificationsIcon from "@mui/icons-material/Notifications";
import avatarImg from "../static/avatarDog.jpeg";

const IconBar = styled(Box)(({ theme }) => ({
  display: "none",
  alignItems: "center",
  gap: "1.25rem",
  padding: "0 0.625rem",
  [theme.breakpoints.up("sm")]: { display: "flex" },
}));

const IconBarMobile = styled(Box)(({ theme }) => ({
  display: "flex",
  alignItems: "center",
  gap: "1.25rem",
  padding: "0 0.625rem",
  [theme.breakpoints.up("sm")]: { display: "none" },
}));

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
    </AppBar>
  );
};

export default NavBar;
