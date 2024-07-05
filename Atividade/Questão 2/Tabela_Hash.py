# Classe que representa um Nodo de uma lista encadeada simples
class Nodo:
    def __init__(self, sigla, nome_estado):
        self.sigla = sigla
        self.nome_estado = nome_estado
        self.proximo = None

    def __repr__(self):
        return self.sigla

# Classe que representa uma Lista Encadeada Simples
class ListaEncadeadaSimples:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodo = self.head
        nodos = []
        while nodo is not None:
            nodos.append(nodo.sigla)
            nodo = nodo.proximo
        nodos.append("None")
        return " -> ".join(nodos)

    def inserir_no_inicio(self, nodo):
        nodo.proximo = self.head
        self.head = nodo

# Função hash conforme o enunciado
def funcao_hash(sigla):
    if sigla == 'DF':
        return 7
    return (ord(sigla[0]) + ord(sigla[1])) % 10

# Classe que representa a Tabela Hash
class TabelaHash:
    def __init__(self):
        self.tabela = [ListaEncadeadaSimples() for _ in range(10)]

    def inserir(self, sigla, nome_estado):
        posicao = funcao_hash(sigla)
        nodo = Nodo(sigla, nome_estado)
        self.tabela[posicao].inserir_no_inicio(nodo)

    def imprimir(self):
        for i, lista in enumerate(self.tabela):
            print(f"Posição {i}: {lista}")

# Programa principal
if __name__ == "__main__":
    # Criação da tabela hash
    tabela_hash = TabelaHash()

    # Inserção dos estados e Distrito Federal na tabela hash
    estados = [
        ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"),
        ("BA", "Bahia"), ("CE", "Ceará"), ("DF", "Distrito Federal"), ("ES", "Espírito Santo"),
        ("GO", "Goiás"), ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"), ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"),
        ("PE", "Pernambuco"), ("PI", "Piauí"), ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"), ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"),
        ("SP", "São Paulo"), ("SE", "Sergipe"), ("TO", "Tocantins")
    ]

    for sigla, nome in estados:
        tabela_hash.inserir(sigla, nome)

    # Inserção do estado fictício
    tabela_hash.inserir("BK", "Estado Fictício")

    # Impressão da tabela hash
    tabela_hash.imprimir()