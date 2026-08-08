import sys
print(type(sys.argv[0]))
print(type(sys.argv[1]))
print(type(sys.argv[2]))

if len(sys.argv) < 3:
    print("Please provide your name and age as command line arguments.")
    sys.exit(1)
elif len(sys.argv) > 3:
    print("Too many arguments provided. Please provide only your name and age.")
    sys.exit(1)

try:
    print("Hello! My name is " + sys.argv[1] + " and I am " + sys.argv[2] + " years old. And, the script name is " + sys.argv[0])
except IndexError:
    sys.exit("Please provide your name and age as command line arguments.")