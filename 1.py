import numpy as np
import matplotlib.pyplot as plt

def plot(config, time_all, longitudinal, transverse):
    x_ticks = [t * config["tr"] for t in range(0, config["duration"] + 2)]

    plt.figure()

    # you may comment/uncomment one the following two lines to show the individual plots
    plt.plot(time_all, longitudinal, label="M_z (Longitudinal)", color="blue")
    plt.plot(time_all, transverse, label="M_xy (Transverse)", color="red")

    plt.xticks(
        x_ticks,
        ['–TR', '0'] + [f'{i}TR' for i in range(1, len(x_ticks) - 1)]
    )
    plt.xlabel("Time")
    plt.ylabel("Magnetization / M0")

    plt.title("Magnetization (T1 & T2)")
    plt.grid(True)
    plt.legend()
    plt.show()

def calc_magnetization(config):
    m = config["M0"]
    t1_r = lambda x: m * (1 - np.exp(-x / config["t1"]))
    t2_r = lambda x: m * np.exp(-x / config["t2"])

    # initial time samples for the first [-TR, 0]  interval
    time_all = list(np.linspace(0, config["tr"], config["sample_num"]))
    longitudinal = [1] * config["sample_num"]
    transverse = [0] * config["sample_num"]

    for t in range(0, config["duration"]):
        time = np.linspace(0, config["tr"], config["sample_num"])
        mz = t1_r(time)
        mxy = t2_r(time)

        time_all.extend(list(time + (t+1) * config["tr"]))
        longitudinal.extend(mz / config["M0"])
        transverse.extend(mxy / config["M0"])
        m = mz[-1]
    plot(config, time_all, longitudinal, transverse)

def main():
    config = {
        "duration": 4,
        "t1": 1300,
        "t2": 80,
        "tr": 1000,
        "M0": 3, # doesn't affect the normalized plot
        "sample_num": 100 # for smooth curves
    }
    calc_magnetization(config)

if __name__ == '__main__':
    main()