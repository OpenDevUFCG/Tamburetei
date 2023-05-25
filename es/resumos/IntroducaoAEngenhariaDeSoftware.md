# Introdução a Engenharia de Software

# Crise de Software

- Ocorre por volta dos anos 60
- Dificuldades em produzir sistemas de larga escala / complexos
- Alta complexidade
- Falta de técnicas
- Alta demanda de software
    - Fora do prazo
    - Custo alto
    - Sem qualidade
- Conferência Internacional de Engenharia de Software (anos 70) para criação de uma abordagem sobre a ES
- A partir dessa conferência, foram realizadas mais e mais, gerando mais conhecimento sobre a Engenharia de Software.

# Margaret Hamilton

## A ****Mãe da Engenharia de Software****

- Quando trabalhou no projeto da Apollo 11, percebeu uma grande interseção entre a parte de Hardware e a parte de Software, o que a fez perceber a necessidade de uma nova área.
- Liderou a Engenharia de Software no projeto Apollo

# Importância

- Os conceitos da Engenharia de Software impactam na redução de bugs que podem acarretar problemas de diversas áreas na sociedade;

## Therac 25

- Máquina de Radioterapia controlada por computador (1985-1987)
    - 6 acidentes (5 mortes)
    - Overdose de radiação
- Por que isso aconteceu?
    - Falta de verificação (Quase não foram realizados testes)
    - Falta de documentação (Dificuldade de manter / evoluir software com isso)
    - Códigos de erro incompreensíveis

### [Outros bugs que tiveram sérias consequências](https://www.tecmundo.com.br/tecnologia/49572-bugs-10-falhas-de-computadores-que-causaram-muito-prejuizo-e-confusao.htm)

# Engenharia de Software

- Disciplina gerencial e tecnológica que lida com a produção e manutenção sistemática de **produtos de software** desenvolvidos dentro de estimativas de **custo** e de **tempo**;

## Engenheiro de Software

- Deve adotar uma abordagem sistemática e organizada em seu trabalho e usar técnicas e ferramentas apropriadas dependendo do problema a ser resolvido, de acordo com as restrições de desenvolvimento e os recursos disponíveis.

## Objetivo

- Software dentro do custo e prazo e com qualidade!

## Modelo do Processo de Desenvolvimento de Software

1. Requisitos
    - Coletar funcionalidades
2. Design
    - Detalhar modelos dos requisitos
3. Implementação
4. Validação
5. Evolução

# Planejamento e Gerenciamento

- Pessoas
    - Motivação
    - Alocação
- Processo
    - Qualidade (Métricas)
    - Melhoria

## Planejamento

### Análise de Riscos

- Mudança de pessoas
- Mudança de requisitos
- Dependência
- Hardware
- Ferramentas CASE

### Estimar

- Custo
- Tempo

# Requisitos

## O que são?

- Serviços que o sistema deve fornecer e restrições à operação do mesmo

## Classificação

- Funcional
    - Creditar, Debitar
- Não Funcional
    - Performance, Segurança

## Dificuldades

- O cliente não sabe o que ele realmente deseja!
- Problemas na comunicação
- Mudança constante de requisitos

-> Por conta disso, é necessário definir bem o escopo.

## Engenharia de Requisitos

- Identificação, especificação e descrição dos requisitos do sistema de software

# Etapas do Desenvolvimento de um Software

## Modelagem

- É a 1ª fase do projeto
- Instrumento para o entendimento e comunicação do produto final que será desenvolvido.
- Problema
    - simplicidade (favorece a comunicação)
    - complexidade (favorece a precisão) do modelo

## Implementação

- É a 2ª fase do projeto
- Segue o design proposto
    - Que paradigma e linguagem de programação
    usar?
    - A mesma para todas os contextos?
        - Sistema Operacional
        - Sistema em tempo real
        - Locadora de DVD

### CASE tool

- Computer-Aided Software Engineering (Engenharia de software assistida por computador)
- Compilar, Depurar...

## Validação e Verificação

- É a 3ª fase do projeto
- Testes
    - Como fazer?
    - Que tipo de teste fazer?
    - Unidade
    - Integração
    - Validação, ...
- Métodos formais
    - Prova de Teoremas
    - Verificação de Modelos

## Evolução

- É a 4ª fase do projeto
1. Responsável por incluir novos requisitos (Evolução Aditiva)
    - Novos dispositivos móveis
2. Corrigir erros (Evolução Defectiva)
3. Preparar o programa para mudanças (Evolução Perfectiva)
    - Refatoramentos
- Fase mais custosa do ciclo de vida de software