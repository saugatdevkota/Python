with open("names.txt", "a") as file:
    while True:
        try:
            name = input("What is your name? ").strip().title()
            file.write(f"{name}\n")
        except (EOFError, KeyboardInterrupt):
            print("\n.....Printing and Exiting....\n")
            break

"""
with open("names.txt","r") as file:
    # lines = file.readlines()
    for line in sorted(file):
        print(f"Hello, {line}".rstrip())
"""


