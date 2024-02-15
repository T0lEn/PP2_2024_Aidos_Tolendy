#ex1
def greeting(name):
  print("Hello, " + name);

#ex2
import mymodule

mymodule.greeting("Jonathan")

#ex3
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

#ex4
import mymodule as mx

a = mx.person1["age"]
print(a)


#ex5
import platform

x = platform.system()
print(x)


