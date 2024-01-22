
#Copy a Dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


#Make a copy of a dictionary with the dict() function:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}