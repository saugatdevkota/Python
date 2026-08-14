def main():
    name = input("Enter your name: ")
    print(hello(name))
    hello()

def hello(to = "World"):
    ans= f"Hello, {to}"
    return ans

if __name__ == "__main__":
    main()