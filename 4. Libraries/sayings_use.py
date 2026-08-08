import sys
from sayings import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])
else:
    print("Please provide a name as a command line argument.")
    sys.exit(1)