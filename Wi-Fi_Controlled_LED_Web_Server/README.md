🌐 ESP8266 LED Web Controller (MicroPython)

A simple IoT project using ESP8266 + MicroPython to control an LED from a web browser. It supports:

🔴 LED ON / OFF control
🎚️ Brightness control using PWM slider
📱 Mobile-friendly web interface
🌐 Local WiFi web server (no internet required)
🚀 Features
Control LED from any device (phone / laptop)
Real-time brightness adjustment (0–1023)
Simple HTTP server (no frameworks)
Lightweight MicroPython implementation
Works on local WiFi network
🧰 Hardware Required
ESP8266 (NodeMCU / Wemos D1 Mini)
LED
220Ω resistor
Breadboard + jumper wires
🔌 Circuit Diagram
Component	ESP8266 Pin
LED +	D2 (GPIO4)
LED -	GND
📡 How It Works
ESP8266 connects to WiFi network
Starts a local web server on port 80
Provides a web page UI
User controls LED via browser:
ON button → full brightness
OFF button → LED off
Slider → adjust brightness
⚙️ Setup Instructions
1. Flash MicroPython (if not already done)

Install MicroPython firmware on ESP8266.

2. Upload Code to ESP8266
mpremote connect /dev/ttyUSB0 fs cp main.py :main.py
3. Run the Project
mpremote connect /dev/ttyUSB0 run main.py
4. Get IP Address

After running, check terminal:

Connected!
IP: 192.168.43.120
5. Open in Browser

Open any browser and go to:

http://192.168.43.120
🎛️ Controls
Control	Action
ON Button	LED turns ON (full brightness)
OFF Button	LED turns OFF
Slider	Adjust brightness (0–1023)
💡 Technical Overview
WiFi Mode
Uses STA_IF (Station Mode)
Connects ESP8266 to existing WiFi network
Server
Simple socket-based HTTP server
Listens on port 80
LED Control
Uses PWM (machine.PWM)
Duty cycle controls brightness:
0 → OFF
1023 → FULL brightness
🧠 Key Concepts Used
MicroPython GPIO control
PWM (Pulse Width Modulation)
Socket programming
HTTP request handling
HTML + JavaScript UI
⚠️ Important Notes
Use correct WiFi SSID & password
PWM only works on supported GPIO pins
Do NOT use .value() with PWM (use .duty() instead)
Ensure ESP is powered properly
🛠️ Common Issues
❌ PWM error: 'PWM' object has no attribute 'value'

✔ Fix: Replace .value() with .duty()

❌ Web page not opening

✔ Check:

IP address
Same WiFi network
ESP is running
📁 Project Structure
ESP8266_LED_Controller/
│
├── main.py
├── README.md
├── .gitignore
👨‍💻 Author

Built for learning IoT + Web Server + MicroPython on ESP8266

🔥 Future Improvements
📊 Live LED status indicator
⚡ Smooth fade animations
📱 App-like UI redesign
🌐 Multiple device control dashboard
🔐 Password-protected web panel