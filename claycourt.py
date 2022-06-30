from court import Tenniscourt


class Claycourt(Tenniscourt):
    sponsor = str
    def __init__(self, type,id, reservation_time,reservation_number,players,sponsor):
        super().__init__(type,id, reservation_time,reservation_number,players)
        self.sponsor = sponsor

    def maintenance(self):
        print("watering the court")
        print("Brushing it to redistribute the top dressing")
        for i in range (0,101):
            if i % 20 == 0:
                print(str(i) + "%")
        print("you can play")