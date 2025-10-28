import matplotlib.pyplot as plt
import RPi.GPIO as GPIO
import time


def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)
    plt.title("Зависимость напряжения от времени")
    plt.xlabel('Время, с')
    plt.ylabel('Напряжеине, В')
    plt.show()

def plot_sampling_period_hist(time):
    sampling_periods = []
    for i in range (1, len(time)):
        period = time[i] - time[i-1]
        sampling_periods.append(period)
    plt.figure(figsize=(10,6))
    plt.hist(sampling_periods)
    plt.title("Распределение периодов дискретизации измерений по времени за одно измерение")
    plt.xlabel('Период измерений, с')
    plt.ylabel('Количество измерений, шт')
    plt.xlim(0, 0.2)
    plt.grid(True, linestyle = '--', alpha = 0.7, axis = 'y')
    plt.legend()
    plt.tight_layout()
    plt.show()

    
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



    def successive_approximation_adc(self):
        left, right = 0 , 256
        while left < right - 1:
            middle = (left+right) // 2
            self.number_to_dac(middle)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio):
                right = middle
            else:
                left = middle
        return left

    def get_sar_voltage(self):
        digital_value = self.successive_approximation_adc()
        voltage = (digital_value/255)*self.dynamic_range
        return voltage




if __name__ == "__main__":
    adc = R2R_ADC(dynamic_range= 3.3, compare_time=0.01, verbose=False)
    voltage_values = []
    time_values =[]
    sampling_periods = []
    duration = 3.0
    try:
        
        start_time = time.time()

        while time.time() - start_time < duration:
            voltage = adc.get_sar_voltage()
            print(f"voltage: {voltage:.3f} V")
            print(f"time: {time.time() - start_time:.3f} s")
            time_values.append(time.time()-start_time)
            voltage_values.append(voltage)

        plot_voltage_vs_time(time_values, voltage_values, adc.dynamic_range)
        plot_sampling_period_hist(time_values)
    except KeyboardInterrupt:
        print("Stopped by the keyboard\n")
    finally:
        adc.deinit()

