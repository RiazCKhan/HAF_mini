import { Box, Button, Modal, Stack, TextField, styled } from "@mui/material";
import { useState } from "react";
import AddIcon from "@mui/icons-material/Add";

const faker = [
  {
    id: 1,
    itemName: "Item",
    quantity: "Quantity",
  },
  {
    id: 2,
    itemName: "Item",
    quantity: "Quantity",
  },
  {
    idd: 3,
    itemName: "Item",
    quantity: "Quantity",
  },
];

const CreateModal = (props) => {
  const [openItemModal, setOpenItemModal] = useState(false);

  const dummyData = faker.map((item) => {
    return (
      <Stack direction="row" spacing={2}>
        <TextField
          id="outlined-password-input"
          label={item.itemName}
          type="text"
        />
        <TextField
          id="outlined-password-input"
          label={item.quantity}
          type="number"
        />
        <Button size="small">
          <AddIcon />
        </Button>
      </Stack>
    );
  });

  const MyStyleModal = styled(Modal)({
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
  });

  return (
    <Box>
      <Button onClick={(event) => setOpenItemModal(true)}>
        <AddIcon />
      </Button>
      <MyStyleModal
        open={openItemModal}
        onClose={(event) => setOpenItemModal(false)}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box
          sx={{
            display: "flex",
            flexDirection: "column",
            width: "auto",
            backgroundColor: "white",
            p: 3,
            borderRadius: 2,
          }}
        >
          <Box
            component="form"
            sx={{
              "& .MuiTextField-root": { m: 1, width: "25ch" },
            }}
            noValidate
            autoComplete="off"
          >
            <div>{dummyData}</div>
          </Box>
          <Box sx={{ display: "flex", justifyContent: "end", p: 1 }}>
            <Button variant="contained">Submit</Button>
          </Box>
        </Box>
      </MyStyleModal>
    </Box>
  );
};

export default CreateModal;
