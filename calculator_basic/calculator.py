num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

op = input("Input operator (*,/,+,-): ")
if op == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif op == "/":
    print(f"{num1} / {num2} = {num1 / num2}")
elif op == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif op == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
else: print("Insert a valid operator")
