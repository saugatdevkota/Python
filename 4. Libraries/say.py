import cowsay
import sys
my_fish = r'''
\
 \  
        /`·.¸
     /¸...¸`:·
 ¸.·´  ¸   `·.¸.·´)
: © ):´;      ¸  {
 `·.¸ `·  ¸.·´\`·¸)
     `\\´´\¸.·´
'''
if len(sys.argv) == 2:
    cowsay.cow("hello!" + sys.argv[1])
    # cowsay.trex("hello!" + sys.argv[1])
    # cowsay.dragon("hello!" + sys.argv[1])
    cowsay.draw("Hello!" + sys.argv[1], my_fish)
