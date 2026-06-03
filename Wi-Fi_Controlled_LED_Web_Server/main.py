import network
import socket
from machine import Pin, PWM
import time

# LED setup
# led = Pin(4, Pin.OUT)
led = PWM(Pin(4))
led.freq(1000)
# led.value(0)

led.duty(0)

# WiFi credentials
ssid = "moto g85 5G"
password = ""

# Connect WiFi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

print("Connecting...")

while not wifi.isconnected():
    time.sleep(1)

print("Connected!")
print("IP:", wifi.ifconfig()[0])

# Web server setup
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
server = socket.socket()
server.bind(addr)
server.listen(1)

print("Server running...")

while True:
    client, addr = server.accept()
    print("Client connected:", addr)

    request = client.recv(1024).decode()

    if "/on" in request:
        led.duty(1023)

    elif "/off" in request:
        led.duty(0)

    # Brightness control
    if "/brightness" in request:
        try:
            value = int(request.split("val=")[1].split(" ")[0])
            led.duty(value)
        except:
            pass

   # HTML UI
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>ESP8266 LED Control</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>

    <body style="text-align:center;font-family:Arial;padding-top:50px;">

        <h2>ESP8266 LED Control</h2>

        <a href="/on"><button style="padding:15px;width:120px;background:green;color:white;">ON</button></a>
        <a href="/off"><button style="padding:15px;width:120px;background:red;color:white;">OFF</button></a>

        <br><br>

        <input type="range" min="0" max="1023" oninput="sendValue(this.value)">

        <script>
            function sendValue(val){
                var xhttp = new XMLHttpRequest();
                xhttp.open("GET", "/brightness?val=" + val, true);
                xhttp.send();
            }
        </script>

    </body>
    </html>
    """

    client.send("HTTP/1.1 200 OK\r\n")
    client.send("Content-Type: text/html\r\n")
    client.send("Connection: close\r\n\r\n")
    client.send(html)

    client.close()