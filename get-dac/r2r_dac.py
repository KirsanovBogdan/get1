import RPi.GPIO as GPIO


class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_number(self, number, dynamic_range):
        if not (0.0 <= number <= dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} B)")
            print ("Устанавливаем 0.0 В")
            return 0
        return int (number / (dynamic_range - dynamic_range/(2**8))* 255)
    
    def set_voltage(self, voltage, gpio_bits):
        GPIO.output(self.gpio_bits, [int(element) for element in bin(voltage)[2:].zfill(8)])


if __name__ == "__main__":
    try:
        dac = R2R_DAC([16,20,21,25,26,17,27,22], 3.11, True)
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах:"))
                number = dac.set_number(voltage, 3.11)
                dac.set_voltage(number, [16,20,21,25,26,17,27,22])

            except ValueError:
                print ("Вы ввели не число. Попробуйте ещё раз \n")
    finally:
        dac.deinit()