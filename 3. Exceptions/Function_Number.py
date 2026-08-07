# def main():
#     print(f"x is {get_number()}")

# def get_number():
#     while True:
#         try:
#             x = int(input("Enter a number: "))
        
#         except ValueError:
#             print("PLease enter a valid integer.")
#         else:
#             return x
# main()

def main():
    print(f"x is {get_number("What is your number? ")}")

def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass #instead of printing error message, we can use pass to ignore the error and continue the loop

            #print("Invalid input. Please enter a valid integer.")

main()

# learned concepts try and except block, while loop, function with parameter, return statement, pass statement and prompt 