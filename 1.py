import numpy as np
import matplotlib.pyplot as plt


def plot(config, time_all, mag_all):
    x_ticks = [t * config["tr"] for t in range(0, config["duration"] + 2)]
    plt.plot(time_all, mag_all)
    plt.xticks(
        x_ticks,
        ['–TR', '0'] + [f'{i}TR' for i in range(1, len(x_ticks) - 1)]
    )
    plt.xlabel("Time")
    plt.ylabel("M_z / M0")
    plt.title("Longitudinal Magnetization (T1 Recovery)")
    plt.grid(True)
    plt.show()

def calc_longitudinal(config):
    m = config["M0"]
    t1_r = lambda x: m * (1 - np.exp(-x / config["t1"]))

    time_all = list(np.linspace(0, config["tr"], config["sample_num"]))
    mag_all = [1] * config["sample_num"]
    for t in range(0, config["duration"]):
        time = np.linspace(0, config["tr"], config["sample_num"])
        mag = t1_r(time)
        time_all.extend(list(time + (t+1) * config["tr"]))
        mag_all.extend(mag / config["M0"])
        m = mag[-1]
    plot(config, time_all, mag_all)

def calc_transverse(config):
    plot(config, time_all, mag_all)

def main():
    config = {
        "duration": 4,
        "t1": 1300,
        "t2": 80,
        "tr": 1000,
        "M0": 3,
        "sample_num": 100
    }
    calc_longitudinal(config)

if __name__ == '__main__':
    main()