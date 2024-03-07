# ex1
from functools import reduce
import operator

def multiply_list(numbers):
    if not numbers:
        return None
    result = reduce(operator.mul, numbers)
    return result

input_str = input("Enter numbers separated by spaces: ")
numbers_list = [int(num) for num in input_str.split()]
result = multiply_list(numbers_list)
print(result)


# ex2

def count_upper_lower(input_string):
    upper_count = sum(1 for char in input_string if char.isupper())
    lower_count = sum(1 for char in input_string if char.islower())
    return upper_count, lower_count

input_str = input("Enter a string: ")

upper_count, lower_count = count_upper_lower(input_str)

print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)


# ex3

def is_palindrome(input_string):
    return input_string == input_string[::-1]

input_str = input("Enter a string: ")

if is_palindrome(input_str):
    print("Palindrome")
else:
    print("Not a palindrome")


#ex4

import time
import math

def square_root_after_milliseconds(number, milliseconds):
    time.sleep(milliseconds / 1000)  
    result = math.sqrt(number)
    return result

number = int(input("Enter the number: "))
milliseconds = int(input("Enter the milliseconds: "))

sqrt_result = square_root_after_milliseconds(number, milliseconds)

print(f"Square root of {number} after {milliseconds} milliseconds is {sqrt_result}")


#ex5

def all_elements_true(input_tuple):
    return all(input_tuple)


sample_tuple = (True, True, True)
result = all_elements_true(sample_tuple)
print(result)  

sample_tuple = (True, False, True)
result = all_elements_true(sample_tuple)
print(result)  

