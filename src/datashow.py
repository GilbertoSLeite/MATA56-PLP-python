class Datashow:
    def __init__(self):
        self._room = None

    def setRoom(self, room):
        if self._room is not None:
            raise Exception("Este datashow não está disponível no momento. Por favor libere o datashow ou escolha outro.")
        self._room = room

    def isAvaliable(self):
        return self._room is None
    
    def free(self, rc = False):
        if not rc and self._room is not None:
            self._room.freeDatashow()
        self._room = None