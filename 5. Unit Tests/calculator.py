def main():
    x=get_x()
    y=get_y()
    what = input("Operation: 1. Add 2. Subtract 3. Multiply 4. Divide choose 1-4: ")
    ans = calculate(x,y,what)
    print(f"{ans}")

def get_x():
    while True:
        try:
            x = int(input("x: "))
            return x
        except ValueError:
            pass

def get_y():
    while True:
        try:
            y = int(input("y: "))
            return y
        except ValueError:
            pass

def calculate(x,y,operation):
    if operation == "1":
        return x + y
    elif operation == "2":
        return x - y
    elif operation == "3":
        return x * y
    elif operation == "4":
        return (f"{x / y:.4f}") if y != 0 else "Error: Division by zero"

if __name__ == "__main__":
    main()