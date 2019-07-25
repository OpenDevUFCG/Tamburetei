from Stack import Stack

# Nossa classe da Pilha já havia sido implementada
# anteriormente no arquivo Stack, então vamos utilizá-la
# para resolver um problema envolvendo Pilhas.

# Problema: Crie uma função que, utilizando os conceitos de
# pilhas, ordene um array de inteiros de tamanho 10. Entretanto,
# não é permitido que haja efeito colateral na lista recebida
# como parâmetro.

unordered = [6, 8, 9, 2, 5, 4, 7, 3, 1, 15]

# Vamos começar a pensar: no enunciado da questão, já foi dito
# que era necessário utlizar os conceitos de pilha para resolver
# o problema. Vamos então criar uma pilha e, enquanto os
# elementos estão chegando ordenados, continuamos a inserí-los
# na pilha. Considerando o array de entrada, nossa pilha ficaria
# da seguinte forma:

stack = [6, 8, 9]
inserting_next = 2

# Entretanto, o 2 deve ficar no fim da pilha, e para isso teremos
# que remover elementos até que a pilha esteja vazia, e não temos
# onde guardar esses elementos. Podemos então criar uma pilha
# auxiliar, que guarda os elementos maiores que o proximo elemento
# a ser inserido. Assim, na inserção do 2, o passo a passo seria:

stack = [6, 8, 9]
inserting_next = 2
aux_stack = []

stack = [6, 8]
aux_stack = [9]

stack = [6]
aux_stack = [9, 8]

stack = []
aux_stack = [9, 8, 6]

stack = [2]
aux_stack = [9, 8, 6]

stack = [2, 6]
aux_stack = [9, 8]

stack = [2, 6, 8]
aux_stack = [9]

stack = [2, 6, 8, 9]
aux_stack = []

# Agora que já sabemos como é a lógica do algoritmo, podemos
# criar uma função que o representa. Vejamos:

def sort_with_stacks(unordered_array, debug=False):
    """
    Ordena um array utilizando pilhas.
    
    Recebe um parâmetro indicando se deve printar o passo a passo
    das pilhas enquanto executa o algoritmo, assim como explicado acima,
    para facilitar o entendimento.
    """
    def do_debug(debug):
        if (debug):
            print(main_stack.to_array())
            print(aux_stack.to_array())

    main_stack = Stack(10, int)
    aux_stack = Stack(10, int)

    for element in unordered_array:
        if (debug): print("Transferindo para Auxiliar:")

        while not main_stack.is_empty():
            # Enquanto ainda há elementos na pilha, os removeremos,
            # guardando-os na pilha auxiliar
            if (main_stack.top() < element):
                # Se o elemento do topo for menor que o elemento
                # a inserir, paramos de remover.
                break

            do_debug(debug)

            aux_stack.put(main_stack.pop())

        if (debug):
            print("---\nAdicionando elemento atual:")

        # Adicionamos o elemento atual em sua posição correta
        main_stack.put(element)

        if (debug):
            do_debug(debug)
            print("---\nRetornando elementos para principal:")

        # Readicionamos os elementos à pilha principal

        while not aux_stack.is_empty():
            main_stack.put(aux_stack.pop())

            if (debug):
                do_debug(debug)
                print('---')

        if (debug): print("---\n\nPróximo elemento.\n")

    return main_stack.to_array()

# Vejamos agora o resultado da execução do nosso algoritmo:
print(sort_with_stacks(unordered))

# Caso deseje ver o passo a passo, descomente a linha abaixo e execute
# novamente.

# print(sort_with_stacks(unordered, True))

# Façamos agora um teste real: vamos utilizar a função rand do numpy
# para testar nossa função. Essa função gera um conjunto de n números
# aleatórios. O objetivo do nosso teste será comparar o resultado da
# nossa ordenação com o resultado da ordenação nativa de Python.

from numpy.random import rand

for i in range(10):
    # Geramos então 10 inteiros aleatórios entre 0 e 100:
    random_numbers = [int(j*100) for j in rand(10)]

    # Ordenamos com a nossa função e com a função nativa
    result = sort_with_stacks(random_numbers)
    random_numbers.sort()

    # Comparamos o resultado:
    assert result == random_numbers