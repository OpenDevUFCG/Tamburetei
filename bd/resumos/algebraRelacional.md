---
title: Álgebra Relacional
---
*Seção 8.5 - Fundamentals of DataBase Systems 7th edition.*

## Sumário
- [Álgebra Relacional](#%C3%A1lgebra-relacional)
  - [Sumário](#sum%C3%A1rio)
  - [Introdução](#Introduç%C3%A3o)
  - [Expressões inline e relações intermediárias](#Expressões-inline-e-relações-intermediárias)
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
  - [Relacionais adicionais](#Operações-relacionais-adicionais)
    - [GENERALIZED PROJECTION](#Generalized-Projection)
    - [AGGREGATE FUNCTION](#Operação-de-funções-de-agregação-e-Agrupamento)
    - [RECURSIVE CLOSURE](#Fechamento-Recursivo)
    - [OUTER JOIN](#OUTER-JOIN)
    - [OUTER UNION](#OUTER-UNION)

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

---
## Expressões inline e relações intermediárias
---

Todas as operações previamente citadas podem ser escritas como uma única **expressão algébrica relacional(expressões in-line)** ou podem ser escritas com o auxílio de **relações intermediárias**.


- **Expressão in-line:**
    ```
    𝛑 Name, age, sex(σ age > 18(R))
    ```

- **Utilizando relações intermediárias:**
    ```
    rel_temp <- σ age > 18(R)

    𝛑 Name, age, sex(rel_temp)
    ``` 

---
## Relações Unárias
---
### SELECT

Representada pelo símbolo *sigma* (**σ**), a operação **SELECT** é utilizada para selecionar um subconjunto das tuplas de uma relação. O funcionamento dessa operação se assemelha a um filtro, já que essas tuplas devem satisfazer a condição definida.

O SELECT é estruturado da seguinte forma:

```
σ <condição de seleção> ( R )
```

Onde:
    
- **σ** :Sigma, letra que representa a operação SELECT;
- **<condição de seleção>:** Expressão booleana que serve para filtrar as tuplas, ou seja, apenas as tuplas que satisfizerem a condição, retornam true, serão selecionadas;
- **(R)**: Relação na qual será feita a filtragem.

Essa operação possui a propriedade da `Comutatividade`, ou seja:
```
 σ <condição-02> (σ <condição-01> ( R )) == σ <condição-01> (σ <condição-02> ( R )).
```
#### Exemplos:

Para todos os próximos exemplos, utilizaremos a seguinte relação

**EMPREGADO**

**Nome** | **Salário** | **Idade** |
--- | --- | --- |
Maria | 15000 | 22 |
José | 5000 | 22 |
Mario | 13000 | 23 | 

#### - Exemplo 01

Selecionar empregados cujo salário está acima de 10000 reais.
```
  σ Salário > 10000 (EMPREGADO)
```

**EMPREGADO**

**Nome** | **Salário** | **Idade** 
:---: | :---: | :---: |
Maria | 15000 | 22 |
Mario | 13000 | 23 |

**Resultado:** A operação filtrou o empregado "José" já que ele recebe 5000 reais.

#### - Exemplo 02

Selecionar empregados exatamente 22 anos.

```
  σ Idade = 22 (EMPREGADO)
```

**Nome** | **Salário** | **Idade** |
--- | --- | --- |
Maria | 15000 | 22 |
José | 5000 | 22 |

**Resultado:** A operação agora filtrou o empregado "Mario" já que ele tem 23 anos. 

#### - Exemplo 03

`Comutatividade`: Selecionar Empregados que tem um salário superior a 10000 reais e tem exatamente 22 anos.
```
  σ Salário > 10000(σ Idade = 22 (EMPREGADO))
  
  ou

  σ Idade = 22 (σ Salário > 10000 (EMPREGADO))
```

**EMPREGADO**

**Nome** | **Salário** | **Idade**  |
:---: | :---: | :---: |
Maria | 15000 | 22 |

**Resultado:** A operação filtrou o empregado "Mário", ele ganha mais que 10000 reais, porém não tem 22 anos. O SELECT também filtrou o "José", uma vez que apesar de ter 22 anos ele não ganha mais que 10000 reais

---
### PROJECT

Representada pelo símbolo do *pi* (**π**), a operação **PROJECT** funciona de forma análoga à operação *SELECT*, todavia, ao invés de selecionar tuplas(linhas), o PROJECT seleciona atributos(colunas). Sendo assim, o resultado dessa operação será uma *relação* contendo todas as tuplas da relação original na sua ordem original, porém apenas com as colunas que foram selecionadas.

> :warning: **OBS:** Caso a seleção de atributos que não incluam atributos chave (*key*), ou seja, as tuplas poderão ter valores repetidos. Se isso ocorrer, a operação removerá automaticamente as tuplas repetidas. Isso não acontece no SQL, a operação análoga ao PROJECT mantém as tuplas repetidas.

O PROJECT utiliza a seguinte estrutura:

```
π <atributos > ( R )
```

Onde:
- **π:** PI, letra que representa a operação PROJECT;
- <**atributos**>: Lista de atributos (colunas) que estarão presentes na nova relação criada;
- **(R):** Relação na qual será feita a operação.


#### Exemplos:

#### - Exemplo 01

Selecionar apenas o nome e salário dos empregados:

```
  π Nome, Salário (EMPREGADO)
```

**EMPREGADO**

**Nome** | **Salário** |
---      | ---         |
Maria    | 15000       |
José     | 5000        |
Mario    | 13000       |

**Resultado:** Uma nova relação empregado que possui apenas o nome e salário dos funcionários.

#### - Exemplo 02

Selecionar apenas a idade dos empregados:

```
  π Idade (EMPREGADO)
```

**EMPREGADO**

|**Idade** |
| --- |
| 22 |
| 23 |

**Resultado:** Dado que Maria e José tem a mesma idade, a operação mostrou apenas uma tupla com valor *22* na idade, já que a relação resultante da retirada dos nomes e salários possuiria duas tuplas repetidas, o que não é permitido pela álgebra relacional.

---
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

---
## Teoria dos Conjuntos

As operações desse grupo são aquelas também usadas na teoria dos conjuntos.

#### Exemplos:

As duas relações a seguir, ESTUDANTE e INSTRUTOR, serão utilizadas nos próximos exemplos de Teoria dos Conjuntos.

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

---
### UNION

A operação de união junta as tuplas de uma relação R com as tuplas de uma relação S e cria uma nova relação `R ⋃ S`, onde não há tuplas duplicadas. As duas relações nessa operação devem ser compatíveis, ou seja, devem ter o mesmo número de atributos e esses atributos devem ser do mesmo tipo e domínio.

Essa operação é representada por **∪** e possui as seguintes propriedades:

- **Comutatividade:** R ⋃ S == S ⋃ R
- **Associatividade:** (R ⋃ S) ⋃ T ==  R ⋃ (S ⋃ T)

#### Exemplo

Dado `ESTUDANTE ∪ INSTRUTOR `, tem-se:

**Primeiro Nome**| **Último Nome** |
--- | --- |
Maria | Alves |  
José | Sousa |
Mario | Olivedos | 
Carla | Yun |

> Note que as tuplas repetidas foram removidas, gerando apenas valores únicos.

---
### INTERSECTION

Diferente da operação anterior, na **INTERSECTION** a operação irá incluir apenas as tuplas que estão em ambas as relações. Essa operação possui os mesmos requisitos da UNION, ou seja, as relações devem ter o mesmo número de atributos e esses atributos devem ser do mesmo tipo.

Esta operação é representada por **∩** e utiliza a estrutura `R ∩ S`. Os atributos que estão na relação resultante terão os mesmos nomes dos atributos da relação *R*.

Essa operação possui as seguintes propriedades:

- **Comutatividade** R ⋂ S == S ⋂ R
- **Associatividade** (R ⋂ S) ⋂ T ==  R ⋂ (S ⋂ T)

#### Exemplo

Aplicando `ESTUDANTE ∩ INSTRUTOR`, tem-se:

**Primeiro Nome** | **Último Nome** |
--- | --- |
Maria | Alves |
Mario | Olivedos |

---
### DIFFERENCE ou MINUS

Também conhecida como *minus* ou *except*, esta é uma operação de exclusão e utiliza a estrutura `R - S`, resultando numa nova relação com todas as tuplas que estão em **R**, mas não em **S**.

Essa operação não é comutatitiva, ou seja, `R - S != S - R`.

#### Exemplo

Aplicando `ESTUDANTE - INSTRUTOR`, o resultado será:

**Primeiro Nome** | **Último Nome** |
--- | --- |
José | Sousa |

---
### CARTESIAN PRODUCT

Essa operação `R X S` produz uma nova relação Z formada pela combinação de todas as tuplas de R com as tuplas de S, resultando na relação Z que possui a quantidade de colunas de R somada a quantidade de colunas de S, ou seja, para `R(A1, A2, ... , An) × S(B1, B2, ... , Bn)`, o resultado será `Q(A1, A2, ... , An, B1, B2, ... , Bn)`.

Essa operação é representada da seguinte forma:

```
Z <- R X S
```

Onde:
- **X:** Símbolo que representa a operação de produto cartesiano;
- **Z:** Relação produzida a partir do produto cartesiano;
- **R e S:** RElações participantes da operação.

**n° tuplas:** n° tuplas de R * n° tuplas de S;

**Ordem:** n° atributos de R + n° atributos de S.

> :warning: **OBS:** O produto cartesiano por si só *não* traz conhecimento **real** por si só, sendo necessária à utilização do SELECT, por exemplo, para filtrar os dados que podem ter algum significado.

#### Exemplo

Para `ESTUDANTE × INSTRUTOR`, tem-se:

**ESTUDANTE.Primeiro Nome** | **ESTUDANTE.Último Nome** | **INSTRUTOR.Primeiro Nome** | **INSTRUTOR.Último Nome** |
---                         | ---                       | ---                         | ---                       | 
Maria                       | Alves                     | Maria                       | Alves                     |
Maria                       | Alves                     | Carla                       | Yun                       |
Maria                       | Alves                     | Mario                       | Olivedos                  |
José                        | Sousa                     | Maria                       | Alves                     |
José                        | Sousa                     | Carla                       | Yun                       |
José                        | Sousa                     | Mario                       | Olivedos                  |
Carla                       | Yun                       | Maria                       | Alves                     |
Carla                       | Yun                       | José                        | Sousa                     |
Carla                       | Yun                       | Mario                       | Olivedos                  |

---
## Relacionais Binárias
---
### JOIN

Muito utilizada em bancos relacionais que possuem mais de uma relação e em que se faz necessário realizar operações que envolvam tuplas relacionadas de tabelas diferentes. A operação de **JOIN** funciona de maneira semelhante a um [SELECT](#select) seguido de um [CARTESIAN PRODUCT](#cartesian-product).

Essa operação é representada da seguinte maneira:

```
DEPARTMENT ⋈ Mgr_ssn = Ssn EMPLOYEE
```

Onde:
- **⋈:** Símbolo que representa a operação de JOIN;
- **Mgr_ssn = Ssn:** Condição de seleção;
- **Department e employee:** Relações sobre as quais a operação será feita.

**n° tuplas:** desde n° tuplas de R * n° tuplas tuplas S até 0, caso a *condição* imposta nunca seja satisfeita.

**Ordem:** n° atributos de R + n° atributos atributos de S.

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

---
#### EQUIJOIN

Ocorre de maneira análoga ao JOIN, porém o operador da seleção é automaticamente um **=**.

> **OBS:** Como a condição de seleção é uma **=** o EQUIJOIN resulta em colunas repetidas, uma vez que ele não apaga colunas iguais.

---
#### NATURAL JOIN

Denotada por `*`, essa operação foi criada para excluir colunas repetidas ao se fazer um [EQUIJOIN](#equijoin).

Essa operação se organiza da seguinte maneira:

```
NOVA_REL <- R * <condição1 AND condição2> S
```

Onde:
- **NOVA_REL:** Relação resultante;
- **R e S:** Relações sobre as quais a operação será realzada;
- *: Símblo da operação natural join;
- <**condição1 AND condição2**>: Condições que ditarão como será feita a seleção das tuplas     , chamado de `THETA_JOIN`.

> :warning: **OBS:** Para que essa operação funcione é necessário que o nome dos atributos que vão ser comparados sejam iguais.

##### Exemplo

`Q ← R(A, B, C) * S(A, D, E)`

A condição de junção ímplicita é *R.A* = *S.A* e o resultado será `Q(A, B, C, D, E)`.

---
### DIVISION

A operação R ÷ S funciona da seguinte maneira. sendo o conjunto de atributos de S um subconjunto dos atributos de R, R ÷ S pega todos os valores das tuplas de R que se conseguem abranger  TODAS as tuplas de S e cria uma nova relação a partir disso.

#### Exemplo 01

FUNCIONÁRIO
| Nome | Proj_n | SSN |
| --- | --- | --- |
| regis | 1 | 1234 |
| regis | 2 | 1234 |
| Bia | 1 | 7410 |
| Bia | 3 | 7410 |

PROJETOS
| Proj_n |
| --- |
| 1 |
| 2 |

FUNCIONÁRIO ÷ PROJETOS
| Nome | SSN |
| --- | --- |
| Regis | 1234 |

#### Exemplo 02

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

---
## Operações relacionais adicionais
---
São operações que realizam tarefas que as operações *originais* não conseguem resolver para a SGBDR (Sistema de gerenciamento de banco de dados Relacional)

A relação a seguir será utilizada nos próximos exemplos.

PESSOA

| Nome     | Salário | Netflix | Aluguel |
| ---      | ---     | ---     | ---     |
| José     | 7000    | 22      | 2000    |
| Rodrigo  | 8000    | 22      | 2500    |
| Evaristo | 34000   | 46      | 4000    |
| Joseana  | 40000   | 46      | 5000    |

---
### **Generalized Projection**
A Generalized Projection (Projeção Generalizada)  estende a operação [PROJECT](#PROJECT), permitindo que a lista de atributos selecionados incluam operações feitas sobre os atributos.

Essa operação é estruturada da seguinte forma:

```
π <f1, f2, ..., fn> (R)
```

Onde:
- **π:** Símbolo da operação PROJECT;
- **f1, f2, ..., fn:** Funções sobre os atributos da relação, podendo ser operações aritméticas ou valores constantes;
- **(R:)** Relação sobre a qual a operação será realizada.

> :warning: **Atenção:** O nome dos atributos criados a partir das funções pode ficar sem sentido, por isso normalmente se utiliza a operação de [Rename](#rename) para complementar essa operação.

**Exemplo:**

Selecionar Nome, salário e a despesa totais, que é formada pela soma do preço da Netflix e dp aluguel:

```
RELACAO <- ρ(Nome, salário, despesas) (π Nome, Salário, Netflix + Aluguel (PESSOA))
```

RELACAO
| Nome     | Salário | despesas |
| ---      | ---     | ---      |
| José     | 7000    | 2022     |
| Rodrigo  | 8000    | 2522     |
| Evaristo | 34000   | 4046     |
| Joseana  | 40000   | 5046     |

---
### **Aggregate Functions and Grouping**
A operação de funções de agregação é uma operação que permite a utilização de [`Funções de agregação`](https://www.devmedia.com.br/sql-funcoes-de-agregacao/38463), funções essas que servem para sumarizar informações a partir de um conjunto de tuplas da base de dados, assim como permite o `agrupamento` de tuplas a partir dos valores de atributos especificados é outra necessidade.

Essa operação se estrutura da seguinte maneira:

```
<`grouping attributes`> I <function list> (R)
```

Onde:
- <**grouping attributes**>: Atributos que servirão para fazer o agrupamento;
- **I:** Símbolo da operação de Funçoẽs de agregação;
- <**function list**>: Lista de tuplas (<`função`><`atributo`>), onde `função` é uma das funções permitidas (como SUM, AVERAGE, MAXIMUM, MINIMUM, COUNT) e `Atributo` é o atributo sobre o qual a função vai ser operada;
- **(R):** Relação sobre a qual ocorrerá a operação.

> :warning: **OBS:** Caso a operação SELECT não seja utilizada em seguida, os nomes dos atributos criados na nova relação será uma concatenação `função_atributo`.

**Exemplo:**

Criar uma relação que seleciona a quantidade dos diferentes tipos preços da netflix e o salário médio das pessoas pra cada preço da netflix.

```
  R <- ρ(Netflix, num_contas, sal_medio) (π Netflix, COUNT Netflix, AVERAGE salário (PESSOA))
```
R
| Netflix     | num_contas | sal_medio |
| ---         | ---        | ---       |
| 22          | 2          | 7500      |
| 46          | 2          | 37000     |


---
### **Recursive Closure**

O fechamento recursivo é uma operação em que existe um **relacionamento recursivo** entre as tuplas da mesma relação, como empregado e supervisor por exemplo. 

> :warning: **OBS:** Essa operação não é possível de ser implementada com operações básicas da álgebra realacional, todavia, é implementada na linguagem [`SQL`(colocar o link para o resumo de SQL)]().

**Ex:**  

Caso seja requisitado os ids de todos os funcionários que estejam sendo supervisionados pelo funcionário X, ou por aqueles que ele supervisiona. Será necessário acessar os supervisionados do X, depois os supervisionados dos supervisionados de X e assim em diante.

---
### **OUTER JOIN**

A operação `outer join` possui o mesmo princípio de um [`join`](#join) comum, todavia, ao fazer o "matching" das duas relações ela não descarta as tuplas que não possuem par, ao invés disso, associa essas tuplas a valores *NULL*.

Essa operação é estruturada da seguinte forma:

```
DEPARTMENT ⋈ Mgr_ssn = Ssn EMPLOYEE
```

> obs: O símbolo acima possui perninhas dependendo do tipo, mas não achei do tamanho correto

O outer join pode ser dividido em 3 variasções:

- **LEFT OUTER JOIN:** As tuplas da relação à esquerda que não possuem par são associados a valores *NULL*, enquanto as tuplas que não possuem par na relação a direito são descartadas;

- **RIGHT OUTER JOIN:** Mesma ideia do `left outer join`, porém, nesse caso as tuplas da relação à direita que não possuem par são associados a valores *NULL*, enquanto as tuplas que não possuem par na relação a esquerda são descartadas; 

- **FULL OUTER JOIN** Tanto as tuplas da relação a direita, quanto as tuplas da relação a esquerda que não possuirem um par quando for realizada a operação de `join` são associados a valores *NULL*.

**Exemplos:**

A relação a seguir será utilizada nos próximos exemplos:
EMPREGADO
| nome | id_dept |
| --- | --- |
| Josenildo | 1 |
| Joselanda | 2 |
| Joana | 1 |
| Jefferson | 4 |

DEPARTAMENTO
| id | nome_dep |
| --- | --- |
| 1 | Administração |
| 2 | Financeiro |
| 3 | Marketing |

**Exemplo 01 - LEFT OUTER JOIN**

```
REL <- π nome, id_dept, nome_dep (EMPREGADO ⋈ id_dept = id DEPARTAMENTO)
```
REL
| nome      | id_dept | nome_dep      |
| ---       | ---     | ---           |
| Josenildo | 1       | Administração |
| Joselanda | 2       | Financeiro    |
| Joana     | 1       | Administração |
| Jefferson | 4       | NULL          |

**Exemplo 02 - RIGHT OUTER JOIN** 

```
REL <- π nome, id, nome_dep (EMPREGADO ⋈ id_dept = id DEPARTAMENTO)
```

REL
| nome      | id  | nome_dep      |
| ---       | --- | ---           |
| Josenildo | 1   | Administração |
| Joselanda | 2   | Financeiro    |
| Joana     | 1   | Administração | 
| NULL      | 3   | marketing     |

**Exemplo 03 - FULL OUTER JOIN** 

```
REL <- π nome, id, nome_dep (EMPREGADO ⋈ id_dept = id DEPARTAMENTO)
```

REL
| nome      | id  | nome_dep      |
| ---       | --- | ---           |
| Josenildo | 1   | Administração |
| Joselanda | 2   | Financeiro    |
| Joana     | 1   | Administração | 
| NULL      | 3   | marketing     |
| Jefferson | 4   | NULL          |

---
### **OUTER UNION**

Essa operação é a mesma do `FULL OUTER JOIN`. Sendo:

- R(nome, id, dep)
- S(id_dept, nome_dept)

REL <- R ⋃* <dep = id_dept> S gera a seguinte relação:

> REL(nome, id, dep, nome_dept)

Onde, assim como no [`FULL OUTER JOIN`](#outer-join), as tuplas que não tinham par são associadas a valores *NULL*.
