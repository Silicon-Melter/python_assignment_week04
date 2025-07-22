add = lambda x, y:x+y
subtract = lambda x, y:x-y
multiply = lambda x, y:x*y
divide = lambda x, y:x/y

x = int(input("input x: "))
y = int(input("input y: "))
print(f"{x} + {y} = {add(x,y)}")
print(f"{x} - {y} = {subtract(x,y)}")
print(f"{x} * {y} = {multiply(x,y)}")
print(f"{x} / {y} = {divide(x,y):.2f}")
