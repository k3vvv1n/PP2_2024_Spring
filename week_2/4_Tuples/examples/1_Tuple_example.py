
#Tuple

thistuple = ("apple", "banana", "cherry")
print(thistuple) # ('apple', 'banana', 'cherry')


#Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) # 3


#Create Tuple With One Item
thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


#It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)