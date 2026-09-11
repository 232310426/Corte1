import socket

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))
server.listen(1)

print(f"Servidor escuchando en {HOST}:{PORT}")

conn, addr = server.accept()

print("ESP32 conectado desde:", addr)

while True:
    datos = conn.recv(1024)

    if not datos:
        print("El ESP32 cerró la conexión")
        break

    mensaje = datos.decode()

    print("Mensaje recibido:", mensaje)

    if mensaje.startswith("Hola servidor"):
        conn.send(b"Conexion TCP exitosa")

    comando = input("Comando (HOLA/IP/SALIR): ")

    conn.send(comando.encode())

    if comando == "SALIR":
        break

conn.close()
server.close()