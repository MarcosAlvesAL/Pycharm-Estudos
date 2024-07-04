# Nodo que representa um Estado
class Node:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.next = None

# Tabela Hash com 10 posições
class HashTable:
    def __init__(self):
        self.table = [None] * 10  # [EXIGÊNCIA DE CÓDIGO 1 de 7]

    def hash_function(self, sigla):
        if sigla == "DF":
            return 7  # [EXIGÊNCIA DE CÓDIGO 5 de 7]
        return (ord(sigla[0]) + ord(sigla[1])) % 10  # [EXIGÊNCIA DE CÓDIGO 5 de 7]

    def insert(self, sigla, nomeEstado):
        index = self.hash_function(sigla)
        new_node = Node(sigla, nomeEstado)
        new_node.next = self.table[index]
        self.table[index] = new_node  # [EXIGÊNCIA DE CÓDIGO 3 de 7]

    def print_table(self):
        for i in range(10):
            print(f"Posição {i}:", end=" ")
            current = self.table[i]
            while current:
                print(current.sigla, end=" -> ")
                current = current.next
            print("None")  # [EXIGÊNCIA DE CÓDIGO 4 de 7]

# Inserção dos estados e Distrito Federal na tabela hash
def main():
    estados = [
        ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"), ("BA", "Bahia"),
        ("CE", "Ceará"), ("DF", "Distrito Federal"), ("ES", "Espírito Santo"), ("GO", "Goiás"),
        ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"), ("MG", "Minas Gerais"),
        ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"), ("PE", "Pernambuco"), ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"), ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"), ("SP", "São Paulo"),
        ("SE", "Sergipe"), ("TO", "Tocantins")
    ]  # [EXIGÊNCIA DE CÓDIGO 6 de 7]

    tabela_hash = HashTable()

    for sigla, nomeEstado in estados:
        tabela_hash.insert(sigla, nomeEstado)

    # Inserindo estado fictício
    tabela_hash.insert("BK", "Bruno Kostiuk")  # [EXIGÊNCIA DE CÓDIGO 7 de 7]

    tabela_hash.print_table()

if __name__ == "__main__":
    main()