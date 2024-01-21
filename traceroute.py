# Hakan Duran 150200091

import subprocess
import re
import statistics

def tracert(IP):

    delays = []

    for i in range(10):
        output = subprocess.check_output(["tracert", IP], universal_newlines=True)

        delay = None

        for line in output.split('\n'):
            match = re.search(r"(\d+) ms", line)
            if match:
                delay = int(match.group(1))

        if delay is not None:
            delays.append(delay)
            print(f"{i+1}. delay: {delay}")

    if delays:
        min_delay = min(delays)
        max_delay = max(delays)
        avg_delay = statistics.mean(delays)

        return min_delay, max_delay, avg_delay
    else:
        return None, None, None

if __name__ == "__main__":

    IP_list = ["161.9.89.79","193.255.0.141","193.140.0.149","81.212.217.121","212.156.104.150","172.217.169.206","151.101.194.216","23.185.0.1","62.115.55.17","62.67.19.66"]
    city_list = ["localhost","Istanbul","Ankara","Denizli","Zonguldak","California","UK","Canada","Sweden","Germany"]

    for i in range(10):
        IP = str(IP_list[i])
        print("")
        print(f"\t{IP} - {city_list[i]}")
        print("")

        minimum, maximum, average = tracert(IP)

        if average is not None:
            print(f"Minimum: {minimum} ms")
            print(f"Maximum: {maximum} ms")
            print(f"Average: {average} ms")
        else:
            print("Failed.")
