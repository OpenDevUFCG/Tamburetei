Teoria da Computação

2022.1

Reposição

### Questões

#### Estágio 1

1. Projete o AFD com alfabeto {0,1} que aceite palavras em que a substring "01" aparece na mesma quantidade de vezes que a substring "10" (ex., aceita "010", rejeita "001).
2. Como poderíamos construir um autômato que combina dois autômatos que não têm o mesmo alfabeto de modo que a linguagem deste terceiro autômato contenha todas as palavras que os dois autômatos aceitariam? Você pode dar uma resposta formal ou explicar informalmente a construção usando dois autômatos de exemplo. Caso opte por um exemplo, você pode assumir que os dois alfabetos têm um símbolo em comum e um símbolo que o outro alfabeto não tem.
3. Transforme o AFND abaixo em um AFD.

    ![AFND](https://i.imgur.com/zTYNt9R.png)
   
#### Estágio 2

1. Construa um autômato de pilha para a linguagem $0^m1^n2^n3^m$, onde m,n >= 0.
2. O que é uma gramática linear à direita? Mostre um exemplo de gramática linear à direita que tenha uma linguagem de tamanho infinito e mostre as árvores de derivação para duas palavras de comprimento 4 ou maior.
3. Qual a intuição por trás do lema do bombeamento? (Por exemplo, qual o objetivo das 3 regras que o definem?)

#### Estágio 3

1. O que é a forma normal de Chomsky? Dê um exemplo de uma conversão de uma gramática para esta forma normal. Sua conversão deve usar os 5 passos.
2. Construa uma máquina de Turing para a linguagem $0^m1^n2^m3^n$, onde m,n >= 0.
3. Sobre decidibilidade, responda as seguintes questões:
   
    <ol type="a">
      <li>O que são as classes das linguagens Turing-Reconhecível e Turing-Decidível?</li>
      <li>Suponha uma linguagem L1, que é Turing-Decidível. Agora considere uma linguagem L2 tal que L2 $\subset$ L1. O que podemos dizer sobre a decidibilidade de L2? Justifique.</li>
    </ol>
