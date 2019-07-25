# # Esta implementação foi feita em Python 3.
# Esteja ciente disso ao executar :)

# Nesse arquivo, focaremos na implementação
# dos nós de uma lista encadeada, ou Linked List.
# Entretanto, existem dois tipos de Linked List:
# Single Linked List, onde cada nó só aponta
# para o nó sucessor, e Double Linked List,
# onde cada nó aponta tanto para o nó antecessor
# quanto para o sucessor. Vejamos a implementação
# desses dois tipos de nós:

class SingleLinkedListNode(object):
    def __init__(self, value=None, next_node=None):
        """
        Construtor da classe.

        Recebe como parâmetro o valor do nó e,
        caso necessário, o nó seguinte. Quando não há
        um nó seguinte, consideraremos o next_node
        como None que, de certa forma, equivale a null.
        """
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        """
        Define o nó sucessor do nó atual.
        Caso já exista um nó definido como sucessor,
        o sobreescreve, perdendo a referência.
        """
        self.next_node = next_node

    def set_value(self, value):
        """
        Define o valor do nó atual.
        Caso já exista um valor definido, o sobreescreve,
        perdendo a referência.
        """
        self.value = value

    def is_nil(self):
        """
        Verifica se o nó atual é um nó NIL, isto é,
        que existe mas não tem referência de valor.
        """
        return self.value == None

    def get_next(self):
        """
        Recupera o nó sucessor.
        """
        return self.next_node

    def get_value(self):
        """
        Recupera o valor do nó
        """
        return self.value

# O nó da DoubleLinkedList também precisa de todas as operações
# e atributos que o nó da SingleLinkedList, e apenas adiciona os
# atributos e funções referentes ao nó antecessor. Assim, faremos
# com que o nó da DoubleLinkedList herde o nó da SingleLinkedList:

class DoubleLinkedListNode(SingleLinkedListNode): # <-- Herança aqui
    def __init__(self, value=None, next_node=None, previous_node=None):
        """
        Construtor da classe.

        Inicia o nó da Single Linked List com os parâmetros
        recebidos e define seu nó antecessor.
        """
        super(DoubleLinkedListNode, self).__init__(value, next_node)
        # Com a linha acima, agora temos a herança estabelecida e podemos
        # acessar os atributos e funções herdadas utilizando self.

        self.previous_node = previous_node

    def set_previous_node(self, previous_node):
        """
        Define o nó antecessor do nó atual.
        Caso já exista um nó definido como antecessor,
        o sobreescreve, perdendo a referência.
        """
        self.previous_node = previous_node

    def get_previous(self):
        """
        Recupera nó antecessor.
        """
        return self.previous_node

# Agora podemos importar os nós nos arquivos de implementação
# das Linked Lists.