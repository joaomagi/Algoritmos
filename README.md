# Algoritmos
# Referência de Estudo

Estou estudando esses conceitos a partir do livro **Entendendo Algoritmos: Um Guia Ilustrado Para Programadores e Outros Curiosos**, escrito por [Aditya Y. Bhargava](https://github.com/KAYOKG/BibliotecaDev/blob/main/LivrosDev/Entendendo%20Algoritmos%20-%20Um%20Guia%20Ilustrado%20Para%20Programadores%20e%20Outros%20Curiosos%20-%20Autor%20(Aditya%20Y.%20Bhargava).pdf).

Este livro tem me inspirado a aprender sobre algoritmos e estruturas de dados

---
# Pesquisa Simples

A pesquisa simples, também conhecida como busca linear, é um método básico de busca em uma lista de itens. Ela envolve percorrer sequencialmente cada elemento da lista, um por um, até encontrar o valor desejado.

### Exemplo 1:
Suponha que você tenha uma lista de números e esteja procurando por um número específico. Você começa verificando o primeiro número da lista, depois o segundo, o terceiro, e assim por diante, até encontrar o número desejado.

### Exemplo em código:
Código disponível [aqui](https://github.com/joaomagi/Algoritmos/blob/main/Pesquisa_simples.py).

### Complexidade de Tempo:
A pesquisa simples tem uma complexidade de tempo de O(n), onde n é o tamanho da lista. Isso significa que o tempo de execução aumenta linearmente com o tamanho da lista.

---

# Pesquisa Binária

A pesquisa binária é um método eficiente de busca em uma lista ordenada. Ela consiste em dividir repetidamente a lista ao meio até encontrar o valor desejado.

### Exemplo 1:
Imagine que você tenha uma lista de nomes em ordem alfabética e esteja procurando por um nome específico. Você começa olhando para o nome no meio da lista. Se o nome estiver depois do nome do meio, você olha na metade superior da lista; caso contrário, olha na metade inferior. Esse processo é repetido até encontrar o nome desejado.

### Exemplo em código:
Código disponível [aqui](https://github.com/joaomagi/Algoritmos/blob/main/Pesquisa_binaria.py).

### Complexidade de Tempo:
A pesquisa binária tem uma complexidade de tempo de O(log n), onde n é o tamanho da lista. Isso significa que, mesmo que a lista seja muito grande, o tempo de execução aumenta muito lentamente à medida que o tamanho da lista aumenta.

---

# Notação Big O

A notação Big O é uma maneira de descrever o desempenho de um algoritmo em relação ao tamanho dos dados de entrada.

### Exemplo:
- O(1): Tempo de execução constante. Independentemente do tamanho da entrada, o tempo de execução permanece constante.
- O(n): Tempo de execução linear. O tempo de execução aumenta proporcionalmente ao tamanho da entrada.
- O(log n): Tempo de execução logarítmico. O tempo de execução aumenta de forma muito lenta à medida que o tamanho da entrada aumenta.
- O(n log n):
- O(n²):
- O(n!):

![Big O](https://github.com/joaomagi/Algoritmos/blob/main/Imagens/BigO.png)
---

# Array
Arrays são uma estrutura de dados básica que armazena uma coleção de elementos do mesmo tipo em posições contíguas na memória. Eles permitem o acesso rápido a qualquer elemento usando índices.

### Exemplo 1:
Imagine que você tenha uma lista "top 10" de vilões da TV e queira acessar o vilão no índice 5. Em um array, você pode ir diretamente ao índice 5 e encontrar o vilão desejado instantaneamente.

### Exemplo em código:
Código disponível [aqui](https://github.com/joaomagi/Algoritmos/blob/main/Array.py).

### Características:
- Contíguo na Memória: Todos os elementos estão armazenados em locais adjacentes.
- Acesso Direto: Você pode acessar qualquer elemento diretamente pelo índice. Por exemplo, o quinto elemento de um array que começa no endereço 00 estará no endereço 04.
- Tamanho Fixo: O tamanho do array é definido na sua criação e não pode ser alterado.

---

# Lista encadeadas
As listas encadeadas são estruturas de dados onde cada item pode estar em qualquer lugar da memória. Cada item armazena o endereço do próximo item, criando uma cadeia de referências.

### Exemplo 1:
Imagine uma caça ao tesouro onde cada pista leva à próxima localização. Você começa no primeiro endereço que te diz "o próximo item está no endereço 123". Quando chega ao endereço 123, ele diz "o próximo item está no endereço 938", e assim por diante.

### Exemplo em código:
Código disponível [aqui](https://github.com/joaomagi/Algoritmos/blob/main/Lista_encadeada.py)

### Características:
- Endereços de Memória Ligados: Os itens não estão armazenados contiguamente, mas cada item sabe onde está o próximo.
- Inserção Fácil: Para adicionar um novo item, você simplesmente o coloca em qualquer lugar da memória disponível e atualiza os endereços.
- Flexibilidade de Memória: Não precisa de um bloco contíguo de memória, então sempre que houver espaço suficiente, você pode adicionar itens à lista.
---
# Ordenação por seleção
A ordenação por seleção é um algoritmo simples para ordenar uma lista de elementos, como números, nomes ou qualquer outro tipo de dados. A ideia básica por trás desse algoritmo é selecionar repetidamente o menor (ou maior) elemento da lista não ordenada e movê-lo para o início (ou final) da lista ordenada.

### Exemplo 1:
Imagine que você tem uma lista de músicas em seu computador, e para cada artista, você tem um contador de plays. Agora, você quer organizar essa lista de artistas do mais tocado para o menos tocado, para poder categorizá-los facilmente.

A ideia por trás da ordenação por seleção é bem intuitiva. Você começa selecionando o artista mais tocado da lista e o adiciona a uma nova lista ordenada. Em seguida, você busca o próximo artista mais tocado da lista original e o adiciona à lista ordenada, e assim por diante, até que todos os artistas estejam na lista ordenada.

### Exemplo em código:
Código disponível [aqui](https://github.com/joaomagi/Algoritmos/blob/main/Ordenacao_por_sele%C3%A7%C3%A3o.py)

### Complexidade de tempo:
Na ordenação por seleção, a complexidade de tempo é frequentemente expressa como 
𝑂
(
𝑛
2
)
O(n 
2
 ), onde 
𝑛
n é o tamanho da lista a ser ordenada. Isso significa que o tempo de execução aumenta quadráticamente com o tamanho da lista

# Recursão
Recursão é um conceito importante na programação, onde uma função chama a si mesma para resolver partes menores do problema. É como se você seguisse uma pista para encontrar outra pista, e assim por diante, até atingir o seu objetivo final.

### Exemplo 1:
Você começa a procurar uma chave e encontra uma caixa. Ao abri-la, você não encontra a chave, mas outra caixa menor dentro dela. Curioso, você abre essa segunda caixa e encontra outra caixa ainda menor.

Essa sequência de abrir caixas continua, e você se vê abrindo uma após a outra, cada vez encontrando uma caixa menor, até que finalmente, depois de abrir várias delas, você encontra a chave que estava procurando.

Esse processo de abrir caixas dentro de caixas é como a recursão na programação. Cada vez que você se depara com uma caixa, você precisa abrir outra caixa dentro dela, e assim por diante, até que encontre o que está procurando, no caso, a chave. Assim como na recursão, você está resolvendo uma parte do problema em cada etapa, até chegar à solução final.

### Exemplo em código:
Código disponível [aqui](https://github.com/joaomagi/Algoritmos/blob/main/Recursao.py)

# Hash
Evitar entradas duplicadas...• As tabelas hash são extremamente rápidas para pesquisar, inserir e
remover itens.
### Funções Hash
...
### Utilização como cache
...
