import emoji
def main():
    output = input_emoji()
    print(f"Output: {output}")

def input_emoji():
    user_input = input("Input: ")
    return emoji.emojize(user_input, language='alias')

if __name__ == "__main__":
    main()