import {
  Box,
  Button,
  Paper,
  Stack,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Typography,
} from "@mui/material";
import AddIcon from "@mui/icons-material/Add";
import SendIcon from "@mui/icons-material/Send";

import CreateModal from "../modals/CreateModal";
import { ReferralFields } from "../../static/TableFormFields";

function createData(name, calories, fat, carbs, protein) {
  return { name, calories, fat, carbs, protein };
}

const rows = [
  createData("Frozen yoghurt", 159, 6.0, 24, 4.0),
  createData("Ice cream sandwich", 237, 9.0, 37, 4.3),
  createData("Eclair", 262, 16.0, 24, 6.0),
  createData("Cupcake", 305, 3.7, 67, 4.3),
  createData("Gingerbread", 356, 16.0, 49, 3.9),
];

const AgentTable = () => {
  return (
    <Box sx={{ flex: 4, p: 2 }}>
      <Box sx={{ padding: "1rem" }}>
        <Stack sx={{ flexDirection: "row", justifyContent: "space-between" }}>
          <Typography
            variant="h6"
            sx={{ margin: "0 0.5rem", fontWeight: "300" }}
          >
            Referrals
          </Typography>
          <CreateModal tablename={"Referral"} fields={ReferralFields} />
        </Stack>
        <TableContainer component={Paper}>
          <Table sx={{ minWidth: 650 }} aria-label="simple table">
            <TableHead>
              <TableRow>
                <TableCell>Client Name</TableCell>
                <TableCell align="center">Agency</TableCell>
                <TableCell align="center">Email</TableCell>
                <TableCell align="center">Phone Number</TableCell>
                <TableCell align="center">Status</TableCell>
                <TableCell align="center">Items</TableCell>
                <TableCell align="right">Request</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {rows.map((row) => (
                <TableRow
                  key={row.name}
                  sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
                >
                  <TableCell component="th" scope="row">
                    {row.name}
                  </TableCell>
                  <TableCell align="center">{row.calories}</TableCell>
                  <TableCell align="center">{row.fat}</TableCell>
                  <TableCell align="center">{row.carbs}</TableCell>
                  <TableCell align="center">{row.protein}</TableCell>
                  <TableCell align="center">
                    <Button size="small">
                      <AddIcon size="small" />
                    </Button>
                  </TableCell>
                  <TableCell align="right">
                    <Button size="small">
                      <SendIcon size="small" />
                    </Button>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>
    </Box>
  );
};

export default AgentTable;
