# main.py
from .models import Datashow, Sala

def main():
    # Instanciando datashows
    datashow1 = Datashow(identificador="DS-001", marca="Epson")
    datashow2 = Datashow(identificador="DS-002", marca="Sony")

    # Instanciando salas
    sala1 = Sala(numero=101, capacidade=40)
    sala2 = Sala(numero=102, capacidade=30)

    print("=== Estado Inicial ===")
    print(datashow1)
    print(datashow2)
    print(sala1)
    print(sala2)
    print()

    # Tentando alocar datashow1 na sala1
    sala1.alocar_datashow(datashow1)
    # Tentando alocar datashow1 na sala2 (deve falhar, pois já foi alocado)
    sala2.alocar_datashow(datashow1)
    print()

    # Tentando alocar datashow2 na sala2 (deve ter sucesso)
    sala2.alocar_datashow(datashow2)
    print()

    print("=== Após Alocações ===")
    print(sala1)
    print(sala2)
    print()

    # Liberando datashow1 da sala1
    sala1.liberar_datashow()
    print()

    print("=== Após Liberação do Datashow da Sala 1 ===")
    print(sala1)
    print(sala2)
    print()

main()

