# task 1


def my_function():
  print("Hello from a function");

# task 2

def my_function():
  print("Hello from a function")

my_function()

# task 3

def my_function(fname, lname):
  print(fname);

# task 4

def my_function(x):
  
    return x + 5;

# task 5

def my_function(*kids):
  print("The youngest child is " + kids[2]);

#task 6

def my_function(**kid):
  print("His last name is " + kid["lname"]);


#example 1

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes");

#example 2

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus");

#example 3

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus");

#example 4

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes");

#example 5

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil");

#example 6

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits);

#example 7

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9));

#example 8

def myfunction():
  pass;

#example 9 

def my_function(x, /):
  print(x)

my_function(3);

#example 10

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8);

#example 11

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6);


