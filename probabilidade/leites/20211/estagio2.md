---
title: Prova 2º estagio
---

- **Disciplina:** Introdução à Probabilidade
- **Período:** 2021.1

## Aviso!

1. O periodo 2021.1 foi efetuado de forma remota por causa disso as provas da disciplina de probabilidade foram efetuadas pelo PVAE, dessa forma as questões aqui presentes foram apenas algumas das que podiam ser sorteadas entre os alunos.

## Questões


<br>**Questão 1**
    
Um pesquisador estudou o comportamento de consumo de bebidas lácteas no Brasil. Analisou alguns consumidores quanto à classe econômica (alta, média ou baixa) e ao principal aspecto determinante na escolha da marca (valor ou qualidade). Os dados obtidos estão na tabela a seguir.  

- | **Alta** | **Média**  | **Baixa** |
:---: | :---:| :---: | :---: |
Valor | 90 | 75 | 150
Quantidade | 100 | 50 | 80
    
Qual a probabilidade de um consumidor escolhido ao acaso
    
 **(a) ser da classe alta?**
        
Ω = 515, Classe Alta = 190
        
$P({Classe Alta \above{1pt}{Ω}}) = ({190 \above {1pt}{515}})$ = 
        
$P ≅ 0,37$
        
    
<br>**(b) priorizar o valor da mercadoria e ser da classe alta?**

Ω = 515, Valor da Mercardoria ∩ Classe Alta = 90
        
$P({Valor da Mercardoria ∩ Classe Alta \above{1pt}{Ω}}) = ({90 \above {1pt}{515}})$
        
$P ≅ 0,17$

<br>**(c) ser da classe média ou priorizar a qualidade da mercadoria?**
  
Ω = 515, Classe Média = 125, Qualidade da mercadoria = 200
        
$P({Classe Média ∪ Qualidade da Mercadoria\above{1pt}{Ω}})$ 
        
= ${P(ClasseMedia) + P(Qualidade) - P(ClasseMedia ∩Qualidade)  \above{1pt}{Ω}}$
        
= ${P(125) + P(200) - P(50) \above{1pt}{515}}$
        
= ${275 \above{1pt}{515}}$ ≅ $0,53$
        
    
<br>**(d) ser da classe baixa dado que priorizou o valor da mercadoria?)**

Ω = 515, Classe Baixa = 200, Valor da mercadoria = 315

$P(ClasseBaixa |ValorDaMercadoria)=$\
$= P{ClasseBaixa ∩ ValorDaMercadoria \above{1pt}{ValorDaMercadoria }}$
$= P{150 \above{1pt}{315 }} ≅ 0,48$
        
<br>**Questão 2**
    
A probabilidade de que uma empresa norte-americana seja localizada em Xangai, na China, é de 0,4; a probabilidade de que seja localizada em Pequim, na China, é de 0,3; e a probabilidade de que seja localizada em nenhuma dessas cidades é de 0,4. Qual a probabilidade de que a empresa seja localizada
    
**(a)** em ambas as cidades? 

- Temos que: 
  - Xangai: 0,4 ; Pequim: 0,3 ; Nenhuma das cidades: 0,4

    $P(X∩P)=0,4-0,3 = 0,1$

    
**(b)** apenas em Pequim?
    
- Temos que: 
  - Xangai: 0,4 ; Pequim: 0,3 ; Nenhuma das cidades: 0,4

    $P(X^c∩P) = P(P) - (X∩P)$

    $0,3 -0,1 = 0,2$
        
<br>**Questão 3**
    
Considere o experimento aleatório que consiste no lançamento de um dado que foi fabricado de tal forma que a probabilidade de ocorrer um número ímpar é o quádruplo da probabilidade de ocorrer um número par na face superior, sendo que os três números ímpares ocorrem com igual probabilidade, bem como os três números pares.
    
**(a)** Calcule a probabilidade de sair um número maior do que 2. 
    
1. Obtendo os dados necessários:
   - Ocorrer um número par:
      $A = {2, 4, 6}, sendo P(A) = 3n$
       
   - Ocorrer um número ímpar: $B = {1, 3, 5}, sendo P(B) = 3m$
       
   - P(B) é o quádruplo da prob. de P(A), logo
        **P(B) = P(A) * 4** 
       
    Sabendo que P(A) + P(B) = 1
       
   - Espaço amostral será:
       
       Ω = 4x + x + 4x + x + 4x + x = 1
       
       = 15x = 1 
       
       **x =** ${1 \above {1pt}{15}}$
       
2. Sair um número maior que 2 = {3, 4, 5, 6} 
            
    ${4 \above {1pt}{15}} + {1 \above {1pt}{15}} + {4 \above {1pt}{15}} + {1 \above {1pt}{15}} = {10 \above {1pt}{15}}$  **≅ 0,67**
            
    
**(b)** Qual a probabilidade de sair um múltiplo de 2, sabendo-se que saiu um número menor do que 3?

- múltiplo de 2 = {2, 4, 6} 
    
- ${1 \above {1pt}{15}} + {1 \above {1pt}{15}} + {1 \above {1pt}{15}} = {3 \above {1pt}{15}}$ **= 0,2**
        

<br>**Questão 4** 

Três dispositivos, A1, A2 e A3, que compõe um alarme, estão dispostos de tal forma que qualquer um deles funcionará independentemente quando algo estranho ocorrer. Cada dispositivo tem probabilidade de funcionar efetivamente igual a 0,75, 0,80 e 0,85, respectivamente. Determine a probabilidade de que

**(a) apenas o terceiro dispositivo não funcione.**


- Dados da questão: A1 = 0,75; A2 = 0,80; A3 = 0,85
        
$A3^c = 0,15$
        
$P(A1∩A2∩A3^c) = P(0,75∩0,8∩0,15)$
$= 0,75*0,8*0,15$ 
        
$=0,09$
        

**(b) todos os três dispositivos funcionem.**

$P(A1∩A2∩A3) = P(0,75∩0,8∩0,15)$
    
$=0,75*0,8*0,85$
    
$= 0,51$