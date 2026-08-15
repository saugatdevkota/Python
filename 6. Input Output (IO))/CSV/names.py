while True:
    try:
        names=[]
        details=[]
        name = input("Enter Name: ")
        add = input("Enter Address: ")
        with open("names.csv","a") as file:
            details.append(name)
            details.append(",")
            details.append(add)
            names.append(details)
            file.write(name)
            file.write(f",{add}\n")
    except (KeyboardInterrupt, EOFError):
        print("\n\nSaving in file and exiting..")
        break

with open("names.csv") as file:
    for name in file:
        print(name.rstrip())