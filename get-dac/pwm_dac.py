import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

class pwm_dac:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 0)

        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        self.pwm.start(0)
    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()
    def set_voltage(self, voltage, gpio_pin, dynamic_range):
        if not (0.0 <= voltage <= dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} B")
            print ("Устанавливаем 0.0 В")
            return 0
        duty_cycle = (voltage / self.dynamic_range) * 100
        self.pwm.ChangeDutyCycle(duty_cycle)

if __name__ == "__main__":
    dac = pwm_dac(12, 500, 3.285, True)
    try:
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage, 12, 3.285)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
    

    finally:
        dac.deinit()


