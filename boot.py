# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
import webrepl
import dht
import machine
from mqtt import MQTTClient
import time
import ssd1306

webrepl.start()
d = dht.DHT22(machine.Pin(2))
client = MQTTClient("ISSNEST", "m12.cloudmqtt.com",user="kqcqutsu", password="MP86zXZ6Zkds", port=13743)
client.connect()
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    time.sleep(2) 
    d.measure()
    x = str(d.temperature())
    y = str(d.humidity())
    client.publish(topic="kqcqutsu/feeds/temperature", msg=x)
    time.sleep(1) 
    client.publish(topic="kqcqutsu/feeds/humidity", msg=y)
    time.sleep(1)
    oled.fill(0)
    oled.text('Temperature:' + x, 0, 0)
    oled.text('Humidity: ' + y, 0, 10)
    oled.show()
    
gc.collect()