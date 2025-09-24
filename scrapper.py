import requests
import json

URL = "https://www.reddit.com/r/malaysia.json?limit=100"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(URL, headers=headers)
data = response.json()

print(json.dumps(data, indent=2))