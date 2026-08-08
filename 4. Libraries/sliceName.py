import sys
#  if len(sys.argv) < 3:
#      print("Too few arguments")

for arg in sys.argv[1:]:
    print("Hello, " + arg + "!")

#trying to remove an item from the list
list = ["saugat", "indu", "dikshya", "deepak"]
reverse_list = list[::-1]
list2 = list.pop(2)
print(list)
print("removed item:", list2)
print("reversed list:", reverse_list)