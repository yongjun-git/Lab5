import time
from hal import hal_lcd as LCD

def main():
    lcd = LCD.lcd()
    lcd.lcd_clear()

    show_colon = True

    while True:
        local_time = time.localtime()

        if show_colon:
            time_string = time.strftime("%H:%M:%S", local_time)   # 14:05:09
        else:
            time_string = time.strftime("%H %M %S", local_time)   # 14 05 09

        date_string = time.strftime("%d:%m:%Y", local_time)       # 17:11:2026

        lcd.lcd_display_string(time_string, 1)
        lcd.lcd_display_string(date_string, 2)

        show_colon = not show_colon    # flip for next second
        time.sleep(1)                  # REQ-01: update every 1 second

if __name__ == "__main__":
    main()