import socket

HOST = "0.0.0.0"
PORT = 5000

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind((HOST, PORT))

servidor.listen(1)

print("==============================")
print("       SERVIDOR TCP")
print("==============================")
print("Puerto:", PORT)
print("Esperando conexión...")

conexion, direccion = servidor.accept()

print("ESP32 conectado:", direccion)

while True:

    datos = conexion.recv(1024)

    if not datos:
        break

    mensaje = datos.decode().strip()

    print("ESP32:", mensaje)

    if mensaje == "HOLA":
        respuesta = "Hola ESP32"

    elif mensaje == "IP":
        respuesta = "El servidor recibió tu solicitud de IP"

    elif mensaje == "ESTADO":
        respuesta = "Servidor funcionando correctamente"

    elif mensaje == "SALIR":
        respuesta = "Conexión finalizada"
        conexion.send(respuesta.encode())
        break

    else:
        respuesta = "Comando desconocido"

    conexion.send(respuesta.encode())

conexion.close()
servidor.close()

print("Conexión cerrada")
print("Servidor finalizado")