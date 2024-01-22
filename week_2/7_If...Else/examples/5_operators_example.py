
#And
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
#Both conditions are True
  

#Or
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
#At least one of the conditions is True
  

#Nota = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
#a is NOT greater than b
  

#Nested If
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
#Above ten,
#and also above 20!
    

#The pass Statement
a = 333
b = 200
if b > a:
  pass
# having an empty if statement like this, would raise an error without the pass statement