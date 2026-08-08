import random
cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
random.shuffle(cards)
names = ["Saugat", "Indu", "Dikshya", "Deepak"]
for i in range(4):
    random_cards = random.sample(cards, 3)
    cards = [item for item in cards if item not in random_cards]
    print(f"{names[i]}: {random_cards}")
