---
title: Introdução
---

## Sumário

- [Processadores de Linguagens](#processadores-de-linguagens)
  - [Compiladores](#compiladores)
  - [Interpretadores](#interpretadores)
  - [Híbridos](#hibridos)
  - *[JITs](jits)*
- [Tarefas do Compilador](#tarefas-do-compilador)
- [Fases do Compilador](#fases-do-compilador)
  - [Análise Léxica](#analise-lexica)
  - [Análise Sintática](#analise-sintatica)
  - [Análise Semântica](#analise-semantica)
  - [Geração de Código Intermediário](#geracao-de-codigo-intermediario)
  - [Geração de Código Objeto](#geracao-de-codigo-objeto)
  - [Otimização de Código Independente/Dependente de Máquina](#otimizacao-de-codigo-independente-dependente-de-maquina)
- [Desenvolvimento de Compiladores](#desenvolvimento-de-compiladores)

## Processadores de Linguagens

#### Compiladores

Os compiladores são *softwares* utilizados para realizar a tradução de programas entre linguagens diferentes. Essa tradução é, portanto, uma transformação de uma linguagem de programação (chamada de linguagem fonte) para uma linguagem em que o programa pode ser executado (chamada de linguagem destino).

#### Interpretadores

Os interpretadores são um outro tipo de processador de linguagem, diferindo dos compiladores por não produzirem um programa em linguagem destino. Ao invés disso, processam diretamente as operações no programa-fonte. Enquanto o uso de compilação garante que a execução dos programas seja rápida e sem a necessidade de máquina virtual acompanhando o código executável, a interpretação facilita muito o processo de depuração.

#### Híbridos

Para usufruir das vantagens dos compiladores e dos interpretadores, é interessante utilizar híbridos. Numa abordagem híbrida, o programa-fonte é compilado para um programa intermediário e este, por sua vez, passa por um interpretador. Em Java, o *bytecode* é o programa intermediário e a *JVM* é o interpretador de código intermediário.

#### *JITs*

Os compiladores *Just-In-Time* (*JITs*) são semelhantes aos de abordagem híbrida, porém não há interpretação de código intermediário, pois ele é compilado diretamente para código de máquina durante a execução. Além disso, as tarefas mais custosas são realizadas durante a compilação para código intermediário, garantindo que os JITs mantenham um desempenho muito superior aos interpretadores clássicos.

## Tarefas do Compilador

As tarefas de um compilador podem ser divididas em 2 etapas: análise e síntese. Na etapa de **análise**, o programa-fonte é dividido em pedaços e o compilador lhe impõe uma estrutura gramatical a partir da qual será criada uma representação intermediária. Também é nessa etapa que se produz a tabela de símbolos e se detecta erros léxicos, sintáticos e semânticos. Já na etapa de **síntese**, o programa destino é construído a partir da representação intermediária e da tabela de símbolos.

A **tabela de símbolos** é uma estrutura de dados que permite o armazenamento de informações sobre as entidades do programa-fonte. Para cada uma das entidades (como variáveis e métodos), haverá um registro na tabela contendo um identificador único e uma série de informações necessárias para as operações do compilador.

Se algum **erro** for detectado no programa-fonte durante esse processo, reportá-lo adequadamente para o usuário também é responsabilidade do compilador. Além disso, outros *softwares* (como pré-processador e o montador) podem ser necessários para a compilação, por isso, diversos compiladores são projetados com esses *softwares* "anexados".

## Fases do Compilador

A tabela abaixo descreve resumidamente as fases de um compilador, suas entradas e suas saídas. Costuma-se dizer que as fases de 1 a 4 (inclusive) constituem o *frontend*, enquanto as demais constituem o *backend* do compilador.

| N | Nome | Entrada | Saída | Opcional? |
| :--: | :--: | :--: | :--: | :--: |
| 1 | Análise Léxica | Fluxo de Caracteres | Fluxo de Tokens | Não |
| 2 | Análise Sintática | Fluxo de Tokens | Árvore Sintática | Não |
| 3 | Análise Semântica | Árvore Sintática | Árvore Sintática | Não |
| 4 | Geração de Código Intermediário | Árvore Sintática | Representação Intermediária | Não |
| 5 | Otimização de Código Independente de Máquina | Representação Intermediária | Representação Intermediária | Sim |
| 6 | Geração de Código Objeto | Representação Intermediária | Código de Máquina Destino | Não |
| 7 | Otimização de Código Dependente de Máquina | Código de Máquina Destino | Código de Máquina Destino | Sim |

#### Análise Léxica

A análise léxica é a primeira fase de um compilador, sendo responsável por converter o fluxo de caracteres do programa-fonte em um fluxo de *tokens*. A produção de um *token* ocorre a partir de agrupamentos de sequências significativas de caracteres (chamadas de **lexemas**). Diz-se que uma sequência de caracteres constitui um *lexema* se ela segue um **padrão** pré-estabelecido pelo compilador. Assim, cada *token* é um par de valores na forma `<padrão, lexema>`.

Quando o *lexema* e o padrão são idênticos, é possível representar o *token* apenas como `<padrão>`. Além disso, se o padrão for `id`, o *lexema* do *token* será um apontador para a tabela de símbolos.

#### Análise Sintática

A análise sintática é responsável por produzir, a partir dos *tokens*, uma estrutura de dados semelhante a uma árvore. Essa árvore é capaz de descrever a estrutura gramatical dos *tokens*, tal que seus nós são operações cujos argumentos são os nós-filhos. 

#### Análise Semântica

A análise semântica é responsável por verificar a consistência semântica do programa-fonte, utilizando a árvore sintática e a tabela de símbolos para  essa tarefa. Também é nessa fase que são realizadas checagens adicionais, como a checagem de tipos (com coerção, quando possível).

#### Geração de Código Intermediário

O gerador de código intermediário é responsável pela produção de uma representação intermediária para o programa-fonte. Idealmente, essa representação deve ser fácil de produzir, mas também de traduzir para código objeto.

#### Geração de Código Objeto

O gerador de código objeto é responsável por mapear a representação intermediária para código na linguagem destino. Se a linguagem destino for código de máquina, essa fase pode tornar-se responsável por atribuições bem específicas, como a seleção de registradores para alocar variáveis do código.

#### Otimização de Código Independente/Dependente de Máquina

As fases de otimização de código são opcionais e ocorrem logo após as fases de geração de código. As maneiras de implementar essas otimizações variam bastante, porém, sempre consomem muito tempo do compilador e buscam melhorar a eficiência do código em termos de velocidade, espaço e uso de CPU. A otimização independente de máquina visa o código intermediário, enquanto a dependente de máquina visa o código objeto. 

## Desenvolvimento de Compiladores

O processo de desenvolvimento de compiladores envolve o uso de ferramentas de desenvolvimento comuns (como *IDEs*) e específicas (como o *LEX*), devendo acompanhar tanto a evolução das linguagens de programação, quanto das arquiteturas de computadores. Além disso, atualmente há uma tendência de utilização de linguagens de domínio específico (*Domain-Specific Languages* ou *DSLs*).
