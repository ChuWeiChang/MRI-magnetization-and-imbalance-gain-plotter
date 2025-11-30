import numpy as np
import matplotlib.pyplot as plt
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Simulate MRI magnetization evolution."
    )

    parser.add_argument(
        "--duration",
        type=int,
        default=4,
        help="Duration in units of TR (default: 4)",
    )
    parser.add_argument(
        "--t1",
        type=float,
        default=1300.0,
        help="T1 in ms (default: 1300)",
    )
    parser.add_argument(
        "--t2",
        type=float,
        default=80.0,
        help="T2 in ms (default: 80)",
    )
    parser.add_argument(
        "--tr",
        type=float,
        default=1000.0,
        help="TR in ms (default: 1000)",
    )
    parser.add_argument(
        "--B0",
        type=float,
        default=3.0,
        help="Main field strength in Tesla (default: 3; only for reference).",
    )
    parser.add_argument(
        "--sample-num",
        type=int,
        default=100,
        help="Number of sample points for plotting (default: 100)",
    )

    return parser.parse_args()

def plot(config, time_all, longitudinal, transverse):
    x_ticks = [t * config["tr"] for t in range(0, config["duration"] + 2)]

    plt.figure()

    # you may comment/uncomment one the following two lines to show the individual plots
    plt.plot(time_all, longitudinal, label="M_z (Longitudinal)", color="blue")
    plt.plot(time_all, transverse, label="M_xy (Transverse)", color="red", alpha=0.8)

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
    m0 = config["B0"]
    t1_r = lambda x: m0 * (1 - np.exp(-x / config["t1"]))
    t2_r = lambda x: m0 * np.exp(-x / config["t2"])

    # initial time samples for the first [-TR, 0]  interval
    time_all = list(np.linspace(0, config["tr"], config["sample_num"]))
    longitudinal = [1] * config["sample_num"]
    transverse = [0] * config["sample_num"]

    for t in range(0, config["duration"]):
        time = np.linspace(0, config["tr"], config["sample_num"])
        mz = t1_r(time)
        mxy = t2_r(time)

        time_all.extend(list(time + (t+1) * config["tr"]))
        longitudinal.extend(mz / config["B0"])
        transverse.extend(mxy / config["B0"])
        m0 = mz[-1]
    plot(config, time_all, longitudinal, transverse)

def main():
    args = parse_args()
    config = {
        "duration": args.duration,
        "t1": args.t1,
        "t2": args.t2,
        "tr": args.tr,
        "B0": args.B0,  # doesn't affect the normalized plot
        "sample_num": args.sample_num,
    }
    calc_magnetization(config)

if __name__ == '__main__':
    main()