import json
import requests

with open("first_v2_api.json") as f:
    loaded = json.load(f)

the_book = loaded["results"][0]

title = the_book["title"]
cover_url = the_book["cover_url"]
web_url = the_book["web_url"]
print(f"{title=}")
print(f"{cover_url=}")
print(f"{web_url=}")

v1_url = the_book["url"]

resp = requests.get(v1_url)
resp.raise_for_status()

with open("second_v1_api.json", "w", encoding="utf-8") as f:
    f.write(resp.text)
