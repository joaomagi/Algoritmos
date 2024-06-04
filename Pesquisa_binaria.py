'''
A pesquisa binária é um algorito eficiente para encontrar um valor em uma lista que precisa estar em forma ordenada,
a pesquisa binária tem notação Big O, O(log n) também conhecido como tempo logarítmico, o que a torna mais eficiente que a pesquisa simples, 
a pesquisa simples, O(n), conhecido como tempo linear, funciona de forma linear indo de item por item de forma linear o que acaba tornando o processo mais lento
'''


def pesquisa_binaria(lista, item):
    # baixo e alto serve para acompanhar a parte da lista que você está procurando
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:  # Loop para continuar procurando o item
        meio = (baixo + alto)//2  # Calculo para descobrir o número do meio
        chute = lista[meio]  # Chute sempre será o meio da lista
        if chute == item:  # Acha o item escolhido
            return meio
        elif chute > item:  # Chute muito alto
            alto = meio - 1
        else:
            baixo = meio + 1  # Chuto muito baixo
    return None  # Item não existe


minha_lista = [1, 3, 5, 7, 9]
print(pesquisa_binaria(minha_lista, 3))  # Índice esperado 1
print(pesquisa_binaria(minha_lista, 9))  # Índice esperado 4
print(pesquisa_binaria(minha_lista, -1))  # None
print(pesquisa_binaria(minha_lista, 32))  # None
