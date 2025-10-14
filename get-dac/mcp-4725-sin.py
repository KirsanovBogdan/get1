import mcp4725_driver as mcp4725
from signal_generator import get_sin_wave_amplitude, wait_for_sampling_period
import time

amplitude = 2
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    try:
        dac = mcp4725.MCP4725(5.16, 0x61, True)

        while True:
            dac.set_voltage(amplitude * get_sin_wave_amplitude(signal_frequency, time.time()))
            wait_for_sampling_period(sampling_frequency)
    finally:
        dac.deinit()