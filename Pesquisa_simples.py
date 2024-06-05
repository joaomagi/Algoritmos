def pesquisa_simples(lista, item):
    for i, valor in enumerate(lista): # For que passa pela lista com um loop onde o I, é o índice e valor é o elemento atual
        if valor == item: # Vê se o elemento atual é igual ao número procurado
            return i  # Retorna o índice do item encontrado
    return None  # Retorna que o item não existe

minha_lista = [1, 3, 5, 7, 9]
print(pesquisa_simples(minha_lista,9)) # Índice esperado 4
print(pesquisa_simples(minha_lista,3)) # Índice esperado 1
print(pesquisa_simples(minha_lista,-1)) # None
print(pesquisa_simples(minha_lista, 32))  # None
