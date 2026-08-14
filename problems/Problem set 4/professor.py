import random


def main():
    level = get_level()
    score = 0

    for i in range(10):
        times = 0
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        while True:
            try:
                ans = int(input(f"{x} + {y} = "))

                if ans == answer:
                    score+=1
                    break
                elif ans != answer:
                    times+=1
                    print("EEE")

                if times == 3:
                    print(f"{x} + {y} = {answer}")
                    break

            except ValueError:
                print("EEE")
                pass
    print("Score:", score)




def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in {1,2,3}:
                return level
        except ValueError:
            pass



def generate_integer(level):
    if level == 1:
        return random.randint(0,9)

    elif level == 2:
        return random.randint(10,99)

    elif level == 3:
        return random.randint(100,999)

    else:
         raise ValueError



if __name__ == "__main__":
    main()
