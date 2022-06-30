from claycourt import Claycourt
from jugador import Players



if __name__ == "__main__":
    
    match = ["sebastian","ivan"]
    documents = [12039193,320323]
    ea = [19,20]
   #def __init__(self, type,id, reservation_time,reservation_number,player,sponsor):
    newreserve = Claycourt("clay",123,"2",324214,Players(match,documents,ea),"gatorade")
    print(vars(newreserve))
    print(vars(newreserve.players))
    newreserve.maintenance()
