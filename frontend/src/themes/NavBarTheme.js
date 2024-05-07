import { Box, styled } from "@mui/material";

export const IconBar = styled(Box)(({ theme }) => ({
  display: "none",
  alignItems: "center",
  gap: "1.25rem",
  padding: "0 0.625rem",
  [theme.breakpoints.up("sm")]: { display: "flex" },
}));

export const IconBarMobile = styled(Box)(({ theme }) => ({
  display: "flex",
  alignItems: "center",
  gap: "1.25rem",
  padding: "0 0.625rem",
  [theme.breakpoints.up("sm")]: { display: "none" },
}));

