import socket

HOST = "127.0.0.1"
PUERTO = 6066

# Crear socket TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("===================================")
print("       CLIENTE MINICHAT")
print("===================================")

print(f"Conectando con {HOST}:{PUERTO}...")

# Conectarse al servidor
cliente.connect((HOST, PUERTO))

print("Conexión establecida.")

# Solicitar nombre del usuario
nombre = input("Escribe tu nombre: ")

# Enviar nombre al servidor
cliente.sendall(nombre.encode("utf-8"))

print("\nEscribe tus mensajes.")
print("Comandos disponibles: /hora /ayuda /salir\n")

while True:
    # Escribir mensaje
    mensaje = input(f"{nombre}: ")

    # Enviar mensaje
    cliente.sendall(mensaje.encode("utf-8"))

    # Verificar si desea salir
    if mensaje.lower() == "/salir":
        break

    # Recibir respuesta
    respuesta = cliente.recv(1024).decode("utf-8")

    if not respuesta:
        break

    print(f"Servidor: {respuesta}")

cliente.close()

print("\nConexión cerrada.")