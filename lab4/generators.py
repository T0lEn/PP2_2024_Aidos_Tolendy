#ex1
def generate_squares(N):
    
    for num in range(N):
        yield num ** 2


N = int(input("Enter the value of N: "))


squares_generator = generate_squares(N)


for square in squares_generator:
    print(square);


#ex2

def even_numbers_generator(n):
    
    for num in range(n + 1):
        if num % 2 == 0:
            yield num


n = int(input("Enter the value of n: "))


even_gen = even_numbers_generator(n)


print(','.join(map(str, even_gen)))


#ex3

def divisible_by_three_and_four(n):
    
    for num in range(n + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num


n = int(input("Enter the value of n: "))
generator = divisible_by_three_and_four(n)


for num in generator:
    print(num);


#ex4

def squares(a, b):
    
    for num in range(a, b + 1):
        yield num ** 2


a = int(input("Enter the starting number (a): "))
b = int(input("Enter the ending number (b): "))

print("Squared numbers from", a, "to", b, ":")
for square in squares(a, b):
    print(square);


#ex5

def countdown(n):
    
    while n >= 0:
        yield n
        n -= 1


n = int(input("Enter the value of n: "))

print("Countdown from", n, "to 0:")
for number in countdown(n):
    print(number)
