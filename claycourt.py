from court import Tenniscourt


class Claycourt(Tenniscourt):
    sponsor = str
    def __init__(self, type, location, reservation_time,sponsor):
        super().__init__(self, type, location, reservation_time)
        self.sponsor = sponsor

    def maintenance(self):
        print("watered")
        print("Brush to redistribute the top dressing")