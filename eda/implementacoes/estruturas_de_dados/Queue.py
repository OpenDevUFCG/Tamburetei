# Esta implementação foi feita em Python 3.
# Esteja ciente disso ao executar :)

# Uma Queue, ou fila, é uma estrutura de dados
# que segue o padrão FIFO: First In, First Out,
# isto é, o primeiro a entrar é o primeiro a sair.

# Seguindo as diretrizes dos roteiros de LEDA,
# nossa fila terá as seguintes funções:
# enqueue, dequeue, head, isEmpty e isFull. Assim como
# em LEDA, também verificaremos as exceções nos
# parâmetros das funções. Vejamos como ficaria
# a nossa classe para implementação da fila:

class Queue(object):
    def __init__(self, max_size, item_type):
        """
        Construtor da classe.

        Recebe como parâmetro o tamanho máximo que 
        a fila pode atingir e o tipo do item da fila,
        definindo que a fila só terá itens de um tipo
        (ou int, ou float, ou string, etc).
        """
        self.queue = []
        self.max_size = max_size
        self.item_type = item_type

    def enqueue(self, new_item):
        """
        Adiciona um novo item à fila.
        Se a fila já estiver cheia, retorna uma exceção.
        """

        if (new_item is None):
            raise Exception("Não é possível adicionar None à fila")

        if (type(new_item) != self.item_type):
            raise Exception("A fila só permite itens do tipo {}".format(str(self.item_type)))

        if (self.is_full()):
            raise Exception("Fila cheia: impossível adicionar itens.")

        self.queue.append(new_item)

    def dequeue(self):
        """
        Remove um item da fila. Naturalmente, o item a
        ser removido da fila é aquele que está no topo.
        """

        if (self.is_empty()):
            raise Exception("Fila vazia: impossível remover itens.")

        removed = self.queue.pop(0)
        return removed

    def head(self):
        """
        Recupera o item no topo da fila.
        """

        if (self.is_empty()):
            raise Exception("Fila vazia: impossível recuperar item.")
        
        head_item = self.queue[0]
        return head_item

    def is_empty(self):
        """
        Verifica se a fila está vazia.
        """

        return (len(self.queue) == 0)

    def is_full(self):
        """
        Verifica se a fila está cheia.
        """

        return (len(self.queue) == self.max_size)

# Agora, criaremos algumas asserções, verificando a corretude
# da implementação da nossa fila :)

# Teste 1: fila de tamanho 1:

queue_test1 = Queue(1, int)
assert queue_test1.is_full() == False
assert queue_test1.is_empty() == True
queue_test1.enqueue(0)
assert queue_test1.is_full() == True
assert queue_test1.is_empty() == False
assert queue_test1.head() == 0
try:
    queue_test1.enqueue(1)
except Exception as exc:
    assert str(exc) == "Fila cheia: impossível adicionar itens."

assert queue_test1.dequeue() == 0
try:
    queue_test1.dequeue()
except Exception as exc:
    assert str(exc) == "Fila vazia: impossível remover itens."

try:
    queue_test1.head()
except Exception as exc:
    assert str(exc) == "Fila vazia: impossível recuperar item."

# Teste 2: fila de tamanho 3:

queue_test2 = Queue(3, int)
assert queue_test2.is_empty() == True
for i in range(0, 3):
    assert queue_test2.is_full() == False
    queue_test2.enqueue(i)
    assert queue_test2.is_empty() == False

assert queue_test2.is_full() == True

try:
    queue_test2.enqueue(1)
except Exception as exc:
    assert str(exc) == "Fila cheia: impossível adicionar itens."

assert queue_test2.dequeue() == 0
assert queue_test2.dequeue() == 1
assert queue_test2.dequeue() == 2
try:
    queue_test2.dequeue()
except Exception as exc:
    assert str(exc) == "Fila vazia: impossível remover itens."

try:
    queue_test2.head()
except Exception as exc:
    assert str(exc) == "Fila vazia: impossível recuperar item."

# Teste 3: verificando tipos

queue_test3 = Queue(5, str)
try:
    queue_test3.enqueue(None)
except Exception as exc:
    assert str(exc) == "Não é possível adicionar None à fila"

try:
    queue_test3.enqueue(0.5)
except Exception as exc:
    assert str(exc) == "A fila só permite itens do tipo {}".format(str(str))

try:
    queue_test3.enqueue(1)
except Exception as exc:
    assert str(exc) == "A fila só permite itens do tipo {}".format(str(str))