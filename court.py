class Tenniscourt:
    type = str
    location = str
    reservation_time = int
    reservation_number = int
    players = str

    def __init__(self,type,location, reservation_time, reservation_number,players):
        self.type = type
        self.location = location
        self.reservation_time = reservation_time
        self.reservation_number = reservation_number
        self.players = players
        
    def maintenance(self):
        pass
    