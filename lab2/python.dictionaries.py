# task 1

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

# task 2

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

# task 3
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"

#task 4
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

# task 5

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

#examples of w3schools

# ex 1
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# ex 2
print(len(thisdict))

# ex 3
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# ex 4
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

# ex 5
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
# ex 6
x = thisdict.get("model")

# ex 7
x = thisdict.keys()

# ex 8
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

# ex 9
x = car.keys()

print(x) #before the change

# ex 10
car["color"] = "white"

print(x) #after the change

# ex 11
x = thisdict.values()

# ex 12
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change


#ex13
x = thisdict.items()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary");

#ex14
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

#ex15
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"});

#ex16
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#ex17
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)


#ex18
for x in thisdict.values():
  print(x);

#ex19
for x in thisdict.keys():
  print(x);


#ex20
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


#ex21
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
#ex22
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}