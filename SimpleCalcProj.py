operator = input("Enter operator: +, -, *, /: ")
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

if operator == "+":
    result = num1 + num2
    print(round(result))

elif operator == "-":
    result = num1 - num2
    print(round(result))

elif operator == "/":
    result = num1 / num2
    print(round(result))

elif operator == "*":
    result = num1 * num2
    print(round(result))

else:
    print("Invalid operator")


