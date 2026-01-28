import requests
from bs4 import BeautifulSoup
import json

url = "https://www.forexfactory.com/calendar.php"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

news = []

for row in soup.select("tr.calendar__row"):
    time_el = row.select_one("td.calendar__time")
    currency_el = row.select_one("td.calendar__currency")
    impact_el = row.select_one("td.calendar__impact")
    event_el = row.select_one("td.calendar__event")
    actual_el = row.select_one("td.calendar__actual")
    forecast_el = row.select_one("td.calendar__forecast")
    previous_el = row.select_one("td.calendar__previous")

    if time_el and currency_el and event_el:
        impact_title = impact_el["title"] if impact_el else ""
        # You can map impact to color in frontend:
        # High = red, Medium = orange, Low = yellow
        news.append({
            "time": time_el.text.strip(),
            "currency": currency_el.text.strip(),
            "impact": impact_title.strip(),
            "event": event_el.text.strip(),
            "actual": actual_el.text.strip() if actual_el else "",
            "forecast": forecast_el.text.strip() if forecast_el else "",
            "previous": previous_el.text.strip() if previous_el else ""
        })

# Save JSON
with open("forex_news.json", "w") as f:
    json.dump(news, f, indent=4)

print("Forex news updated!")
