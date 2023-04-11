---
title: Resumo Livro Sistemas Operacionais Modernos
---
###### O resumo não é do livro completo
## Gerenciamento de Memória

A parte do sistema operacional que gerencia (parcialmente) a hierarquia de memórias é denominada gerenciador de memória. Sua função é gerenciar a memória de modo eficiente: manter o controle de quais partes da memória estão em uso e quais não estão, alocando memória aos processos quando eles precisam e liberando-a quando esses processos terminam.

### Sem abstração de memória

<aside>
💡 A abstração de memória mais simples é a ausência de abstração.

</aside>

Os primeiros computadores de grande porte (antes de 1960), microcomputadores (antes de 1970) e computadores pessoais (antes de 1980) não possuíam abstração de memória. Cada programa simplesmente considerava a memória física.

Nessas condições, não era possível executar dois programas na memória simultaneamente.

O sistema operacional pode estar na parte inferior da memória em RAM ou pode estar em ROM, ou os drivers de dispositivo podem estar na parte superior da memória em ROM e o resto do sistema em RAM embaixo.

Um modo de obter algum grau de paralelismo em um sistema sem abstração de memória é programar com múltiplos threads. Embora essa ideia funcione, sua utilidade é limitada porque as pessoas normalmente desejam que programas não relacionados sejam executados ao mesmo tempo, algo que a abstração de threads não proporciona.

### Executando múltiplos programas sem abstração de memória

Mesmo sem abstração de memória, entretanto, é possível executar múltiplos programas simultaneamente. O que o sistema operacional deve fazer é salvar o conteúdo completo da memória em um arquivo de disco e , em seguida, introduzir e executar o próximo programa.

<aside>
💡 Realocação estática: quando um programa era carregado no endereço 16.384, a constante 16.384 era adicionada a todos os endereços de programa durante o processo de carregamento. Embora esse mecanismo funcione se executado corretamente, não é uma solução muito comum e deixa mais lento o carregamento.

</aside>

## Abstração de memória: espaços de endereçamento

### A noção de espaço de endereçamento

Para que múltiplas aplicações estejam na memória simultaneamente sem interferência mútua, dois problemas devem ser resolvidos: proteção e realocação.

Um espaço de endereçamento é o conjunto de endereços que um processo pode usar para endereçar a memória.

<aside>
💡 Um desvantagem da realocação usando registradores e registradores base é a necessidade de executar uma adição e uma comparação em cada referência à memória.

</aside>

### Troca de memória

Dois métodos gerais para lidar com a sobrecarga de memória têm sido desenvolvidos com o passar dos anos. A estratégia mais simples, denominada troca de processos (swapping), consiste em trazer, em sua totalidade, cada processo para a memória, executá-lo durante um certo tempo e, então, devolvê-lo ao disco. Processos ociosos muitas vezes são armazenados no disco, de forma que não ocupem qualquer espaço na memória quando não estão executando (embora alguns deles ‘acordem’ periodicamente para fazer seu trabalho, e, em seguida, vão ‘dormir’ novamente). A outra estratégia, denominada memória virtual, permite que programas possam ser executados mesmo que estejam apenas parcialmente carregados na memória principal.

### Gerenciando a memória livre

Quando a memória é atribuída dinamicamente, o sistema operacional deve gerenciá-la. De modo geral, há dois modos de verificar a utilização da memória: mapas de bits e listas livres.

### Gerenciamento de memória com mapa de bits

Com um mapa de bits, a memória é dividida entre unidades de alocação tão pequenas quanto palavras ou tão grandes como vário kilobytes. A cada unidade de alocação corresponde a um bit no mapa de bits, o que é 0 se a unidade estiver livre e 1 se estiver ocupada (ou vice-versa).

<aside>
💡 Quanto menor a unidade de alocação, maior será o mapa de bits

</aside>

O principal problema com essa técnica é que, quando se decide carregar na memória um processo com tamanho de k unidades, o gerenciador de memória precisa encontrar espaço disponível na memória procurando no mapa de bits uma sequência de k bits consecutivos em 0.

### Gerenciamento de memória com listas encadeadas

Cada elemento desta lista encadeada especifica um segmento de memória livre (L) ou um segmento de memória alocada a um processo (P), o endereço onde se inicia esse segmento, seu comprimento e um ponteiro para o próximo elemento da lista.

Um processo que termina sua execução geralmente tem dois vizinhos na lista encadeada de segmentos de memória ( exceto quando estiver no início ou no fim dessa lista). Esses vizinhos podem ser ou segmentos de memória alocados a processos ou segmentos de memória livres.

## Algoritmos para alocar memória

### First fit

O algoritmo mais simples é o first fit. O gerenciador de memória procura ao longo da lista de segmentos de memória por um segmento livre que seja suficientemente grande para esse processo. Esse segmento é, então quebrado em duas partes, uma das quais é alocada ao processo, e a parte restante transforma-se em um segmento de memória livre de tamanho menor, exceto no caso improvável de o tamanho do segmento de memória locado ao processo se ajustar exatamente ao tamanho do segmento de memória livre original.

<aside>
💡 O algoritmo first fit é rápido porque procura o menos possível

</aside>

### Next fit

O algoritmo next fit funciona da mesmo maneira que o algoritmo first fit, exceto pelo fato de sempre memorizar a posição em que encontra um segmento de memória disponível de tamanho suficiente. Quando o algoritmo next fit tornar a ser chamado para encontrar um novo segmento de memória livre, ele inicializará sua busca a partir desse ponto, em vez de procurar sempre a partir do inicio da lista.

### Best fit

Esse algoritmo pesquisa a lista inteira e escolhe o menor segmento de memória livre que seja adequado ao processo.

O algoritmo best fit é mais lento que o first fit, pois precisa pesquisar a lista inteira cada vez que for chamado. O algoritmo best fit, surpreendentemente, também resulta em maior desperdício de memória do que os algoritmos first fit e next fit, pois tende a deixar disponíveis inúmeros segmentos minúsculos de memória e consequentemente inúteis. Em média, o algoritmo firs fit gera segmentos de memória disponíveis maiores.

### Worst fit

Para evitar o problema de alocar um segmento de memória disponível de tamanho quase exato ao requisitado pelo processo e, assim gerar outro minúsculo segmento de memória disponível, seria possível pensar em um algoritmo worst fit, isto é, em que sempre se escolhesse o maior segmento de memória disponível, de modo que, quando dividido, o segmento de memória disponível restante, após a alocação ao processo, fosse suficientemente grande para ser útil depois. Entretanto, simulações têm mostrado que o algoritmo worst fit não é uma ideia muito boa.

## Memória virtual

A ideia básica por trás da memória virtual é que cada programa tem seu próprio espaço de endereçamento, que é dividido em blocos chamados páginas.

### Paginação

A maioria dos sistemas com memória virtual utiliza uma técnica denominada paginação.

Endereços podem ser gerados com o uso da indexação, de registradores base, registradores de segmento ou outras técnicas.

Esses endereços gerados pelo programa são denominados endereços virtuais e constituem o espaço de endereçamento virtual.

<aside>
💡 Quando a memória virtual é usada, o endereço virtual não é colocado diretamente no barramento da memória. Em vez disso ele vai a uma MMU, que mapeia endereços virtuais em endereços físicos

</aside>

O espaço de endereçamento virtual é dividido em unidades denominadas páginas. As unidades correspondentes na memória física são denominadas molduras de página. As páginas e as molduras de página são sempre do mesmo tamanho.

A MMU constata que essa página virtual não está mapeada e força o desvio da CPU para o sistema operacional. Essa interrupção é denominada falta de página. O sistema operacional, então, escolhe uma moldura de página pouco usada e a salva em disco, ou seja, escreve seu conteúdo de volta no disco (se já não estiver lá). Em seguida, ele carrega a página virtual referenciada pela instrução na moldura de página recém liberada, atualiza o mapeamento da tabela de páginas e reinicializa a instrução causadora da interrupção.

<aside>
💡 O número de página é usado como um índice para a tabela de páginas, a fim de obter a moldura de páginas física correspondente àquela página virtual

</aside>

### Tabelas de páginas

No caso mais simples, o mapeamento dos endereços virtuais em endereços físicos pode ser resumido da seguinte forma: o endereço virtual é dividido em número de página virtual (bits mais significativos) e um deslocamento (bits menos significativos).

O número da página virtual é usado como índice dentro da tabela de páginas para encontrar a entrada dessa tabela associada à pagina virtual em questão. A partir dessa entrada, chega-se ao número de moldura de página física correspondente (caso ela já exista). O número da moldura de página física é concatenado aos bits do deslocamento, substituindo, assim, o número de página virtual pelo da moldura de página física, para formar o endereço físico que será enviado à memória.

<aside>
💡 Desse modo, o objetivo da tabela de páginas é mapear páginas virtuais em molduras de página física.

</aside>

### Acelerando a paginação

Em qualquer sistema de paginação, dois problemas importantes devem ser enfrentados:

1. O mapeamento do endereço virtual para endereço físico deve ser rápido.
2. Se o espaço de endereço virtual for grande, a tabela de páginas será grande.

O projeto mais simples é ter uma tabela de páginas consistindo de um arranjo de registradores de hardware rápidos, com uma entrada para cada página virtual, indexada pelo número dessa página. Quando um processo é inicializado, o sistema operacional carrega os registradores com a tabela de páginas do processo, retirada de uma cópia mantida na memória principal. Durante a execução do processo, não são mais necessárias referências à memória para a tabela de páginas. As vantagens desse processo são que ele é direto e não requer referências à memória durante o mapeamento. Uma desvantagem é que é excessivamente caro se a tabela de páginas for grande. Outra desvantagem é que a necessidade de carregar a tabela de páginas completa a cada alternância de contexto prejudica o desempenho.

No outro extremo, a tabela de páginas pode estar inteiramente na memória principal. Tudo de que o hardware precisa, nesse caso, é de um registrador único que aponte para o início da tabela de páginas. O projeto permite que o mapa virtual físico seja mudado em uma alternância de contexto por meio do carregamento de um registro. Naturalmente há a desvantagem de requerer uma ou mais referências á memória para ler as entradas na tabela de páginas durante a execução de cada instrução, tornando-a muito lenta.

### TBL ou memória associativa

A TBL ou às vezes memória associativa se localiza dentro da MMU e consiste em um pequeno número de entradas, raramente mais do que 64. Cada entrada contém informações sobre um página - incluindo o número de página virtual -, um bit que é colocado em 1 quando a página é modificada, o código de proteção (permissão de leitura/escrita/execução) e a moldura de página em que está localizada. Esses campos têm uma correspondência de um para um com os campos na tabela de páginas, exceto para o número de página virtual, que não é necessário na tabela de páginas. Outro bit indica se a entrada é valida (em uso) ou não.

Quando o número de página virtual não esta presente na TLB. A MMU detecta a ausência de página e, então, faz uma busca comum na tabela de páginas. A MMU então destitui uma das entradas da TLB e a substitui por essa entrada da tabela de páginas que acabou de ser buscada.

### Gerenciamento da TLB por software

As entradas da TLB são explicitamente carregadas pelo sistema operacional. Quando ocorre uma ausência de página na TLB, em vez de a própria MMU buscar na tabela de páginas a página virtual requisitada, ela apenas gera uma interrupção e repassa o problema ao sistema operacional. Este deve, então, encontrar a página virtual na tabela de páginas, destituir uma das entradas da TLB, inserir aí a nova página virtual e reinicializar a instrução interrompida.

Se a TLB for suficientemente grande ( digamos 64 entradas) para que se reduza a taxa de ausência de página, o gerenciamento da TLB por software acaba tendo uma eficiência aceitável.

### Tabelas de páginas para memórias grandes

As TLBs poder ser usadas para acelerar a tradução de endereços virtuais para endereços físicos em relação ao esquema original de tabela de páginas na memória. Há ainda o problema de como lidar com espaços de endereço virtual muito grandes.

### Tabelas de páginas multinível

Como método inicial, considere o uso de uma tabela de páginas multinível para resolver o problema de espaços de endereço virtual muito grandes.

O segredo para o método de tabela de páginas multinível é evitar que todas elas sejam mantidas na memória o tempo todo, especialmente as que não são necessárias.

### Tabelas de página invertidas

Para espaços de endereçamento virtuais de 32 bits, a tabela de páginas multinível funciona razoavelmente bem. Contudo, à medida que aparecem computadores de 64 bits, a situação muda drasticamente.

Um possível solução é a tabela de páginas invertidas:

<aside>
💡 nela existe apenas uma entrada por moldura de página na memória real, em vez de uma entrada por página do espaço de endereçamento virtual

</aside>

Embora as tabelas de páginas invertidas possam economizar muito espaço elas apresentam um problema sério: a tradução de virtual para físico torna-se muito mais difícil.

Uma solução possível para esse dilema é a utilização da TLB. Se esta puder conter todas as páginas mais intensamente usadas, a tradução pode ocorrer tão rapidamente quanto nas tabelas de páginas convencionais. Ocorrendo uma ausência na TLB, contudo, a tabela de páginas invertidas deve ser pesquisada no software. Um modo de realizar essa pesquisa é ter uma tabela de espelhamento (hash) nos endereços virtuais.

<aside>
💡 Tabelas de página invertidas são comuns em máquinas de 64 bits porque, mesmo com um tamanho de página muito grande, o número de entradas de tabelas de páginas é enorme.

</aside>

## Algoritmos de substituição de páginas

Quando ocorre uma falta de página, o sistema operacional precisa escolher uma página a ser removida da memória a fim de liberar espaço para uma nova página a ser trazida para a memória. Se a página a ser removida tiver sido modificada enquanto estava na memória, ela deverá ser reescrita no disco com o propósito de atualizar a cópia virtual lá existente.

Embora seja possível escolher aleatoriamente uma página a ser descartada a cada falta de página, o desempenho do sistema será muito melhor se a página escolhida for uma que não estiver sendo muito usada.

### O algoritmo ótimo de substituição de página

<aside>
💡 O melhor dos algoritmos de substituição de página é fácil de descrever, mas impossível de implementar.

</aside>

Ele funciona da seguinte maneira: no momento em que ocorre uma falta de página, existe um determinado conjunto de páginas na memória. Uma delas será referenciada na próxima instrução, ou seja, trata-se da mesma página que contém a instrução que gerou a falta de página.

O algoritmo ótimo diz apenas que se deve remover a página com o maior rótulo. Se determinada página só for usada após seis milhões de instruções, a primeira deverá ser removida antes da segunda. Dessa maneira, o algoritmo ótimo de substituição de página adia a ocorrência da próxima falta de página o máximo possível.

O único problema com esse algoritmo é que ele é irrealizável. Na ocorrência de uma falta de página, o sistema operacional não tem como saber quando cada uma das páginas será referenciada novamente.

### O algoritmo de substituição de página não usada recentemente (NRU)

A maioria dos computadores com memória virtual tem 2 bits de status - o bit referenciado (R) e o bit modificado (M) -, associados a cada página virtual, que permitem que o sistema operacional saiba quais páginas físicas estão sendo usadas e quais não estão. O bit R é colocado em 1 sempre que a página é referenciada (lida ou escrita). O bit M é colocado em 1 sempre que se escreve na página.

O algoritmo NRU remove aleatoriamente uma página da classe de ordem mais baixa que não esteja vazia. Está implícito nesse algoritmo que é melhor remover uma página modificada, mas não referenciada, a pelo menos um tique do relógio do que uma página não modificada que está sendo intensamente referenciada. A principal vantagem do algoritmo NRU é ser fácil de entender e de implementar e, além disso, fornece um desempenho que, apesar de não ser ótimo, pode ser adequado.

### O algoritmo de substituição de página primeiro a entrar, primeiro a sair

<aside>
💡 O algoritmo de substituição de página primeiro a entrar, primeiro a sair é um algoritmo de baixo custo.

</aside>

O sistema operacional mantém uma lista de todas as páginas atualmente na memória, com a página mais antiga na cabeça da lista e a página que chegou mais recentemente situada no final dessa lista. Na ocorrência de uma falta de página, a primeira página da lista é removida e a nova página é adicionada no final da lista.

### O algoritmo de substituição de página segunda chance

Uma modificação simples no algoritmo de substituição de página FIFO evita o problema de se jogar fora uma página intensamente usada, e isto é feito simplesmente inspecionando o bit R da página mais antiga, ou seja, a primeira página da fila. Se o bit R for 0, essa página, além de ser a mais antiga, não estará sendo usada, de modo que será substituída imediatamente. Se o bit R for 1, ele será colocado em 0, a página será posta no final da lista de páginas e seu tempo de carregamento (chegada) será atualizado como se ela tivesse acabado de ser carregada na memória.

<aside>
💡 O que o algoritmo segunda chance faz é procurar uma página antiga que não tenha sido referenciada no intervalo de relógio anterior. Se todas as páginas foram referenciadas, o segunda chance degenera-se para o FIFO puro

</aside>

### O algoritmo de substituição de página do relógio

Embora o segunda chance seja um algoritmo razoável, ele é desnecessariamente ineficaz, pois permanece constantemente reinserindo páginas no final da lista. Uma estratégia melhor é manter todas as páginas em uma lista circular em forma de relógio.

Quando ocorre uma falta de página, a página indicada pelo ponteiro é examinada. Se o bit R for 0, a pagina é removida, a nova página é inserida em seu lugar no relógio e o ponteiro avança uma posição. Se R for 1, ele é zerado e o ponteiro avança para a próxima página. Esse processo é repetido até que uma página seja encontrada com R = 0.

### Algoritmo de substituição de página usada menos recentemente (LRU)

Uma boa aproximação do algoritmo ótimo de substituição de página é baseada na observação de que as páginas muito utilizadas nas últimas instruções provavelmente serão muito utilizadas novamente nas próximas instruções.

Ao contrário, páginas que não estão sendo utilizadas por um longo período de tempo provavelmente permanecerão inutilizadas por muito tempo. Essa ideia sugere um algoritmo realizável:

<aside>
💡 Quando ocorrer uma falta de página, elimine a página não utilizada pelo período de tempo mais longo

</aside>

Essa estratégia é chamada de paginação LRU.

Embora o LRU seja teoricamente realizável, não é barato. Para implementar completamente o LRU, é necessário manter uma lista vinculada de todas as páginas na memória, com a página usada mais recentemente na dianteira e a página usada menos recentemente na parte de trás. A dificuldade é que a lista deve ser atualizada em cada referência à memória.

Entretanto, há outros modos de implementar o LRU com hardwares especiais. Esse método requer equipar o hardware com um contador de 64 bits, C, que é automaticamente incrementado após cada instrução.

### Simulação do LRU em software

<aside>
💡 Embora ambas as implementações anteriores ao LRU sejam perfeitamente realizáveis, poucas máquinas tem esse hardware

</aside>

Uma solução em software é empregar o algoritmo de substituição de página não usada frequentemente. A implementação desse algoritmo requer contadores em software, cada um deles associado a uma página, inicialmente zerados. A cada interrupção de relógio, o sistema operacional percorre todas as páginas na memória. Para cada página, o bit R, que pode estar em 0 ou 1, é adicionado ao contador correspondente. Assim, esses contadores constituem uma tentativa de saber quantas vezes cada página já foi referenciada. Quando ocorrer uma falta de página , a página que tiver a menor contagem será selecionada para a substituição.

<aside>
💡 O problema principal do algoritmo NFU é que ele nunca se esquece de nada.

</aside>

Uma pequena modificação no algoritmo NFU possibilita a simulação do algoritmo LRU. Essa modificação tem dois passos. Primeiro, os contadores são deslocados um bit à direita. Em seguida, o bit R de cada página é adicionado ao bit mais à esquerda do contador correspondente, em vez de ao bit mais à direita.

### O algoritmo de substituição de página do conjunto de trabalho

Muitos sistemas de paginação tentam gerenciar o conjunto de trabalho de cada processo e assegurar que ele esteja presente na memória antes de o processo ser executado. Essa prática, denominada modelo de conjunto de trabalho foi concebida para reduzir substancialmente a frequência de faltas de página. Carregar páginas de um processo na memória antes de ele ser posto em execução também se denomina pré-paginação.

### O algoritmo de substituição de página WSClock

O algoritmo básico do conjunto de trabalho é enfadonho, pois é preciso pesquisar em cada falta de página toda a tabela de páginas para que seja localizada uma página adequada para ser substituída. Há um algoritmo melhorado, com base no algoritmo do relógio, que também usa informações do conjunto de trabalho: é o chamado WSClock. Em virtude da simplicidade de implementação e do bom desempenho, esse algoritmo é amplamente utilizado.

<aside>
💡 A estrutura de dados necessária é uma lista circular de molduras de página

</aside>

Inicialmente, essa lista circular encontra-se vazia. Quando a primeira página é carregada, ela é inserida nessa lista. À medida que mais páginas são carregadas na memória, elas também são inseridas na lista para formar um anel. Cada entrada dessa lista contém o campo instante do último uso, do algoritmo do conjunto de trabalho básico, bem como o bit R e o bit M.

O que acontece se o ponteiro deu uma volta completa retornando a seu ponto de partida? Existem duas possibilidades a serem consideradas:

1. Pelo menos uma escrita foi escalonada
2. Nenhuma escrita foi escalonada

No primeiro caso, o ponteiro simplesmente continua a se mover, procurando por uma página limpa.

No segundo caso, todas as páginas pertencem ao conjunto de trabalho; caso contrário, pelo menos uma escrita em disco teria sido escalonada. Em razão da falta de informações adicionais, a coisa mais simples a fazer é reivindicar qualquer página limpa e usá-la. A localização de uma página limpa pode ser registrada durante a varredura. Se nenhuma página limpa existir, então a página atual será escolhida e reescrita em disco.

## Tabela algoritmos de substituição

| Algoritmo | Comentário |
| --- | --- |
| Ótimo | Não implementável, mas útil como um padrão de desempenho |
| NRU  | Aproximação muito rudimentar do LRU |
| FIFO | Pode descartar páginas importantes |
| Segunda chance | Algoritmo FIFO bastante melhorado |
| Relógio | Realista |
| LRU  | Excelente algoritmo, porém difícil de ser implementado de maneira exata |
| NFU | Aproximação bastante rudimentar do LRU |
| Envelhecimento | Algoritmo eficiente que aproxima bem o LRU |
| Conjunto de trabalho | Implementação um tanto cara |
| WSClock | Algoritmo bom e eficiente |

## Questões de projeto para sistemas de paginação

### Política de alocação local versus global

Algoritmos de substituição local alocam uma fração fixa de memória para cada processo. Algoritmos de substituição global alocam molduras de página entre os processos em execução. Assim, o número de molduras de página alocadas a cada processo varia no tempo.

Em geral, os algoritmos globais funcionam melhor, especialmente quando o tamanho do conjunto de trabalho varia durante o tempo de vida de um processo. Se um algoritmo local é usado e o conjunto de trabalho cresce durante a execução do processo, uma ultra paginação (thrashing) pode ocorrer mesmo que existam muitas molduras de página disponível na memória. Se o conjunto de trabalho diminuir durante durante a execução do processo, os algoritmos locais desperdiçam memória.

Se um algoritmo global for usado, pode ser possível inicializar cada processo com um número de molduras de página proporcional a seu tamanho, mas a alocação tem de ser atualizada dinamicamente durante a execução do processo. Uma maneira de gerenciar a alocação é usar o algoritmo PFF. 

<aside>
💡 O algoritmo PFF informa quando aumentar ou diminuir a alocação de página de um processo, mas nada diz acerca de quais páginas substituir quando ocorrerem faltas de página. Ele somente controla o tamanho do conjunto de alocação

</aside>

É importante notar que alguns algoritmos de substituição de página podem funcionar tanto com uma política de substituição local como uma global. Por exemplo, o FIFO pode substituir a página mais antiga em toda a memória (algoritmo global) ou a página mais antiga possuída pelo processo atual (algoritmo local). Da mesma maneira, o LRU - ou algum algoritmo aproximado - pode substituir a página menos usada recentemente e toda a memória (algoritmo global) ou a página menos usada recentemente possuída pelo processo atual (algoritmo local). 

<aside>
💡 A escolha de local versos global é independente, em alguns casos, do algoritmo escolhido

</aside>

### Controle de carga

Mesmo com o melhor algoritmo de substituição de página e uma ótima alocação global de molduras de página a processos, pode ocorrer ultra paginação (thrashing).

Um sintoma dessa situação é que o algoritmo PFF indica que alguns processos precisam de mais memória, mas que nenhum outro processo necessita de menos memória. Nesse caso, não existe como alocar mais memória a processos que dela precisam sem que, com isso, se prejudiquem alguns outros processos, A única solução possível é livrar-se temporariamente de alguns dos processos.

<aside>
💡 Um bom modo de reduzir o número de processos que competem por memória é levar alguns deles para disco e liberar a memória a eles alocada

</aside>

### Tamanho de página

<aside>
💡 O tamanho de página é um parâmetro que frequentemente pode ser escolhido pelos sistema operacional

</aside>

A determinação do melhor tamanho de página requer o balanceamento de vários fatores conflitantes, o que leva a não se conseguir um tamanho ótimo geral. Há dois agrupamentos a favor de um tamanho pequeno de pagina:

- É provável que um segmento de código, dados ou pilha escolhido aleatoriamente não ocupe um número inteiro de páginas. Em média, metade da última página permanecerá vazia e , portanto, esse espaço será desperdiçado.

<aside>
💡 Esse desperdício é denominado fragmentação interna

</aside>

- Tamanhos grandes de página farão com que partes do programa não usadas ocupem a memória desnecessariamente.

<aside>
💡 Páginas pequenas implicam muitas páginas e, consequentemente, uma grande tabela de páginas

</aside>

### Espaços separados de instruções e dados

Em um computador com esse projeto, ambos os espaços de endereçamento podem ser paginados, independentemente um do outro. Cada um deles possui sua própria tabela de páginas, que contém o mapeamento individual de páginas virtuais para molduras de página física. Quando o hardware busca uma instrução, ele sabe que deve usar o espaço I e a tabela de páginas do espaço I. Da mesma maneira, referências aos dados devem acontecer por intermédio da tabela de páginas do espaço D.

### Páginas compartilhadas

Outro aspecto importante do projeto é o compartilhamento de páginas. Em grandes sistemas com multiprogramação, é comum haver vários usuários executando simultaneamente o mesmo programa. É nitidamente mais eficiente compartilhar páginas para evitar a situação de existirem duas cópias ou mais da mesma página presentes na memória.

<aside>
💡 Nem todas as páginas são compartilháveis. Em particular, as páginas somente leitura são compartilháveis, mas páginas com dados alteráveis durante a execução não o são

</aside>

Quando dois ou mais processos compartilham o mesmo código, um problema ocorre com as páginas compartilhadas. Suponha que os processos A e B estejam ambos executando o editor e compartilhando suas páginas. Se o escalonador decide remover A da memória, descartando todas as suas páginas e carregando as molduras de página vazias com outro programa, ele leva o processo B a causar muitas faltas de página, até que suas páginas estejam novamente presentes na memória.

### Bibliotecas compartilhadas

O compartilhamento pode ser feito em outras granularidades além de páginas individuais. Se um programa for inicializado duas vezes, a maioria dos sistemas operacionais automaticamente compartilhará todas as páginas de texto, de modo que apenas uma cópia esteja na memória. As páginas de texto sempre são apenas para leitura, por isso não há nenhum problema nesse caso.

Em sistemas modernos, há muitas bibliotecas grandes usadas por muitos processos. Ligar estaticamente todas essas bibliotecas a cada programa executável no disco as tornaria ainda mais infladas do que já são, em vez disso, uma técnica comum é usar bibliotecas compartilhadas.

### Arquivos mapeados

<aside>
💡 As bibliotecas compartilhadas são realmente um caso especial de um recurso mais geral, chamado arquivos mapeados em memória

</aside>

A ideia é que um processo pode emitir uma chamada ao sistema para mapear um arquivo em uma porção de seu espaço de endereçamento virtual. Na maior parte das implementações, nenhuma página é trazida durante o período do mapeamento, mas, à medida que as páginas são usadas, são paginadas, uma a uma, por demanda, usando o arquivo no disco como memória auxiliar.

### Interface da memória virtual

Em alguns sistemas avançados, os programadores dispõem de algum controle sobre o mapa de memória e podem usá-lo de maneiras não tradicionais para aumentar o desempenho do programa.

<aside>
💡 Uma razão para dar o controle do mapa de memória a programadores é permitir que dois ou mais processos compartilhem a mesma memória.

</aside>

## Questões de implementação

### Envolvimento do sistema operacional com a paginação

Existem quatro circunstâncias em que o sistema operacional tem de se envolver com a paginação:

<aside>
💡 Na criação do processo, no tempo de execução do processo, na ocorrência de falta de página e na finalização do processo.

</aside>

- **Na criação:** Quando um novo processo é criado em um sistema com paginação, o sistema operacional deve determinar qual será o tamanho (inicial) do programa e de seus dados e criar uma tabela de páginas para eles. Um espaço precisa ser alocado na memória para a tabela de páginas, e esta deve ser inicializada. A tabela de páginas não precisa estar presente na memória quando o processo é levado para disco, mas ela tem de estar na memória quando o processo estiver em execução. Além disso, um espaço deve ser alocado na área de trocas do disco (swap área), de modo que, quando uma página é devolvida ao disco, ela tenha para onde ir.
- **Na Execução:** Quando um processo é escalonado para execução, a MMU tem de ser reinicializada para o novo processo, e a TBL, esvaziada para livrar-se de resíduos do processo executado anteriormente. A tabela de páginas do novo processo deve torna-se a tabela atual, o que em geral é feito copiando-se a tabela ou um ponteiro para ela em algum(ns) registrador(es) em hardware.
- **Na falta de página:** Quando ocorre uma falta de página, o sistema operacional tem de ler o(s) registrador(es) em hardware para determinar o endereço virtual causador da falta de página. A partir dessa informação, ele precisa calcular qual página virtual é requisitada e, então, localizá-la em disco. Em seguida, ele procura uma moldura de página. Por fim, o sistema operacional tem de salvar o contador de programa para que ele aponte para a instrução que causou a falta de página, de modo que possa ser executada novamente.
- **Na finalização do processo:** Quando o processo termina, o sistema operacional deve liberar sua tabela de páginas, suas páginas e o espaço em disco que as páginas ocupam.

### Tratamento de falta de página

A sequência de eventos ocorre da seguinte maneira:

1. O hardware gera uma interrupção que desvia a execução para o núcleo, salvando o contador de programa na pilha.
2. Uma rotina em código de montagem é ativada para salvar o conteúdo dos registradores de uso geral e outras informações voláteis, a fim de impedir que o sistema operacional o destrua.
3. O sistema operacional descobre a ocorrência de uma falta de página e tenta identificar qual página virtual é necessária.
4. Uma vez conhecido o endereço virtual causador da falta de página, o sistema operacional verifica se esse endereço é valido e se a proteção é consistente com o acesso. Se não, o processo recebe um sinal ou é eliminado. Se o endereço for válido e nenhuma violação de proteção tiver ocorrido, o sistema verificará se existe uma moldura de página disponível.
5. Se o conteúdo da moldura de página tiver sido modificado, a página será escalonada para ser transferida para o disco.
6. Tão lofo a moldura de página seja limpa, o sistema operacional buscará o endereço em disco onde está a página virtual solicitada e escalonará uma operação em disco para trazê-la para a memória.
7. Quando a interrupção de disco indicar que a página chegou na memória, as tabelas de páginas serão atualizadas para refletir sua posição, e será indicado que a moldura de página está em estado normal.
8. A instrução causadora da falta de página é recuperada para o estado em que ela se encontrava quando começou sua execução, e o contador de programa é reinicializado, a fim de apontar para aquela instrução.
9. O processo causador da falta de página é escalonado para execução, e o sistema operacional retorna para a rotina, em linguagem de máquina, que a chamou.
10. Essa rotina recarrega os registradores e outras informações de estado e retorna ao espaço de usuário para continuar a execução, como se nada tivesse ocorrido.

### Backup de instrução

Quando um programa referencia uma página não presente na memória, a instrução causadora da falta de página é bloqueada no meio de sua execução e ocorre uma interrupção, desviando-se assim para o sistema operacional. Após o sistema operacional buscar em disco a página necessária, ele deverá reinicializar a instrução causadora da interrupção.

<aside>
💡 Em algumas máquinas os projetistas da CPU fornecem uma solução, geralmente na forma de um registrador interno escondido em que o conteúdo do contador de programa é salvo antes de cada instrução ser executada

</aside>

### Retenção de páginas na memória

Se um dispositivo de E/S estiver atualmente na fase de transferência via DMA para aquela página, sua remoção da memória fará com que uma parte dos dados seja escrita na página correta, e a outra parte, na nova página carregada na memória. Uma solução para esse problema é trancar as páginas envolvidas com E/S na memória, de modo que não possam ser removidas. Essa ação do sistema operacional é muitas vezes denominada retenção de página(pinning). Outra solução é fazer todas as operações de E/S para buffers no núcleo e, posteriormente, copiar os dados para as páginas do usuário.

### Memória secundária

O algoritmo mais simples para a locação de espaço em disco consiste na manutenção de uma área de troca (swap área) em disco ou, ainda melhor que isso , em um disco separado do sistema de arquivos.

Quando o sistema operacional é inicializado, essa área de troca encontra-se vazia e é representada na memória como uma única entrada contendo sua localização e seu tamanho. No esquema mais simples, quando o primeiro processo é inicializado, reserva-se uma parte dessa área de troca, do tamanho desse processo, e a área de troca restante fica reduzida dessa quantidade. Quando novos processos são inicializados, a eles também são atribuídos pedaços da área de troca de tamanhos iguais aos ocupados por cada um deles. À medida que os processos vão terminando, seus espaços em disco são gradativamente liberados. A área de troca em disco é gerenciada como uma lista de pedaços disponíveis.

### Separação da política e do mecanismo

O sistema de gerenciamento de memória é dividido em três partes:

1. Um manipulador de MMU de baixo nível.
2. Um manipulador de falta de página que faz parte do núcleo.
3. Um paginador externo executado no espaço do usuário.

Todos os detalhes de como a MMU trabalha são escondidos em seu manipulador, que possui código dependente de máquina, devendo ser reescrito para cada nova plataforma que o sistema operacional executar.

## Segmentação

Um compilador tem muitas tabelas construídas em tempo de compilação, possivelmente incluindo:

1. O código-fonte sendo salvo para impressão (em sistemas em lote)
2. A tabela de símbolos que contém os nomes e os atributos das variáveis.
3. A tabela com todas as constantes usadas, inteiras e em ponto flutuante.
4. A árvore sintática, que contém a análise sintática do programa.
5. A pilha usada pelas chamadas de rotina dentro do compilador.

É necessário uma maneira de livrar o programador da obrigatoriedade de gerenciar a expansão e a contração de tabelas, do mesmo modo que a memória virtual elimina a preocupação de organizar o programa em sobreposições.

Uma solução extremamente abrangente e direta é prover a máquina com muitos espaços de endereçamento completamente independentes, chamados de segmentos.

É preciso enfatizar que um segmento é uma entidade lógica, que o programador conhece e usa como entidade lógica. 

<aside>
💡 Um seguimento pode conter uma rotina, um arranjo, uma pilha ou um conjunto de variáveis escalares, mas em geral ele não apresenta uma mistura de diferentes tipos.

</aside>

<aside>
💡 A segmentação também facilita o compartilhamento de rotinas ou dados entre vários processos.

</aside>

<aside>
💡 Como cada segmento forma uma entidade lógica da qual o programador está ciente diferentes segmentos podem possuir diferentes tipos de proteção.

</aside>

A proteção faz sentido em uma memória segmentada, mas não em uma memória unidimensional paginada: em uma memória segmentada o usuário está ciente do que existe em cada segmento.

### Comparação entre paginação e segmentação

| Consideração | Paginação | Segmentação |
| --- | --- | --- |
| O programador precisa saber que essa técnica está sendo usada? | Não | Sim |
| Há quantos espaços de endereçamento linear? | 1 | Muitos |
| O espaço de endereçamento total pode superar o tamanho da memória física? | Sim | Sim |
| Rotinas e dados podem ser distinguidos e protegidos separadamente? | Não | Sim |
| As tabelas cujo tamanho flutua podem ser facilmente acomodadas? | Não | Sim |
| O compartilhamento de rotinas entre os usuários é facilitado? | Não | Sim |
| Por que essa técnica foi inventada? | Para obter um grande espaço de endereçamento linear sem a necessidade de comprar mais memória física. | Para permitir que programas e dados sejam divididos em espaços de endereçamento logicamente independentes e para auxiliar o compartilhamento e a proteção. |

### Implementação de segmentação pura

<aside>
💡 A implementação da segmentação difere da paginação em um ponto essencial: as páginas têm tamanhos fixos e os segmentos não.

</aside>

Após o sistema ter executado por um tempo, a memória estará dividida em regiões, algumas com segmentos e outras com lacunas. Esse fenômeno, chamado de fragmentação externa (ou checkerboarding), desperdiça memória nas lacunas. Isso pode ser sanado com o uso de compactação.

### Segmentação com paginação: MULTICS

Se os segmentos são grandes, talvez seja inconveniente mantê-los na memória em sua totalidade. Isso gera a ideia de paginação dos segmentos, de modo que somente as páginas realmente necessárias tenham de estar na memória.

Cada programa do MULTICS tem uma tabela de segmentos, com um descritos para cada segmento. Visto que potencialmente existe mais do que um quarto de milhão de entradas na tabela, a tabela de segmentos forma, por si só, um segmento, que também é paginado.

<aside>
💡 Um endereço no MULTICS consiste de duas partes: o segmento e o endereço dentro do segmento.

</aside>

Quando ocorre uma referência à memória, o seguinte algoritmo é executado:

1. O número do segmento é usado para encontrar o descritor do segmento.
2. Faz-se uma verificação para ver se a tabela de páginas do segmento está na memória. Se a tabela de páginas está na memória, ela é localizada. Do contrário, ocorre uma falta de segmento. Se existe uma violação de proteção, ocorre uma interrupção.
3. A entrada da tabela de páginas para a página virtual requisitada é examinada. Se a página não está na memória, ocorre uma falta de página. Se ela está na memória, o endereço de memória principal do início da página é extraído da entrada da tabela de páginas.
4. O deslocamento é adicionado ao início da página a fim de gerar o endereço da memória principal onde a palavra está localizada.
5. A leitura ou a escrita pode finalmente ser feita.

### Segmentação com paginação: o Pentium Intel

Em muitos aspectos, a memória virtual no Pentium se parece com a do MULTICS, incluindo a presença de segmentação e paginação.

O coração da memória virtual do Pentium consiste em duas tabelas, a LDT (tabela de descritores local) e a GDT (tabela de descritores global).