def main():
    x = int(input("Enter a number to square: "))
    print(f"The square of {x} is {square(x)}")

def square(n):
    return n ** 2

if __name__ == "__main__":
    main()