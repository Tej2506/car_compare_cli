from helpers import scrape_car_details, save_car_details_to_db
from db.models import session, Car, Manufacturer, Feature

if __name__  == '__main__':
    print("Welcome to Car Compare CLI")

    def delete_entries(entries):
        for data in entries:
            session.delete(data)
            session.commit()


    while True:
        car_name = input("Enter the name of the car or type 'exit' to quit: ")
        if car_name.lower()== 'exit':
            entries_made_cars = session.query(Car).all()
            entries_made_manufacturers = session.query(Manufacturer).all()
            delete_entries(entries_made_cars)
            delete_entries(entries_made_manufacturers) 
            break
       
       
        manufacturer = input("Enter the name of the manufacturer: ")
        car_details = scrape_car_details(manufacturer, car_name)
        save_car_details_to_db(car_details)

        print(f"Details for {car_name} have been successfully saved.")

        saved_cars = session.query(Car).all()
        saved_manufacturers = session.query(Manufacturer).all()
        saved_features = session.query(Feature).all()
        print(saved_cars)
        print(saved_manufacturers)
        print(saved_features)

        




