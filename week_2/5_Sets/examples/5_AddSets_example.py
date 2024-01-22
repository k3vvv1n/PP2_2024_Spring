
#Add Sets

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset) #{'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}


#Add Any Iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset) #{'banana', 'cherry', 'apple', 'orange', 'kiwi'}

