# Modelo Relacional

## Sumário
- [Modelo Relacional](#modelo-relacional)
  - [Sumário](#sum%C3%A1rio)
  - [Conceitos Iniciais](#conceitos-iniciais)
    - [Chave](#chave)
  - [Definições Formais](#defini%C3%A7%C3%B5es-formais)
    - [Esquema](#esquema)
    - [Tupla](#tupla)
    - [Estado da relação](#estado-da-rela%C3%A7%C3%A3o)
  - [Constraints](#constraints)
    - [Integridade Relacional](#integridade-relacional)
      - [Restrição de Chave](#restri%C3%A7%C3%A3o-de-chave)
        - [Super Key](#super-key)
      - [Key](#key)
      - [Primary Key](#primary-key)
      - [Restrição de Integridade de Entidade](#restri%C3%A7%C3%A3o-de-integridade-de-entidade)
      - [Restrição de Integridade Referencial](#restri%C3%A7%C3%A3o-de-integridade-referencial)
      - [Restrição de domínio](#restri%C3%A7%C3%A3o-de-dom%C3%ADnio)
  - [Esquema de BD Relacional](#esquema-de-bd-relacional)
  - [Estado de BD Relacional](#estado-de-bd-relacional)
  

## Conceitos Iniciais

O modelo de dados Relacional se baseia no conceito de **relação** que é baseada na ideia de *conjuntos* da matemática. Uma relação se assemelha a uma tabela de valores, cada linha representa uma entidade do mundo real e as colunas são os atributos.

Exemplo:

**Aluno**

**Nome** | **CPF** | **Idade** | **Endereço**
--- | --- | --- | --- 
Maria | 123.345.678-92 | 23 | R. José de Franco, 12
José | 921.432.432-22 | 22 | R. Maria de Franco, 14
Mario | 131.432.987-44 | 14 | R. Maria de José, 91

Na tabela acima, *Aluno* é o nome da relação, as linhas são cada aluno e os valores dos atributos e as colunas são os atributos.

### Chave

Um valor que identifica unicamente cada linha(entidade). Podemos ver que na relação *Aluno* da primeira tabela, a chave pode ser o CPF já que ele é único sempre.

**Termo Formal** | **Termo Informal**
--- | ---
Relação | Tabela
Tupla | Linha
Atributo | Cabeçalho da coluna
Domínio | Todos os valores possiveis da coluna
Esquema | Definição da tabela
Estado da relação | Povoamento de uma tabela

## Definições Formais

Vamos mostrar algumas definições formais, que podem se diferenciar na prática.

### Esquema

Descrevemos as relações através de esquemas, da seguinte forma:

`R(A1, A2, A3..., An)` *R* é o nome da relação, e *An* são os atributos. Exemplo: `ALUNO(Nome, CPF, Idade, Endereço)`.

Também podemos definir um domínio para cada atributo, que será o conjunto de valores permitidos para um dado. Tendo a descrição do tipo e outra do formato. Exemplo: `dom(Nome) = varchar(25)`.

### Tupla

Tupla na matemática, é um conjunto ordenado de valores representado por `<...>`. Formalmente, as linhas de uma relação são um conjunto de tuplas. Exemplo:

`<"Maria", "123.345.678-92", 23 , "R. José de Franco, 12">`

### Estado da relação

É uma fotografia atual do banco de dados, sendo o conjunto de dados que temos agora. No início temos um estado vazio, ao popularmos o banco, temos um outro estado e assim toda vez que atualizamos. Sendo assim visto como um conjunto de tuplas, representado por `r(R) ⊂ dom (A1) X dom (A2) X ....X dom(An)`.

`r(R) = {t1, t2, ..., tn}` onde *ti* é uma n-tupla.

`ti = <v1, v2, ..., vn>` onde cada vj ∈ dom(Aj)

## Constraints

Constraints(Restrições) servem para determinar quais valores são permitidos e quais não em um banco de dados. Principais tipos:

1. **Restrições inerentes ou implícitas**: Impostas pela própria natureza do modelo de dados(ex: tuplas iguais não são permitidas em um estado de uma relação)
2. **Restrições baseadas no esquema ou explícitas**: Definidas no esquema(Ex: Cardinalidade máxima de uma relação entre entidades: aluno só pode ter um curso)
3. **Restrições baseadas na aplicação ou semânticas**: Normalmente são especificadas no nível mais alto, na aplicação

### Integridade Relacional

Existem quatro tipos principais de restrições baseadas no esquema e que devem ser verificadas em todos os estados válidos de uma relação:

#### Restrição de Chave

Por definição, todas as tuplas(linhas) são distintas, ou seja, não pode existir linhas na tabela que *todos* os valores são iguais a outra linha. Usualmente, existe um conjunto de valores que tem a propriedade que nenhuma tupla vai ter valores iguais para estes. Suponha que listemos esse atributos e os chamemos de **SK**, ele terá essa propriedade:

`t1[SK] != t2[SK]` para qualquer tupla da relação.

##### Super Key
Qualquer conjunto de atributos SK que possa identificar unicamente todas as tuplas da relação é chamado de *Super Key*, toda relação tem pelo menos uma *SK*. Note que a *SK* podem ter valores redudantes ou inúteis para identificar unicamente cada linha.

#### Key
A *Key* é uma *Super Key* mínima, ou seja, se removemos qualquer atributo dela, ela deixa de identificar a tupla unicamente.

> Uma key é uma super key, mas não necessariamente o contrário.

#### Primary Key
Perceba que uma relação pode-se escolher mais de uma *key*, estas são chamadas de *candidates keys*. A *key* escolhida para identificar cada tupla da relação, é chamada de *primary key*. Também chamada de **PK**.

#### Restrição de Integridade de Entidade
Os atributos que formam a *Primary Key* não podem ser **NULL** para qualquer tupla em `r(R)`. Outros valores também podem conter essa restrição, sem serem *Primary Key*.

#### Restrição de Integridade Referencial

Restrição que envolvem duas relações, estas possuem atributos *FK*. Tendo uma relação que *referencia* e uma *referenciada*, uma terá um atributo *FK* que será o valor *PK* da outra. 

#### Restrição de domínio
Cada valor de uma tupla deve ser do domínio do seu atributo ou **NULL* se for permitido.

## Esquema de BD Relacional
Um conjunto *S* de esquemas de relação que pertencem ao banco

`S  = {R1, R2,...., Rn} + IC`. S é o nome do banco de dados, *R* são os esquemas individuais e *IC* são os conjuntos de restrições de integridade.
## Estado de BD Relacional

Um estado de um banco de dados relacional pode ser visto como uma instância ou fotografia do banco de dados inteiro, considerando todas suas relações e restrições.

`BD = {r1, r2,...., rm}` tal que cada ri é um estado de Ri. Um estado que não satisfaz as restrições, é *inválido*.

