def main():
    greet = input("Greetings: ").lower()
    print(value(greet))

def value(g):
    if g[:5]=="hello":
        value=0
    elif g[:1]=="h":
        value = 20
    else:
        value = 100
    return value

if __name__ == "__main__":
    main()
