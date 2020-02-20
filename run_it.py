from addition import addition
from multiplication import multiplication
from division import division
from subtraction import subtraction

num_1 = int(input("Please insert your first number: "))
num_2 = int(input("Please insert your second number: "))
operation = input("Please insert your operation ")

if operation == "x" or operation == "X" or operation == "*":
    print(multiplication(num_1, num_2))
elif operation == "+":
    print(addition(num_1, num_2))
elif operation == "-":
    print(subtraction(num_1, num_2))
elif operation == "/":
    print(division(num_1, num_2))
else:
    print("You are trying to break my calculator")
