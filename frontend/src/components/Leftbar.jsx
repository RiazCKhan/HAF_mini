import { Box, List } from "@mui/material";
import LeftbarItem from "./LeftbarItem";
import { LeftbarStatic } from "../static/LeftbarStatic";

const leftBarProps = LeftbarStatic.map((item) => {
  return (
    <LeftbarItem
      key={item.id}
      title={item.title}
      icon={item.icon}
      link={item.link}
    />
  );
});

const Leftbar = () => {
  return (
    <Box sx={{ flex: 1, p: 2, display: { xs: "none", sm: "block" } }}>
      <List>{leftBarProps}</List>
    </Box>
  );
};

export default Leftbar;
