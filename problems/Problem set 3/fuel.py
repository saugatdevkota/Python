def main():
    percent = get_percentage()
    if percent <=1:
        print("E")
    elif percent >=99:
        print("F")
    else:
        print(f"{percent}%")

def get_percentage():
    while True:
        fraction = input("Enter fraction i.e x/y: ")
        try:
            x,y = fraction.split("/")
            x= int(x)
            y= int(y)
            if x<0 or y<=0 or x>y:
                continue
            return round(100*x/y)

        except (ValueError, ZeroDivisionError):
            pass

main()
