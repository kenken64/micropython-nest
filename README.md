* pip install esptool
* pip install adafruit-ampy
* esptool -p COM27 --baud 115200 write_flash --flash_size=detect 0 esp8266-20170906-v1.9.2-50-g1aaba5ca.bin
* picocom -b115200 -ep /dev/ttyUSB0
* ampy --port /dev/ttyUSB0 put mqtt.py
