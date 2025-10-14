import RPi.GPIO as gpio

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.pin = gpio_pin
        self.dynamic_range = dynamic_range
        gpio.setmode(gpio.BCM)
        gpio.setup(self.pin, gpio.OUT)
        self.pwm = gpio.PWM(self.pin, pwm_frequency)
        self.pwm.start(0)

    def deinit(self):
        gpio.output(self.pin, 0)
        gpio.cleanup()

    def setvoltage(self, voltage):
        self.pwm.ChangeDutyCycle(voltage/self.dynamic_range * 100)

if __name__ == "__main__":
    dac = PWM_DAC(12, 500, 3.18, True)
    try:
        while True:
            try:
                voltage = float(input("input voltage i Volts: "))
                dac.setvoltage(voltage)
            except ValueError:
                print("incorrect input, try again")
    finally:
        dac.deinit()
