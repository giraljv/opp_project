class Tenniscourt:
    type = str
    mesure = {}
    location = str
    reservation_time = int

    def __init__(self,type,mesure,location, reservation_time):
        self.type = type
        self.mesure = mesure
        self.location = location
        self.reservation_time = reservation_time
        
    def maintenance(self):
        pass
    