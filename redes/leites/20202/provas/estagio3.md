---
title: Prova 3º estagio
---

- **Disciplina:** Redes de Computadores
- **Período:** 2020.2

## Aviso!

1. O periodo 2020.2 foi efetuado de forma remota, por causa disso, as provas da disciplina de redes foram efetuadas pelo AVA - Computação, dessa forma as questões aqui presentes foram apenas algumas das que podiam ser sorteadas entre os alunos.


## Questões

#### Questão 1 

Qual a importância do processo de abertura e fechamento de uma conexão TCP entre duas estações? Por que esse procedimento não é necessário no UDP?

#### Questão 2 

Um aluno resolveu implementar uma variação do mecanismo de controle de congestionamento do TCP fazendo duas alterações: 1) iniciar a janela de congestionamento com o tamanho de 16 MSS, 2) o valor inicial do limiar é de 2048 e 3) ao detectar uma falha por timeout reduzir o tamanho da janela de congestionamento para metade do valor do limiar reajustado. Ao testar a sua implementação ele identificou que conseguiu um desempenho melhor do que estava tendo anteriormente. Por que isso aconteceu?

#### Questão 3

Como o TCP compatibiliza a quantidade de informações que podem ser transmitidas/recebidas entre duas estações em um determinado instante?

#### Questão 4

Ao iniciar uma conexão, o TCP tenta descobrir a que taxa pode transmitir sem que congestione a rede que interliga as duas estações. Para tanto ele faz uso do mecanismo de controle de congestionamento, que se baseia no monitoramento de dois eventos que geram erros em uma comunicação. Quais são esses dois eventos e quais as reações do protocolo com cada um deles?

#### Questão 5

Na camada de transporte do modelo TCP/IP pode-se utilizar os protocolos TCP e UDP. Por que é necessária a implementação de mais de um protocolo nessa camada?

#### Questão 6

Cada camada da pilha de protocolos possui um identificador que é utilizado para permitir diferenciar unicamente as entidades envolvidas em uma comunicação. No caso da camada de transporte (mais especificamente usando o protocolo TCP), quais informações um processo rodando em um host utiliza para identificar um outro processo rodando em um outro host? E se os processos estiverem num mesmo host, como esta identificação acontece?
