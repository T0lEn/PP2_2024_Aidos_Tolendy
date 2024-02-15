# ExampleGet your own Python Server
# Return an iterator from a tuple, and print each value:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))


# Strings are also iterable objects, containing a sequence of characters:

mystr = "banana"

miyt = iter(mystr)

print(next(miyt))
print(next(miyt))
print(next(miyt))
print(next(miyt))
print(next(miyt))
print(next(miyt))

#Iterate the values of a tuple:

tuplee = ("apple", "banana", "orange")

for x in tuplee:
    print(x);

#Iterate the characters of a string:

strchik = "banana"
for x in strchik:
    print(x);


# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.)

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


# Stop after 20 iterations:
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)