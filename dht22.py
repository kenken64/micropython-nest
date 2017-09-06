import dht
import machine
d = dht.DHT22(machine.Pin(2))
d.measure()
d.temperature()
d.humidity()