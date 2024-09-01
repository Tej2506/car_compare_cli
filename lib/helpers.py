import requests
from bs4 import BeautifulSoup

def scrape_car_details(manufacturer, car_name):
    manufacturer_search_query = brand.replace(" ", "-").lower()
    car_name_search_query = car_name.replace(" ", "-").lower()
    url = f"https://www.cardekho.com/{manufacturer_search_query}/{car_name_search_query}"

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve data fro {car_name}")
        return None

    soup = BeautifulSoup(response.text,'html.parser')
    car_details = {}
    car_details['name'] = soup.find('h1', class_='thcHeading').text
    car_details['manufacturer'] = manufacturer
    car_details['power'] = soup.find('td', class_= 'iconsname').text
    return car_details
