from machine import Pin, I2C
import mcu
import ssd1306

gpio = mcu.gpio()
i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.fill(0)
oled.text("Hello", 0, 0)
oled.text("World", 0, 10)
oled.show()
