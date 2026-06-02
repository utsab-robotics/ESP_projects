# from machine import Pin
# from time import sleep

# led = Pin(2, Pin.OUT)   # built-in LED (safe test)

# while True:
#     led.off()
#     sleep(1)
#     led.on()
#     sleep(1)

from machine import Pin
from time import sleep

led = Pin(4, Pin.OUT)   # D2 = GPIO4

while True:
    led.value(1)   # ON
    sleep(1)
    led.value(0)   # OFF
    sleep(1)