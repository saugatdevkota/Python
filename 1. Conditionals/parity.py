def main():
    number = int(input("Enter a number: "))
    if parity(number):
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

def parity(n):
    return n % 2 == 0
    
    # return True if n % 2 == 0 else False

    #if n % 2 == 0:
    #    return True
    #else:
    #    return False

main()