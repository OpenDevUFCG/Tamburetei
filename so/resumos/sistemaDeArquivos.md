---
title: Resumo de Sistema de Arquivos
---

## Introdução

O sistema de arquivos unix é um sistema hierárquico, cada diretório tem filhos que pode ser outros diretórios ou arquivos, a funcionalidade principal é implementar uma hierarquia de nomes e descobrir onde o conteúdo associado a esse nome está armazenado.

Existe a necessidade de se armazenar informação permanentemente, um arquivo é a abstração usada para permitir essa forma de armazenamento permanente.

Além dos dados propriamente, arquivos tem metadados associados a si, que servem para:
    a. Identificar a informação armazenada
    b. Definir permissões de acesso ao arquivo
    c. Informar onde os dados do arquivo estão armazenados
    d. Outras informações importantes para a gerência dos arquivos 

Um sistema de arquivos define a forma como o sistema operacional organiza os dados e os metadados dos arquivos em um dispositivo de armazenamento permanente.
 
A eficiência de um sistema de arquivos depende da capacidade de manter parte das informações em memória, evitando que toda operação seja feita no dispositivo. Um sistema de arquivos define também as estruturas de dados que precisam ser mantidas em memória para esse fim.

O acesso às informações armazenadas em arquivos é feito através de chamadas ao sistema bem definidas(read/write, open/close, get/set, seek).

A maior parte dos sistemas de arquivos armazena os metadados em arquivos especiais chamados de diretórios, os diretórios são organizados hierarquicamente.

Cada entrada do diretório associa um nome de um arquivo a uma estrutura de dados chamada i-node. O diretório armazena apenas um metadado, que é o nome do arquivo, todos os outros metadados são armazenados no i-node, o i-node contém, entre outras coisas, informações sobre a localização dos dados de um arquivo no sistema de arquivos, o i-node têm tamanho fixo e cada i-node tem um “endereço” diferente que define onde ele está armazenado no sistema de arquivos. 

Cada diretório possui referência a pelo menos dois diretórios, . representa o nome do diretório em questão e .. o nome do seu diretório pai.

Se um i-node está apontando para mais de um arquivo, significa que os arquivos apontados são iguais(possuem o mesmo conteúdo), porém possuem nomes diferentes.

## Como o sistema de arquivos se organiza no disco?

    a. Boot Sector: Usado para dar boot no sistema, se a partição do disco em questão tiver um SO.
    b. Super Block: Estrutura que armazena informações sobre essa estrutura de arquivos(ex. número de blocos do sistema de arquivos). 
    c. Block Bit Map: Informações sobre os blocos que estão livres(não estão armazenados).
    d. Inode Table: Área para armazenar os I-nodes.
    e. Data Blocks: Área para armazenar os arquivos. 

## Como saber se um I-node está livre ou está sendo usado?

Através do seu número de ligações, se o i-node possui 0 ligações significa que não está associado a nenhum nome de arquivo.

## Qual o tamanho da Inode Table e qual o tamanho dos data blocks?

O tamanho de um será sempre inversamente proporcional ao tamanho do outro, desta forma, se a área dos Inodes for maior, mais arquivos eu vou poder criar mas menos espaço eu vou ter para armazenar os arquivos, porém se a área dos data blocks for maior, menos arquivos vão poder ser criados mas haverá mais espaço para armazenar informação. Esses tamanhos serão definidos quando o sistema de arquivos estiver sendo criado.

## Como se processa a chamada open("/a/b/c",O_RDONLY)?

    a. O “bootstrap” é feito sabendo a priori qual é o número do i-node do diretório /, que por padrão é o i-node 2, com essa informação encontramos todos os blocos em que o / está armazenado.
    b. Ao acessar o /, procuramos bloco por bloco pelo arquivo chamado a, quando achamos o a, pegamos o i-node do mesmo e na tabela de i-nodes lemos as informações do i-node e conseguimos as informações de todos os blocos onde o a está armazenado.
    c. Ao acessar o /a, procuramos bloco por bloco pelo arquivo chamado b, e o ciclo acima de repete para o arquivo b.
    d. Ao acessar o /a/b, procuramos bloco por bloco pelo arquivo chamado c, quando achamos o c, pegamos o i-node do mesmo e na tabela de i-nodes lemos as informações do i-node, verificando finalmente se o usuário tem permissão de abrir aquele arquivo para leitura.

## Quais são as estruturas que o SO mantém em memória(cache) para não ficar sempre buscando no disco?

Teremos uma tabela de hash que relaciona os i-nodes com identificadores de sistemas de arquivos. Isso irá manter na memória os i-nodes que estão sendo manipulados(ou, de forma geral, os que foram acessados frequentemente).

Os data blocks também são mantidas em cache através de uma estrutura de dados chamada buffers de E/S, que nada mais é do que uma tabela hash, a forma como essa tabela é implementada é diferente, haverá um conjunto de listas, onde a informação estará armazenada, a função hash vai informar qual a lista que devemos consultar.

Uma cópia do super bloco e do mapa de bits serão armazenados na memória.

## Como os buffers de E/S realizam a gravação e leitura de informações?

As operações de leitura são feitas da seguinte forma:
    Eu descubro qual o bloco que quero ler e procuro na hash table se o bloco está presente em memória, se ele estiver, eu simplesmente leio a informação que eu preciso. Se o bloco não estiver em memória, devemos alocar mais um elemento(bloco) na lista adequada e providenciar que seja feita a leitura do disco para a memória.

As operações de escrita são feitas da seguinte forma:
    Não escrevemos diretamente no disco, escrevemos no bloco que está em memória, de tempo em tempos o SO se encarrega de fazer a gravação do que está em memória no disco, para que a informação fique persistente.