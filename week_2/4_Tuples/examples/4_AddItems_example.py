
#Add Items

#Convert the tuple into a list, add "orange", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple) #('apple', 'banana', 'cherry', 'orange')


thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple) #('apple', 'banana', 'cherry', 'orange')


