import requests
from bs4 import BeautifulSoup
from db.models import Car, Manufacturer, session

def scrape_car_details(manufacturer, car_name):
    manufacturer_search_query = manufacturer.replace(" ", "-").lower()
    car_name_search_query = car_name.replace(" ", "-").lower()

    url = f"https://www.cardekho.com/{manufacturer_search_query}/{car_name_search_query}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers = headers)
    if response.status_code != 200:
        print(f"Failed to retrieve data fro {car_name}")
        return None

    soup = BeautifulSoup(response.text,'html.parser')
    car_details = {}
    car_details['name'] = car_name
    car_details['manufacturer'] = manufacturer
    car_details['price'] = soup.find('div', class_= 'price').text.split('Rs.')[1].split('*')[0]
    tr_elements = soup.find('div', class_="qccontent").find_all('tr')
    car_specs=["Engine", "Power", "Torque"]
    
    for row in tr_elements:
        car_spec = row.find_all('td')[0].text.strip()
        car_spec_value = row.find_all('td')[1].text.strip()
        if car_spec in car_specs:
            car_details[car_spec] = car_spec_value
    
    return car_details

def save_car_details_to_db(car_details):
    if not car_details:
        return

    manufacturer_name = car_details['manufacturer']
    car_name = car_details['name']
    car_price = car_details.get('price') 
    car_power = car_details.get('Power')
    car_engine = car_details.get('Engine')
    car_torque = car_details.get('Torque')
    

    manufacturer = session.query(Manufacturer).filter_by(name=manufacturer_name.lower()).first()
    if not manufacturer:
        manufacturer = Manufacturer(name = manufacturer_name)
        session.add(manufacturer)
        session.commit()
    
    car = session.query(Car).filter_by(name=car_name.lower()).first()
    if not car:
        car = Car(
            name=car_name, 
            price=car_price, 
            power=car_power, 
            engine=car_engine, 
            torque=car_torque
        )
        session.add(car)
        session.commit()
    session.close()



