
#Append Items

#Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) # ["apple", "banana", "cherry", "orange"]


#Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) #["apple", "orange", "banana", "cherry"]


#Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) # ["apple", "banana", "cherry", "mango", "pineapple", "papaya"]


thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) # ["apple", "banana", "cherry", "kiwi", "orange"]