# key = 6d6ccda4d2b81c4ec67b182fa33fa7c4af674135fa30010b458871f16e4fdcf6
import sys
import json
import requests

if len(sys.argv) <2:
    sys.exit("Missing command-line argument")

try:
    float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

quantity = float(sys.argv[1])

url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=6d6ccda4d2b81c4ec67b182fa33fa7c4af674135fa30010b458871f16e4fdcf6"
response = requests.get(url)
# print(json.dumps(response.json(), indent=4))

o = response.json()
price = float(o["data"]["priceUsd"])
total = price * quantity
print(f"${total:,.4f}")

