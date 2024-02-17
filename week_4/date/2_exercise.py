import datetime

x = datetime.datetime.now()
y = datetime.timedelta(days=1)

print("yesterday:", (x - y).strftime("%x"))
print("today:", x.strftime("%x"))
print("tomorrow:", (x + y).strftime("%x"))
