# Write a python program which reminds you of drinking water every hour or two. Your program can either beep or send desktop notifications for a specific operating system

import time
from plyer import notification

def water_reminder(interval):
    while True:
        notification.notify(
            title="💧 Stay Hydrated!",
            message="It's time to drink water. Take a sip and stay healthy! 💧",
        )
        time.sleep(interval)

if __name__ == "__main__":
    reminder_interval = 360000
    print("Water reminder program started. Stay hydrated! 💧")
    water_reminder(reminder_interval)
