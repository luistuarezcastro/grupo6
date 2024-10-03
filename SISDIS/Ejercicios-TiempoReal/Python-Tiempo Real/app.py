from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import eventlet

# Inicia Flask y SocketIO
app = Flask(__name__)   #microframework permite crear apliacaciones web
socketio = SocketIO(app)   #comunicacion en tiempo real

# Ruta principal que carga la página web  flash sireve una pagina html (cliente)
@app.route('/')
def index():
    return render_template('index.html')

# Escucha mensajes del cliente
@socketio.on('message') #este decorador indica que la función  handle_message(data) donde le escuche los mensajes enviado desde los 
#clientes cada vez que un cliente envia un mensaje, el servidor lo recibe y procesa
def handle_message(data):
    print(f'Recibido mensaje: {data}')
    # Envía una respuesta al cliente    emit envia respuesta a todos los clientes concetados con el mensaje recibido, esto es lo que hace en tiempo real
    emit('response', {'data': f'Servidor recibió el mensaje: {data}'}, broadcast=True)

# Ejecuta el servidor
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
