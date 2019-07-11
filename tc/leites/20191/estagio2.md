## Prova 02

**Professor:** Andrey Brito

1. Transforme o AFND abaixo em uma ER.  
![](https://user-images.githubusercontent.com/14113480/61055213-5fa55180-a3c7-11e9-8bf2-09ea4c07142f.png)
2. Considerando a expressão regular definida por R = `(1 U (001)*)` transforme-a em um AFND.
3. Projete a gramática livre de contexto para a seguinte linguagem (0^k)\*(1^j)\*(2^k), onde i = k, i > 0, j = 1.
4. Responda as alternativas com verdadeiro ou falso, justificando a sua escolha.  
   a. A linguagem L = {ww | w E {0,1}\*} é regular uma vez que posso escolher a palavra w = {0^P0^P}, que pertence a linguagem, e bombeá-la fazendo x = λ, y = 00 e z = O^(p-2)0^p e a palavra resultante ainda pertencerá a L.  
   b. Intuitivamente a linguagem L = {w E {0,1}\* | w tem a mesma quantidade de símbolos 0 e 1} não é regular, pois um autômato não teria como contar e comparar a quantidade de símbolos 0 e símbolos c. Pelo mesmo motivo, a linguagem L2, L2 = {w E {0,1}\* | w tem a mesma quantidade de ocorrências de substrings 01 e 10} não é regular.  
   d. A gramática é ambígua? S -> SS | (S) | ().  
   e. Algumas gramáticas livres de contexto podem ser convertidas em autômatos finitos.