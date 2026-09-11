import socket
HOST = "0.0.0.0"
PUERTO = 6066
# Crear socket TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Asociar dirección y puerto
servidor.bind((HOST, PUERTO))
# Esperar conexiones
servidor.listen(1)
print("===================================")
print(" SERVIDOR MINICHAT")
print("===================================")
print(f"Esperando conexión en el puerto {PUERTO}...")
cliente, direccion = servidor.accept()
print(f"Cliente conectado desde: {direccion}")
while True:
    # Recibir mensaje
    mensaje = cliente.recv(1024).decode("utf-8")
    if not mensaje:
        break
    print(f"\nCliente: {mensaje}")
    # Verificar si el cliente desea salir
    if mensaje.lower() == "salir":
        respuesta = "Conexión finalizada."
        cliente.sendall(respuesta.encode("utf-8"))
        break
    # Escribir respuesta
    respuesta = input("Servidor: ")
    cliente.sendall(respuesta.encode("utf-8"))
    if respuesta.lower() == "salir":
        break

cliente.close()
servidor.close()
print("\nConexión cerrada.")