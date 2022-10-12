class DataManager:
    # This class is responsible for structuring the flight data.
    def __init__(self, c):
        self.flight_deals = c
        self.message = False
        self.flight_price = []

