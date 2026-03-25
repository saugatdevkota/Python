exp = input("Enter a arthmetic expression: ")
exp = exp.split(" ", maxsplit=2)

exp[0]=float(exp[0])
exp[2]=float(exp[2])

if exp[1]=="+":
    result = exp[0] + exp[2]
    print(result)
elif exp[1]=="-":
    result = exp[0] - exp[2]
    print(result)
elif exp[1]=="*":
    result = exp[0] * exp[2]
    print(result)
elif exp[1]=="/":
    result = exp[0] / exp[2]
    print(result)
else:
    print("Invalid input")
