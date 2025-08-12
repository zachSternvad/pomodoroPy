import time
import datetime

def countdown(h, m, s):
    total_seconds = h * 3600 + m * 60 +s
    
    while total_seconds > 0:
        timer = datetime.timedelta(seconds = total_seconds)
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
        
    print("Brrrrr! NO MORE TIME!")
    
h = input("How many hours: ")
m = input("How many minutes: ")
s = input("How many seconds: ")
countdown(int(h), int(m), int(s))