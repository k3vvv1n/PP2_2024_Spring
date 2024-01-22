
#Get Values

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.values()
print(x) # dict_values(['Ford', 'Mustang', 1964])


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change
#dict_values(['Ford', 'Mustang', 1964])
#dict_values(['Ford', 'Mustang', 2020])


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["color"] = "red"
print(x) #after the change
#dict_values(['Ford', 'Mustang', 1964])
#dict_values(['Ford', 'Mustang', 1964, 'red'])


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.items()
print(x) # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["year"] = 2020
print(x) #after the change
#dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
#dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["color"] = "red"
print(x) #after the change
#dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
#dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'red')])