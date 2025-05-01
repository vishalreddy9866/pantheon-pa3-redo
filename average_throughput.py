def get_average(filepath):
    with open(filepath) as f:
        lines = f.readlines()
    values = []
    for line in lines:
        if "0.00-" in line and "bits/sec" in line:
            try:
                val = float(line.strip().split()[-2])
                unit = line.strip().split()[-1]
                if unit == "Mbits/sec":
                    val *= 1
                elif unit == "Kbits/sec":
                    val /= 1000
                elif unit == "Gbits/sec":
                    val *= 1000
                values.append(val)
            except:
                continue
    return sum(values)/len(values) if values else 0

print("BBR avg:", get_average("bbr.log"))
print("Cubic avg:", get_average("cubic.log"))
print("Reno avg:", get_average("reno.log"))

