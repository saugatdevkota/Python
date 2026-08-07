def main():
    x= input_x()
    y= input_y()
    percent = round(x/y)
    if percent <=1:
        print("E")
    elif percent >=99:
        print("F")
    else:
        print(f"{percent}%")

def input_x():
    while True:
        try:
            return int(input("Enter Numerator: "))
        except ValueError:
            pass

def input_y():
    while True:
        try:
            return int(input("Enter Denominator: "))
        except ValueError:
            print("Enter integer: ")
        except ZeroDivisionError:
            print("denominator cannot be zero")


main()