
#Change a Range of Item Values

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) # ["apple", "blackcurrant", "watermelon", "orange", "kiwi", "mango"]


thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) # ["apple", "blackcurrant", "watermelon", "cherry"]


thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) # ["apple", "banana", "watermelon", "cherry"]


