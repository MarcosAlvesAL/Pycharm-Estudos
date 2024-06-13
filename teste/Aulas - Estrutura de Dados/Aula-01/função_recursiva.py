# Função que retorna o valor fatorial
def fatorial_recursivo(n):
    # se o valor passado for menor que 0: retornar none
    valor_fat = 1
    if n < 0:
        return None
    # se o valor for 1 ou 0 retornar o: valor_fat
    elif n == 0 or n == 1:
        return valor_fat
    # Pegar o valor passado por parametro e mutiplicar por ele mesmo -1 até chegar em 1
    else:
        return n * fatorial_recursivo(n-1)

print(fatorial_recursivo(3))
