from util.calculator import add as add_def, subtract as subtract_def, multiply as multiply_def, divide as divide_def
from util.string_operations import reverse_string, capitalize_string, lowercase_string, uppercase_string

print("Using calculator.py:")
x = int(input("input x: "))
y = int(input("input y: "))
print(f"{x} + {y} = {add_def(x,y)}")
print(f"{x} - {y} = {subtract_def(x,y)}")
print(f"{x} * {y} = {multiply_def(x,y)}")
print(f"{x} / {y} = {divide_def(x,y):.2f}")

print("\nUsing string_operations.py:")
sample_string = input("input string: ")
print("Original:", sample_string)
print("Reversed:", reverse_string(sample_string))
print("Capitalized:", capitalize_string(sample_string))
print("Lowercase:", lowercase_string(sample_string))
print("Uppercase:", uppercase_string(sample_string))
