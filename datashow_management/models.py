# models.py

# Exemplos de constantes nomeadas
STATUS_DISPONIVEL = "DISPONÍVEL"
STATUS_ALOCADO = "ALOCADO"

class Datashow:
    """
    Classe que representa um projetor (Datashow).
    """

    def __init__(self, identificador, marca):
        # Vinculação das variáveis de instância (nomes -> objetos/valores)
        self.identificador = identificador
        self.marca = marca
        self.status = STATUS_DISPONIVEL  # Estado inicial do datashow

    def esta_disponivel(self):
        """
        Verifica se o datashow está disponível.
        """
        return self.status == STATUS_DISPONIVEL

    def alocar(self):
        """
        Aloca o datashow (caso esteja disponível).
        """
        if self.esta_disponivel():
            self.status = STATUS_ALOCADO
            return True
        return False

    def liberar(self):
        """
        Libera o datashow para uso.
        """
        self.status = STATUS_DISPONIVEL

    def __str__(self):
        return f"Datashow {self.identificador} ({self.marca}) - Status: {self.status}"


class Sala:
    """
    Classe que representa uma sala, podendo ter um Datashow alocado.
    """

    def __init__(self, numero, capacidade):
        self.numero = numero
        self.capacidade = capacidade
        # Vinculação: sala mantém referência a um objeto Datashow ou None
        self.datashow_alocado = None  

    def alocar_datashow(self, datashow):
        """
        Aloca um datashow à sala, caso o Datashow esteja disponível
        e a sala não tenha outro datashow alocado.
        """
        if self.datashow_alocado is not None:
            print(f"Sala {self.numero} já possui um Datashow alocado.")
            return False

        if not datashow.esta_disponivel():
            print(f"Datashow {datashow.identificador} não está disponível para alocação.")
            return False

        # Efetiva a alocação
        alocado = datashow.alocar()
        if alocado:
            self.datashow_alocado = datashow
            print(f"Datashow {datashow.identificador} alocado à Sala {self.numero}.")
            return True
        else:
            print(f"Falha ao alocar o Datashow {datashow.identificador}.")
            return False

    def liberar_datashow(self):
        """
        Remove a alocação do datashow, se houver.
        """
        if self.datashow_alocado:
            self.datashow_alocado.liberar()
            print(f"Datashow {self.datashow_alocado.identificador} foi liberado da Sala {self.numero}.")
            self.datashow_alocado = None
        else:
            print(f"Não há Datashow alocado na Sala {self.numero}.")

    def __str__(self):
        if self.datashow_alocado:
            return (f"Sala {self.numero} (capacidade: {self.capacidade}) "
                    f"- Datashow: {self.datashow_alocado.identificador} ({self.datashow_alocado.status})")
        else:
            return f"Sala {self.numero} (capacidade: {self.capacidade}) - Sem Datashow alocado."

