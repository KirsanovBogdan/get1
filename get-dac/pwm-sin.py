import pwm_dac as pwm
from signal_generator import get_sin_wave_amplitude, wait_for_sampling_period
import time

amplitude = 2
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    dac = pwm.pwm_dac(12, 5000, 3.167, True)
    try:
        

        while True:
            dac.set_voltage(amplitude * get_sin_wave_amplitude(signal_frequency, time.time()), 12, 3.167)
            wait_for_sampling_period(sampling_frequency)
    finally:
        dac.deinit()