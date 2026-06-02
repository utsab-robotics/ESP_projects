# 🚀 NodeMCU (ESP8266) Setup with Arduino IDE

This guide walks you through setting up a **NodeMCU (ESP8266)** with the **Arduino IDE**, from installation to uploading your first code.

---

## 📦 Requirements

### Hardware

* NodeMCU (ESP8266)
* USB Cable (data cable)

### Software

* Arduino IDE

---

## 💻 Install Arduino IDE

Download and install Arduino IDE from the official website:

https://www.arduino.cc/en/software

---

## ⚙️ Add ESP8266 Board Support

### 1. Open Preferences

Go to:

```
File → Preferences
```

### 2. Add Board Manager URL

In **Additional Board Manager URLs**, paste:

```
https://arduino.esp8266.com/stable/package_esp8266com_index.json
```

Click **OK**

---

## 📥 Install ESP8266 Board Package

1. Go to:

```
Tools → Board → Boards Manager
```

2. Search for:

```
esp8266
```

3. Install:

```
ESP8266 by ESP8266 Community
```

---

## 🔌 Connect NodeMCU

* Plug your NodeMCU into your computer using USB cable

---

## 🔍 Select Board

Go to:

```
Tools → Board → ESP8266 Boards → NodeMCU 1.0 (ESP-12E Module)
```

---

## 🔗 Select Port

Go to:

```
Tools → Port
```

Select the port (example):

```
/dev/ttyUSB0
```

> On Windows, it may appear as `COM3`, `COM4`, etc.

---

## 🧪 Upload Your First Code

### Example Blink Code

```cpp
#define LED_PIN 2

void setup() {
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_PIN, LOW);  // ON (built-in LED is inverted)
  delay(1000);

  digitalWrite(LED_PIN, HIGH); // OFF
  delay(1000);
}
```

---

## 🚀 Upload the Code

1. Click the **Upload (→)** button in Arduino IDE
2. Wait for the message:

```
Hard resetting via RTS pin...
```

This indicates a successful upload ✅

---

## 💡 Expected Output

* The built-in LED on NodeMCU (D4) will blink every second

---

## ❗ Troubleshooting

### Port not showing

* Reconnect USB cable
* Try different USB port
* Check permissions (Linux):

  ```
  sudo usermod -aG dialout $USER
  ```

  Then log out and log in again

---

### Upload fails

* Press and hold **FLASH/BOOT** button while uploading (if needed)

---

### LED not blinking

* Ensure correct board selected
* Ensure correct pin (GPIO2 for built-in LED)

---

## 🧠 Notes

* Uploading code from Arduino IDE replaces any existing firmware (e.g., MicroPython)
* Only one firmware can run at a time

---

## ✅ Done!

You have successfully:

* Installed Arduino IDE
* Added ESP8266 support
* Connected NodeMCU
* Uploaded your first program 🎉

---
