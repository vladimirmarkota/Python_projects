import time
import winsound

users_time = int(input("Enter seconds: "))

for x in range(users_time, 0, -1):
    seconds = x % 60
    minutes = (x // 60) % 60
    hours = (x // 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

def beep():
    winsound.Beep(700, 1000)

beep()
print("Time's up!")
