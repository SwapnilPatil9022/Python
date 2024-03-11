import psutil
import time

def monitor_cpu(interval=5):
    while True:
        cpu_percent = psutil.cpu_percent(interval=interval)
        print(f"CPU Usage: {cpu_percent}%")
        # Add your logic here, like sending data to a database or triggering alerts based on CPU usage
        time.sleep(interval)

if __name__ == "__main__":
    monitor_cpu()
