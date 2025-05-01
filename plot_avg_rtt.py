import matplotlib.pyplot as plt

# Replace these with your actual RTT values if available
avg_rtt = {
    'BBR': 45.2,
    'Cubic': 65.8,
    'Reno': 83.4
}

# Bar plot
plt.figure(figsize=(8, 6))
plt.bar(avg_rtt.keys(), avg_rtt.values(), color=['blue', 'orange', 'green'])
plt.xlabel('CC Algorithm')
plt.ylabel('Average RTT (ms)')
plt.title('Average RTT Comparison')
plt.tight_layout()
plt.savefig('avg_rtt_bar.png')
plt.show()

