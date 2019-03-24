# Álgebra Relacional

## Sumário
- [Álgebra Relacional](#%C3%A1lgebra-relacional)
  - [Sumário](#sum%C3%A1rio)
  - [Visão Geral](#vis%C3%A3o-geral)
  - [Relações Unárias](#rela%C3%A7%C3%B5es-un%C3%A1rias)
    - [SELECT](#select)
      - [Exemplo](#exemplo)
        - [Comutativa](#comutativa)
    - [PROJECT](#project)
      - [Exemplo](#exemplo-1)
    - [RENAME](#rename)
      - [Exemplo](#exemplo-2)
  - [Teoria dos conjuntos](#teoria-dos-conjuntos)
    - [UNION](#union)
      - [Exemplo](#exemplo-3)
    - [INTERSECTION](#intersection)
      - [Exemplo](#exemplo-4)
    - [DIFFERENCE](#difference)
      - [Exemplo](#exemplo-5)
    - [CARTESIAN PRODUCT](#cartesian-product)
      - [Exemplo](#exemplo-6)
  - [Relacionais binárias](#relacionais-bin%C3%A1rias)
    - [JOIN](#join)
      - [Exemplo](#exemplo-7)
      - [EQUIJOIN](#equijoin)
      - [NATURAL JOIN](#natural-join)
        - [Exemplo](#exemplo-8)
    - [DIVISION](#division)
      - [Exemplo](#exemplo-9)


## Visão Geral

A maioria dos banco de dados relacionais usam linguagem SQL que é a *linguagem prática* do modelo relacional. SQL é baseada nos conceitos de **álgebra relacional**, que é uma *linguagem formal* do modelo relacional. Todas as operações básicas do modelo relacional são da **álgebra relacional**.

Toda query feita, o resultado é uma nova relação, as operação da álgebra produzem novas relações que podem também ser manipuladas por outra operações. A **álgebra relacional** é muito importante para pois provê uma base formal para as operações do modelo relacional, e mais importante, é usada para implementar e otimizar queries nos sistemas de banco dados, sendo assim, importante de ser estudada.

As operações da álgebra relacional pode ser dividida em quatro grupos:

**Grupo** | **Operações** 
:---: | :---:
Relacionais Unárias | *SELECT*, *PROJECT* e *RENAME* 
Teoria dos Conjuntos | *UNION*, *INTERSECTION* *DIFFERENCE* e *CARTESIAN PRODUCT* |
Relacionais Binárias | *JOIN* e *DIVISION* |
Relacionais Adicionais | *OUTER JOINS*, *OUTER UNION* e *AGGREGATE FUNCTIONS* |

Vamos descrever cada grupo de operações nos próximos tópicos.

## Relações Unárias

### SELECT

A operação **SELECT** é usada para escolher um subconjunto das tuplas de uma relação, esse subconjunto tem que satisfazer uma condição que podemos definir. Parecido com um *filtro*, já que irá filtar as tuplas que satisfazem a condição.

Esta operação é representada pelo símbolo de sigma(*σ*) e geralmente com esta estrutura `σ <condicao_da_selecao> (R)`. A condição é uma expressão boolean, ou seja, só pode retornar *verdadeiro* ou *falso*, as tuplas que retornarem *verdadeiro* na condição, serão as selecionadas. *R* é o nome da relação que será filtrada.

#### Exemplo

Para exemplificar, imagine a seguinte relação

**EMPREGADO**

**Nome** | **Salário** | **Idade** 
--- | --- | --- 
Maria | 15000 | 22
José | 5000 | 22
Mario | 13000 | 23 


Podemos selecionar os empregados(tuplas) que possuem salário maior que 10000 com a operação *SELECT*: `σ Salário>10000 (EMPREGADO)`. Essa operação irá retornar:


**EMPREGADO**

**Nome** | **Salário** | **Idade** 
:---: | :---: | :---:
Maria | 15000 | 22
Mario | 13000 | 23

Outro tipo de operação poderia ser selecionar os empregados que possuem idade igual a *22 anos*: `σ Idade=22 (EMPREGADO)`. O resultado vai ser: 

**Nome** | **Salário** | **Idade** 
--- | --- | --- 
Maria | 15000 | 22
José | 5000 | 22

##### Comutativa

Podemos aninhar condições, no caso, aninhar outro SELECT. Por exemplo, podemos selecionar os empregaodos que possuem salário maior que 10000 e tenha idade igual a 22 anos. A operação vai ficar assim: `σ Salário>10000(σ Idade=22 (EMPREGADO))`. O resultado:

**EMPREGADO**

**Nome** | **Salário** | **Idade** 
:---: | :---: | :---:
Maria | 15000 | 22

### PROJECT

Se pensamos em uma relação como uma tabela, a operação *SELECT* seleciona *linhas* de uma tabela e descarta as outras, seguindo essa lógica, a operação **PROJECT** seleciona *colunas* de uma tabela, e descarta as outras.

A operação é representada por *PROJECT* pelo símbolo do *pi*(π) e segue a seguinte estrutura: `π <lista_de_atributos> (R)`. Na *<lista_de_atributos>* colocamos a lista de colunas que queremos selecionar da relação, o resultado dessa operação será uma *relação* contendo as tuplas na mesma ordem que a relação original(R) porém apenas com as colunas que selecionamos

#### Exemplo

Temos de novo a relação EMPREGADO: 

**EMPREGADO**

**Nome** | **Salário** | **Idade** 
--- | --- | --- 
Maria | 15000 | 22
José | 5000 | 22
Mario | 13000 | 23 

Vamos selecionar apenas o nome e o salário: `π Nome, Salário (EMPREGADO)`. O resultado será:

**EMPREGADO**

**Nome** | **Salário** 
--- | --- 
Maria | 15000
José | 5000
Mario | 13000

Uma situação que pode ocorrer é quando selecionamos atributos que não possuem atributos *key*, ou seja, que podem ter valores repetidos. Se isso ocorrer, a operação remove as tuplas repetidas. Exemplo, se fizeremos `π Idade (EMPREGADO)`, Maria e José possuem a mesma idade e ficaria repetido no resultado da operação, ao invés disso a operação irá mostrar apenas uma tupla com valor *22* na *idade*.

**EMPREGADO**

|**Idade** |
| --- |
| 22 |
| 23 |

### RENAME

É comum termos situações que precisamos aplicar várias operações em sequência, invés de irmos aninhando essas operações em uma única operação, podemos usar a operação **RENAME** para facilitar.

A operação é representada pelo símbolo rho(*ρ*), formalmente ela pode ser representada das seguintes maneira:

1.  `ρS(R)` - Altera apenas a relação *R*.  A relação *R* agora vai ser referenciada por *S*
2.  `ρ(B1, B2, ... , Bn)(R)` - Altera os atributos de *R*. Os atributis *B1, B2, ..., BN* irão substituir os atributos originais *A1, A2, ..., AN*
3. `ρS(B1, B2, ... , Bn)(R)` - Quando queremos modificar tanto o nome da relação como os atributos. São o passo *1* e *2* ao mesmo tempo.

Alternativamente, podemos usar o **operador de atribuição**(←)
 nas relações intermediárias para poder renomear os atributos ou a relação, exemplo:

```
TEMPORARIO(Nome_empregado, Idade_empregado) <- π Nome, Idade (EMPREGADO)
```

As colunas agora se chamarão *Nome_empregado* e *Idade_empregado* e a relação *TEMPORARIO*. Usando esse operador, podemos quebrar uma sequência de operações em valores intermediários, que serão apenas válidos na operação, ou seja, é uma renomeação temporária.

#### Exemplo

Imagine que queremos selecionar os empregados que possuem idade igual a *22* e queremos apenas as colunas *Nome* e *Salário*. Para selecionar a idade iremos usar a operação [Select](#select) e para selecionar as colunas a operação [PROJECT](#project)


Podemos fazer `π Nome, Salário (σ Idade=22 (EMPLOYEE))`, porém como já foi dito, é melhor quebrar algumas operações em valores intermediários, faremos isso com o operador de atribuição:

```
EMPREGADOS_IDADE22 ← σ Idade=22 (EMPLOYEE)
RESULTADO ← π Nome, Salário (EMPREGADOS_IDADE22)
```

**RESULTADO**

**Nome** | **Salário**
--- | --- | --- 
Maria | 15000 
José | 5000


**PS:** Em SQL operação *RENAME* é a **ALIAS**.

## Teoria dos conjuntos

As operações desse grupo são as operações usadas também na teoria dos conjuntos.

### UNION

É uma operação binária, ou seja, aplicada a **dois** conjuntos de tuplas, o seu resultado é uma união de relações. As duas relações nessa operação devem ser compatíveis, isso significa que devem ter o mesmo número de atributos e que devem ser do mesmo tipo.

Essa operação é representada por **∪**

#### Exemplo

Imaginemos duas tabelas, **ESTUDANTE** e **INSTRUTOR**, vamos fazer a união delas.


**ESTUDANTE**

**Primeiro Nome**| **Último Nome** 
--- | --- 
Maria | Alves  
José | Sousa
Mario | Olivedos 


**INSTRUTOR**

**Primeiro Nome**| **Último Nome** 
--- | --- 
Maria | Alves
Carla | Yun
Mario | Olivedos 


Se fizermos `ESTUDANTE ∪ EMPREGADO `, teremos:


**Primeiro Nome**| **Último Nome** 
--- | --- 
Maria | Alves  
José | Sousa
Mario | Olivedos 
Carla | Yun

Perceba que as tuplas repetidas foram removidas, ficando apenas valores únicos.


### INTERSECTION

Na **INTERSECTION** diferente da anterior, a operação irá incluir apenas as tuplas que estão em **ambas** as relações. Essa operação seguirá as mesmas regras que a anterior, ou seja, os tipos devem ser compatíveis.

Esta operação é representada por **∩**, seguindo a estrutua `R ∩ S`. Os atributos que ficaram no resultado vão ter o mesmo nome dos atributos da relação *R*.

#### Exemplo

**ESTUDANTE**

**Primeiro Nome**| **Último Nome** 
--- | --- 
Maria | Alves  
José | Sousa
Mario | Olivedos 


**INSTRUTOR**

**Primeiro Nome**| **Último Nome** 
--- | --- 
Maria | Alves
Carla | Yun
Mario | Olivedos 


Aplicando `ESTUDANTE ∩ INSTRUTOR`, teremos:

**Primeiro Nome**| **Último Nome** 
--- | --- 
Maria | Alves  
Mario | Olivedos 

### DIFFERENCE

Conhecida também por *minus* ou *except*. É uma operação de exclusão, seguindo a estrutura **R - S**, irá mostrar todas as tuplas que estão em **R** e não estão em **S**.

Essa operação não é comutatitiva, ou seja: `R - S != S - R`.

#### Exemplo

**ESTUDANTE**

**Primeiro Nome**| **Último Nome** 
--- | --- 
Maria | Alves  
José | Sousa
Mario | Olivedos 


**INSTRUTOR**

**Primeiro Nome**| **Último Nome** 
--- | --- 
Maria | Alves
Carla | Yun
Mario | Olivedos 

Aplicando `ESTUDANTE - INSTRUTOR`, o resultado vai ser:

**Primeiro Nome**| **Último Nome** 
--- | --- 
José | Sousa

### CARTESIAN PRODUCT

Nessa operação binária, irá combinar todos os atributos e valores de uma relação com a outra, sem precisar ter tipos compatíveis. 

Denotada por **×**, segue essa estrutura `R × S` e terá uma combinação de todos os valores de cada tupla, no caso se temos `R(A1, A2, ... , An)× S(B1, B2, ... , Bn)`, o resultado será `Q(A1, A2, ... , An, B1, B2, ... , Bn)`.


#### Exemplo

**ESTUDANTE**

**Primeiro Nome**| **Último Nome** 
--- | --- 
Maria | Alves  
José | Sousa


**INSTRUTOR**

**Primeiro Nome**| **Último Nome** 
--- | --- 
Maria | Alves
Carla | Yun

Se fizermos `ESTUDANTE × INSTRUTOR`, teremos:

**ESTUDANTE.Primeiro Nome**| **ESTUDANTE.Último Nome** |**INSTRUTOR.Primeiro Nome**| **INSTRUTOR.Último Nome** 
--- | --- | --- | --- 
Maria | Alves  | Maria | Alves
Maria | Alves  | Carla | Yun
José | Sousa | Maria | Alves
José | Sousa | Carla | Yun
Maria | Alves | Maria | Alves
Maria | Alves | José | Sousa
Carla | Yun | Maria | Alves
Carla | Yun | José | Sousa

## Relacionais binárias

### JOIN

É muito comum em bancos relacionais que possuimos mais de uma relação queremos realizar operações que combine tuplas relacionadas em tabelas diferentes. A operação de **JOIN** serve para isso, é como se fosse um [SELECT](#select) seguido de um [CARTESIAN PRODUCT](#cartesian-product).

Representada pelo símbolo **⋈**, segue a estrutura `R ⋈ <condicao_de_selecao> S`.

#### Exemplo
Imagine que temos a tabela **EMPREGADO** e **DEPARTAMENTO**, queremos uma nova tabela com os chefes de cada departamento.

**EMPREGADO**

**CPF** |**Nome** | **Salário** | **Idade** 
--- | --- | --- | --- 
123.456.123-21 | Maria | 15000 | 22
456.123.312-55 |José | 5000 | 22
789.392.858-56 |Mario | 13000 | 23 

**DEPARTAMENTO**

**CPF_do_manager** |**Nome_departamento**
--- | --- 
123.456.123-21 | Departamento X
789.392.858-56 | Departamento Y

Se fizermos `DEPARTAMENTO ⋈ CPF_do_manager=CPF EMPREGADO`, teremos:


**CPF_do_manager** |**Nome_departamento** |**Nome** | **Salário** | **Idade** 
--- | --- | --- | --- | --- | --- 
123.456.123-21 | Departamento X | Maria | 15000 | 22
789.392.858-56 | Departamento Y | Mario | 13000 | 23 

#### EQUIJOIN

Acontece quando o operador de seleção é o **=**.

#### NATURAL JOIN

Denotado por `*`, junta duas relações com base em um atributo que tenha o mesmo nome, não deixando repetido. Se o atributo não tiver o mesmo nome quando fizer a operação, ele renomeia e prevalece o primeiro.

##### Exemplo

`Q ← R(A, B, C) * S(A, D, E)`

A condição de junção ímplicita é *R.A* = *S.A* e o resultado vai ser `Q(A, B, C, D, E)`.


### DIVISION

A operação **DIVISION** denotado por **÷**, segue a estrutura `R(Z) ÷ S(X)` que significa que queremos as tuplas de *R* que contém todos os subconjuntos de *S*.

#### Exemplo
Imagine as relações **R** e **S**, queremos selecionar as tuplas de **R** que incluem todos os valores de **A** que possuem na tabela **S**.

**R**

**A** | **B**
:---: | :---:
a1 | b1
a2 | b1
a3 | b1
a1 | b2
a2 | b2
a3 | b2
a4 | b2
a1 | b3

**S**

| **A** |
| :---: |
| a1 |
| a2 |
| a3 |


Quando fizermos `RESULTADO ← R(Z) ÷ S(X) `, teremos:

**RESULTADO**

| **B** |
| :---: |
| b1 |
| b2 |
