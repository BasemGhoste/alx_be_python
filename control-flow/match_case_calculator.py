# User order number
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the secund number: "))

# Requesting a calculation from the user
operation = input("Choose the operation (+, -, *, /): ")

# Match case for obvious reason
match operation:
    case '+':
        result = num1 + num2
        print(f"The result is: {result}.")
    case '-':
        result = num1 - num2
        print(f"The result is: {result}.")
    case '*':
        result = num1 * num2
        print(f"The result is: {result}.")
    case '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result is: {result}.")
        else:
            print("Cannot divide by zero.")
    case _:
        print("Invalid operation selected.")



