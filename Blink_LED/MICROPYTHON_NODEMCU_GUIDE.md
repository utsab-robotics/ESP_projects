# 🐍 MicroPython NodeMCU (ESP8266) Complete Guide

This guide explains how to install MicroPython on NodeMCU (ESP8266), connect to REPL, and control LEDs (built-in + external).

---

# ⚠️ Important

MicroPython replaces Arduino firmware.

Only one firmware can run at a time:

- Arduino ❌ MicroPython  
- MicroPython ❌ Arduino  

---

# 📦 Requirements

## 🧩 Hardware
- NodeMCU (ESP8266)
- USB data cable
- LED + 220Ω resistor (for external LED)

## 💻 Software
- Python 3
- esptool
- mpremote

---

# 🧰 Install Tools

```bash
pip install esptool
pip install mpremote

🧹 Step 1: Erase Flash
esptool --chip esp8266 --port /dev/ttyUSB0 erase_flash

⚙️ Step 2: Flash MicroPython

esptool --chip esp8266 --port /dev/ttyUSB0 \
write_flash --flash_mode dio --flash_size 4MB \
0x00000 ESP8266_GENERIC-20260406-v1.28.0.bin

🔌 Step 3: Connect to REPL

mpremote connect /dev/ttyUSB0 repl

If successful, you will see:

>>>
🧪 Step 4: Test MicroPython
print("MicroPython working")
💡 LED CONTROL
🔵 1. Built-in LED (GPIO2)

Note: Built-in LED is usually active LOW (inverted logic)

from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)   # Built-in LED (GPIO2)

while True:
    led.off()   # LED ON
    sleep(1)
    led.on()    # LED OFF
    sleep(1)


💡 2. External LED on D2 (GPIO4)
🔌 Wiring

D2 (GPIO4) → LED (+)
GND        → LED (-)
Use 220Ω resistor


💡 Code
from machine import Pin
from time import sleep

led = Pin(4, Pin.OUT)   # D2 = GPIO4

while True:
    led.value(1)   # ON
    sleep(1)
    led.value(0)   # OFF
    sleep(1)


📤 Upload Code as main.py

mpremote connect /dev/ttyUSB0 fs cp main.py :main.py
🔄 Run Program

mpremote connect /dev/ttyUSB0 reset

OR press the RESET button on NodeMCU.

🧠 Auto Run Behavior

If main.py exists on the device:

✔ It runs automatically on boot

🛑 Stop Program
Press Ctrl + C in REPL
OR press RESET button
🔄 Delete File (if needed)
mpremote connect /dev/ttyUSB0 fs rm main.py
⚠️ Troubleshooting
❌ REPL not working
fuser -k /dev/ttyUSB0
❌ Garbage output on screen
Wrong boot state
Reflash firmware again
❌ LED not blinking
Check GPIO pin (2 or 4)
Check LED polarity
Check wiring
✅ DONE

You now know:

✔ MicroPython installation
✔ REPL usage
✔ Built-in LED control
✔ External LED control (D2 / GPIO4)
✔ File upload system
✔ Auto-run behavior