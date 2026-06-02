# 🐍 NodeMCU (ESP8266) Setup with MicroPython

This guide explains how to install MicroPython on a NodeMCU (ESP8266), connect to the REPL, upload files, and control LEDs.

---

## ⚠️ Important

MicroPython replaces the Arduino firmware.

- Arduino IDE Firmware ❌ + MicroPython ❌
- MicroPython ✔️ OR Arduino ✔️

Only one firmware can exist on the board at a time.

---

## 📦 Requirements

### Hardware

- NodeMCU (ESP8266)
- USB Data Cable
- LED
- 220Ω Resistor

### Software

- Python 3
- esptool
- mpremote

---

## 🧰 Install Required Tools

Install the required Python packages:

```bash
pip install esptool
pip install mpremote
```

Verify installation:

```bash
esptool version
mpremote --help
```

---

## 📥 Download MicroPython Firmware

Download the latest ESP8266 firmware from:

https://micropython.org/download/ESP8266_GENERIC/

Example firmware:

```text
ESP8266_GENERIC-20260406-v1.28.0.bin
```

Place the downloaded file inside your project folder.

---

## 🧹 Step 1: Erase Existing Firmware

```bash
esptool --chip esp8266 --port /dev/ttyUSB0 erase_flash
```

Expected Output:

```text
Chip erase completed successfully
```

---

## ⚙️ Step 2: Flash MicroPython

```bash
esptool --chip esp8266 --port /dev/ttyUSB0 \
write_flash --flash_mode dio --flash_size 4MB \
0x00000 ESP8266_GENERIC-20260406-v1.28.0.bin
```

---

## 🔌 Step 3: Connect to REPL

```bash
mpremote connect /dev/ttyUSB0 repl
```

Expected Output:

```python
>>>
```

---

## 🧪 Step 4: Test MicroPython

```python
print("MicroPython working")
```

Output:

```text
MicroPython working
```

---

## 💡 Step 5: Built-in LED (GPIO2)

### Code

```python
from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

while True:
    led.off()
    sleep(1)

    led.on()
    sleep(1)
```

---

## 💡 Step 6: External LED on D2 (GPIO4)

### Wiring

```text
D2 (GPIO4) -----> LED (+)
GND -----------> LED (-)

Use a 220Ω resistor.
```

### Code

```python
from machine import Pin
from time import sleep

led = Pin(4, Pin.OUT)

while True:
    led.value(1)
    sleep(1)

    led.value(0)
    sleep(1)
```

---

## 📤 Upload Code to ESP8266

```bash
mpremote connect /dev/ttyUSB0 fs cp main.py :main.py
```

---

## 🔄 Run Program

```bash
mpremote connect /dev/ttyUSB0 reset
```

or press the RESET button.

---

## 🧠 Auto Run Behaviour

When the board boots:

```text
boot.py
   ↓
main.py
```

If `main.py` exists, it runs automatically.

---

## 🛑 Stop Program

Inside REPL:

```text
Ctrl + C
```

---

## 🗑️ Delete Uploaded File

```bash
mpremote connect /dev/ttyUSB0 fs rm main.py
```

---

## ⚠️ Troubleshooting

### REPL Not Working

```bash
fuser -k /dev/ttyUSB0
```

### LED Not Blinking

- Check GPIO pin
- Check LED polarity
- Check wiring

### Garbage Characters

- Wrong boot state
- Reflash MicroPython

---

## ✅ What You Learned

- Installing MicroPython
- Flashing ESP8266
- Using REPL
- Uploading Files
- Auto-running Programs
- Controlling LEDs