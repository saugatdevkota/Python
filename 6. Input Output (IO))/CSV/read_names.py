details = []
with open("names.csv") as file:
    for line in file:
        name, address = line.rstrip().split(",")
        details.append([name, address])

# for detail in details:
#     print(detail)
for detail in details:
    print(detail)
    