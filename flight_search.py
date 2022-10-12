import requests
import datetime
from datetime import timedelta
FLIGHT_URL = "https://tequila-api.kiwi.com/v2/search"

today_date = datetime.datetime.now().strftime("%d/%m/%Y")
next_week_date = (datetime.datetime.now() + timedelta(7)).strftime("%d/%m/%Y")

affil_id = "AFFIL_ID"

class FlightSearch:
    def __init__(self):
        self.parameters = {
            "fly_from": "DEPARTURE_CITY_IATA_CODE",
            "dateFrom": today_date,
            "dateTo": next_week_date,
            "AffilID": affil_id
        }

        self.headers = {
            "apikey": "API_KEY"
        }

        self.data = requests.get(url=FLIGHT_URL, params=self.parameters, headers=self.headers)
        self.data.raise_for_status()
        self.flight_data = self.data.json()['data']