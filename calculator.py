# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform the calculation based on the operation
result = None
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero is not allowed!")
else:
    print("Error: Invalid operation entered!")

# Print the result if calculation was successful
if result is not None:
    print(f"The result of {num1} {operation} {num2} is: {result}")