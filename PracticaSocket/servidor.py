import socket
HOST = "0.0.0.0"
PUERTO = 6066
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PUERTO))
servidor.listen(1)
servidor.settimeout(60)
print(f"Servidor iniciado.")
print(f"Esperando al cliente en el puerto {PUERTO}...")
try:
 cliente, direccion = servidor.accept()
 print(f"Cliente conectado desde: {direccion}")
 # Recibir mensaje del cliente
 mensaje = cliente.recv(1024).decode("utf-8")
 print("El cliente dice:")
 print(mensaje)
 # Enviar respuesta
 respuesta = f"Gracias por conectarte al servidor {HOST}"
 cliente.sendall(respuesta.encode("utf-8"))
 cliente.close()
except socket.timeout:
 print("Tiempo de espera agotado. No se conectó ningún cliente.")
finally:
 servidor.close()
 print("Servidor finalizado.")