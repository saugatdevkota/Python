x = float(input("Enter a number: "))
print(x,"Normal float") #prints the float as it is

x = round(x) #rounds the float to the nearest integer
print(x,"Rounded float") #prints the rounded float
print(f"{x:,}")
print(f"{x:,.2f}") #prints the rounded float with two decimal places