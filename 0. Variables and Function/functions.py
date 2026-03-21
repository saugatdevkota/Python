"""
def hello(to="world"):
    print(f"Hello, {to}!")
    
name = input("Enter your name: ")
hello()
"""
def main():
    name = input("Enter your name: ")
    hello(name)
    hello()
    
def hello(to="world"):
    print(f"Hello, {to}!")

main()