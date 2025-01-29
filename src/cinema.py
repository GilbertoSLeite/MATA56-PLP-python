from typing import List
from datashow import Datashow
from room import Room

class Cinema:
    def __init__(self):
        self.datashows: List[Datashow] = []
        self.rooms: List[Room] = []
    
    def freeDatashowAt(self, index):
        if index < len(self.datashows):
            self.datashows[index].free()
        else:
            raise Exception("Não existe Datashow com esse indice.")
        
    def appendRoom(self, Room):
        self.rooms.append(Room)

    def removeRoom(self, index):
        if index < len(self.rooms):
            if self.rooms[index].hasDatashow():
                self.rooms[index].freeDatashow()
            del self.rooms[index]
        else:
            raise Exception("Não existe Sala com esse indice.")
    
    def appendDatashow(self, Datashow):
        self.datashows.append(Datashow)

    def removeDatashow(self, index):
        if index < len(self.datashows):
            if not self.datashows[index].isAvaliable():
                self.datashows[index].free()
            del self.rooms[index]
        else:
            raise Exception("Não existe Datashow com esse indice.")
    
    def getRoomAt(self, index):
        if index < len(self.rooms):
            return self.rooms[index]
        else:
            raise Exception("Não existe Sala com esse indice.")

    def getDatashowAt(self, index):
        if index < len(self.datashows):
            return self.datashows[index]
        else:
            raise Exception("Não existe Datashow com esse indice.")

    def getFirstAvaliableDatashow(self):
        for datashow in self.datashows:
            if datashow.isAvaliable():
                return datashow
        return None
    
    def getFirstEmptyRoom(self):
        for room in self.rooms:
            if not room.hasDatashow():
                return room
        return None
    
    def printStats(self):
        i = 0
        for datashow in self.datashows:
            print("Datashow ", i, ": ", "Disponível" if datashow.isAvaliable() else "Indisponível")
            i+=1
        i = 0
        for room in self.rooms:
            print("Sala ", i, ": ", "Datashow disponível" if room.hasDatashow() else "Datashow indisponível")
            i+=1