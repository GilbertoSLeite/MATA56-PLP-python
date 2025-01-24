from datashow import Datashow
from room import Room
from cinema import Cinema

print("Exemplo - Alocando datashows à salas a partir de uma lista.")
cinema = Cinema()
print("\n## Criando uma lista com 5 datashows.")
for i in range(5):
    cinema.appendDatashow(Datashow())
cinema.printStats()

print("\n## Criando uma lista com 10 salas.")
for i in range(10):
    cinema.appendRoom(Room())
cinema.printStats()

print("\n## Alocando todos os datashows")
ds = cinema.getFirstAvaliableDatashow()
r = cinema.getFirstEmptyRoom()
while ds is not None and r is not None:
    r.setDatashow(ds)
    ds = cinema.getFirstAvaliableDatashow()
    r = cinema.getFirstEmptyRoom()
cinema.printStats()

print("\n## Liberando datashow 1, 3 e 4")
cinema.freeDatashowAt(1)
cinema.freeDatashowAt(3)
cinema.freeDatashowAt(4)
cinema.printStats()