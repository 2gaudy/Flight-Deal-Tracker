import requests
import datetime as dt
from flight_data import FlightData

tequila_url = "https://tequila-api.kiwi.com/"

tequila_api_key = "TBuLJ7FHtLqmR3c648PsdSvflQEx-tZ_"

get_tequila_endpoint = f"{tequila_url}locations/query"

search_tequila_endpoint = f"{tequila_url}v2/search"

tequila_header = {
    "apikey": tequila_api_key
}

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def get_destination_code(self, city):
        query = {
            "term": city
        }

        flight_info = requests.get(url=get_tequila_endpoint, headers=tequila_header, params=query)
        flight_json = flight_info.json()
        print(flight_json)
        print(flight_json['locations'][0]['code'])
        return flight_json['locations'][0]['code']

    def search_for_flights(self, origin_city, destination_city, from_time, to_time):
        headers = {"apikey": tequila_api_key}

        query = {
            "fly_from": origin_city,
            "fly_to": destination_city,
            "date_from": from_time,
            "date_to": to_time,
            "flight_type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "max_stopovers": 3,
            "curr": "USD"
        }

        response = requests.get(url=search_tequila_endpoint, headers=headers, params=query)

        try:
            data = response.json()["data"][0]
            print(data)
        except IndexError:
            print(f"No flights found for {destination_city}")
            return None

        flight_data = FlightData(price=data['price'] ,
                                 origin_city= data['route'][0]['cityFrom'],
                                 origin_airport=data["route"][0]["flyFrom"],
                                 destination_city= data["route"][0]["cityTo"],
                                 destination_airport= data['route'][0]["flyTo"],
                                 out_date=data["route"][0]["local_departure"].split("T")[0],
                                 return_date=data["route"][1]["local_departure"].split("T")[0]
                                 )
        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data