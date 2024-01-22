
#Functions can Return a Boolean

def myFunction() :
  return True

print(myFunction()) #True

def myFunction() :
  return True

if myFunction(): #True
  print("YES!")
else: #False
  print("NO!")
# isinstance() function, which can be used to determine if an object is of a certain data type:
x = 200
print(isinstance(x, int)) #True -> 200 = integer
