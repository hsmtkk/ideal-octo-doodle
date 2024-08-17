import json
import requests
import os.path

with open("second_v1_api.json") as f:
    loaded = json.load(f)

chapter_urls = loaded["chapters"]
print(chapter_urls)

for chapter_api_url in chapter_urls:
    resp = requests.get(chapter_api_url)
    resp.raise_for_status()
    decoded = resp.json()
    chapter_content_url = decoded["content"]
    filename = decoded["filename"]

    resp = requests.get(chapter_content_url)
    resp.raise_for_status()
    path = os.path.join("chapters", filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(resp.text)
