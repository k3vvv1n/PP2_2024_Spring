
#Remove Specified Index

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) #["apple", "cherry"]


#If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) # ["apple", "banana"]


#The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) # ["banana", "cherry"]


thislist = ["apple", "banana", "cherry"]
del thislist # error because we deleted all the elements thislist and thislist