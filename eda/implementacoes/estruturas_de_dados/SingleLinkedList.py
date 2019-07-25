# # Esta implementação foi feita em Python 3.
# Esteja ciente disso ao executar :)

# Nesse arquivo, focaremos na implementação da Single
# Linked List, uma estrutura similar a um array, mas
# de tamanho dinâmico, e que funciona por meio de nós,
# onde a lista mantém uma referência ao primeiro nó,
# e cada nó mantém o seu valor e a referência ao nó
# seguinte. As funções implementadas se baseiam nas
# necessárias em LEDA.

from LinkedListNodes import SingleLinkedListNode

class SingleLinkedList(object):
    def __init__(self):
        """
        Construtor da classe.

        Inicia uma Single Linked List vazia, apenas
        com referência ao primeiro elemento.
        """
        self.head = SingleLinkedListNode()

    def is_empty(self):
        """
        Retorna se a lista está vazia.
        A lista está vazia se o primeiro elemento
        for um nó NIL.
        """
        return self.head.is_nil()

    def insert(self, element):
        """
        Insere um novo elemento na LinkedList.
        
        O elemento passado como parâmetro deve ser
        um elemento válido e, caso seja None, deve ser
        ignorado.
        """
        if (element != None):

            if (self.head.is_nil()):
                self.head.set_value(element)
            else:
                current_node = self.head
                while (not current_node.get_next() == None):
                    current_node = current_node.get_next()

                current_node.set_next_node(SingleLinkedListNode(element))

    def remove(self, element):
        """
        Remove um elemento existente na LinkedList.
        
        O elemento passado como parâmetro deve ser
        um elemento válido, isto é, não pode ser None.
        Caso o elemento passado não exista na lista,
        esta deve se manter inalterada.
        """

        to_return = None

        if (element != None and not self.head.is_nil()):
            if (self.head.get_value() == element):
                if (self.head.get_next() != None):
                    self.head = self.head.get_next()
                else:
                    self.head.set_value(None)
                to_return = element
            
            else:
                current_node = self.head
                while (current_node.get_next() != None):
                    if (current_node.get_next().get_value() == element):
                        current_node.set_next_node(current_node.get_next().get_next())
                        to_return = element
                        break
                    else:
                        current_node = current_node.get_next()

        return to_return

    def size(self):
        """
        Calcula o tamanho da lista encadeada.
        """
        linked_size = 0
        current_node = self.head
        while (current_node != None and not current_node.is_nil()):
            linked_size += 1
            current_node = current_node.get_next()
        return linked_size

    def search_index(self, searched_value):
        """
        Busca um elemento na lista encadeada e retorna
        sua posição. Caso o elemento não seja encontrado,
        deve-se retornar -1.
        """
        index = -1
        if (searched_value != None):
            current_node = self.head
            while (current_node != None and not current_node.is_nil()):
                index += 1
                if (current_node.get_value() == searched_value):
                    break
                current_node = current_node.get_next()
        return index

    def search(self, searched_value):
        """
        Busca um elemento na lista encadeada e retorna
        seu valor. Caso o elemento não seja encontrado,
        deve-se retornar None.
        """
        node_value = None
        if (searched_value != None):
            current_node = self.head
            while (current_node != None and not current_node.is_nil()):
                if (current_node.get_value() == searched_value):
                    node_value = searched_value
                    break
                current_node = current_node.get_next()
        return node_value

    def to_array(self):
        """
        Transforma a lista encadeada em uma lista,
        respeitando a ordem dos elementos da lista
        encadeada
        """
        array = []
        current_node = self.head
        while (current_node != None and not current_node.is_nil()):
            array.append(current_node.get_value())
            current_node = current_node.get_next()
        return array

# Agora, criaremos algumas asserções, verificando a corretude
# da implementação da nossa Single linked List :)

# Teste 1: inserção e remoção na lista

sll = SingleLinkedList()
assert sll.is_empty() == True
assert sll.to_array() == []
assert sll.size() == 0

sll.insert(3)
assert sll.is_empty() == False
assert sll.search(3) == 3
assert sll.search_index(3) == 0
assert sll.to_array() == [3]
assert sll.size() == 1

assert sll.remove(3) == 3
assert sll.size() == 0

# Teste 2: mais inserção e remoção na lista :D

sll = SingleLinkedList()
assert sll.is_empty() == True
assert sll.to_array() == []

sll.insert(1)
assert sll.is_empty() == False
assert sll.search(1) == 1
assert sll.search_index(1) == 0
assert sll.to_array() == [1]
assert sll.size() == 1

sll.insert(5)
assert sll.is_empty() == False
assert sll.to_array() == [1, 5]
assert sll.search(5) == 5
assert sll.search_index(5) == 1
assert sll.size() == 2

sll.insert(10)
assert sll.is_empty() == False
assert sll.search(10) == 10
assert sll.search_index(10) == 2
assert sll.to_array() == [1, 5, 10]
assert sll.size() == 3

assert sll.remove(5)
assert sll.to_array() == [1, 10]
assert sll.size() == 2

assert sll.remove(1)
assert sll.to_array() == [10]
assert sll.size() == 1

assert sll.remove(10)
assert sll.to_array() == []
assert sll.size() == 0

# Teste 3: Erros

sll = SingleLinkedList()
assert sll.is_empty() == True
assert sll.to_array() == []
assert sll.size() == 0

sll.insert(15)
assert sll.is_empty() == False
assert sll.search(15) == 15
assert sll.search_index(15) == 0
assert sll.to_array() == [15]
assert sll.size() == 1

assert sll.remove(3) == None
assert sll.size() == 1
assert sll.to_array() == [15]

sll.insert(None)
assert sll.size() == 1
assert sll.to_array() == [15]
assert sll.remove(None) == None