def main():
    t = input("What time is it now: ").strip()
    if 7 <= convert(t) <= 8:
        print("breakfast time")
    elif 12 <= convert(t) <=13:
        print("lunch time")
    elif 18 <= convert(t) <= 19:
        print("dinner time")
    else:
        print("Chill its not a meal time")

def convert(time):
    time = time.split(":",maxsplit=1)
    time[0]=int(time[0])
    time[1]=int(time[1])
    return time[0] + (time[1]/60)


if __name__ == "__main__":
    main()
