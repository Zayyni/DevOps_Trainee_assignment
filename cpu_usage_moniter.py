import psutil
import time

def cpu_usage():
    return psutil.cpu_percent(interval=0.5)

if __name__=="__main__":
    while True:
        cpu_usage_value=cpu_usage()
        print(f"CPU Usage: {cpu_usage_value}%")
        time.sleep(0.5)
