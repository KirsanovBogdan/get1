import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 1
signal_frequency = 1
sampling_frequency = 10

if __name__ == "__main__":
    try:
        dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.167, True)

        while True:
            dac.setvoltage(amplitude * sg.get_sin_wave_amplitude(signal_frequency, time.time()))
            sg.wait_for_sampling_period(sampling_frequency)
    finally:
        dac.deinit()