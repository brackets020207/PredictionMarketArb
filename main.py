import requests
import json
cursor = ""
event_tickers = []
data = {}
while True:
    url = f"https://trading-api.kalshi.com/trade-api/v2/events?status=open&limit=200&cursor={cursor}"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    
    data = json.loads(response.content)
    for event_dict in data["events"]:
        event_tickers.append(event_dict["event_ticker"])
        cursor = data['cursor']
    if (cursor == ""):
        break
print(event_tickers)

for e_ticker in event_tickers:
    url = f"https://trading-api.kalshi.com/trade-api/v2/markets?status=open"
    headers = {"accept": "application/json",
               "Authorization": "INSERT TOKEN"}
    response = requests.get(url, headers=headers)
    data = json.loads(response.content)
    print(data)

    

