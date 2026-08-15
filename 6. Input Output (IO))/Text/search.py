names = []
search = input("Enter name to search: ").strip().title()

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

result = False
for i,name in enumerate(names):
    i+=1
    if name == "Saugat":
        result = True
        number = i
        
if result:
    print(f"{search} found in line: {number}")
else:
    print("Name not found....")


    # print("Hello,",name)