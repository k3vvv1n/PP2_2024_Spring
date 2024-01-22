
#Get the Length of a Set

thisset = {"apple", "banana", "cherry"}
print(len(thisset)) #3

#Set Items - Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)

#{'cherry', 'apple', 'banana'}
#{1, 3, 5, 7, 9}
#{False, True}


set1 = {"abc", 34, True, 40, "male"}
print(set1) #{True, 34, 40, 'male', 'abc'}


#It is also possible to use the set() constructor to make a set.
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) #{'apple', 'banana', 'cherry'}

