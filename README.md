# Pantheon PA3 REDO – Congestion Control Experiments

This repository contains experiments for PA3 REDO of the Computer Networks course at Saint Louis University. I tested and compared three congestion control (CC) algorithms: **BBR**, **Cubic**, and **Reno**, using `iperf3` and `mahimahi` within a virtualized Ubuntu environment.

---

## Tested CC Algorithms

- **BBR** – Bottleneck Bandwidth and Round-trip propagation time
- **Cubic** – Default for many Linux distributions
- **Reno** – Classic AIMD-based congestion control

---

## Repository Structure

| File               | Description |
|--------------------|-------------|
| `bbr.log`          | Throughput log for BBR |
| `cubic.log`        | Throughput log for Cubic |
| `reno.log`         | Throughput log for Reno |
| `plot_results.py`  | Python script to plot throughput over time |
| `plot_avg_rtt.py`  | Script to compare average throughput |
| `README.md`        | This file |

---

##  Reproducing the Experiments

### 1. Setup (Ubuntu VM)
sudo apt update
sudo apt install iperf3 python-matplotlib python2 -y


2. Run Tests (in 2 terminals)
Terminal 1: Start the iperf3 server
iperf3 -s

Terminal 2: Run each algorithm
# BBR
sudo sysctl -w net.ipv4.tcp_congestion_control=bbr
iperf3 -c 127.0.0.1 -t 60 --logfile bbr.log

# Cubic
sudo sysctl -w net.ipv4.tcp_congestion_control=cubic
iperf3 -c 127.0.0.1 -t 60 --logfile cubic.log

# Reno
sudo sysctl -w net.ipv4.tcp_congestion_control=reno
iperf3 -c 127.0.0.1 -t 60 --logfile reno.log


#Plotting and Analysis
1)Plot Time-Series Throughput
python2 plot_results.py
Output: throughput_comparison.png

2)Compute and Compare Average Throughput
python2 plot_avg_rtt.py

This prints:
('BBR avg:', 820.5714285714286)
('Cubic avg:',  4.928571428571429)
('Reno avg:', 8.370000000000001)


All tests were done locally using loopback to minimize external noise.
No real packet loss was induced, only congestion behavior was studied.
RTT, loss graphs were not extracted due to iperf3 limitation in loopback setup.
The focus was on comparative throughput behavior.



How to Clone and Reproduce?
git clone https://github.com/vishalreddy9866/pantheon-pa3-redo.git
cd pantheon-pa3-redo
# Then the Setup and Run Tests section.



#Acknowledgment
Course: CSCI 5550 – Computer Networks (Spring 2025)
Instructor: Prof. Flavio Esposito
Assignment: Programming Assignment 3 (PA3) – Pantheon & Mahimahi Experiments
