import matplotlib.pyplot as plt


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
