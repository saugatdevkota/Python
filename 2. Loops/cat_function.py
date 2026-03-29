def main(): #main function
    num = get_number()
    meow(num)

def get_number(): #to get the number of times to meow
    while True:
        n=int(input("No. of times should I meow? "))
        if n>0:
            return n

def meow(n): #to print meow n times
    for _ in range(n):
        print("Meow")

main()