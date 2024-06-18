# Algoritimos de ordenação:
# Bubble Sort
def bubbleSort(dados):
  #tamanho do conjunto de dados
  tam = len(dados)
  #laço que ocorre quantidade de vezes igual ao
  #tamanho do conjunto de dados
  for v in range(0, tam, 1):
    #laço interno que pega os valores em pares
    for i in range(0, tam-1, 1):
      #comparação
      if dados[i] > dados[i+1]:
        #troca os dados usando variável auxiliar
        aux = dados[i]
        dados[i] = dados[i+1]
        dados[i+1] = aux

# Merge Sort
def mergeSort(dados):
  #Condiçao que indica se os dados ainda precisam ser divididos
  if len(dados) > 1:
    #divide recursivamente
    meio = len(dados)//2
    esquerda = dados[:meio]
    direita = dados[meio:]
    mergeSort(esquerda)
    mergeSort(direita)
    #intercala/mescla os dados
    i = j = k = 0
    while i<len(esquerda) and j<len(direita):
      if esquerda[i]<direita[j]:
        dados[k]=esquerda[i]
        i=i+1
      else:
        dados[k]=direita[j]
        j=j+1
      k=k+1
    while i<len(esquerda):
      dados[k]=esquerda[i]
      i=i+1
      k=k+1
    while j<len(direita):
      dados[k]=direita[j]
      j=j+1
      k=k+1

# Quick Sort
def quickSort(dados,inicio,fim):
  if inicio < fim:
    posicao_de_particionamento = partition(dados,inicio,fim)
    quickSort(dados,inicio,posicao_de_particionamento - 1)
    quickSort(dados,posicao_de_particionamento + 1,fim)

def partition(dados,inicio,fim):
  pivo = dados[inicio]
  esq = inicio + 1
  dir = fim
  flag = False
  while not flag:
    while esq <= dir and dados[esq] <= pivo:
      esq = esq + 1
    while dir >= esq and dados[dir] >= pivo:
      dir = dir -1
    if dir < esq:
      flag = True
    else:
      temp = dados[esq]
      dados[esq] = dados[dir]
      dados[dir] = temp
  temp = dados[inicio]
  dados[inicio] = dados[dir]
  dados[dir] = temp
  return dir

#Programa Principal
dados = [50,25,92,16,76,30,43,54,19]
mergeSort(dados)
print(dados)



