# _*_ coding: utf-8 _*_
""" LED.py 測試 LED 或簡易的判斷腳位輸出是否正常?
接線: Digital or PWM -> pin 220 電阻 -> LED+ -> LED- -> GND
"""
import time
from machine import Pin

# Arduino setup()
led = Pin(2, Pin.OUT)  # create LED object from pin2, Set Pin2 to output
ms_start = time.ticks_ms()  # 記錄開始測量時間

# Arduino loop()
while time.ticks_diff(time.ticks_ms(), ms_start) < 5000:  # 測試 5 秒
    led.value(1)    # Set led turn on, 同指令 led.on()
    time.sleep(1)
    led.value(0)    # Set led turn off, 同指令 led.off()
    time.sleep(1)
