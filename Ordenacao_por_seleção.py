def buscarMenor(arry):
    # Define o menor elemento inicialmente como o primeiro elemento da lista
    menor = arry[0]
    menor_indice = 0  # O índice do menor elemento começa com zero
    for i in range(1, len(arry)):  # For que passa pela lista apartir do segundo elemento
        if arry[i] < menor:  # If para comparar cada elemento até encontrar o menor e depois substituir
            menor = arry[i]  # Atualiza o menor elemento
            menor_indice = i  # Atualiza o índice do menor elemento
    return menor_indice  # Retorna o índice do menor elemento


def ordenacaoPorSelecao(arry):
    novoArry = []  # Cria uma nova lista vazia para começar a ordenar
    for i in range(len(arry)):  # For para percorrer todos os itens
        menor = buscarMenor(arry)  # Busca o menor elemento da lista original
        # Remove o menor elemento da lista original e adicona a nova
        novoArry.append(arry.pop(menor))
    return novoArry  # Retorna a nova lista ja ordenada


minha_lista = [3, 1, 7, 9, 5]
print(ordenacaoPorSelecao(minha_lista)) # Ordem esperada [1, 3, 5, 7, 9]
minha_lista2 = [30, -1, 25, 100, -5]
print(ordenacaoPorSelecao(minha_lista2)) # Ordem esperada [-5, -1, 25, 30, 100]

