import RPi.GPIO as GPIO
import time
import math

def get_sin_wave_amplitude(freq, time):
    return (math.sin(2 * math.pi * freq * time) + 1)/2

def wait_for_sampling_period(sampling_frequency):
    time.sleep(float(1 / sampling_frequency))

def get_triangle_wave_amplitude(freq, time):
    x = float(freq * time)
    return 2 * abs(float(x - int(x + 0.5)))