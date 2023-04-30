---
title: Resumo sobre Conceitos Iniciais
---

## Criação de processos e escalonamento 

quando um processo quer criar um outro processo, ele vai ter que criar uma entrada na tabela de processos para armazenar as informações do novo processo, inicializar essa estrutura de dados (processo) com os dados adequados, e criar uma nova imagem pra esse novo processo que vai ser criado, isso é feito através de uma chamada ao sistema. Nos sistemas unix, essa chamada ao sistema(system call) se chama fork.

quando o fork é executado, ele aloca uma área de memória pelo menos do mesmo tamanho da área de memória que o processo pai P1 está executando(P1’ é mais ou menos uma cópia do pai, onde ambos possuem o mesmo código, mesmo dados e mesma pilha, diferenciando-se apenas pelo local de memória), os processos, pai e filho, não dependem um do outro após a cópia ser feita.

ao início do fork, o filho criado vai possuir o id igual o id do pai, durante o fork, o filho adquire um novo id.

quando um processo que está rodando é bloqueado, ou quando ele vai de rodando para pronto pra rodar, é preciso escolher um novo processo para ganhar a CPU, quem faz essa decisão é o escalonador, um dos escalonadores mais populares é o round-robin.

a ideia do escalonamento round-robin é tentar ser igual com todos os processos, a ideia é que todos os processos que estão ativos vão ganhar uma fração da CPU que é mais ou menos a mesma. Para fazer isso, o algoritmo usa uma fila, onde o processo que está na cabeça é o que está rodando, e todos os processos em sequência estão prontos para rodar e serão executados nessa ordem.

quando um processo é criado, ele é colocado no estado “pronto pra rodar” e é colocado no final da fila.

quando um processo vai de “rodando” para bloqueado, ele sai da fila.

quando um processo que estava bloqueado é colocado no estado “pronto para rodar”, ele ganha prioridade dentro da fila, tendo em vista que o tempo de espera enquanto o mesmo estava bloqueado pode ter sido muito grande, os outros processos foram sendo executados várias vezes antes que esse processo estivesse novamente pronto para rodar, então é importante dar uma prioridade a esse processo,que por sua vez, fura fila e assume o segundo lugar na fila, logo após o que está sendo executado no momento.
 

## Threads

um padrão arquitetural muito comum é o dispatcher, o próprio terminal é um dispatcher, o dispatcher possui vários clientes que submetem requisições para ele, o dispatcher lê e repassa a requisição para ser executada por outra entidade.

os servidores que possuem esse padrão, precisam executar muitas tarefas independentes, (essas tarefas não precisam seguir uma ordem específica), dessa forma, o servidor pode executar essas requisições em paralelo.

em implementações mais tradicionais, mais antigas, isso era implementado da seguinte forma: o dispatcher espera a requisição dos clientes e um fork é criado para atender cada uma das requisições(cada requisição era atendida por um filho do dispatcher). Mesmo quando o sistema só tinha um processador, essa forma de implementação era válida, porque a requisição poderia envolver entrada/saída ou utilização da CPU, então enquanto uma requisição fazia IO, outras requisições poderiam usar a CPU, aumentando a utilização do sistema.

entretanto, usar múltiplos processos para implementar o fork tem seus problemas, o fork é uma sistema ao sistema cara(demora muito a ser executada), além disso, os filhos gerados através do fork, não podem se comunicar entre si e nem com o processo pai, devido ao não compartilhamento de memória por padrão, gerando a necessidade de uma implementação de comunicação entre os processos.

a abstração thread vem como alternativa de implementação, uma thread é uma unidade de computação escalonável, possui um fluxo de execução tal como um processo. Mais barato de criar e compartilham memória, facilitando a programação.

exemplo de caso de uso que podemos usar as threads é o google earth, com as threads temos: responsividade na interface com o usuário, melhoria de desempenho para renderização, melhoria de desempenho para IO, estruturação da aplicação.

## Condição de corrida

ainda falando sobre o programa contador de palavras, supondo que temos dois fluxos de execução, f1 e f2, e ambos compartilham e manipulam uma mesma área de memória, existe a possibilidade de que um dos fluxos de execução seja interrompido e perca a CPU em um momento indevido. Neste exemplo, vamos supor que f1 seja interrompido e f2 comece a executar, ao final da execução de f2 o f1 retorna a sua execução, porém f1 mantém armazenado o mesmo valor da primeira execução, ao invés de atualizar com o valor da execução de f2, desta forma, o valor final de f1 sobrescreve o valor de execução de f2 ao invés de somar os dois valores. o exemplo em questão é uma condição de corrida.

A condição de corrida sempre pode acontecer quando um código manipula uma área de memória que é compartilhada com mais de um fluxo, visto que o mesmo não possui nada que impeça a execução do segundo fluxo em caso do primeiro ser interrompido(se os fluxos forem só de leitura, não existe problema).

a região crítica do fluxo é seu código, em que em caso de interrupção em sua execução gera uma condição de corrida.

a melhor forma de resolver esse problema é implementar uma exclusão mútua na região crítica, ou seja, implementar uma maneira de garantir que se o fluxo f1 seja interrompido em sua região crítica, o fluxo f2 não execute sua respectiva região crítica, desta forma f1 receberia a CPU novamente e não ocorreriam erros no programa.

os requisitos para solução de exclusão mútua: deve garantir a exclusão mútua no acesso às regiões críticas, não pode fazer hipóteses sobre o número de processadores ou a velocidade relativa dos processadores, só deve impedir que um fluxo entre na região crítica se outro fluxo estiver usando a região crítica, deve evitar inanição(starvation).

## Solução de condição de corrida com espera ocupada

Essa solução não precisam de auxílio do sistema operacional para serem executadas/ implementadas, essa solução inclui algum código antes da região crítica que vai verificar se o fluxo em questão pode entrar na região crítica, então supondo que o f1 esteja executando sua respectiva região crítica, o f2 não poderá executar sua respectiva região crítica e ficará em loop até poder acessar/executar a região crítica, ao final da região crítica de cada fluxo deve haver um sinalizar apontando que a região crítica não está mais em uso.

No final da parte 1, o erro no sistema continua devido à solução aplicada, pois para “consertar” uma região crítica foi criada uma nova região crítica, na parte 2 é criada uma nova solução, nesta solução são criadas outras duas variáveis globais, uma delas indica de quem é a vez de executar a região crítica e a outra indica o número de threads que está executando de maneira concorrente, um id da thread também é setado, ocorre uma verificação para saber se é ou não a vez da thread executar sua região crítica, essa verificação é dada através do id da thread, e enquanto não for sua vez de executar, ela fica em loop, essa solução só possui uma variável referente a thread, que a thread_id, essa solução só admite uma thread por vez.

O problema da solução citada na parte 2, é que ela não atende a um dos requisitos de exclusão mútua: só deve impedir que um fluxo entre na região crítica se outro fluxo estiver usando a região crítica.

## Motivação para o uso de semáforos

Esse problema de exclusão mútua  pode ser resolvido usando outro tipo de solução, soluções que são oferecidas pelo sistema operacional que permitem que um processo ou uma thread ao invés de ficar em espera ocupada peça ao SO para bloquear aquele processo/thread e colocar um outro processo/thread para executar. A primeira solução desse tipo de estratégia chama-se semáforo. 