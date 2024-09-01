import requests
from bs4 import BeautifulSoup
from lib.db.models import Car, Manufacturer, session

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
    car_details['price'] = soup.find(i, class_= 'icon-cd_R').text
    return car_details

def save_car_details_to_db(car_details):
    if not car_details:
        return

    manufacturer_name = car_details['manufacturer']
    car_name = car_details['name']
    car_price = car_details['price']
    car_power = car_details['power']

    manufacturer = session.query(Manufacturer).filter_by(name=manufacturer_name).first()
    if not manufacturer:
        manufacturer = Manufacturer(name = manufacturer_name)
        session.add(manufacturer)
        session.commit()

    car = Car(name= car_name, price = car_price, power = car_power)
    session.add(car)
    session .commit()
