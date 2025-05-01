import matplotlib.pyplot as plt

def parse_iperf_log(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    times = []
    throughputs = []

    for line in lines:
        if "0.00-" in line and "bits/sec" in line:
            parts = line.strip().split()
            try:
                time = float(parts[2].split('-')[1])  # second value of "0.00-1.00 sec"
                throughput = float(parts[-2])  # throughput value
                unit = parts[-1]
                if unit == "Mbits/sec":
                    throughput *= 1
                elif unit == "Kbits/sec":
                    throughput /= 1000
                elif unit == "Gbits/sec":
                    throughput *= 1000
                times.append(time)
                throughputs.append(throughput)
            except:
                continue
    return times, throughputs

# Parse logs
bbr_time, bbr_tp = parse_iperf_log("bbr.log")
cubic_time, cubic_tp = parse_iperf_log("cubic.log")
reno_time, reno_tp = parse_iperf_log("reno.log")

# Plot
plt.figure(figsize=(10,6))
plt.plot(bbr_time, bbr_tp, label="BBR")
plt.plot(cubic_time, cubic_tp, label="Cubic")
plt.plot(reno_time, reno_tp, label="Reno")
plt.xlabel("Time (s)")
plt.ylabel("Throughput (Mbits/sec)")
plt.title("Throughput Comparison")
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("throughput_comparison.png")
plt.show()

