from addition import addition as add
from multiplication import multiplication as m
from division import division as d
from subtraction import subtraction as s

num_1 = input("Please insert your first number: ")
num_2 = input("Please insert your second number: ")
operation = input("Please insert your operation")

if operation == "x" or operation == "X" or operation == "*":
    print(m(num_1, num_2))
elif operation == "+":
    print(add(num_1, num_2))
elif operation == "-":
    print(s(num_1, num_2))
elif operation == "/":
    print(d(num_1, num_2))
else:
    print("You are trying to break my calculator")