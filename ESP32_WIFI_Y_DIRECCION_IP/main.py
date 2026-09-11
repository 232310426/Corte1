import network
import time

# Datos de la red Wi-Fi
ssid = "Wokwi-GUEST"
password = ""

# Crear la interfaz Wi-Fi en modo estación
wifi = network.WLAN(network.STA_IF)

# Activar la interfaz
wifi.active(True)

# Solicitar conexión
print("Conectando a Wi-Fi...")
wifi.connect(ssid, password)

# Esperar hasta establecer la conexión
while not wifi.isconnected():
    print("Conectando...")
    time.sleep(1)

# Obtener configuración de red
config = wifi.ifconfig()

# Obtener dirección MAC
mac = wifi.config("mac")

# Convertir la MAC a formato XX:XX:XX:XX:XX:XX
mac_str = ":".join("{:02X}".format(byte) for byte in mac)

print()
print("========================================")
print("     INFORMACIÓN DE RED DEL ESP32")
print("========================================")
print("Estado: CONECTADO")
print("SSID:", wifi.config("ssid"))
print("IP:", config[0])
print("Máscara:", config[1])
print("Gateway:", config[2])
print("DNS:", config[3])
print("MAC:", mac_str)
print("========================================")
print("El ESP32 está listo para comunicarse.")
print("========================================")
