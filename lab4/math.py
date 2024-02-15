#ex1
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

#ex 2

x = abs(-7.25)

print(x)

#ex3

x = pow(4, 3)

print(x)

#ex4

import math

x = math.sqrt(64)

print(x)

#ex5

import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

#ex6

import math

x = math.pi

print(x)

#exercise github

import math

def degrees_to_radians(degrees):
    
    return degrees * (math.pi / 180)


degrees = float(input("Enter the degree value: "))
radians = degrees_to_radians(degrees)
print(f"{degrees} degrees is equal to {radians} radians.")


#ex2

def trapezoid_area(a, b, h):
    
    return 0.5 * (a + b) * h


a = float(input("(a): "))
b = float(input("(b): "))
h = float(input("(h): "))


area = trapezoid_area(a, b, h)


print("The area of the trapezoid is:", area)


#ex3

import math

def regular_polygon_area(n, s):
    
    return (n * s ** 2) / (4 * math.tan(math.pi / n))


n = int(input("Enter the number of sides: "))
s = float(input("Enter the length of each side: "))


area = regular_polygon_area(n, s)


print("The area of the regular polygon is:", area)

#ex4

def parallelogram_area(base, height):
    return base * height

base = float(input())
height = float(input())

area = parallelogram_area(base, height)

print("The area of the parallelogram is:", area)