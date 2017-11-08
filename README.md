* pip install esptool
* pip install adafruit-ampy
* esptool.py --port /dev/ttyUSB0 erase_flash
* esptool -p COM27 --baud 115200 write_flash --flash_size=detect 0 esp8266-20170906-v1.9.2-50-g1aaba5ca.bin
* picocom -b115200 -ep /dev/ttyUSB0
* ampy --port /dev/ttyUSB0 put mqtt.py

>>> import network
>>> wlan = network.WLAN(network.STA_IF)
>>> wlan.active(True)
>>> wlan.connect('System@NUS-ISS', 'password-12')
>>> wlan.ifconfig()

http://micropython.org/webrepl/
