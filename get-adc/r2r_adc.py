import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def number_to_dac(self, number):
        for i in range(8):
            GPIO.output(self.bits_gpio[i], dec2bin(number)[i])

    def sequential_counting_adc(self):
        for value in range (256):
            self.number_to_dac(value)
            time.sleep(self.compare_time)
            compValue = GPIO.input(self.comp_gpio)
            if compValue == 1:
                return value
        return 255

    def get_s_voltage(self):
        digital_value = self.sequential_counting_adc()
        voltage = (digital_value/255)*self.dynamic_range
        return voltage



'''if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.3)

        while True:
            voltage = adc.get_sc_voltage()
            print(f"voltage: {voltage:.3f} V")
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Stopped by the keyboard\n")
    finally:
        adc.deinit()'''

if __name__ == "__main__":
    adc = None
    try:
        adc =R2R_ADC(dynamic_range = 3.3, compare_time = 0.01, verbose = False)
        while True:
            voltage = adc.get_sar_voltage()
            print(f"voltage: {voltage:.3f} V")
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Stopped by the keyboard\n")
    finally:
        adc.deinit()

