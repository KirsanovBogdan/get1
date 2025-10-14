import pwm_dac as pwm
from signal_generator import get_sin_wave_amplitude, wait_for_sampling_period
import time

amplitude = 3.1
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    try:
        dac = pwm.PWM_DAC(12, 500, 3.18, True)

        while True:
            dac.setvoltage(amplitude * get_sin_wave_amplitude(signal_frequency, time.time()))
            wait_for_sampling_period(sampling_frequency)
    finally:
        dac.deinit()