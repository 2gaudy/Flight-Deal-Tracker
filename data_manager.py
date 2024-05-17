from pprint import pprint
import requests

sheety_prices_endpoint = "https://api.sheety.co/0fb28b01142c17aa77e816af0f36d0c8/flightDealsFinder/prices"

class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        sheet_get = requests.get(url=sheety_prices_endpoint)
        sheet_get.raise_for_status()
        data = sheet_get.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_prices_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)
