import {
  ListItem,
  ListItemButton,
  ListItemIcon,
  ListItemText,
} from "@mui/material";

import { Link } from "react-router-dom";

const LeftBarItem = (props) => {
  const { title, icon, link } = props;

  return (
    <Link to={link} style={{ color: "black", textDecoration: "none" }}>
      <ListItem disablePadding>
        <ListItemButton>
          <ListItemIcon>{icon}</ListItemIcon>
          <ListItemText primary={title} />
        </ListItemButton>
      </ListItem>
    </Link>
  );
};

export default LeftBarItem;
