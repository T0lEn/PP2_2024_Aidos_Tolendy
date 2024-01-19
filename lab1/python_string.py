#exercise 1
x = "Hello World"
print(len(x))

#exercise 2
txt = "Hello World"
x = txt[0]

#exercise 3
txt = "Hello World"
x = txt[2:5]

#exercise 4
txt = "Hello World"
x = txt.strip()

#exercise 5
txt = "Hello World"
txt = txt.upper()

#exercise 6
txt = "Hello World"
txt = txt.lower()

#exercise 7
txt = "Hello World"
txt = txt.replace("H", "J")

#exercise 8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


#examples from w3schools


a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Get the character at position 1
a = "Hello, World!"
print(a[1]) 


for x in "banana":
  print(x);


a = "Hello, World!"
print(len(a));


txt = "The best things in life are free!"
print("free" in txt);

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.");


txt = "The best things in life are free!"
print("expensive" not in txt);


txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.");


#Get the characters from position 2 to position 5
b = "Hello, World!"
print(b[2:5])

# Get the characters from the start to position 5

b = "Hello, World!"
print(b[:5])


# Get the characters from position 2, and all the way to the end

b = "Hello, World!"
print(b[2:])


# Getting the characters:

# From: "o" in "World!" (position -5)

# To, but not included: "d" in "World!" (position -2)


b = "Hello, World!"
print(b[-5:-2])

# The upper() method returns the string in upper case

a = "Hello, World!"
print(a.upper())


# The lower() method returns the string in lower case

a = "Hello, World!"
print(a.lower())

# The strip() method removes any whitespace from the beginning or the end
a = " Hello, World! "
print(a.strip())

# The replace() method replaces a string with another string

a = "Hello, World!"
print(a.replace("H", "J"))

# The split() method splits the string into substrings if it finds instances of the separator
a = "Hello, World!"
print(a.split(","))

#example The format() method takes unlimited number of arguments, and are placed into the respective placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


# The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."


