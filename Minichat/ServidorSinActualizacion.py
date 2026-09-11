import socket
HOST = "127.0.0.1"
PUERTO = 6066
# Crear socket TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("===================================")
print(" CLIENTE MINICHAT")
print("===================================")
print(f"Conectando con {HOST}:{PUERTO}...")
# Conectarse al servidor
cliente.connect((HOST, PUERTO))
print("Conexión establecida.")
print("Escribe 'salir' para terminar.\n")
while True:
 # Escribir mensaje
 mensaje = input("Cliente: ")
 # Enviar mensaje
 cliente.sendall(mensaje.encode("utf-8"))
 if mensaje.lower() == "salir":
   break
 # Recibir respuesta
 respuesta = cliente.recv(1024).decode("utf-8")
 print(f"Servidor: {respuesta}")
 if respuesta.lower() == "salir": 
   break
 cliente.close()
print("\nConexión cerrada.")