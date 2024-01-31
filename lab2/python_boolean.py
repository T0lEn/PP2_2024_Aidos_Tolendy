#task 1

print(10 > 9)

True

#task 2

print(10 == 9)

False

#task3

print(10 < 9)

False

#task 4

print(bool("abc"))

True

#task 5

print(bool(0))

False


#examples

#ex1
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a");


#ex2
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#ex3
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))



#ex4
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")