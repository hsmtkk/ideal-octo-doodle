import datetime
import requests

url = "https://learning.oreilly.com/api/v2/search"
query = "python"
limit = 3
today = datetime.datetime.now()
last_month = today - datetime.timedelta(days=30)
date_format = "%Y-%m-%d"
issued_after = last_month.strftime(date_format)
issued_before = today.strftime(date_format)
params = {
    "query": "python",
    "limit": limit,
    "issued_after": issued_after,
    "issued_before": issued_before,
}
resp = requests.get(url, params=params)
resp.raise_for_status()
with open("first_v2_api.json", "w", encoding="utf-8") as f:
    f.write(resp.text)
