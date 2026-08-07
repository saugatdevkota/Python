def main():
    want = input("Do you want to add, subtract, multiply, divide or find remainder? (Type 'add', 'subtract', 'multiply', 'divide' or 'remainder'): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if want == "add":
        print(f"{add(num1,num2):.0f}")

    elif want == "subtract":
        print(f"{subtract(num1,num2):.0f}")
    
    elif want == "multiply":
        print(f"{multiply(num1,num2):.0f}")

    elif want == "divide":
        print(f"{divide(num1,num2):.1f}")

    elif want == "remainder":
        print(f"{remainder(num1,num2):.2f}")

    else:
        print("Invalid input. Please try again.")

def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2

def remainder(num1,num2):
    return num1 % num2

main()