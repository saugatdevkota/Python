def main():
    x = int(input("Enter a number: "))
    print(f"The square of {x} is",squared(x))

def squared(num):
    return num * num

main()