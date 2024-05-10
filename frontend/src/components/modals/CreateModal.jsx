import { Box, Button, Modal, TextField, styled } from "@mui/material";
import { useState } from "react";
import AddIcon from "@mui/icons-material/Add";

const CreateModal = (props) => {
  const [openCreateModal, setOpenCreateModal] = useState(false);

  const { tablename, fields } = props;

  const modalFormFields = fields.map((field) => {
    return (
      <TextField
        key={field.id}
        id="outlined-password-input"
        label={field.field}
        type={field.type}
      />
    );
  });

  const MyStyleModal = styled(Modal)({
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
  });

  return (
    <Box>
      <Button onClick={(event) => setOpenCreateModal(true)}>
        <AddIcon />
        New {tablename}
      </Button>
      <MyStyleModal
        open={openCreateModal}
        onClose={(event) => setOpenCreateModal(false)}
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
            <div>{modalFormFields}</div>
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
