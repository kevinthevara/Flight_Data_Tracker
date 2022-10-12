import requests

get_url = "SHEETY_GET_URL"
put_url = "SHEETY_PUT_URL"

tequila_url = "https://tequila-api.kiwi.com/locations/query"

class FlightData:
    def __init__(self):
        self.data = requests.get(url=get_url)
        self.data.raise_for_status()
        self.sheety_cities = self.data.json()
        self.cities = []
        self.codes = []
        for x in self.sheety_cities["prices"]:
            self.cities.append(x["city"])

    def iata_find(self, m):
        r = 0
        self.tequila_headers = m

        for x in self.cities:
            self.tequila_params = {
                "term": str(x)
            }
            self.tequila_data = requests.get(url=tequila_url, params=self.tequila_params, headers=self.tequila_headers)
            self.tequila_info = self.tequila_data.json()
            self.codes.append(self.tequila_info["locations"][0]["code"])

        for x in range(10):
            if x > 0:
                code = self.codes[r]
                print(code)
                self.sheety_params = {
                    "price": {
                        "iataCode": code
                    }
                }
                self.sheety_put = requests.put(url=f"SHEETY_API/{x+1}", json=self.sheety_params)
                print(self.sheety_put.text)
                r += 1

