# Esta implementação foi feita em Python 3.
# Esteja ciente disso ao executar :)

# Uma stack, ou pilha, é uma estrutura de dados
# que segue o padrão LIFO: Last In, First Out,
# isto é, o último a entrar é o primeiro a sair.

# Seguindo as diretrizes dos roteiros de LEDA,
# nossa pilha terá as seguintes funções:
# put, pop, top, isEmpty e isFull. Assim como
# em LEDA, também verificaremos as exceções nos
# parâmetros das funções. Vejamos como ficaria
# a nossa classe para implementação da Pilha:

class Stack(object):
    def __init__(self, max_size, item_type):
        """
        Construtor da classe.

        Recebe como parâmetro o tamanho máximo que 
        a pilha pode atingir e o tipo do item da pilha,
        definindo que a pilha só terá itens de um tipo
        (ou int, ou float, ou string, etc).
        """
        self.stack = []
        self.max_size = max_size
        self.item_type = item_type

    def put(self, new_item):
        """
        Adiciona um novo item à pilha.
        Se a pilha já estiver cheia, retorna uma exceção.
        """

        if (new_item is None):
            raise Exception("Não é possível adicionar None à pilha")

        if (type(new_item) != self.item_type):
            raise Exception("A pilha só permite itens do tipo {}".format(str(self.item_type)))

        if (self.is_full()):
            raise Exception("Pilha cheia: impossível adicionar itens.")

        self.stack.append(new_item)

    def pop(self):
        """
        Remove um item da pilha. Naturalmente, o item a
        ser removido da pilha é aquele que está no topo.
        """

        if (self.is_empty()):
            raise Exception("Pilha vazia: impossível remover itens.")

        removed = self.stack.pop()
        return removed

    def top(self):
        """
        Recupera o item no topo da pilha.
        """

        if (self.is_empty()):
            raise Exception("Pilha vazia: impossível recuperar item.")
        
        top_item = self.stack[-1]
        return top_item

    def is_empty(self):
        """
        Verifica se a pilha está vazia.
        """

        return (len(self.stack) == 0)

    def is_full(self):
        """
        Verifica se a pilha está cheia.
        """

        return (len(self.stack) == self.max_size)

    def to_array(self):
        """
        Retorna o array que representa a Pilha.
        """
        
        return self.stack

# Agora, criaremos algumas asserções, verificando a corretude
# da implementação da nossa Pilha :)

# Teste 1: pilha de tamanho 1:

stack_test1 = Stack(1, int)
assert stack_test1.is_full() == False
assert stack_test1.is_empty() == True
stack_test1.put(0)
assert stack_test1.is_full() == True
assert stack_test1.is_empty() == False
assert stack_test1.top() == 0
try:
    stack_test1.put(1)
except Exception as exc:
    assert str(exc) == "Pilha cheia: impossível adicionar itens."

assert stack_test1.pop() == 0
try:
    stack_test1.pop()
except Exception as exc:
    assert str(exc) == "Pilha vazia: impossível remover itens."

try:
    stack_test1.top()
except Exception as exc:
    assert str(exc) == "Pilha vazia: impossível recuperar item."

# Teste 2: pilha de tamanho 3:

stack_test2 = Stack(3, int)
assert stack_test2.is_empty() == True
for i in range(0, 3):
    assert stack_test2.is_full() == False
    stack_test2.put(i)
    assert stack_test2.is_empty() == False
    assert stack_test2.top() == i

assert stack_test2.is_full() == True
assert stack_test2.is_empty() == False

try:
    stack_test2.put(1)
except Exception as exc:
    assert str(exc) == "Pilha cheia: impossível adicionar itens."

assert stack_test2.pop() == 2
assert stack_test2.pop() == 1
assert stack_test2.pop() == 0
try:
    stack_test2.pop()
except Exception as exc:
    assert str(exc) == "Pilha vazia: impossível remover itens."

try:
    stack_test2.top()
except Exception as exc:
    assert str(exc) == "Pilha vazia: impossível recuperar item."

# Teste 3: verificando tipos

stack_test3 = Stack(5, str)
try:
    stack_test3.put(None)
except Exception as exc:
    assert str(exc) == "Não é possível adicionar None à pilha"

try:
    stack_test3.put(0.5)
except Exception as exc:
    assert str(exc) == "A pilha só permite itens do tipo {}".format(str(str))

try:
    stack_test3.put(1)
except Exception as exc:
    assert str(exc) == "A pilha só permite itens do tipo {}".format(str(str))