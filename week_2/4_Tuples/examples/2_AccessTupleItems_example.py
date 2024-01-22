
#Access Tuple Items

thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) # banana


#Negative Indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) #cherry


#Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) #('cherry', 'orange', 'kiwi')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4]) #('apple', 'banana', 'cherry', 'orange')


#Range of Negative Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1]) #('orange', 'kiwi', 'melon')


#Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple: #True
  print("Yes, 'apple' is in the fruits tuple")