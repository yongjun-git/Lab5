from hal import hal_led as led
from threading import Thread
from time import sleep

from hal import hal_keypad as keypad

delay = 0    # 0 = LED off, 1 = blink every 1 second

def led_thread():
    global delay

    while(True):
        if delay != 0:
            led.set_output(20, 1)
            sleep(delay)
            led.set_output(20, 0)
            sleep(delay)
        else:
            sleep(0.1)    # rest, so the CPU is not kept busy

def led_control_init():
    led.init()  
    global delay

    t1 = Thread(target=led_thread)
    t1.start()

    # Start blinking every 1 second (delay = 0 keeps the LED off)
    delay = 0