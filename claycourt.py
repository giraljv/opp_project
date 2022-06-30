from court import Tenniscourt


class Claycourt(Tenniscourt):
    sponsor = str
    def __init__(self, type,location, reservation_time,reservation_number,players,sponsor):
        super().__init__(type,location, reservation_time,reservation_number,players)
        self.sponsor = sponsor

    def maintenance(self):
        print("watered")
        print("Brush to redistribute the top dressing")