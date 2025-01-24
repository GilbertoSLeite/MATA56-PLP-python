# Sistema de Alocação de Datashow

Este projeto demonstra de forma simples a alocação de projetores (Datashows) em salas de aula utilizando Python e os conceitos de nomes, vinculações, escopo, tempo de vida de variáveis e constantes nomeadas.

## Conceitos Fundamentais Demonstrados

1. **Nomes (identificadores)**  
   - Classes, métodos, atributos e constantes como `Datashow`, `Sala`, `alocar_datashow`, `STATUS_DISPONIVEL`, etc.

2. **Vinculações (Bindings)**  
   - Atribuição de valores/objetos a variáveis de instância, como `self.datashow_alocado = datashow`.

3. **Escopo**  
   - Escopo de módulo para as constantes (`STATUS_DISPONIVEL`, `STATUS_ALOCADO`) e escopo de classe/instância para atributos como `self.identificador`, `self.status`.

4. **Tempo de vida**  
   - As instâncias de `Datashow` e `Sala` são criadas em tempo de execução e, *em Python*, o Garbage Collector garante a persistência delas enquanto houver referências a elas.

5. **Constantes nomeadas**  
   - Uso de constantes `STATUS_DISPONIVEL` e `STATUS_ALOCADO` para dar mais clareza e evitar valores “mágicos” espalhados pelo código.

## Estrutura

```
datashow_management/
├── __main__.py    # Ponto de entrada da aplicação (execução)
├── models.py      # Classes Datashow e Sala, com constantes e lógica de alocação
README.md          # Documentação do projeto
```

## Como Executar

1. **Clone ou baixe** este repositório.
2. Certifique-se de ter o **Python 3** instalado.
3. No diretório raiz do repositório, execute:
   ```bash
   python -m datashow_management
   ```
4. Observe a saída no console, que demonstra a alocação e liberação de datashows em salas.

