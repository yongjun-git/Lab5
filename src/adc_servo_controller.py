from hal import hal_adc as adc
from hal import hal_servo as servo

def main():
    adc.init()      # Section 3
    servo.init()    # Section 4

    while(True):
        adc_value = adc.get_adc_value(1)          # potentiometer = channel 1
        angle = 180 - (adc_value * 180 / 1023)    # Figure 3
        print("ADC = " + str(adc_value) + ", angle = " + str(angle))
        servo.set_servo_position(angle)

if __name__ == "__main__":
    main()