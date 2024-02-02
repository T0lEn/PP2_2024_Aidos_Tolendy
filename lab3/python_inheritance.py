#task 1

class Student(Person)
    
#task2

class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()

#example 1

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname();

#example 2

class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.;
    c;

#example 3
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname);

#example 4
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname);

#example 5
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019;

#example 6

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019);

#example 7

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear);

