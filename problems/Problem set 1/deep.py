a = input("What's the answer to the Great Question of Life, the Universe and Everything? ")
a=a.strip().lower()
if a=="42" or a=="forty-two" or a=="forty two":
    print("Yes")
else:
    print("NO")