def retorna_divisores(valor):
    divisores = []
    for i in range(1, valor+1):
        if valor % i == 0:
            divisores.append(i)
    return divisores

def eh_primo(valor):
    divisores = []
    for i in range(1, valor+1):
        if valor % i == 0:
            divisores.append(i)
    if (len(divisores) > 2) or (len(divisores) == 1):
        return False
    else:
        return True
    
def retorna_valores_primos(lista):
    primos = []
    for i in lista:
        if eh_primo(i):
            primos.append(i)
    return primos
    
def main():
    n = int(input('Digite um valor para ver seus divisores: '))
    div = retorna_divisores(n)
    prim = retorna_valores_primos(div)
    
    print('Divisores : {}\nPrimos : {}'.format(div, prim))
    print('O tamanho da lista div e prim sucessivamente eh: {}, {}'.format(len(div), len(prim)))
    
main()
