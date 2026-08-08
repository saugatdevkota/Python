import requests
import sys
import json

if len(sys.argv) != 2:
    print("Please provide artist name as a command line argument.")
    sys.exit(1)

url = f"https://itunes.apple.com/search?entity=song&limit=50&term={sys.argv[1]}"
response = requests.get(url)
# print(json.dumps(response.json(), indent=4))
o = response.json()
# trackname = o["results"][0]["trackName"]
# print(trackname)
for result in o["results"]:
    print(result['trackName'])
