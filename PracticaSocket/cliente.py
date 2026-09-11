import socket
HOST = "127.0.0.1"
PUERTO = 6066
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
 print(f"Conectando a {HOST} en el puerto {PUERTO}...")
 cliente.connect((HOST, PUERTO))
 print("Conexión establecida.")
 # Obtener dirección local del cliente
 direccion_local = cliente.getsockname()
 print(f"Dirección local: {direccion_local}")
 # Enviar mensaje al servidor
 mensaje = f"Hola desde {direccion_local}"
 cliente.sendall(mensaje.encode("utf-8"))
 # Recibir respuesta
 respuesta = cliente.recv(1024).decode("utf-8")
 print("El servidor dice:")
 print(respuesta)
except ConnectionRefusedError:
 print("No se pudo conectar con el servidor.")
 print("Verifica que el servidor esté ejecutándose.")
except Exception as e:
 print(f"Error: {e}")
finally:
 cliente.close()
 print("Cliente finalizado.")