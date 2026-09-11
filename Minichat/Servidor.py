import socket
from datetime import datetime

HOST = "0.0.0.0"
PUERTO = 6066

# Crear socket TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Asociar dirección y puerto
servidor.bind((HOST, PUERTO))

# Esperar conexiones
servidor.listen(1)

print("===================================")
print("       SERVIDOR MINICHAT")
print("===================================")
print(f"Esperando conexión en el puerto {PUERTO}...")

# Aceptar conexión
cliente, direccion = servidor.accept()

print(f"Cliente conectado desde: {direccion}")

# Recibir nombre del usuario
nombre = cliente.recv(1024).decode("utf-8")

print(f"Usuario conectado: {nombre}")

while True:

    # Recibir mensaje
    mensaje = cliente.recv(1024).decode("utf-8")

    # Si no recibe información, termina la conexión
    if not mensaje:
        break

    print(f"\n{nombre}: {mensaje}")

    # Comando /salir
    if mensaje.lower() == "/salir":
        respuesta = "Conexión finalizada."
        cliente.sendall(respuesta.encode("utf-8"))
        break

    # Comando /ayuda
    elif mensaje.lower() == "/ayuda":
        respuesta = "Comandos disponibles: /hora /ayuda /salir"

    # Comando /hora
    elif mensaje.lower() == "/hora":
        hora = datetime.now().strftime("%H:%M:%S")
        respuesta = f"Hora del servidor: {hora}"

    # Mensaje normal
    else:
        respuesta = input("Servidor: ")

    # Enviar respuesta
    cliente.sendall(respuesta.encode("utf-8"))

cliente.close()
servidor.close()

print("\nConexión cerrada.")