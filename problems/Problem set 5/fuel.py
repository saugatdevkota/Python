def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    text = gauge(percentage)
    print(text)


def convert(fraction):
    x, y = fraction.split("/")
    x, y = int(x), int(y)

    if y == 0:
        raise ZeroDivisionError

    if x < 0 or y < 0 or x > y:
        raise ValueError

    return round((x / y) * 100)


def gauge(percent):
    if percent <= 1:
        return "E"
    elif percent >= 99:
        return "F"
    else:
        return f"{percent}%"


if __name__ == "__main__":
    main()
