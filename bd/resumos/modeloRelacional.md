---
title: Modelo Relacional
---

## Sumário

- [Modelo Relacional](#modelo-relacional)
  - [Sumário](#sum%C3%A1rio)
  - [Conceitos Iniciais](#conceitos-iniciais)
    - [Chave](#chave)
  - [Definições Formais](#defini%C3%A7%C3%B5es-formais)
    - [Esquema](#esquema)
    - [Tupla](#tupla)
    - [Estado da Relação](#estado-da-rela%C3%A7%C3%A3o)
  - [Constraints](#constraints)
    - [Integridade Relacional](#integridade-relacional)
      - [Restrição de Chave](#restri%C3%A7%C3%A3o-de-chave)
        - [Super Key](#super-key)
        - [Key](#key)
        - [Primary Key](#primary-key)
      - [Restrição de Integridade de Entidade](#restri%C3%A7%C3%A3o-de-integridade-de-entidade)
      - [Restrição de Integridade Referencial](#restri%C3%A7%C3%A3o-de-integridade-referencial)
      - [Restrição de Domínio](#restri%C3%A7%C3%A3o-de-dom%C3%ADnio)
  - [Esquema de BD Relacional](#esquema-de-bd-relacional)
  - [Estado de BD Relacional](#estado-de-bd-relacional)
  

## Conceitos Iniciais

O modelo de dados Relacional se baseia no conceito de **relação**, originário dos *conjuntos* da matemática. Uma relação se assemelha a uma tabela de valores, tal que cada linha representa uma entidade do mundo real e as colunas são seus atributos. Por exemplo:

**Aluno**

**Nome** | **CPF** | **Idade** | **Endereço** |
--- | --- | --- | --- |
Maria | 123.345.678-92 | 23 | R. José de Franco, 12 |
José | 921.432.432-22 | 22 | R. Maria de Franco, 14 |
Mario | 131.432.987-44 | 14 | R. Maria de José, 91 |

Na tabela acima, *Aluno* é o nome da relação, as linhas representam cada aluno existente e as colunas representam os atributos desses alunos.

### Chave

Um valor que identifica unicamente cada linha (entidade). Nota-se que na relação *Aluno*, uma possível chave é o CPF dos alunos, já que seu valor é sempre único.

**Termo Formal** | **Termo Informal** |
--- | --- |
Relação | Tabela |
Tupla | Linha |
Atributo | Cabeçalho da coluna |
Domínio | Todos os valores possiveis da coluna |
Esquema | Definição da tabela |
Estado da relação | Povoamento de uma tabela |

## Definições Formais

A seguir, estão algumas definições formais que podem diferir do contexto prático.

### Esquema

As relações são descritas através de esquemas. Em `R(A1, A2, A3..., An)`, *R* é o nome da relação e *An* são os atributos dessa relação. Por exemplo, `ALUNO(Nome, CPF, Idade, Endereço)`.

Também é possível definir um domínio para cada atributo, ou seja, o conjunto de valores permitidos para um dado. Como exemplo, tem-se `dom(Nome) = varchar(25)`.

### Tupla

Na matemática, uma tupla é um conjunto ordenado de valores representado por `<...>`. Formalmente, as linhas de uma relação são um conjunto de tuplas. Como exemplo, tem-se: `<"Maria", "123.345.678-92", 23 , "R. José de Franco, 12">`.

### Estado da Relação

É uma "fotografia" atual do banco de dados, ou seja, o conjunto de dados que se tem no instante atual. Inicialmente tem-se um estado vazio. Após popular o banco de dados, tem-se um outro estado. Consequentemente, a cada atualização há um novo estado da relação, que é representado como um conjunto de tuplas na forma `r(R) ⊂ dom(A1) X dom(A2) X .... X dom(An)`.

`r(R) = {t1, t2, ..., tn}` onde *ti* é uma n-tupla.
`ti = <v1, v2, ..., vn>` onde cada vj ∈ dom(Aj).

## Retrições (*Constraints*)

As restrições (*constraints*) são utilizadas para determinar quais valores serão (ou não) permitidos no banco de dados. Entre os principais tipos de *constraints* estão:

1. **Restrições inerentes ou implícitas**: Impostas pela própria natureza do modelo de dados. Por exemplo, tuplas iguais não são permitidas em um estado de uma relação.
2. **Restrições baseadas no esquema ou explícitas**: Definidas no esquema. Por exemplo, a cardinalidade máxima de uma relação entre entidades, como "o aluno só pode ter um curso".
3. **Restrições baseadas na aplicação ou semânticas**: Normalmente são especificadas no nível mais alto (na aplicação).

### Integridade Relacional

Existem quatro tipos principais de restrições baseadas no esquema e que devem ser verificadas em todos os estados válidos de uma relação.

#### Restrição de Chave

Por definição, todas as tuplas (linhas) são distintas, ou seja, não podem existir tuplas na relação cujos os valores são **todos** iguais aos de outra tupla. Usualmente, existe um conjunto de valores com a propriedade de que não serão repetidos entre diferentes tuplas. Suponha que esses atributos sejam listados e que o conjunto resultante seja chamado de **super-chave** (*superkey* ou *SK*), tem-se então a propriedade `t1[SK] != t2[SK]` para quaisquer tuplas `t1` e `t2` da relação.

##### *Super Key*

Qualquer conjunto de atributos que seja capaz de identificar unicamente todas as tuplas da relação é chamado de *super key*. Toda relação tem pelo menos uma *SK*. Note que a *SK* pode incluir atributos redudantes ou inúteis para identificar unicamente cada tupla.

##### Key

A *key* é a *superkey* mínima, ou seja, se removido qualquer um de seus atributos, perde-se a capacidade de identificar unicamente as tuplas.

> Uma key é uma superkey, mas não necessariamente o contrário.

##### Primary Key

Perceba que, em uma relação, pode-se escolher mais de uma *key*. Esse conjunto é chamado de chaves candidatas (*candidate keys*). A *key* escolhida para identificar cada tupla da relação é chamada de chave primária (*primary key* ou *PK*).

#### Restrição de Integridade de Entidade

Os atributos que formam a *primary key* não podem ser **NULL** para qualquer tupla em `r(R)`. Enquanto isso, outros valores podem conter essa mesma restrição sem serem *primary key*.

#### Restrição de Integridade Referencial

Para as restrições que envolvem duas relações, devem existir atributos que formem a chave estrangeira (*foreign key* ou *FK*). Tendo uma relação que *referencia* e uma *referenciada*, uma terá um atributo *FK* que será o valor *PK* da outra. 

#### Restrição de Domínio

Cada valor de uma tupla deve ser do domínio do seu atributo ou **NULL**, se permitido.

## Esquema de BD Relacional

Um conjunto *S* de esquemas de relação que pertencem ao banco. Por exemplo, `S  = {R1, R2,...., Rn} + IC` onde *S* é o nome do banco de dados, *R* são os esquemas individuais e *IC* são o conjunto de restrições de integridade.

## Estado de BD Relacional

Um estado de um banco de dados relacional pode ser visto como uma instância ou fotografia do banco de dados inteiro, considerando todas suas relações e restrições. Por exemplo, `BD = {r1, r2,...., rm}` tal que cada *ri* é um estado de *Ri*. Um estado que não satisfaz as restrições é dito inválido.

