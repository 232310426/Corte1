import network
import socket
import time

# -----------------------------
# CONFIGURACIÓN DEL SERVIDOR
# -----------------------------

SERVER_IP = "host.wokwi.internal"
SERVER_PORT = 5000


# -----------------------------
# CONEXIÓN WIFI
# -----------------------------

print("Conectando a WiFi...")

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

wlan.connect("Wokwi-GUEST", "")

while not wlan.isconnected():
    print("Esperando conexión WiFi...")
    time.sleep(1)

print("WiFi conectado")
print("IP del ESP32:", wlan.ifconfig()[0])


# -----------------------------
# CREAR SOCKET TCP
# -----------------------------

print("Creando conexión TCP...")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((SERVER_IP, SERVER_PORT))

    print("Conectado al servidor")
    
    # -----------------------------
    # ENVIAR SALUDO INICIAL
    # -----------------------------

    esp32_ip = wlan.ifconfig()[0]

    mensaje = "Hola servidor, soy el ESP32. Mi IP es: " + esp32_ip

    sock.send(mensaje.encode())

    print("Mensaje enviado:", mensaje)

    # -----------------------------
    # RECIBIR RESPUESTA
    # -----------------------------

    respuesta = sock.recv(1024)

    print("Respuesta del servidor:")
    print(respuesta.decode())


    # -----------------------------
    # CICLO DE COMANDOS
    # -----------------------------

    while True:

        print("Esperando comando del servidor...")

        datos = sock.recv(1024)

        if not datos:
            print("El servidor cerró la conexión")
            break

        comando = datos.decode().strip()

        print("Comando recibido:", comando)


        # -------------------------
        # COMANDO HOLA
        # -------------------------

        if comando == "HOLA":

            respuesta = "Hola servidor, soy el ESP32"

            sock.send(respuesta.encode())

            print("Respuesta enviada:", respuesta)


        # -------------------------
        # COMANDO IP
        # -------------------------

        elif comando == "IP":

            respuesta = "La IP del ESP32 es: " + wlan.ifconfig()[0]

            sock.send(respuesta.encode())

            print("Respuesta enviada:", respuesta)


        # -------------------------
        # COMANDO SALIR
        # -------------------------

        elif comando == "SALIR":

            respuesta = "Cerrando conexión..."

            sock.send(respuesta.encode())

            print(respuesta)

            break


        # -------------------------
        # COMANDO DESCONOCIDO
        # -------------------------

        else:

            respuesta = "Comando no reconocido"

            sock.send(respuesta.encode())

            print("Respuesta enviada:", respuesta)


# -----------------------------
# CERRAR SOCKET
# -----------------------------

except Exception as e:

    print("Error de conexión:", e)

finally:

    sock.close()

    print("Socket cerrado")
    print("Comunicación finalizada")