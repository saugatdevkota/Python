#making this as my own library of saying hello and goodbye to the user
import sys
def main():
    if len(sys.argv) == 2:
        hello(sys.argv[1])
        goodbye(sys.argv[1])

def hello(name):
    print(f"Hello, {name}!")

def goodbye(name):
    print(f"Goodbye, {name}!")

if __name__ == "__main__":
    main()