# task 1

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x);

# task 2

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue

  print(x);

# task 3

for x in range(6):
  print(x);

# task 4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break

  print(x);


#examples 1

for x in range(2, 6):
  print(x);

#example 2

for x in range(2, 30, 3):
  print(x);

#example 3

for x in range(6):
  print(x)
else:
  print("Finally finished!");

#example 3

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!");

#example 4
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y);

#examples 5
for x in [0, 1, 2]:
  pass;