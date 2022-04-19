# _*_ coding: utf-8 _*_
""" LED.py 測試 LED 或簡易的判斷腳位輸出是否正常?
接線: Digital or PWM -> pin 220 電阻 -> LED+ -> LED- -> GND
"""
import utime as time
from machine import Pin

# Arduino setup()
led = Pin(2, Pin.OUT)  # create LED object from pin2, Set Pin2 to output

# Arduino loop()
for _ in range(5):  # 測試 5 次
    led.value(0)    # Set led turn off, 同指令 led.off()
    time.sleep(0.5)
    led.value(1)    # Set led turn on, 同指令 led.on()
    time.sleep(0.5)
