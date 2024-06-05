# Algoritmos
# Referência de Estudo

Estou estudando esses conceitos a partir do livro **Entendendo Algoritmos: Um Guia Ilustrado Para Programadores e Outros Curiosos**, escrito por [Aditya Y. Bhargava](https://github.com/KAYOKG/BibliotecaDev/blob/main/LivrosDev/Entendendo%20Algoritmos%20-%20Um%20Guia%20Ilustrado%20Para%20Programadores%20e%20Outros%20Curiosos%20-%20Autor%20(Aditya%20Y.%20Bhargava).pdf).

Este livro tem me inspirado a aprender sobre algoritmos e estruturas de dados

---
# Pesquisa Simples

A pesquisa simples, também conhecida como busca linear, é um método básico de busca em uma lista de itens. Ela envolve percorrer sequencialmente cada elemento da lista, um por um, até encontrar o valor desejado.

### Exemplo:
Suponha que você tenha uma lista de números e esteja procurando por um número específico. Você começa verificando o primeiro número da lista, depois o segundo, o terceiro, e assim por diante, até encontrar o número desejado.

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

### Array
Arrays são uma estrutura de dados básica que armazena uma coleção de elementos do mesmo tipo em posições contíguas na memória. Eles permitem o acesso rápido a qualquer elemento usando índices.

### Exemplo:
Imagine que você tenha uma lista "top 10" de vilões da TV e queira acessar o vilão no índice 5. Em um array, você pode ir diretamente ao índice 5 e encontrar o vilão desejado instantaneamente.

### Características:
- Contíguo na Memória: Todos os elementos estão armazenados em locais adjacentes.
- Acesso Direto: Você pode acessar qualquer elemento diretamente pelo índice. Por exemplo, o quinto elemento de um array que começa no endereço 00 estará no endereço 04.
- Tamanho Fixo: O tamanho do array é definido na sua criação e não pode ser alterado.


### Lista encadeadas
As listas encadeadas são estruturas de dados onde cada item pode estar em qualquer lugar da memória. Cada item armazena o endereço do próximo item, criando uma cadeia de referências.

### Exemplo:
Imagine uma caça ao tesouro onde cada pista leva à próxima localização. Você começa no primeiro endereço que te diz "o próximo item está no endereço 123". Quando chega ao endereço 123, ele diz "o próximo item está no endereço 938", e assim por diante.

### Características:
- Endereços de Memória Ligados: Os itens não estão armazenados contiguamente, mas cada item sabe onde está o próximo.
- Inserção Fácil: Para adicionar um novo item, você simplesmente o coloca em qualquer lugar da memória disponível e atualiza os endereços.
- Flexibilidade de Memória: Não precisa de um bloco contíguo de memória, então sempre que houver espaço suficiente, você pode adicionar itens à lista.

### Ordenação por seleção


### Recursão



