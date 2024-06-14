# Função
def fibonacci_calculo(n):
    if n <= 0: # se for menor que zero retorna uma lista vazia
        return[]
    elif n == 1: # se for 1 retorna o numero anterior que é o zero
        return [0]
    elif n == 2: # se for 2 retorna os dois numeros anteriores que é zero e um
        return [0,1]

    fib_sequence = [0, 1]
    for i in range(2, n):
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)

    return fib_sequence

# Testando a função
n = 10
print(f"Os primeiros {n} números da série de Fibonacci são: {fibonacci_calculo(n)}")















# ações aninhadas mutiplicação

# Algoritimo sem iteração nem recursão O(1)
# Laço iterarivo simples: O(n)
# Progressão aritmética (PA): O(n²)
# Progressão geométrica (PG): O(2 elevado a n)
# Dividir para conquistar: O(log.n)
# Recursão simples: O(n)
# Recursão Binária: 0(2 elevado a n)