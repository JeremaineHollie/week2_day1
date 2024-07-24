# Task 1, 2, & 3

# if operation == "add":
#    add(num_1, num_2)


num1 = input("Welcome to the calculator! What is the first number in your operation?" )
num2 = input("Great! What is the second number?" )
operation = input("Great! What operation would you like to use? Please type add, subtract, multiply, or divide!")
num1 = int(num1)
num2 = int(num2)
if operation == ('add'):
    print(num1 + num2)
elif operation == ('subtract'):
    print(num1 - num2)
elif operation == ('multiply'):
    print(num1 * num2)
elif operation == ('divide'):
    if num2 != 0:
        print(num1 / num2)
    else:
        print(0)
    



