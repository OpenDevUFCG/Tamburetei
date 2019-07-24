# Resumo do Primeiro Estágio

## Paradigma

Um paradigma é algo que vai servir de modelo ou exemplo a ser seguido em determinada situação. Paradigmas de linguagens de programação são as ideias que têm sido usadas para guiar o design das linguagens de programação. Existem muitas linguagens de programação e nenhuma é adequada a todos os problemas. Conhecer novas linguagens aumenta seu arsenal de ferramentas para resolver problemas.

## Programas

Conjuntos de instruções que representam um algoritmo para a resolução de algum problema. Algumas de suas características são:

- Expressividade: refere-se à adequação das formas de especificar computações, dados e procedimentos a fim de que se apresentem de forma clara e simples, ou  seja, quando operadores muito poderosos substituem um código complexo de programação por um código muito pequeno e simples de entender

- Universalidade: Todo problema, que pode ser resolvido por um computador, deve ter uma solução que seja programável com a LP, esta característica distingue uma linguagem de programação de, por exemplo, uma linguagem de consulta a banco de dados

- Suporte a Abstração: LPs usam abstrações para definir e manipular estruturas de dados, simples ou complexas, e controlar o fluxo de execução de um programa, podendo ser de baixo e de alto nível. As LP de baixo nível: possuem instruções que refletem de forma mais direta operações em nível de máquina e tem como vantagem: maior velocidade de processamento e menor consumo de recursos. As LP de alto nível: fazem uso de instruções mais descritivas, independente de máquina ou sistema operacional e tem como vantagem: maior portabilidade e programação mais simples

## Linguagens de Programação

### Eficiência

Característica referente aos requisitos práticos específicos de uma LP, programas precisam executar em um tempo aceitável para os propósitos de uso da linguagem

### Implementável

Uma LP deve ser passível de tradução para um formalismo que seja executável em uma máquina

### Compiladas vs. Interpretadas:

- LP Compiladas: São linguagens que requerem compiladores, sendo assim, do ponto de vista do código fonte, toda linguagem de programação é compilada. As vantagens são: maior velocidade de processamento e menor consumo de recursos.

![compiladas](https://i.imgur.com/xpgYfBf.png)

- LP Interpretadas:  O programa de interpretação atua como uma simulação de software de
uma máquina cujo ciclo de busca-execução lida com instruções de programa de linguagem de alto nível em vez de instruções de máquina. As vantagens são: maior portabilidade e programação mais simples

![interpretadas](https://i.imgur.com/LGoETzT.png)

- LP Híbridas: LP mais modernas como Java, C# e Python têm seus códigos fontes transformados em uma linguagem intermediária, que será interpretada pela máquina virtual da linguagem quando o programa for executado. O processo de interpretação da linguagem intermediária ocorre durante a execução do programa e consiste na tradução dos comandos da linguagem intermediária para linguagem de máquina. Em tempo de execução, o código intermediário pode ser encarado como um “código fonte” que será compilado dinamicamente pelo interpretador da linguagem em código de máquina.

### Sintaxe vs. Semântica:

- Sintaxe: Como expressões, comandos, declarações e outras construções devem ser arranjados para formar programas
- Semântica: Significado do programa, ou seja, como um programa bem formado deve ser comportar quando executados em uma computador. A semântica é a parte mais importante e que realmente caracteriza a linguagem, porque determina como o programa será composto pelo programador, entendido por outros programadores e interpretado pelo computador. A semântica pode ser:

	* Operacional: Dá uma indicação de como o programa deve ser executado através da aplicação de um conjunto de regras
	* Denotacional: Define o significado de construções da linguagem em um domínio matemático, método mais abstrato para descrição semântica
	* Axiomática: Baseada em lógica matemática, que serve para provar a exatidão dos programas. Cada instrução de um programa tanto é precedida como seguida de uma expressão lógica que especifica restrições a variáveis, as expressões lógicas são usadas para especificar o significado das instruções e as restrições são descritas pela notação do cálculo de predicados

### Valores

Qualquer entidade que pode ser manipulada por um programa, tudo que pode ser armazenado, avaliado diretamente, retornado como resultado de uma função ou passado como argumento. Podem ser:

- Primeira classe: Não existem restrições para seu uso, pode ser passado como argumento, Pode ser usado como retorno de um procedimento, pode ser atribuído a uma variável
- Segunda classe: Existem restrições para seu uso

### Tipos
Um conjunto de valores equipado com um conjunto de operações que podem ser aplicadas uniformemente a todos seus valores. Podem ser:
- Primitivos: são aqueles cujos valores são impossíveis de decompor, toda LP tem por padrão uma coleção de tipos primitivos e nem sempre são iguais
- Compostos: tipos cujos valores são compostos a partir de valores simples, normalmente, as LPs dão suporte a diferente tipos compostos. Podemos classificá-las entre:

	* Cartesiano: valores de vários (possivelmente diferentes) tipos são agrupados em tuplas
	* Mapeamento: Arrays e Funções, onde m mapeia os elementos do conjunto S para valores em T
	* Uniões Disjuntas: valores são escolhidos de dois tipos (normalmente diferentes)
	* Tipos Recursivos: É um tipo definido em termos dele mesmo. Por exemplo, descrever axiomas dos números naturais onde um número natural ou é Zero ou pode ser alcançado via seu Sucessor

### Tipagem

- Fortemente tipada: se é mais provável de gerar erros ou não compilar expressões que não “casam” com os tipos esperados pelos operadores.
- Fracamente tipada: pode aceitar resultados inesperados ou faz conversão implícita de tipos, ou seja, o valor de um tipo pode ser tratado como um valor de outro tipo

### Verificação de Tipos
- Estaticamente tipadas:Todas as expressões têm seus tipos determinados em tempo de compilação.
- Dinamicamente tipadas: apenas valores têm tipos fixos. Variáveis e parâmetros não possuem um tipo associado, mas podem assumir valores de diferentes tipos em diferentes trechos do programa.

### Monomorfismo vs Polimorfismo

#### Monomorfismo
Toda entidade tem um tipo específico, ela facilita verificação de tipos, mas diminui a flexibilidade na construção de componentes reusáveis

#### Polimorfismo
Abstrações que operam de maneira uniforme sobre valores de tipos diferentes.

![polimorfismo](https://i.imgur.com/1FKC4Wd.png)

- Polimorfismo Ad hoc: abstração atua sobre um número finito de tipos não relacionados, mas se comporta diferentemente dependendo do tipo
	* Sobrecarga: Um identificador é sobrecarregado se ele é aplicável a mais de uma operação, a sobrecarga só funciona se o compilador consegue distinguir a operação a ser chamada usando somente informações de tipo
	* Coerção: Conversão implícita de tipo, realizada automaticamente quando o contexto intático exige

- Polimorfismo Universal: Uma única abstração atua de maneira uniforme sobre uma família de tipos.
	* Inclusão: Um tipo pode ter subtipos, que herdam as operações do tipo original, uma única abstração opere de maneira uniforme sobre um família de tipos representada através de uma relação de subtipos, ou seja, a subclasse verifica se ela tem ou não um método com
a assinatura desejada, se não tiver, a classe progenitora torna-se responsável
pelo processamento da mensagem.
	* Paramétrico: Permite que uma abstração possa ser escrito de forma genérica, sendo possível tratar valores de forma idêntica sem considerar o tipo específico que possuem

### Variáveis e Alteração de Valores:
- Classificação quanto à estrutura:
	* Primitivas: armazenam valores de tipos primitivos
	* Compostas: armazenam valores de tipos compostos
- Classificação quanto ao tempo de vida:
	* Temporárias: criadas e usadas dentro de um programa.
	* Persistentes: tem existência independente do tempo de vida (execução) de um programa.

### Arrays
Variáveis típicas da programação imperativa, ela é vista como um mapeamento de um conjunto de índices para variáveis componentes. O conjunto de índices é normalmente um subintervalo de valores consecutivos.

### Stack
Variáveis declaradas e inicializadas no início da execução. 

### Heap
Variáveis criadas ou inicializadas em tempo de execução.

### Escopo
Tempo de vida de uma variável é o intervalo de tempo entre a sua criação (alocação) e a sua destruição (desalocação), o escopo de uma variável determina em que partes do programa essa variável pode ser acessada. Toda variável é associada a um escopo que delimita seu tempo de vida.
- Uma variável local é aquela declarada dentro de um bloco para ser usada apenas dentro dele. 
- Uma variável global é aquela declarada em um bloco externo que contém o bloco em que está sendo usada.

- Escopo Léxico: a estrutura ”textual" do programa é fator determinante para definição do escopo. O que o programa abaixo imprime? 3!
- Escopo Dinâmico: o escopo é determinado através da linha de execução do programa, dependente da ordem de execução das rotinas. O que o programa abaixo imprime? 4! Esse escopo está em desuso.

![escopo_c](https://i.imgur.com/8JGCljo.png)

### Expressões vs Comandos:
- Expressões: lêem estados e computam valores
- Comandos modificam estados, podendo ser:
	* Atribuições: Modificação direta do valor/estado de uma variável, podendo ser:
		* Atribuição simples: x = y + 1;
		* Múltiplas atribuições: v1 = v2 = v3 = 200;
		* Atribuição simultânea: n1, n2, n3 = m1, m2, m3;
		* Operador de atribuição: m += n
	* Chamada de Procedimento: O efeito de uma chamada de procedimento é a aplicação da abstração do procedimento para um conjunto de argumentos, o resultado prático das chamadas de procedimento são as atualização das variáveis (locais e globais)
	* Sequenciais: Um comando sequencial é um conjunto de comandos executados sequencialmente 
	* Colaterais: Uma computação é determinística se podemos prever a sequência de passos a ser seguida, um comando colateral é um conjunto de comandos não determinísticos
	* Condicionais: Um comando condicional possui um conjunto de subcomandos onde exatamente um é escolhido
	* Iterativos: Um conjunto de comandos é executado repetidamente até que certa expressão indique o fim da repetição

### Transparência Referencial
Uma LP possui transparência referencial se qualquer expressão pode ser substituída por outra que tenha o mesmo valor, ou seja, sem efeito colateral

### Expressões com Efeitos Colaterais
- Permite realizar várias tarefas ao mesmo tempo
- Perda de legibilidade. Pode não ser trivial entender a semântica das expressões
- Baixa reusabilidade. Um fragmento de programa depende de um contexto global 

### Sequenciadores
Um sequenciador é uma construção que transfere o controle para outro ponto do programa, denominado de destino do sequenciador, permitindo implementar fluxos de controle com múltiplas entradas e saídas

- Jump: uma transferência de controle explícita de um ponto para outro do programa.
- Escapes: Termina a execução de um comando composto fechado, transferindo o controle da execução para o comando seguinte 
- Exceptions: Quando condições anormais ocorrem, o programa não pode continuar executando normalmente, um programa é dito ser robusto se consegue se recuperar de condições anormais sem encerrar a sua execução. Quando uma condição excepcional ocorre, o controle do programa é transferido para um módulo específico, o handler
