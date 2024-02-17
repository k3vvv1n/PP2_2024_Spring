import datetime

u = datetime.datetime.now()
y= datetime.timedelta(days=5)

print("Today:", u.strftime("%x"))
print("Five days ago:", (u-y).strftime("%x"))