"""
#using while loop to print "Meow" 3 times.
i = 0
while i < 3:
    print("Meow")
    i += 1
print("_____________________________________________")

#Simply goes in list and executes as long as there are items in the list.
for _ in [0, 1, 2]:
    print("Meow")
print("_____________________________________________")

#Using range function to print "Meow" 3 times.
for _ in range(3):
    print("Meow")
print("_____________________________________________")

#using multiplication to print "Meow" 3 times.
print("Meow\n" * 3,end="") 

"""

while True:
    num = int(input("How many times meow? "))
    if num >=0:
        break #escapes recent while loop

for _ in range(num):
    print("Meow")
