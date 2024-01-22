
#Remove Item

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset) #{'apple', 'cherry'}


thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset) #{'cherry', 'apple'}


thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #removed item
print(thisset) #the set after removal 
#banana
#{'apple', 'cherry'}


thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) #set()


thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) #this will raise an error because the set no longer exists


