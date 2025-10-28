from mcp3021_driver import mcp3021
import time
from adc_plot import plot_voltage_vs_time
from adc_plot import plot_sampling_period_hist

if __name__ == "__main__":
    mcp = mcp3021(5.20)
    voltage_values = []
    time_values = []
    sampling_periods = []
    duration = 3.0
    max_voltage = 5.20


    try:
        start_time = time.time()
        while (time.time() - start_time) < duration:
            voltage = mcp.get_voltage()
            current_time = time.time() - start_time
            voltage_values.append(voltage)
            time_values.append(current_time)
            print(f"Время: {current_time:.2f} c, Напряжение: {voltage:.3f}B")
        plot_voltage_vs_time(time_values, voltage_values, mcp.dynamic_range)
        for i in range(1, len(time_values)):
            sampling_periods.append(time_values[i] - time_values[i - 1])
        plot_sampling_period_hist(sampling_periods)
    finally:
        mcp.deinit()