# Output: Sum of two numbers
#        Difference of two numbers
#        Product of two numbers

def basic_operations():
    a = int(input("First Number: "))
    b = int(input("Second Number: "))
    print("Sum is", a + b)
    print("Difference is", a - b)
    print("Product is", a * b)


# Output: Integer division of two numbers
#         Floor division of two numbers


def dividing_operations():
    a = int(input("First Number: "))
    b = int(input("Second Number: "))
    print("Integer division is", a // b)
    print("Floor division is", a / b)


# Output: Get square of every number until n


def get_square():
    n = int(input("Number: "))
    for i in range(0, n):
        print(i * i)


# Output: Print list of integers from 1 to n side by side


def print_integers_by_range():
    n = int(input("Number: "))
    for i in range(1, n+1):
        print(i, end='')
