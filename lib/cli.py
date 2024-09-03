from helpers import scrape_car_details, save_car_details_to_db
from db.models import session, Car, Manufacturer, Feature

def delete_all_entries(entries):
    for data in entries:
        session.delete(data)
        session.commit()

def display_saved_cars(saved_cars):
    if not saved_cars:
        print("No cars have been added yet.")
        return
    
    for car in saved_cars:
        print(f"ID:{car.id:<3} {car.manufacturer.name} {car.name}") 
        print(f"Price: {car.price} \nPower: {car.power} \nTorque: {car.torque} \nEngine: {car.engine}") 
        car_features = ", ".join([feature.name for feature in car.features])
        print(f" Features: \n{car_features}")
        print("=" * 90)

        print("\n")


def car_entry_mode():
    print("Mode to enter new cars to the database")

    while True:
        car_name = input("Enter the name of the car or type 'menu' to go to the main menu: ")
        if car_name.lower() == 'menu':
            break
        
        manufacturer = input("Enter the name of the manufacturer: ")
        car_details = scrape_car_details(manufacturer, car_name)
        save_car_details_to_db(car_details)

        print(f"Details for {car_name} have been successfully saved.")

def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Add More Cars")
        print("2. Compare Cars")
        print("3. Delete a Car")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            car_entry_mode()
        elif choice == '2':
            compare_cars()
        elif choice == '3':
            delete_car()
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            entries_made_cars = session.query(Car).all()
            entries_made_manufacturers = session.query(Manufacturer).all()
            entrie_made_features = session.query(Feature).all()
            delete_all_entries(entries_made_cars)
            delete_all_entries(entries_made_manufacturers) 
            delete_all_entries(entrie_made_features)
            break
        else:
            print("Invalid choice. Please select from the options above.")


def compare_cars():
    saved_cars = session.query(Car).all()
    if not saved_cars:
        print("No cars to compare. Please add some cars first.")
        return

    print("\n--- List of Cars Added ---")

    display_saved_cars(saved_cars)

    input("Press Enter to return to the main menu...")

def delete_car():
    """Functionality to delete a car from the database."""
    saved_cars = session.query(Car).all()
    if not saved_cars:
        print("No cars available to delete.")
        return

    print("\n--- List of Cars Available for Deletion ---")
    for i, car in enumerate(saved_cars, start=1):
        print(f"{i}. {car.manufacturer.name} {car.name}")

    car_number = input("Enter the number of the car to delete or 'menu' to return to the main menu: ")
    if car_number.lower() == 'menu':
        return

    try:
        car_number = int(car_number)
        if 1 <= car_number <= len(saved_cars):
            car_to_delete = saved_cars[car_number - 1]
            session.delete(car_to_delete)
            session.commit()
            print(f"Car '{car_to_delete.name}' deleted successfully.")
        else:
            print("Invalid car number.")
    except ValueError:
        print("Please enter a valid number.")


    

if __name__  == '__main__':
    print("Welcome to Car Compare CLI")
    car_entry_mode()
    main_menu()
