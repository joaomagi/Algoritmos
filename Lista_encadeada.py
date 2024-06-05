# Classe para cada caixa na lista encadeada
class Caixa:
    def __init__(self, numero, proxima=None):
        self.numero = numero  # Número dentro da caixa
        self.proxima = proxima  # Endereço da próxima caixa na lista

# Função para procurar uma chave dentro da caixa


def buscar_chave(caixa_inicial, chave):
    caixa_atual = caixa_inicial  # Começa na primeira caixa

    while caixa_atual is not None:  # Enquanto houver caixas na lista
        if caixa_atual.numero == chave:  # Se a chave estiver dentro da caixa atual
            return 'Achou a chave'  # Chave encontrada
        # Se não estiver se move para a próxima caixa na lista
        caixa_atual = caixa_atual.proxima

    return 'Chave não encontrada'  # Chave não encontrada em nenhuma caixa


# Criando uma pilha de caixas
caixa5 = Caixa(5)
caixa4 = Caixa(4, caixa5)
caixa3 = Caixa(3, caixa4)
caixa2 = Caixa(2, caixa3)
caixa1 = Caixa(1, caixa2)

caixa_inicial = caixa1  # Definindo a primeira caixa

chave = 3  # Colocando a chave em uma caixa

print(buscar_chave(caixa_inicial, chave))  # Esperado 'Achou a chave'
print(buscar_chave(caixa_inicial, 6))  # Esperado 'Chave não encontrada'
