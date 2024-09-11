import time

t = time.strftime("%H:%M:%S")
# print(t)
hour = int(time.strftime("%H"))
# print(hour)

if (hour > 0 and hour < 12):
    print("Good Morning Sir!")
elif (hour >= 12 and hour < 17):
    print("Good Afternoon sir")
elif (hour >= 17 and hour < 21):
    print("Good Evening sir")
else:
    print("Good Night sir")
