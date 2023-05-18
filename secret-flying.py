import requests
from bs4 import BeautifulSoup
import re

def check_flight_deals():
    response = requests.get("https://www.secretflying.com/search2/?cityFrom=Mainland+Europe%2CUK%2CDublin&cityTo=Asia%2COceania%2CSouth+Korea&month=August+2023%2CJune+2023%2CJuly+2023%2CSeptember+2023")

    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.find_all("article")  # Find all <article> elements

    for article in articles:
        description_element = article.find("p")
        if description_element is not None:
            description = description_element.text.strip()
            match = re.search(r'from (.*?) to (.*?) ([£$€].*?) roundtrip', description)
            if match:
                from_location = match.group(1)
                to_location = match.group(2)
                price = match.group(3)
                print(f"From: {from_location}\nTo: {to_location}\nPrice: {price}\n")

check_flight_deals()
