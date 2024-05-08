import { Box, List } from "@mui/material";
import LeftBarItem from "./LeftBarItem";
import { LeftBarStatic } from "../static/LeftBarStatic";

const leftBarProps = LeftBarStatic.map((item) => {
  return (
    <LeftBarItem
      key={item.id}
      title={item.title}
      icon={item.icon}
      link={item.link}
    />
  );
});

const LeftBar = () => {
  return (
    <Box sx={{ flex: 1, p: 2, display: { xs: "none", sm: "block" } }}>
      <List>{leftBarProps}</List>
    </Box>
  );
};

export default LeftBar;
