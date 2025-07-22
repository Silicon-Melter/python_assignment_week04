def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


def multiply(x, y):
    return x*y


def divide(x, y):
    return x/y


x = int(input("input x: "))
y = int(input("input y: "))
print(f"{x} + {y} = {add(x,y)}")
print(f"{x} - {y} = {subtract(x,y)}")
print(f"{x} * {y} = {multiply(x,y)}")
print(f"{x} / {y} = {divide(x,y):.2f}")
