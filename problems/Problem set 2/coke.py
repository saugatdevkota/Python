amount_due = 50
while True:
    inserted_money = int(input("Enter money in cents 25, 10 or 5 cents: "))

    if inserted_money in {5, 10, 25}:
        amount_due = amount_due - inserted_money

    if amount_due <= 0:
        print("Change Owed:", abs(amount_due))
        break

    else:
        print("Amount Due:", amount_due)