
#Set

thisset = {"apple", "banana", "cherry"}
print(thisset)


thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) #('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')


thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset) #{True, 2, 'banana', 'cherry', 'apple'}


thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset) #{False, True, 'cherry', 'apple', 'banana'}


