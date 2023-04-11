# Cálculo Relacional
*Seções 8.6 - 8.7 - Fundamentals of DataBase Systems 7th edition.*

## ìndice
- [Introdução](#introdução)
- [Cálculo Relacional de Tuplas](#cálculo-relacional-de-tuplas)
    - [Expressões e fórmulas](#Expressões-e-fórmulas)
    - [Quantificadores Universais e existenciais](#quantificadores)
- [Cálculo Relacional de domínio](#Cálculo-relacional-de-domínio)
    - [Expressões e fórmulas](#outras-expressões-e-fórmulas)
---
## Introdução

### Cálculo relacional vs Álgebra relacional:

| Cálculo Relacional | Álgebra Relacional |
| ---                | ---                |
| Não-procedimental  | Procedimental      |
| Poder de expressão | Poder de expressão |

- **Linguagens não-procedimentais:** São linguagens que possuem expressões apenas `declarativas`, ou seja, expressões que focam apenas em informar qual o resultado esperado da requisição e não como que essa requisição deve acontecer. A álgebra relacional por ser uma `procedimental` especifica uma *sequência* na qual as operações devem ser realizadas.

- **Poder de expressão:** O poder de expressão é o universo de todos os tipos de requisições que podem ser realizados pela linguagem. O cálculo e álgebra relacionais possuem o **mesmo** Poder de expressão.

O cálculo relacional é a `base da Lógica Matemática` das linguagens de consulta como SQL, dessa maneira, linguagens que realiza quaisquer requisições que o cálculo relacional consegue fazer é chamada de **Linguagem Relacionalmente Completa**. 

> **OBS:** Como foi dito anteriormente, o Cálculo Relacional é a *base*, dessa forma, existem linguagens que possuem um `poder de expressão` ainda maior do que o cálculo relacional.

Existem dois tipos de cálculos relacionais, o `cálculo relacional de tuplas` e o `cálculo relacional de Domínio`:

---
## Cálculo Relacional de tuplas

O cálculo relacional de tuplas se baseia em especificar *variáveis*, que são tuplas de uma relação, onde a variável pode assumir qualquer valor da `amplitude relacional`, ou seja, ela pode assumir a forma de qualquer tupla da relação em que ela se encontra. 

A resposta da requisição é um conjunto de tuplas que `satisfazem` a condição imposta, ou seja, tuplas que sob a condição previamente determinada resultam no valor booleano TRUE.

### **Expressões e fórmulas**

Toda expressão do cálculo relacional de tuplas é estruturada da seguinte forma:

```
{T.A1, T.A2...T.An | Cond(T)}
```

Onde:
- `T` Variável T que assume a forma de todas as tuplas da relação;
- `A1, A2 e An` são os atributos de T1 e T2, respectivamente, que serão retornados como resposta
- `Cond(T)` é a condição envolvendo T que será julgada como verdadeira ou falsa.

A condição (Cond(T)) pode ser de três tipos:

- **R(T):** tuplas T que pertencerem a `amplitude relacional` de R serão avaliadas com *TRUE*, caso contrário como *FALSE*.

    **Ex:** Retornar nome e matrícula de pessoas que são estudantes.
    ```
    {p.name, p.matricula | ESTUDANTE(p)} 
    ```
- **t1.A oc t2.B:** Sendo "oc" um `operador de comparação`{=, <, ≤, >, ≥, ≠}. Essa condição retorna *TRUE* caso os dois atributos (A e B) satisfaçam a expressão, caso contrário, o valor *FALSE* é retornado.

    **Ex:** ID dos empregados que recebem mais do que 50000 reais.
    ```
    {e.id | EMPREGADO(e) AND e.salario > 50000}
    ```
- **t1.A oc const. *OR* const. oc t2.B:** Sendo "oc" um `operador de comparação`{=, <, ≤, >, ≥, ≠}. Essa condição retorna *TRUE* caso algum dos dois atributos (A ou B) satisfaçam a expressão, caso contrário, o valor *FALSE* é retornado.

    **Ex:** ID dos empregados que recebem mais de 30000 reais ou menos de 1000 reais.
    ```
    {e.id | EMPREGADO(e) AND (e.salario > 30000 OR e.salario < 1000)}
    ```

#### Exemplos:

Para os próximos exemplos considere a seguinte relação:

FUNCIONÁRIO
| Nome    | Id  | Dept | Salário |
| ---     | --- | ---  | ---     |
| Rodrigo | 3   | 1    | 5000    |
| Leandra | 2   | 1    | 5000    |
| Matheus | 4   | 1    | 7000    |
| Ana     | 1   | 4    | 3000    |
| Carolyn | 0   | 2    | 10000   |

#### Exemplo 01

Retornar o nome e id de todos os funcionários que trabalham no departamento 1.
```
    FUNC_DEPT1 <- {f.Nome, f.Id | FUNCIONÁRIO(f) AND Dept = 1}
```

FUNC_DEPT1
| Nome    | Id  | Dept | Salário |
| ---     | --- | ---  | ---     |
| Rodrigo | 3   | 1    | 5000    |
| Leandra | 2   | 1    | 5000    |
| Matheus | 4   | 1    | 7000    |

#### Exemplo 02

Retornar o id e salário dos funcionários que recebem 5 mil ou 7 mil reais.
```
    SAL <- {f.Id, f.Salário | FUNCIONÁRIO(f) AND (f.Salário = 5000 OR f.Salário = 7000)}
```

SAL
| Nome    | Id  | Dept | Salário |
| ---     | --- | ---  | ---     |
| Rodrigo | 3   | 1    | 5000    |
| Leandra | 2   | 1    | 5000    |
| Carolyn | 0   | 2    | 10000   |

---
### **Quantificadores**

Existem dois tipos de quantificadores:

- **Quantificador universal (∀t):** Em uma fórmula F, (∀t)(F) significa que a fórmula precisa ser verdade para **TODAS** as tuplas para que ela seja avaliada como *TRUE*, caso exista pelo menos uma tupla que não se encaixe ela é avaliada como *FALSE*.

- **Quantificador existencial(∃t):** Em uma fórmula F, (∃t)(F) é avaliado como *TRUE* caso existe pelo menos uma tupla que satisfaça a fórmula, caso contrário, ela é avaliada como *FALSE*.

E quando falamos de quantificadores nós podemos falar de dois tipos de variáveis:

- **Variáveis livres:** São variáveis que não estão atreladas a nenhum quantificador;
- **Variáveis ligadas:** São as variáveis que são atreladas a um quantificador.

#### Exemplos:
Para os próximos exemplos considere as seguintes relações:

PROFESSOR
| Nome      | id  | id_disciplina | 
| ---       | --- | ---           |
| Tiago     | 45  | 101           |
| Dalton    | 43  | 105           |
| Joseana   | 63  | 103           |
| Elmar     | 20  | 103           |
| Patrícia  | 64  | 102           |

DISCIPLINA
| Nome    | id  | andar | 
| ---     | --- | ---   |
| Lógica  | 101 | 1     |
| Grafos  | 102 | 2     |
| LOAC    | 103 | 1     |
| Cálculo | 104 | 4     |
| PSoft   | 105 | 2     |

#### Exemplo 01

Nome e id de todos os professores que lecionam em uma disciplinas do andar 2
```
    PROFS_ANDAR2 <- {t.name, t.id | PROFESSOR(t) AND (∃w)(DISCIPLINA(w) AND t.id_disciplina = w.id AND w.andar = 2)}
    
    ou

    PROFS_ANDAR2 <- {t.name, t.id | PROFESSOR(t) AND (NOT (∀w)(NOT(DISCIPLINA(w)) OR NOT(t.id_disciplina = w.id) OR 
    NOT(w.andar=2))}
```
> t é uma variável `livre` e w é uma variável `ligada`.

PROFS_ANDAR2
| Nome      | id  | 
| ---       | --- |
| Dalton    | 43  |
| Patrícia  | 64  |

#### Exemplo 02 

Nome e id da disciplina que não possui professor

```
    DISCIPLINAS_SEM_PROF <- {d.Nome, d.id | DISCIPLINA(d) AND (NOT (∃p)(PROFESSOR(p) AND w.id = p.id_disciplina))}

    ou 

    DISCIPLINAS_SEM_PROF <- {d.Nome, d.id | DISCIPLINA(d) AND (∀p)(NOT(PROFESSOR(p)) OR NOT(w.id = p.id_disciplina))}
```

DISCIPLINAS_SEM_PROF
| Nome    | id  | 
| ---     | --- |
| Cálculo | 104 |

---
## Cálculo relacional de domínio

A diferença principal desse cálculo relacional para o de tuplas é o tipo de variável. No cálculo relacional de domínio as variáveis, agora chamadas de `variáveis de domínio`, são os **atributos**.


### Outras expressões e fórmulas
As fórmulas do Cálculo relacional de domínio se estruturam da seguinte forma:
```
    {x1, x2, ... , xn | Cond(x1, x2, ..., xn, xn+1, xn+2, xn+m )}
```

Onde:
- **x1...xn+m:** São os variáveis de domínio;
- **Cond:** Condição que envolvem os atributos e que serão avaliadas como *TRUE* ou *FALSE*.

Assim como no cálculo relacional de tuplas, a *Cond* pode ser de 3 tipos:

- **R(x1, x2, ..., xj):** Sendo R o nome da relação de grau j e (x1, x2, ... , xj) `todos` os atributos de R. Essa condição implica que cada uma dessas variáveis de domínio representa algum dos atributos da relação R.

    **Ex:** Retornar o nome e id de todas as pessoas que pertencem a relação EMPLOYEE.
    ```
        {v, u | EMPLOYEE(vumnop)}
    ```

- **x1 oc x2:** Sendo oc um `operador de comparação`, essa condição compara duas variáveis de domínio(atributos).

    **Ex:** Retornar nome e id de todos os empregados que ganham mais de 50000 reais.
    ```
        {v, u | EMPLOYEE(vumnop) AND p > 50000}
    ```

- **x1 oc k *OR* k oc x2:** Sendo oc um `operador de comparação` e k uma `constante` qualquer, essa condição compara duas variáveis de domínio com uma constante.

    **Ex:** Retornar o nome e id de todos os funcionários que ganham mais de 4000 reais ou menos de 1000 reais.
    ```
        {v, u | (∃m)(∃n)(∃o)(∃p) ∃EMPLOYEE(vumnop) AND (p > 4000 OR p < 1000)}
    ```

#### Exemplos:

Para os seguintes exemplos considere as seguintes relações:

PIZZA
| Sabor               | preço | Tamanho |
| ---                 | ---   | ---     |
| Frango com catupiry | 59,90 | GG      |
| Pepperoni           | 49,90 | M       |
| Aliche              | 39,90 | M       |
| Brigadeiro          | 59,90 | GG      |
| Quatro queijos      | 59,90 | GG      |

#### Exemplo 01

Quero o nome de todas as pizzas que tenham o tamanho GG!

```
    GULOSO <- {s | PIZZA(spt) AND t = GG}
```

GULOSO
| s                   |
| ---                 |
| Frango com catupiry |
| Brigadeiro          |
| Quatro queijos      |

#### Exemplo 02 

Quero o nome e preço de todas as pizzas que sejam com o preço limite de 50 reais.

```
    PRECO_LIMITADO <- {s, b | PIZZA(spt) AND p < 50}
```
PRECO_LIMTIADO
| s                   | b     |
| ---                 | ---   |
| Pepperoni           | 49,90 |
| Aliche              | 39,90 |
