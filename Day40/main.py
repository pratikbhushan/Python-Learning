import requests_cache
from datetime import datetime, timedelta
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager


requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)

data_mgr = DataManager()
sheet_data = data_mgr.get_destination()
pprint(sheet_data)

customer_data = data_mgr.get_customer_emails()

customer_email_list = [row["email"] for row in customer_data]
print(f"Your email list includes {customer_email_list}")

tomorrow = datetime.today() + timedelta(days=1)
six_month_from_today = datetime.today() + timedelta(days=182.5)

flt_srch = FlightSearch()
ORIGIN_CITY_IATA = "BLR"

notification_manager = NotificationManager()

for destination in sheet_data:
    pprint(f"Getting flights for {destination['city']}...")
    
    
    flights = flt_srch.check_flights(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights, return_date=six_month_from_today.strftime("%Y-%m-%d"))
    

    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stopover_flights = flt_srch.check_flights(
            origin_city_code=ORIGIN_CITY_IATA,
            destination_city_code=destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today,
            is_direct=False
        )
        cheapest_flight = find_cheapest_flight(stopover_flights, return_date=six_month_from_today.strftime("%Y-%m-%d"))
        print(f"Cheapest indirect flight price is: ₹ {cheapest_flight.price}")
    
    if cheapest_flight is not None and cheapest_flight.price != "N/A":
        pprint(f"{destination['city']}: ₹ {cheapest_flight.price}")

        if cheapest_flight.price < destination["lowestPrice"]:
            pprint(f"Lower price flight found to {destination['city']}!")
            data_mgr.update_lowest_price(destination["id"], cheapest_flight.price)

            
            if cheapest_flight.stops == 0:
                alert_message = (f"Low price alert! Only ₹ {cheapest_flight.price} to fly direct "
                                 f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                                 f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}.")
            else:
                alert_message = (f"Low price alert! Only ₹ {cheapest_flight.price} to fly "
                                 f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                                 f"with {cheapest_flight.stops} stop(s) "
                                 f"departing on {cheapest_flight.out_date} and returning on {cheapest_flight.return_date}.")

            
            notification_manager.send_message(message=alert_message)

            
            notification_manager.send_emails(email_list=customer_email_list, email_body=alert_message)