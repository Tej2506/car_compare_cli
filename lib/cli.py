from helpers import scrape_car_details, save_car_details_to_db

if __name__  = '__main__':
    print("Welcome to Car Compare CLI")

    while True:
        car_name = input("Enter the name of the car or type 'exit' to quit: ")
        manufacturer = input("Enter the name of the manufacturer: ")
        if car_name.lower()== 'exit':
            break

        car_details = scrape_car_details(car_name, manufacturer)
        save_car_details_to_db(car_details)

        print(f"Details for {car_name} have been successfully saved.")
