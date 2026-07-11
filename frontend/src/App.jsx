import { Container, Typography, Button, Stack } from "@mui/material";

function App() {
  return (
    <Container maxWidth="md">
      <Stack
        spacing={3}
        alignItems="center"
        justifyContent="center"
        sx={{ minHeight: "100vh" }}
      >
        <Typography variant="h3" component="h1">
          Catálogo UISEK
        </Typography>

        <Typography variant="h6" color="text.secondary">
          Frontend - Alberto Andrade | Sebastián Rubio
        </Typography>

        <Button variant="contained">
          Iniciar sesión
        </Button>
      </Stack>
    </Container>
  );
}

export default App;