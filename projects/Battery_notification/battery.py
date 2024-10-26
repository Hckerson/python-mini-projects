# Install dependencies:
# pip install psutil plyer

import psutil
from plyer import notification

def check_battery():
    battery = psutil.sensors_battery()
    
    if battery is None:
        print("Could not retrieve battery information.")
        return

    percent = battery.percent
    plugged = battery.power_plugged

    if percent <= 90 and not plugged:
        notify_low_battery(percent)

def notify_low_battery(percent):
    try:
        notification.notify(
            title="Battery Low",
            message=f"{percent}% Battery remaining!",
            timeout=5  # Notification disappears after 5 seconds
        )
    except Exception as e:
        print(f"Notification failed: {e}")

if __name__ == "__main__":
    check_battery()
