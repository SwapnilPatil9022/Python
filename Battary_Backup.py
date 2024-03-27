import psutil

def get_battery_backup():
    battery = psutil.sensors_battery()
    if battery is None:
        return "Battery information not available"
    
    percent = battery.percent
    power_plugged = battery.power_plugged
    secs_left = battery.secsleft

    status = "Plugged In" if power_plugged else "Not Plugged In"
    if secs_left != psutil.POWER_TIME_UNLIMITED:
        mins_left = secs_left // 60
        hours = mins_left // 60
        minutes = mins_left % 60
        time_left = f"{hours} hours, {minutes} minutes"
    else:
        time_left = "Calculating..."
    
    return f"Battery: {percent}% | Status: {status} | Time Left: {time_left}"

if __name__ == "__main__":
    print(get_battery_backup())
