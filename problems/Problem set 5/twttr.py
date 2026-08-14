def main():
    word = input("Enter any word: ")
    print(shortened(word))

def shortened(word):
    new_word = ""
    for letter in word:
        if letter.lower() not in "aeiou":
            new_word = new_word + letter
    return new_word

if __name__ == "__main__":
    main()
