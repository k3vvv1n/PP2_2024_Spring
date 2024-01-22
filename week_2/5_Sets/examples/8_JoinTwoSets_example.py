
#Join Two Sets

#The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3) #{'a', 1, 'c', 3, 'b', 2}


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1) #{'c', 3, 'b', 2, 'a', 1}