gro_dict = {}
while True:
    try:
        item = input().upper()
    except EOFError:
        pass
        break
    else:
        if item in gro_dict:
            gro_dict[item] +=1
        else:
            gro_dict[item] =1

for item in sorted(gro_dict):
    print(f"{gro_dict[item]} {item}")
