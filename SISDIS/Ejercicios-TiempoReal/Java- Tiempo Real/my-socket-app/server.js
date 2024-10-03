const express = require('express');
const http = require('http');
const socketIo = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

// Ruta principal que carga la página web
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

// Escucha mensajes del cliente
io.on('connection', (socket) => {
    console.log('Nuevo cliente conectado');

    socket.on('message', (data) => {
        console.log(`Recibido mensaje: ${data}`);
        // Envía una respuesta al cliente
        io.emit('response', { data: `Servidor recibió el mensaje: ${data}` });
    });

    socket.on('disconnect', () => {
        console.log('Cliente desconectado');
    });
});

// Ejecuta el servidor
const PORT = 4000;
server.listen(PORT, () => {
    console.log(`Servidor escuchando en http://localhost:${PORT}`);
});
