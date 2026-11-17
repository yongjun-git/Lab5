import time
from threading import Thread
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
from hal import hal_buzzer as buzzer

CORRECT_PIN = [1, 2, 3, 4]

lcd = LCD.lcd()
pin = []            # digits typed so far
wrong_count = 0     # how many wrong PINs
done = False        # True once unlocked or disabled → ignore keys


def show(line1, line2):
    lcd.lcd_clear()                     # avoid leftover text
    lcd.lcd_display_string(line1, 1)
    lcd.lcd_display_string(line2, 2)


def show_enter_pin():                   # REQ-01
    show("Safe Lock", "Enter PIN: ")


def key_pressed(key):
    global pin, wrong_count, done

    if done:                            # already unlocked/disabled
        return
    if key == '*' or key == '#':        # ignore * and #
        return

    pin.append(key)
    lcd.lcd_display_string("Enter PIN: " + "*" * len(pin), 2)   # REQ-02

    if len(pin) == 4:                   # check after 4th digit
        if pin == CORRECT_PIN:          # REQ-03
            show("Safe Unlocked", "")
            done = True
        else:
            wrong_count = wrong_count + 1
            if wrong_count >= 3:        # REQ-05
                show("Safe Disabled", "")
                done = True
            else:                       # REQ-04
                show("Wrong PIN", "")
                buzzer.turn_on_with_timer(1)   # buzzer 1 s
                time.sleep(1)                  # total 2 s on screen
                show_enter_pin()
        pin = []                        # start a fresh PIN


def main():
    buzzer.init()
    show_enter_pin()

    keypad.init(key_pressed)
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()


if __name__ == "__main__":
    main()