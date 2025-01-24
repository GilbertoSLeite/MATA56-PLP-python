from datashow import Datashow

class Room:
    def __init__(self):
        self._datashow = None
    def hasDatashow(self):
        return self._datashow is not None
    def setDatashow(self, datashow):
        if self.hasDatashow():
            raise Exception("Esta sala já possui um datashow. Por favor remova o datashow atual antes de adicionar um outro.")
        datashow.setRoom(self)
        self._datashow = datashow
    def freeDatashow(self, rc=False):
        if not rc and self._datashow is not None:
            self._datashow.free(rc = True)
        self._datashow = None