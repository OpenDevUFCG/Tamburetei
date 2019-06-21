# Álgebra Relacional

## Sumário

- [Álgebra Relacional](#%C3%A1lgebra-relacional)
  - [Sumário](#sum%C3%A1rio)
  - [Introdução](#Introduç%C3%A3o)
  - [Relações Unárias](#rela%C3%A7%C3%B5es-un%C3%A1rias)
    - [SELECT](#select)
    - [PROJECT](#project)
    - [RENAME](#rename)
  - [Teoria dos Conjuntos](#teoria-dos-conjuntos)
    - [UNION](#union)
    - [INTERSECTION](#intersection)
    - [DIFFERENCE](#difference)
    - [CARTESIAN PRODUCT](#cartesian-product)
  - [Relacionais Binárias](#relacionais-bin%C3%A1rias)
    - [JOIN](#join)
      - [EQUIJOIN](#equijoin)
      - [NATURAL JOIN](#natural-join)
    - [DIVISION](#division)

## Introdução

A maioria dos bancos de dados relacionais utilizam linguagem SQL, uma *linguagem prática* do modelo relacional. A SQL é baseada nos conceitos de **álgebra relacional**, uma *linguagem formal* do modelo relacional. Todas as operações básicas do modelo relacional são da álgebra relacional.

Toda consulta (ou *query*) realizada tem como resultado uma nova relação. As operações da álgebra produzem novas relações que também podem ser manipuladas por novas operações. A álgebra relacional é muito importante visto que provê uma base formal para as operações do modelo relacional e principalmente por ser usada para implementar e otimizar as *queries* nos sistemas de bancos de dados.

As operações da álgebra relacional podem ser divididas em 4 grupos principais:

**Grupo** | **Operações** |
:---: | :---: |
Relacionais Unárias | *SELECT*, *PROJECT* e *RENAME* |
Teoria dos Conjuntos | *UNION*, *INTERSECTION* *DIFFERENCE* e *CARTESIAN PRODUCT* |
Relacionais Binárias | *JOIN* e *DIVISION* |
Relacionais Adicionais | *OUTER JOINS*, *OUTER UNION* e *AGGREGATE FUNCTIONS* |

Todos esses grupos de operações serão descritos a seguir.

## Relações Unárias

### SELECT

A operação **SELECT** é utilizada para selecionar um subconjunto das tuplas de uma relação. O funcionamento dessa operação se assemelha a um filtro, já que essas tuplas devem satisfazer a condição definida.

Esta operação é representada pelo símbolo *sigma* (**σ**) e utiliza a estrutura `σ <condicao_da_selecao> (R)`. A condição é uma expressão booleana, ou seja, deve retornar *verdadeiro* ou *falso*, de modo que apenas as tuplas que retornam *verdadeiro* para essa condição são selecionadas. *R* é o nome da relação que será filtrada.

#### Exemplo

Para exemplificar, imagine a seguinte relação

**EMPREGADO**

**Nome** | **Salário** | **Idade** |
--- | --- | --- |
Maria | 15000 | 22 |
José | 5000 | 22 |
Mario | 13000 | 23 | 


Pode-se selecionar os empregados (tuplas) que recebem salário maior que 10000 com a operação *SELECT* usando `σ Salário > 10000 (EMPREGADO)`. Essa operação irá retornar:


**EMPREGADO**

**Nome** | **Salário** | **Idade** 
:---: | :---: | :---: |
Maria | 15000 | 22 |
Mario | 13000 | 23 |

Uma outra operação poderia ser selecionar os empregados que tem 22 anos de idade usando `σ Idade = 22 (EMPREGADO)` e o resultado seria: 

**Nome** | **Salário** | **Idade** |
--- | --- | --- |
Maria | 15000 | 22 |
José | 5000 | 22 |

##### Comutativa

É possível aninhar diversas condições, no caso, aninhar SELECTS a outro SELECT. Por exemplo, pode-se selecionar os empregados que recebem salário maior que 10000 e que tenham 22 anos de idade. A operação vai ter a forma `σ Salário > 10000(σ Idade = 22 (EMPREGADO))` e resultará em:

**EMPREGADO**

**Nome** | **Salário** | **Idade**  |
:---: | :---: | :---: |
Maria | 15000 | 22 |

### PROJECT

Pensando em uma relação como uma tabela, a operação *SELECT* seleciona *linhas* da tabela e descarta as demais. De maneira análoga, a operação **PROJECT** seleciona as *colunas* de uma tabela e descarta as demais.

A operação *PROJECT* é representada pelo símbolo do *pi* (**π**) e utiliza a estrutura `π <lista_de_atributos> (R)`. Na `<lista_de_atributos>` coloca-se a lista de colunas da relação que devem ser seleionadas. O resultado dessa operação será uma *relação* contendo todas as tuplas da relação original na mesma ordem, porém apenas com as colunas que selecionadas.

#### Exemplo

Dada a relação EMPREGADO utilizada previamente, serão selecionados apenas o nome e o salário dos empregados através de `π Nome, Salário (EMPREGADO)`. O resultado será:

**EMPREGADO**

**Nome** | **Salário** |
--- | --- |
Maria | 15000 |
José | 5000 |
Mario | 13000 |

Uma possível situação é a seleção de atributos que não incluam atributos chave (*key*), ou seja, as tuplas poderão ter valores repetidos. Se isso ocorrer, a operação removerá automaticamente as tuplas repetidas. Se fosse realizada a operação `π Idade (EMPREGADO)`, dado que Maria e José tem a mesma idade, a operação iria mostrar apenas uma tupla com valor *22* na idade, conforme apresentado abaixo.

**EMPREGADO**

|**Idade** |
| --- |
| 22 |
| 23 |

### RENAME

É comum deparar-se com situações em que se precisa aplicar várias operações em sequência e, devido ao aninhamento desses vários passos, o código escrito pode tornar-se confuso. Para solurcionar esse problema, utiliza-se a operação **RENAME**.

A operação é representada pelo símbolo *rho* (**ρ**) e pode ser representada formalmente das seguintes maneiras:

1.  `ρS(R)` - Altera apenas a relação *R*.  A relação *R* agora vai ser referenciada por *S*.
2.  `ρ(B1, B2, ... , Bn)(R)` - Altera os atributos de *R*. Os atributos *B1, B2, ..., BN* irão substituir os atributos originais *A1, A2, ..., AN*.
3. `ρS(B1, B2, ... , Bn)(R)` - Altera a relação *R* e seus atributos simultaneamente, ou seja, realiza os tópicos *1* e *2* ao mesmo tempo.

Alternativamente, é possível utilizar o operador de atribuição (**←**) nas relações intermediárias para renomear os atributos ou a relação. Por exemplo:

```
TEMPORARIO(Nome_empregado, Idade_empregado) <- π Nome, Idade (EMPREGADO)
```

As colunas agora se chamarão *Nome_empregado* e *Idade_empregado* e a relação será chamada de *TEMPORARIO*. Usando esse operador, é possível quebrar uma sequência de operações em valores intermediários que serão válidos apenas naquela operação, ou seja, é uma renomeação temporária.

#### Exemplo

Imagine que se deseja selecionar os empregados que tem 22 anos de idade e que devem ser exibidas apenas as colunas *Nome* e *Salário*. Serão utilizadas as operações [SELECT](#select) e [PROJECT](#project) para selecionar os empregados com essa idade e para selecionar apenas as colunas desejadas, respectivamente.


Assim, tem-se `π Nome, Salário (σ Idade = 22 (EMPLOYEE))`, porém, o código torna-se mais compreensível através da utilização de valores intermediários. Isso pode ser feito através do operador de atribuição, como no exemplo abaixo.

```
EMPREGADOS_IDADE22 ← σ Idade = 22 (EMPLOYEE)
RESULTADO ← π Nome, Salário (EMPREGADOS_IDADE22)
```

**RESULTADO**

**Nome** | **Salário** |
--- | --- |
Maria | 15000 |
José | 5000 |


**PS:** Em SQL, a operação *RENAME* é chamada de **ALIAS** (*AS*).

## Teoria dos Conjuntos

As operações desse grupo são aquelas também usadas na teoria dos conjuntos.

### UNION

É uma operação binária, ou seja, aplicada a dois e somente dois conjuntos de tuplas que resulta em uma união de relações. As duas relações nessa operação devem ser compatíveis, ou seja, devem ter o mesmo número de atributos e esses atributos devem ser do mesmo tipo.

Essa operação é representada por **∪**.

#### Exemplo

Imagine duas relações, **ESTUDANTE** e **INSTRUTOR** que devem ser unidas. Tem-se:

**ESTUDANTE**

**Primeiro Nome** | **Último Nome** |
--- | ---  |
Maria | Alves |  
José | Sousa |
Mario | Olivedos | 

**INSTRUTOR**

**Primeiro Nome** | **Último Nome** |
--- | --- |
Maria | Alves |
Carla | Yun |
Mario | Olivedos | 

Dado `ESTUDANTE ∪ INSTRUTOR `, tem-se:

**Primeiro Nome**| **Último Nome** |
--- | --- |
Maria | Alves |  
José | Sousa |
Mario | Olivedos | 
Carla | Yun |

Note que as tuplas repetidas foram removidas, gerando apenas valores únicos.

### INTERSECTION

Diferente da operação anterior, na **INTERSECTION** a operação irá incluir apenas as tuplas que estão em ambas as relações. Essa operação possui os mesmos requisitos da UNION, ou seja, as relações devem ter o mesmo número de atributos e esses atributos devem ser do mesmo tipo.

Esta operação é representada por **∩** e utiliza a estrutura `R ∩ S`. Os atributos que estão na relação resultante terão os mesmos nomes dos atributos da relação *R*.

#### Exemplo

Aplicando `ESTUDANTE ∩ INSTRUTOR`, tem-se:

**Primeiro Nome** | **Último Nome** |
--- | --- |
Maria | Alves |
Mario | Olivedos |

### DIFFERENCE

Também conhecida como *minus* ou *except*, esta é uma operação de exclusão e utiliza a estrutura `R - S`, resultando numa nova relação com todas as tuplas que estão em **R**, mas não em **S**.

Essa operação não é comutatitiva, ou seja, `R - S != S - R`.

#### Exemplo

Aplicando `ESTUDANTE - INSTRUTOR`, o resultado será:

**Primeiro Nome** | **Último Nome** |
--- | --- |
José | Sousa |

### CARTESIAN PRODUCT

Essa operação binária irá combinar todos os atributos e valores das duas relações envolvidas. Não há requisitos de compatibilidade de atributos. 

Denotada por **×** e utilizando a estrutura `R × S`, essa operação resultará em uma combinação de todos os valores de cada tupla. Para `R(A1, A2, ... , An) × S(B1, B2, ... , Bn)`, o resultado será `Q(A1, A2, ... , An, B1, B2, ... , Bn)`.

#### Exemplo

Para `ESTUDANTE × INSTRUTOR`, tem-se:

**ESTUDANTE.Primeiro Nome** | **ESTUDANTE.Último Nome** | **INSTRUTOR.Primeiro Nome** | **INSTRUTOR.Último Nome** |
--- | --- | --- | --- | 
Maria | Alves  | Maria | Alves |
Maria | Alves  | Carla | Yun |
José | Sousa | Maria | Alves |
José | Sousa | Carla | Yun |
Maria | Alves | Maria | Alves |
Maria | Alves | José | Sousa |
Carla | Yun | Maria | Alves |
Carla | Yun | José | Sousa |

## Relacionais Binárias

### JOIN

Muito utilizada em bancos relacionais que possuem mais de uma relação e em que se faz necessário realizar operações que envolvam tuplas relacionadas de tabelas diferentes. A operação de **JOIN** funciona de maneira semelhante a um [SELECT](#select) seguido de um [CARTESIAN PRODUCT](#cartesian-product).

Essa operação é representada pelo símbolo **⋈** e utiliza a estrutura `R ⋈ <condicao_de_selecao> S`.

#### Exemplo

Considere as relações **EMPREGADO** e **DEPARTAMENTO** e que se deseja obter uma nova relação com os chefes de cada departamento.

**EMPREGADO**

**CPF** | **Nome** | **Salário** | **Idade** |
--- | --- | --- | --- |
123.456.123-21 | Maria | 15000 | 22 |
456.123.312-55 |José | 5000 | 22 |
789.392.858-56 |Mario | 13000 | 23 | 

**DEPARTAMENTO**

**CPF_do_chefe** |**Nome_departamento**
--- | --- |
123.456.123-21 | Departamento X |
789.392.858-56 | Departamento Y |

Para `DEPARTAMENTO ⋈ CPF_do_chefe = CPF EMPREGADO`, tem-se:

**CPF_do_chefe** | **Nome_departamento** | **Nome** | **Salário** | **Idade** |
--- | --- | --- | --- | --- |
123.456.123-21 | Departamento X | Maria | 15000 | 22 |
789.392.858-56 | Departamento Y | Mario | 13000 | 23 |

#### EQUIJOIN

Ocorre de maneira análoga ao JOIN, porém o operador da seleção é automaticamente um **=**.

#### NATURAL JOIN

Denotada por `*`, essa operação junta duas relações com base em seus atributos, removendo repetições daqueles com nomes coincidentes.

##### Exemplo

`Q ← R(A, B, C) * S(A, D, E)`

A condição de junção ímplicita é *R.A* = *S.A* e o resultado será `Q(A, B, C, D, E)`.

### DIVISION

A operação **DIVISION** é denotada por **÷** e utiliza a estrutura `R(Z) ÷ S(X)`, indicando que se deseja as tuplas de *R* que contém todos os subconjuntos de *S*.

#### Exemplo

Imagine as relações **R** e **S**, tal que se deseja selecionar as tuplas de **R** que incluem todos os valores de **A** que estejam na tabela **S**.

**R**

**A** | **B** |
:---: | :---: |
a1 | b1 |
a2 | b1 |
a3 | b1 |
a1 | b2 |
a2 | b2 |
a3 | b2 |
a4 | b2 |
a1 | b3 |

**S**

| **A** |
| :---: |
| a1 |
| a2 |
| a3 |

Para `RESULTADO ← R(Z) ÷ S(X) `, tem-se:

**RESULTADO**

| **B** |
| :---: |
| b1 |
| b2 |
