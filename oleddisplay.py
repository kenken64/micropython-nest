import ssd1306
import machine
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)
oled.text('Hello', 0, 0)
oled.text('World', 0, 10)
oled.show()