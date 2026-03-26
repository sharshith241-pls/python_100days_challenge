import time
timestamp=(time.strftime('%H:%M:%S'))
print(timestamp)
hour=int(time.strftime('%H'))
min=time.strftime('%M')
sec=time.strftime('%S')
if(2 <= hour < 12):
    print("Good Morning")
if(12 <= hour <= 17):
    print("Good Afternoon")
if(17 < hour < 20):
    print("Good Evening")
