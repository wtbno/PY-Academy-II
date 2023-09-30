def multiply(*args):
    total = 5
    for number in args:
        total *= number
    return total


multiplication = multiply(1, 2, 3, 4, 5)
print(multiplication)
