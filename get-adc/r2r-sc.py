from adc_plot import plot_sampling_period_hist
from adc_plot import plot_voltage_vs_time
from r2r_adc import R2R_ADC
import time


if __name__ == "__main__":

    voltage_values = []
    time_values =[]
    duration = 3.0
    try:
        adc = R2R_ADC(3.3)
        start_time = time.time()

        while time.time() - start_time < duration:
            voltage = adc.get_sc_voltage()
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

