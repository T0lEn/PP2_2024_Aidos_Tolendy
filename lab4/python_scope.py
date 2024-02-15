# A variable created outside of a function is global and can be used by anyone:
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

# The function will print the local x, and then the code will print the global x:x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

# If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = 300

myfunc()

print(x)

