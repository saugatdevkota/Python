text = input("Enter a camel case: ")
new_word = ""

for each in text:
    if each.isupper():
        new_word = new_word + "_" + each.lower()
    else:
        new_word = new_word + each

print(new_word)
