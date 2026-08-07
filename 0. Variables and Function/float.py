x = float(input("Enter a number: "))

print(x,"Normal float") #prints the float as it is

print(f"{x:,}") #prints the float with commas as thousands separators

x = round(x) #rounds the float to the nearest integer 2.5 gets 2 qnd 2.51 gets 3

print(x,"Rounded float") #prints the rounded float

print(f"{x:,.2f}") #prints the rounded float with two decimal places