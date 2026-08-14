from pyfiglet import Figlet
import sys
import random
figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    font = random.choice(fonts)

elif len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit(1)

    if sys.argv[2] not in fonts:
        sys.exit(1)

    font = sys.argv[2]


else:
    sys.exit(1)

text = input("Input: ")
figlet.setFont(font=font)
print(figlet.renderText(text))

