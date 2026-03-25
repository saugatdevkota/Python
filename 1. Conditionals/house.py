name = input("Enter your name: ")

"""if name == "Saugat" or name == "Heemanshu":
    print("New-Baneshwor")
elif name == "Pratyush":
    print("Kamalpokhari")
elif name == "Samoyal":
    print("Tinkune")
elif name == "Manjil":
    print("Balkumari")
else:
    print("Who t* are you?")"""

#Short approach match case
match name:
    case "Saugat" | "Heemanshu":
        print("New-Baneshwor")
    case "Pratyush":
        print("Kamalpokhari")
    case "Samoyal":
        print("Tinkune")
    case "Manjil":
        print("Balkumari")
    case _:
        print("Who t* are you?")