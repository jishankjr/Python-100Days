# # Write a program to pronounce list of names using win32 API.

# import win32com.client
# speaker = win32com.client.Dispatch("SAPI.SpVoice")

# a = 1



# while True:
#     ans = input("Add names?(y/n): ")
#     if ans == 'y':
#       names = input("Name ",a,"- ")
#       a = a + 1
#     else:
#        exit

# for name in names:
#     speaker.Speak(f"Shoutout to {name}")

import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
names = []
while True:
    a = 0
    ans = input("Add names? (y/n): ")
    if ans == 'y':
        name = input(f"Enter name {a + 1}: ")
        names.append(name)
    elif ans == 'n':
        break
    else:
        print("Invalid input, please enter 'y' or 'n'.")

for name in names:
    speaker.Speak(f"Shoutout to {name}")
