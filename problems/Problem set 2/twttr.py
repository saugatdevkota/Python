word = input("Enter any word: ")
new_word=""
for letter in word:
    if letter.lower() not in {'a','e','i','o','u'}:
        new_word = new_word + letter

print(new_word)
