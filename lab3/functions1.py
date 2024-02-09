#task 1
def convert(grams):
    ounces = 28.3495231 * grams
    return ounces

grams = int(input("Введите кол-во грамм "))
ounces = convert(grams)
print(ounces)


#task 2

def equivalent(f):
    c = (5 / 9) * (f - 32)
    return c
f = int(input("Введите f: "))
c = equivalent(f)
print(c)
#task 3

def solve(numheads, numlegs):
    num_rabbits = (numlegs - 2 * numheads)/2
    num_chickens = numheads - num_rabbits
    if num_rabbits >= 0 and num_chickens >= 0 and num_rabbits.is_integer() and num_chickens.is_integer():
        return int(num_chickens), int(num_rabbits)
    else:   
        return "nothing"
numheads = 35
numlegs = 94
result = solve(numheads, numlegs)
print(result)

#task 4
def filter_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    return [num for num in numbers if is_prime(num)]

input_str = input("Введите числа через пробел: ")
numbers = list(map(int, input_str.split()))
print(filter_prime(numbers))

#task 5
def permutations(string):
    
    def generate_permutations(prefix, remaining):
        if len(remaining) == 0:
            print(prefix)  
        else:
            for i in range(len(remaining)):
                
                new_prefix = prefix + remaining[i]
                new_remaining = remaining[:i] + remaining[i + 1:]
                generate_permutations(new_prefix, new_remaining)

    generate_permutations('', string)


user_input = input("Enter a string: ")


permutations(user_input)

#task 6

def reverse_string(s):
    return s[::-1]
input_string = input("Введите строку: ")
print(reverse_string(input_string))

#task 7

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

nums = [int(x) for x in input("Введите числа: ").split()]
result = has_33(nums)
print(result)

#task 8
def spy_game(nums):
    has_0 = False
    has_00 = False

    for num in nums:
        if num == 0:
            if not has_0:
                has_0 = True
            elif has_0 and not has_00:
                has_00 = True
        elif num == 7:
            if has_0 and has_00:
                return True

    return False

nums = [int(x) for x in input().split()]
result = spy_game(nums)
print(result)

#task 9
def sphere_volume(radius):
    pi = 3.14  
    volume = (4/3) * pi * (radius ** 3)
    return volume


radius = float(input("Enter the radius of the sphere: "))
volume = sphere_volume(radius)
print("The volume of the sphere is:", volume)

#task 10

def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

input_list = [int(x) for x in input().split()]
result = unique_elements(input_list)
print(result)

#task 11
def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]

word = input()
if is_palindrome(word):
    print("True")
else:
    print("False")

#task 12 

def histogram(numbers):
    for num in numbers:
        print('*' * num)


numbers = [int(x) for x in input("Enter a list of integers separated by spaces: ").split()]


histogram(numbers)

#task 13 
import random

def guess_the_number():
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    secret_number = random.randint(1, 20)
    guesses_taken = 0

    while True:
        guess = int(input("Take a guess.\n"))
        guesses_taken += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break

# Call the function to play the game
guess_the_number()