import requests
from bs4 import BeautifulSoup
import json
import time

def scrape_news():
    url = "https://www.forexfactory.com/calendar"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        news_data = []
        rows = soup.find_all("tr", class_="calendar_row")
        
        for row in rows:
            currency_tag = row.find("td", class_="calendar__currency")
            if not currency_tag:
                continue
                
            currency = currency_tag.text.strip()
            # We want major pairs
            if currency in ["USD", "EUR", "GBP", "AUD", "JPY", "CAD", "NZD", "CHF"]:
                actual = row.find("td", class_="calendar__actual").text.strip() or "---"
                forecast = row.find("td", class_="calendar__forecast").text.strip() or "---"
                previous = row.find("td", class_="calendar__previous").text.strip() or "---"
                event = row.find("td", class_="calendar__event").text.strip()
                time_val = row.find("td", class_="calendar__time").text.strip()
                
                # Impact Logic
                impact_tag = row.find("span", class_="icon--ff-impact")
                impact = "Low"
                if impact_tag:
                    impact_str = str(impact_tag).lower()
                    if 'high' in impact_str: impact = "High"
                    elif 'medium' in impact_str: impact = "Medium"

                # Better than expected logic (simplified)
                better = None
                actual_cell = row.find("td", class_="calendar__actual")
                if actual_cell:
                    if "better" in actual_cell.get("class", []): better = True
                    elif "worse" in actual_cell.get("class", []): better = False

                news_data.append({
                    "time": time_val,
                    "currency": currency,
                    "event": event,
                    "actual": actual,
                    "forecast": forecast,
                    "prev": previous,
                    "impact": impact,
                    "betterThanExpected": better
                })
                
        with open('news_feed.json', 'w') as f:
            json.dump(news_data, f, indent=2)
        print(f"Successfully scraped {len(news_data)} events.")

    except Exception as e:
        print(f"Error scraping news: {e}")

if __name__ == "__main__":
    scrape_news()
