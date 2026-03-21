a = input("Enter a string: ")
print(a,"Normal string") #prints the string as it is

a=a.strip() #removes leading and trailing spaces
print(a,"String after strip()") #prints the string after removing leading and trailing spaces

a=a.capitalize() #capitalizes the first letter of the string
print(a,"String after capitalize()") #prints the string after capitalizing the first letter

a=a.title() #capitalizes the first letter of each word in the string
print(a,"String after title()") #prints the string after capitalizing the first letter of each word

a=a.upper() #converts the string to uppercase
print(a,"String after upper()") #prints the string after converting to uppercase

a=a.lower() #converts the string to lowercase
print(a,"String after lower()") #prints the string after converting to lowercase