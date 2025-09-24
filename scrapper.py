import requests
import json
import time

URL = "https://www.reddit.com/r/malaysia.json?limit=100"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(URL, headers=headers)
data = response.json()

results = []
after = None

for i in range(10):
    params = {"limit": 100, "after": after}
    response = requests.get(URL, headers=headers, params=params)
    data = response.json()

    post = data["data"]["children"]
    for p in post:
        post_data = p["data"]
        title = post_data["title"]
        image = post_data.get("url_overridden_by_dest")

        if image and (image.endswith(".jpg") or image.endswith(".png") or image.endswith(".gif")):
            results.append({"title": title, "image_url": image})

    after = data["data"]["after"]
    if not after:
        break

    time.sleep(1)

with open("output.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"Saved {len(results)} posts with images to output.json")