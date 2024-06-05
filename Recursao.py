'''
# Pseudocódigo
def procure_pela_chave(caixa):
    for item in caixa:
        if item.e_uma_caixa():
            procure_pela_chave(item)
        elif item.e_uma_chave():
        print "achei a chave!"
'''
def regressiva(i): # Função para contagem regresiva usando recursividade
    print(i) # Imprime o número atual da contagem
    if i <= 1: # Verifica se o número atual é menor ou igual a 1 (caso base)
        return # encerra a função
    else: # Se o número atual for maior que 1 (caso recursivo)
        regressiva(i-1) # Chama a recursividade regressiva com o número anterior - 1

print(regressiva(5)) # 5, 4, 3, 2, 1