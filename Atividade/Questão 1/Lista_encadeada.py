#MARCOS ALVES DOS SANTOS JUNIOR - RU: 3956503

# Elabore um programa em Python que:

#A. Deve-se implementar uma Lista Encadeada Simples em que: [EXIGÊNCIA DE CÓDIGO 1 de 7];
class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.head = None
        # As numerações dos cartões amarelos (A) iniciam em 201.
        self.numero_amarelo = 201
        # As numerações dos cartões verdes (V) inicial em 1.
        self.numero_verde = 1

# B. Deve-se implementar a função inserirSemPrioridade(nodo) em que: [EXIGÊNCIA DE CÓDIGO 2 de 7];
    def inserirSemPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = nodo

    # C. Deve-se implementar a função inserirComPrioridade(nodo) em que: [EXIGÊNCIA DE CÓDIGO 3 de 7];
    def inserirComPrioridade(self, nodo):
        if self.head is None or self.head.cor == "V":
            nodo.proximo = self.head
            self.head = nodo
            # a. Deve-se andar pela lista a partir da cabeça (head) e inserir o nodo após todos os nodos com cor “A” que estão na lista.
        else:
            atual = self.head
            while atual.proximo and atual.proximo.cor == "A":
                atual = atual.proximo
            nodo.proximo = atual.proximo
            atual.proximo = nodo

    # D. Deve-se implementar a função inserir() em que: [EXIGÊNCIA DE CÓDIGO 4 de 7];
    def inserir(self):
        # a. Deve-se solicitar ao usuário a cor (“A” ou “V”) e o número (inteiro).
        cor = input("Digite a cor do cartão (A ou V): ").strip().lower()
        if cor == "a":
            numero = self.numero_amarelo
            self.numero_amarelo += 1

        elif cor == "v":
            numero = self.numero_verde
            self.numero_verde += 1
        else:
            print("Cor inválida. Use 'A' para amarelo e 'V' para verde.")
            return
        # b. Deve-se criar um nodo com a cor e o número fornecidos pelo usuário.
        novo_nodo = Nodo(numero, cor.upper())
        # c. Se a lista estiver vazia, a cabeça (head) da lista deve apontar para o nodo criado.
        if self.head is None:
            self.head = novo_nodo
        elif cor == "v":
            # d. Senão, se a cor do nodo for “V”, deve-se chamar a função inserirSemPrioridade(nodo).
            self.inserirSemPrioridade(novo_nodo)
        else:
            # e. Senão, se a cor do nodo for “A”, deve-se chamar a função inserirComPriordade(nodo).
            self.inserirComPrioridade(novo_nodo)

        print(f"Paciente inserido com sucesso. Cartão {novo_nodo.numero} - Cor {novo_nodo.cor}")

    # E. Deve-se implementar a função imprimirListaEspera() em que: [EXIGÊNCIA DE CÓDIGO 5 de 7];

    # a. Deve-se imprimir todos os cartões e seus respectivos números a partir do primeiro até o último da lista.
    def imprimirListaEspera(self):
        atual = self.head
        while atual:
            print(f"Cartão {atual.numero} - Cor {atual.cor}")
            atual = atual.proximo

    # F. Deve-se implementar a função atenderPaciente() em que: [EXIGÊNCIA DE CÓDIGO 6 de 7];
    # a. Deve-se remover o primeiro paciente da fila e imprimir uma mensagem chamando o paciente para atendimento informando o número do seu cartão.
    def atenderPaciente(self):
        if self.head is None:
            print("Não há pacientes na fila.")
        else:
            print(f"Chamando paciente com cartão {self.head.numero} - Cor {self.head.cor}")
            self.head = self.head.proximo

#G. Deve-se implementar um menu para utilização do sistema em que: [EXIGÊNCIA DE CÓDIGO 7 de 7];
def menu():

    lista = ListaEncadeada()
    while True:
        print("Menu:")
        print("1 – Adicionar paciente a fila")
        print("2 – Mostrar pacientes na fila")
        print("3 – Chamar paciente")
        print("4 – Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            lista.inserir()
        elif opcao == "2":
            lista.imprimirListaEspera()
        elif opcao == "3":
            lista.atenderPaciente()
        elif opcao == "4":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# INICIO DO PROGRAMA #

menu()


















