import time

t = time.strftime("%H:%M:%S")
hour = int(time.strftime('%H'))
print(t)

if(hour > 5 and hour < 12):
    print("Good Morning...\nHave a nice day")
elif(hour > 12 and hour < 17):
    print("Good Afternoon...")
elif(hour > 17 and hour < 20):
    print("Good Evening...")
else:
    print("Good Night...\nGood Night, Sweet Dream & Take Care...")

