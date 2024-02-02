#task 1

x = lambda a : a;

#example 1

x = lambda a : a + 10
print(x(5));

#example 2
x = lambda a, b : a * b
print(x(5, 6));

#example 3

def myfunc(n):
  return lambda a : a * n;

#example 4

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11));

#example 5

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11));

