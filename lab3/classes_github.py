#task 1
class StringManipulator:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())


manipulator = StringManipulator()
manipulator.getString()
manipulator.printString()

#task 2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

length = float(input("Enter the length of the square: "))
square = Square(length)

print("Area of Shape:", Shape().area())
print("Area of Square:", square.area())

#task 3

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


length = float(input("Введите длину: "))
width = float(input("Введите ширину: "))
rectangle = Rectangle(length, width)


print("Area of Rectangle:", rectangle.area())

#task 4

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        distance = (dx**2 + dy**2)**0.5
        return distance


x1 = float(input())
y1 = float(input())
point1 = Point(x1, y1)

x2 = float(input())
y2 = float(input())
point2 = Point(x2, y2)


point1.show()
point2.show()


distance = point1.dist(point2)
print(distance)


new_x = float(input())
new_y = float(input())
point1.move(new_x, new_y)
point1.show()

#task 5

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} accepted. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} accepted. Current balance: {self.balance}")


owner = input("Enter the account owner's name: ")
initial_balance = float(input("Enter the initial balance: "))
account = BankAccount(owner, initial_balance)


num_deposits = int(input("Enter the number of deposits: "))
for _ in range(num_deposits):
    amount = float(input("Enter deposit amount: "))
    account.deposit(amount)

num_withdrawals = int(input("Enter the number of withdrawals: "))
for _ in range(num_withdrawals):
    amount = float(input("Enter withdrawal amount: "))
    account.withdraw(amount)

#task 6

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


numbers = [int(x) for x in input().split()]


prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Prime numbers in the list:", prime_numbers)
