#task 1

class MyClass:
    x = 5;

#task 2

class MyClass:
    x = 5;
p1 = MyClass()

#task 3

class MyClass:
    x = 5;
p1 = MyClass()
print(p1.x);

#task 4
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age;

#example 1

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age);

#example 2
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1);

#example 3

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1);


#example 4

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc();

#example 5

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc();

#example 6

del p1.age;

