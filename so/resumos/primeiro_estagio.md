# Resumo do Primeiro Estágio

## Assuntos Abordados
- [Processos](#processos)
- [Comunicação entre Processos](#comunicacao)
- [Escalonamento de Processos](#escalonamento)
- [Thread](#thread)

## Processos

- Processos são estrutura de dados que representam instâncias de programas em execução e o seu contexto.
O contexto é formado por valores de variáveis, valores de registradores (Incluindo o Program Counter e 
o Stack Pointer) e os recursos utilizados (arquivos abertos, processos relacionados ...).

- **Multiprogramação (ou time-sharing)** é o chaveamento entre a execução de vários processos criando a ilusão
de uma execução em paralelo. 

- **Troca de contexto** é quando um processo é retirado de execução para que outro seja executado.

- Todos os processos instanciados são filhos de um processo pai e existe um processo que é inicializado
ao realizar o carregamento do Sistema Operacional. No linux, esse processo é chamado de **systemd**.

- Um **PID** é um identificador único para um processo.

- Na família de SO UNIX existe uma operação chamada **fork**. Essa operação clona o processo em dois. O
resultado do fork no filho retorna 0 e no pai retorna o PID do filho.

![imagem de fork](http://www.ppgia.pucpr.br/~laplima/ensino/so/materia/images/ps-fork.png)

- Existem três principais estados para um processo: **Bloqueado, Rodando e Pronto para Rodar**.

![estados de um processo](http://www.ppgia.pucpr.br/~laplima/ensino/so/materia/images/ps-estados.png)

- **Escalonador** é responsável por realizar a troca de contexto entre os processos em execução.

- **Interrupções** são sinais produzidos por hardware para interromper uma execução de um processo.
Existem diversos tipos de interrupções, mas uma interrupção importante é a *interrupção por relógio*.
Ela ajuda o escalonador a realizar a troca de contexto.

- Para guardar as informações dos processos, é necessário existir uma **tabela de processos** gerenciada
pelo SO.

## Comunicação entre Processos

- É possível utilizar diversas técnicas para comunicação entre processos, contudo é necessário
ter cuidado com as regiões de memória compartilhada, pois elas podem levar a diversos problemas:
  * Condição de Corrida: dois ou mais processos estão tentando acessar uma área da memória e o resultado
  depende da ordem de execuçao dos processos.
  
- **Exclusão mútua de execução** é a propriedade esperada em processos para que só um execute um trecho
de código por vez.

- **Região Crítica** é a área do código em que a manipulação de um dado compartilhado pode gerar 
condição de corrida entre processos.

- Existem dois tipos de algoritmos de exclusão mútua: **exclusão mútua com espera ocupada e com bloqueio e desbloqueio**

### Espera ocupada (busy wait)

- Para realizar essa exclusão mútua, é necessária que o SO bloquei as interrupções de relógio para
que o processo não saia de processamento até sair da região crítica.

- Problema da abordagem é que não é boa prática dar essa liberdade ao usuário, pois ele pode
tomar conta do processamento e não devolver para outros processos.

*Necessita de Conteúdo sobre os algoritmos utilizados para realizar a espera ocupada*

### Bloqueio e Desbloqueio

- Espera ocupada gasta muito tempo de processador. A solução é bloquear um processo quando ele tentar
entrar numa região crítica e só acorda-lo quando ele puder acessa-la.

- Dois comandos importantes: `sleep()` e `wakeup(pid)`

- Problema da abordagem é que as operações de teste e de sleep não são atômicas em um computador,
isso pode fazer que o teste execute e seja trocado o contexto, abrindo brecha para o aparecimento de
**Deadlock**.

- Deadlock é uma situação de travamento da execução de dois ou mais processos em que um fica esperando
que o outro o acorde de forma que nenhum consiga ser acordado nem acordar o outro.

#### Semáforos

- Semáforo é um contado de wakeups.

- Contêm duas operações principais *down(sem)* e *up(sem)*
```javascript
  down(sem){
    if (sem == 0) sleep();
    sem--;
  }
```

```javascript
  up(sem){
    sem++;
    if (sem == 1)
      wakeup(processo_dormindo_em_sem);
  }
```

- É importante que não haja interrupção entre o teste e a ação. Por isso, existem comandos chamados de
**TSL** (test and set lock) para realizar o teste e a modificação de um registrador em um só comando.

- **Monitores** são mecanismos de alto nível cujo objetivo principal é garantir a exclusão mútua de 
execução.

## Escalonamento de Processos

- Escalonamento a curto prazo é o escalonamento voltado para organização do processo na CPU.

- Escalonamento a médio prazo é o escalonamento voltado para organização do processo na memória.

- **Algoritmo de escalonamento** é o algoritmo que realiza a lógica para alternar os processos em
execução.

- Para realizar o escalonamento, é necessário que um relógio lance periodicamente interrupções para
que o SO consiga interromper aquele processo e colocar outro em execução.

- Esse tipo de escalonamento em que o processo é interrompido é conhecido como **escalonamento preemptivo**.

- Uma implementação **não preemptiva** é a *Fist-Come, first-served*. Ela não habilita a interrupção
por relógio e um processo é mantido em execução até que terminem ou sejam bloqueados. É implementado
em cima de uma fila de processos.

- Uma implementação preemptiva é o **Round-robin**. Ele também funciona em uma fila, mas as interrupções
de relógios fazem possível que um processo(p1) execute parcialmente e ao final da sua fatia de tempo seja
possível salvar seu estado para que outro processo(p2) rode, e, posteriormente o ele(p1) consiga prosseguir com
sua execução.

## Thread

- Executar um fork para rodar o mesmo código gera uma quantidade de dados replicados e recursos duplicados.

- Para solucionar esse problema, é criado o conceito de **processos leves** ou **threads**.

### Características Importantes

 - Compartilhar recursos entre linhas de execução; ter seu próprio fluxo de controle; morre se o 
 processo que os contém morrer.
 
 - Threads **NÃO** compartilham: seu PC, seu ponteiro de pilha, seu registrador, seus sinais pendentes e bloqueados,
 seus próprios dados e suas propriedades de escalonamento;
 
 ![memória de múltiplas threads](http://www.ppgia.pucpr.br/~laplima/ensino/so/materia/images/ps-modelo_threads.png)
 
