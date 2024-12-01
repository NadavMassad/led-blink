import gpiozero # type: ignore
from time import sleep

led = gpiozero.LED(17)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
