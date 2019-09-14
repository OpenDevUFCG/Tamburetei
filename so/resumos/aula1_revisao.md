## Aula 1 - Sistemas Operacionais

*(segundo professor Fubica, uma das top 5 aulas da cadeira)*

*OBS:* Nesse curso, vamos considerar computadores com uma única CPU porque já é complicado o suficiente de entender com uma CPU só, mas haverá uma aula falando sobre múltiplas CPUs.

O S.O tem duas funções mais importantes:

**1.** Gerenciar os recursos do hardware de tal forma que eles possam ser compartilhados entre vários programas que estão executando ao mesmo tempo 
**2.** Tornar a vida do programador mais simples. Como o S.O. faz isso? Ele oferece uma API para o desenvolvedor de mais alto nível. Logo, o desenvolver não precisa se preocupar com questões de como interagir com determinado dispositivo ou como alocar memória para um programa, por exemplo. Essa API é o conjunto de chamadas ao sistema do S.O. ou System Calls.

### Revisão de Organização e Arquitetura de Computadores

*Quais são as coisas mais importantes de arquitetura a serem lembradas?*

Temos 3 coisas importantes para lembrar:

**1. Nível de privilégio:** O conjunto de instruções da CPU é tipicamente dividido em subconjuntos e, para executar as instruções de um determinado subconjunto, é necessário ter um nível de privilégio para execução. 

Em resumo: diferentes subconjuntos exigem diferentes níveis de privilégio. Para simplificar nossa vida, vamos considerar apenas dois níveis: O nível mais baixo, do usuário, que vamos chamar de nível 0. O nível 1, que é o núcleo, é o nível mais alto. 

O que isso significa? Significa que quando a máquina está operando com o nível de privilégio zero, só as instruções desse subconjunto podem ser executadas. Se o programa que está executando programa com as instruções com nível de privilégio zero executa uma instrução que está no nível 1, isso gera uma exceção.

**2. Exceções:** é algo que ocorre dentro da CPU e ocorre sempre que a CPU não consegue concluir a execução da instrução corretamente. O lançamento da exceção faz com que ocorra algo muito similar ao que ocorre quando vem uma interrupção: salva-se o PC e o Stack Pointer para que se saiba onde estava executando, o nível de privilégio passa para 1  (estando já em 1 ou em 0, passa para 1 com certeza) e se passa a executar o código do S.O. que trata daquela exceção específica de aconteceu. 

Exemplos de exceção: 

- Se eu fizer no meu programa uma divisão por 0, isso vai dar uma exceção. 
- Se eu tentar acessar uma área da memória que não me pertence, isso vai dar uma exceção. 
- Se eu tentar gravar numa área de memória que eu só posso ler, isso vai dar uma exceção. 
- Se eu executar uma instrução que eu não posso executar (porque eu não tenho privilégio para executar aquilo), isso vai dar uma exceção. 

**3. Interrupções:** são sinais elétricos gerados pelas controladoras dos dispositivos para chamar atenção da CPU. Exemplo: temos um computador ligado e apertamos a tecla “E”. Como o teclado avisa para a CPU que algo foi teclado? Ele manda uma interrupção no barramento: no barramento de endereços, ele manda o número da interrupção e, nesse caso, no barramento de dados ele manda o código do caractere que foi digitado. O que acontece quando essa interrupção chega na CPU? Temos um circuito que trata essas interrupções, ele espera que a instrução sendo executada conclua. Quando essa instrução concluir, o hardware vai salvar os valores do PC (aponta pro código, para a próxima instrução a ser executada) e do Stack Pointer (o registrador que aponta pro topo da pilha do programa que está sendo executado). 

Assim, quando vem uma interrupção, eu tenho de parar de executar o que estava fazendo (e o que eu estava fazendo é indicado por onde meu PC e meu Stack Pointer estavam apontando) e vou passar a executar o sistema operacional. Em particular, é a rotina do S.O. que trata daquela interrupção específica que foi gerada. Há uma interrupção bastante importante (que não tem a ver com entrada e saída) chamada Timer. 

	OBS: quando uma interrupção ocorre, há um registrador (chamado PSW) que guarda o nível de privilégio.

### Perguntas feitas pelo professor para a turma

*Por que precisamos de uma pilha para executar um programa?*

	Precisamos da pilha por conta da forma como decidimos que nossos programas irão funcionar, baseados em funções, módulos, métodos, e que têm um escopo de variáveis (locais e globais). A pilha é a estrutura de dados perfeita para manter essa memória, porque quando chamamos uma função, criamos na pilha uma área de memória para armazenar essas informações. Se dentro dessa função chamamos outra função, outra coisa será criada na pilha. 

*Como um programa faz um System Call?*

	O programa precisa gerar uma exceção para que o S.O. possa executar, para isso existe uma instrução especial, chamada de Trap (como se convencionou a chamar essa instrução). Quando o programa executa essa instrução (a qual eu não posso executar no modo usuário), isso vai gerar uma exceção. O S.O. vai executar o tratador de instruções executadas sem a permissão necessária e vai verificar se foi um Trap. Se sim, é apenas um aviso de que “precisa de ajuda” e, se foi qualquer outra coisa que não Trap, é porque “está fazendo besteira”. Assim, o System Call é implementado dessa forma, com uma instrução especial que é chamada para gerar exceção. 
	
	Então, quando gera essa exceção, a máquina vai para um nível de privilégio mais alto, o PC aponta para o código do S.O. que trata essa exceção e esse código vai verificar qual é a System Call que é necessária a ser feita. 

### O mais importante da aula

Quando ocorre uma interrupção ou uma exceção, o S.O. executa. Na realidade, o mais importante de toda essa aula é lembrar que: o S.O. só executa se acontecer uma interrupção ou uma exceção, não tem jeito do S.O. executar sem que uma dessas duas coisas ocorra. 
Quando o S.O. entra no ar, ele programa o Timer para garantir que interrupções ocorrerão de tempos em tempos. Ou seja, ele garante que vai executar de tempos e tempos. 
