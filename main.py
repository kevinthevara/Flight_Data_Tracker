from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

flight_data = FlightData()
flight_search = FlightSearch()
data = DataManager(flight_search.flight_data)
noti = NotificationManager()

flight_data.iata_find(flight_search.headers)
#try,else,expect
for x in data.flight_deals:
    for z in flight_data.sheety_cities["prices"]:
        if x["cityCodeTo"] == z["city"] and x["price"] < z["lowestPrice"]:
            data.flight_price.append(x)
            data.message = True

if data.message == True:
    noti.send_message(data.flight_price)







