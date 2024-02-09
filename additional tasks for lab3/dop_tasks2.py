#task 1
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)

n = int(input())
print(calculate_factorial(n))

#task 2

def reverse_string(s):
    return s[::-1]
input_string = input("Введите строку: ")
print(reverse_string(input_string))

#task 3

def get_max(a, b, c):
    return max(a, b, c)
a = int(input("Первое число: "))
b = int(input("Второе число: "))
c = int(input("Третье число: "))
print(get_max(a, b, c))

#task 4

def is_even(l):
    return l % 2 == 0
l = int(input("Введите число: "))
if is_even(l):
    print("True")
else:
    print("False");

#task 5

def filter_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    return [num for num in numbers if is_prime(num)]

numbers = list(map(int, input()))
print(filter_prime(numbers))

#task 6

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

# Test the function
list1 = list(map(int, input("Enter elements of the first list separated by spaces: ").split()))
list2 = list(map(int, input("Enter elements of the second list separated by spaces: ").split()))
common_elements = find_common_elements(list1, list2)
print("Common elements:", common_elements)

#task 7

def word_frequency(input_string):
    
    words = input_string.split()

    
    frequency_dict = {}

    
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    return frequency_dict


input_string = input("Enter a string: ")
result = word_frequency(input_string)
print("Word frequencies:", result)

#task 8

def fibonacci(n):
    if n <= 0:
        return "Invalid input. n should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test the function
n = int(input("Enter the value of n: "))
print(fibonacci(n))

#task 9

def calculate_running_average(numbers):
    running_sum = 0
    running_averages = []
    for i, num in enumerate(numbers, start=1):
        running_sum += num
        running_averages.append(running_sum / i)
    return running_averages

# Test the function
numbers = list(map(float, input("Enter a series of numbers separated by spaces: ").split()))
running_averages = calculate_running_average(numbers)
print(running_averages)