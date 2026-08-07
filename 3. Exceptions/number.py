# user can input string or number, if user inputs string then it will throw ValueError
while True:
    try:
        x = int(input("Enter a number: "))
        # break #u can also use break here unstead of else, but else is more readable and better practice
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    else:
        break

print(f"x is {x}")