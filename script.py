import requests
from bs4 import BeautifulSoup
import re

# Checks the premium economy flight deals from London
def check_flight_deals():
    response = requests.get("https://speedbird.online/fares.php?view=LowestFares&Selection=Lowest_PremiumFares")
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find_all("table")[3]
    flight_deals = get_flight_deals(table)
    print_flight_deals(flight_deals)

# Read the data
def get_flight_deals(table):
    rows = table.find_all("tr")[1:]
    flight_deals = []
    for row in rows:
        data = row.find_all("td")
        date = data[4].text.strip().lower()
        if not is_valid_month(date):
            continue
        price = data[2].text.strip()
        if not is_under_1000(price):
            continue
        flight_deals.append(data)
    return flight_deals

# Helper functions

def is_valid_month(date):
    return any(month in date for month in ["april", "june", "july", "august", "december"])

def is_under_1000(price):
    price_value = float(re.sub(r"[^\d.]", "", price))
    return price_value < 1000

def print_flight_deals(flight_deals):
    headers = ["Airport", "Location", "Return Fare", "Cost / TP", "Book for"]
    print(" | ".join(headers))
    for deal in flight_deals:
        print(" | ".join([datum.text.strip() for datum in deal]))


check_flight_deals()
