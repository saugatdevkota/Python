#for verticsal obstacles
"""
def main():
    print_column(3)

def print_column(n):
    for _ in range(n):
        print("#")

main()
"""

#for horizontal obstacles
"""
def main():
    print_row(4)

def print_row(length):
    for _ in range(length):
        print("#", end="")

main()
"""

# for rectangular obstacles
def main():
    print_rectangle(3, 4)

def print_rectangle(row, column):
    for _ in range(row):
        for _ in range(column):
            print("#", end="")
        print()

main()

print("-----------")

#same rectangular but using more and simpler functions
def main():
    print_rectangle(4,5)

def print_rectangle(row, column):
    for i in range(row):
        print_row(column)

def print_row(column):
    for i in range(column):
        print("#", end="")
    print()

main()