#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to
# achieve the program requirements.


from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from flight_data import FlightData
import datetime as dt

today = dt.date.today()
tomorrow = today + dt.timedelta(days=1)
tomorrow_formatted = tomorrow.strftime("%d/%m/%Y")

six_months_away = today + dt.timedelta(days=120)
six_months_away_formatted = six_months_away.strftime("%d/%m/%Y")

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

origin_city_iata = "TPA"

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()



# print(type(sheet_data[0]))
# print(type(sheet_data))

for destination in sheet_data:
    flight = flight_search.search_for_flights(
        origin_city_iata,
        destination["iataCode"],
        from_time=tomorrow_formatted,
        to_time=six_months_away_formatted,
        )


