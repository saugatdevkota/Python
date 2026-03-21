name = input("Enter your name: ")
print("Hello " + name + "!") #no space as + concatenates two strings without space

print("Hello, ", name, "!") #no need extra space as , prints out two arguments separated by space

print("Hello, ", end="") #end="" means no new line after print statement
print(name)

print(f"Hello {name}!") #formatted string, we can directly use variable inside the string with {}

#to print quotes we can use escape character \ before the quote
print("Hey its me \"Saugat\"")

