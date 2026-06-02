🐍 MicroPython Installation on NodeMCU (ESP8266)
📦 Install Required Tools

Install the tools needed to flash and communicate with the ESP8266:

pip install esptool
pip install mpremote

Verify installation:

esptool version
mpremote --help
📥 Download MicroPython Firmware

Download the latest ESP8266 firmware from the official MicroPython website:

Official Firmware Download Page

https://micropython.org/download/ESP8266_GENERIC/

For example, you may download a file similar to:

ESP8266_GENERIC-20260406-v1.28.0.bin

Save the downloaded .bin file in your project folder.

Example:

ESP_Project/
│
├── ESP8266_GENERIC-20260406-v1.28.0.bin
├── main.py
└── boot.py
🧹 Step 1: Erase Existing Firmware

Connect your NodeMCU and find the serial port.

Linux:

ls /dev/ttyUSB*

Typical output:

/dev/ttyUSB0

Erase the flash memory:

esptool --chip esp8266 --port /dev/ttyUSB0 erase_flash

Expected output:

Chip erase completed successfully
⚙️ Step 2: Flash MicroPython Firmware

Navigate to the folder containing the downloaded firmware.

Run:

esptool --chip esp8266 --port /dev/ttyUSB0 \
write_flash --flash_mode dio --flash_size 4MB \
0x00000 ESP8266_GENERIC-20260406-v1.28.0.bin

If successful, you'll see:

Hash of data verified.
Leaving...
Hard resetting via RTS pin...
🔌 Step 3: Open the MicroPython REPL

Connect to the REPL (interactive terminal):

mpremote connect /dev/ttyUSB0 repl

You should see:

MicroPython v1.xx on ESP8266

>>>
🧪 Step 4: Verify MicroPython

Inside the REPL, type:

print("MicroPython working")

Output:

MicroPython working

Congratulations! MicroPython is installed correctly.

💡 Step 5: Test the Built-in LED (GPIO2)

Create a file named main.py:

from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

while True:
    led.off()      # LED ON
    sleep(1)

    led.on()       # LED OFF
    sleep(1)

Note: On most NodeMCU boards, the built-in LED uses inverted logic (Active LOW).

💡 Step 6: Test an External LED on D2 (GPIO4)
Wiring
NodeMCU D2 (GPIO4) ─── 220Ω ───► LED (+)

NodeMCU GND ───────────────────► LED (-)
Code
from machine import Pin
from time import sleep

led = Pin(4, Pin.OUT)

while True:
    led.value(1)
    sleep(1)

    led.value(0)
    sleep(1)
📤 Step 7: Upload Code to ESP8266

Upload main.py:

mpremote connect /dev/ttyUSB0 fs cp main.py :main.py

Verify uploaded files:

mpremote connect /dev/ttyUSB0 fs ls

Example output:

boot.py
main.py
🔄 Step 8: Run the Program

Reset the board:

mpremote connect /dev/ttyUSB0 reset

Or press the RESET button on the NodeMCU.

🤖 Auto-Run Behavior

MicroPython automatically executes:

boot.py
↓
main.py

every time the board powers on or resets.

If main.py exists, it starts automatically.

🛑 Stop a Running Program

Inside REPL:

Ctrl + C

This interrupts the running script.

🗑️ Delete a File from ESP8266

Remove main.py:

mpremote connect /dev/ttyUSB0 fs rm main.py

Remove boot.py:

mpremote connect /dev/ttyUSB0 fs rm boot.py
⚠️ Troubleshooting
REPL Not Opening

Check if another application is using the serial port:

fuser -k /dev/ttyUSB0

Then reconnect:

mpremote connect /dev/ttyUSB0 repl
Permission Denied

Add your user to the dialout group:

sudo usermod -aG dialout $USER

Logout and login again.

Board Not Detected

Check available ports:

ls /dev/ttyUSB*

or

ls /dev/ttyACM*
LED Not Blinking

Verify:

Correct GPIO number
LED polarity
Wiring connections
220Ω resistor used
✅ What You Learned
Installing esptool and mpremote
Downloading official MicroPython firmware
Flashing ESP8266
Using the REPL
Uploading files
Running MicroPython programs
Controlling the built-in LED
Controlling an external LED
Managing files on the ESP8266

This structure is much easier to follow in a README because every step is clearly separated and includes the expected output and purpose.