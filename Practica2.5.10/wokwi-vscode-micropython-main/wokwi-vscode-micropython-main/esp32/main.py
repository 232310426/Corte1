import network
import time
import socket

SSID = "Wokwi-GUEST"
PASSWORD = ""

SERVER_IP = "192.168.1.13"
SERVER_PORT = 5000


# ==============================
# CONEXIÓN WI-FI
# ==============================

wifi = network.WLAN(network.STA_IF)
wifi.active(True)

print("Conectando a Wi-Fi...")

wifi.connect(SSID, PASSWORD)

while not wifi.isconnected():
    time.sleep(0.5)

print("Wi-Fi conectado")

ip_esp32 = wifi.ifconfig()[0]

print("IP del ESP32:", ip_esp32)


# ==============================
# CONEXIÓN TCP
# ==============================

cliente = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

print("Conectando al servidor...")

cliente.connect(
    (SERVER_IP, SERVER_PORT)
)

print("Conectado al servidor")


# ==============================
# FUNCIÓN PARA ENVIAR MENSAJES
# ==============================

def enviar_mensaje(mensaje):

    cliente.send(mensaje.encode())

    respuesta = cliente.recv(1024)

    print("Servidor:", respuesta.decode())


# ==============================
# INTERCAMBIO DE MENSAJES
# ==============================

enviar_mensaje("HOLA")

enviar_mensaje("IP")

enviar_mensaje("ESTADO")

enviar_mensaje("SALIR")


# ==============================
# CERRAR CONEXIÓN
# ==============================

cliente.close()

print("Conexión cerrada")