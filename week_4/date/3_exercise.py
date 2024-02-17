import datetime

x = datetime.datetime.now()
y = x.replace(microsecond=0)

#print() x.strftime("%X"))
print(y)
