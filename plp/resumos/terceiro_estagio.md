---
title: Resumo do Terceiro Estágio
---

## Introdução
Paradigmas funcional e imperativo têm algo em comum: o programa lê entradas e gera saídas e resolve problemas através de mapeamento.
O programa segundo o paradigma lógico implementa uma relação, relações são mais gerais que mapeamentos, tornando a programação lógica mais alto nível que a programação imperativa ou funcional.
As linguagens de programação lógicas estão restritas à cláusulas de Horn, que é uma cláusula com no máximo um literal positivo. Sendo assim, um programa lógico é uma coleção de cláusulas Horn.

![intro_logica](https://i.imgur.com/CIEwSA8.png)

## Paradigma Lógico
Também parte da sub categoria “paradigma declarativo”.
Os programas lógicos se preocupam com os fatos e não com os procedimentos.
O conhecimento acerca do problema é descrito usando lógica simbólica.
Formalismo lógico-computacional fundamentado em três princípios:
- Uso de linguagem formal para representação de conhecimento.
- Uso de regras de inferência para manipulação de conhecimento.
- Uso de uma estratégia de busca para controle de inferências.
O programador deve preocupar-se em descrever o problema a ser solucionado, deixando a critério da máquina a busca pela solução.

## Linguagem Formal
Uma linguagem natural pode ser ambígua, já uma linguagem formal é precisa.

## Regras de Inferência
Uma regra de inferência é um padrão de manipulação sintática que: permite criar novas fórmulas a partir de outras existentes e em geral, simulam formas de raciocínio válidas.

![regra_inferencia](https://i.imgur.com/RQ35mzy.png)

## Estratégia de Busca
Um agente pode ter uma enorme quantidade de conhecimento armazenado, mas normalmente ele precisa usar apenas parte de seu conhecimento para resolver um problema. Estratégia de busca serve para decidir que parte do conhecimento armazenado deve ser explorada em busca da solução.

## Prolog
- LP lógica geralmente associada com o contexto de IA e/ou linguística.
- Possui suas raízes na lógica de primeira-ordem.
- Foi uma das primeiras LPs lógicas e se mantém como a mais popular
- Bastante usada para prova de teoremas, sistemas especialistas, processamento de linguagens naturais etc.
- Permite representar o conhecimento que um agente tem sobre seu mundo de uma forma: Simples, direta e em alto nível.
- Programação imperativa é como o computador deve proceder para resolver um problema
- Programação Lógica é declarar o conhecimento que temos acerca do problema, ou seja, o sistema deve ser capaz de encontrar a solução.

### Prolog - Cláusulas Horn:
- Se as condições A1, A2, … e An forem verdadeiras, então a conclusão B é verdadeira
- Se algum Ai for falso, não se pode deduzir que A1 é verdadeiro, mas que não se pode inferir
Toda cláusula termina com um ponto (.).
Nomenclatura:
- Se n = 0 a cláusula é chamada de fato
- Se n >= 1 a cláusula é chamada de regra

![clausula_horn](https://i.imgur.com/WUSli2y.png)

### Prolog - Unificação:
Unificação é o mecanismo usado para determinar se existe uma maneira de instanciar as variáveis de dois predicados de modo a torná-los iguais.

![unificacao](https://i.imgur.com/invCNoy.png)

### Prolog – Algoritmo de Execução:
- Ao receber uma consulta, o Prolog tenta unificá-la com cada um dos fatos e com a cabeça das regras que estão na base de conhecimento.
- Se houver unificação com um fato, retorna as instâncias das variáveis.
- Se existe unificação com a cabeça de uma regra, consulta, recursivamente, o corpo da regra (da esquerda para a direita), podendo haver retrocessos (backtracking) no caso de uma unificação não ser bem sucedida, tentando explorar outras unificações alternativas.
- Se todas as alternativas forem exploradas sem sucesso, então a resolução falha.

### Prolog - Listas:
Lista em Prolog é uma estrutura que representa uma sequência de elementos de qualquer comprimento, sendo a estrutura [h|t] denota uma lista cuja cabeça é h e cuja cauda é t, semelhante a Haskell.

![lista_logica_1](https://i.imgur.com/pHnywR3.png)

Prolog fornece a notação barra vertical para separar alguns elementos da lista do restante da lista.

![lista_logica_2](https://i.imgur.com/Hn6aN0J.png)

Listas em Prolog são heterogêneas, isto é, podem conter valores de diferentes tipos.

Podemos comparar valores de diferentes tipos usando a relação ”=” mas o resultado será false.

![lista_logica_3](https://i.imgur.com/0CIDrl6.png)





