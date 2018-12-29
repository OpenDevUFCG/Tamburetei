# Resolução de exercícios para o primeiro estágio da disciplina Introdução à Probabilidade
Obs.: Idealmente, a aluno deve usar este arquivo apenas como referência e tentar resolver os exercicios 'on my own'

## Questão 1
Os comprimentos, em centímetros, de 30 peças estão dados abaixo:

0,90 | 1,28 | 1,82 | 1,88 | 2,12 | 2,43 | 2,78 | 2,82 | 2,93 | 3,63 | 3,67 | 3,73 | 3,96 | 4,07 | 4,10
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
4,17 | 4,26 | 4,30 | 4,65 | 5,09 | 5,28 | 5,36 | 5,41 | 5,54 | 5,84 | 6,54 | 7,35 | 7,77 | 8,14 | 8,45

**a)** Construa um Box-Plot para esses dados, e a partir dele, obtenha conclusões a respeito da distribuição dos mesmos

**Resolução:**
  - Primeiramente, devemos encontrar o primeiro quantil(*q1*), o segundo(*md(x)*), e o terceiro(*q3*);
  - Para a o *q2* devemos fazer o cálculo da mediana:
    
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20md%28x%29%20%3D%20%28x_%7B15%7D&plus;x_%7B16%7D%29/2%20%5CRightarrow%20md%28x%29%20%3D%204%2C135">
</p>

  - Para a atribuição de *q1* e *q3* devemos analisar o elemento mediano da primeira e segunda metade do aglomerado ordenado de dados respectivamente:
    
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20q_%7B1%7D%20%3D%20x_%7B8%7D%20%3D%202%2C82">
</p>
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20q_%7B3%7D%20%3D%20x_%7B23%7D%20%3D%205%2C41">
</p>

  - Além destas, devemos encontrar as medidas: *LI*(Limite inferior), *LS*(Limite superior), *dq*(Diferença interquartílica), *min*(Valor mínimo), *max*(valor máximo):
  <p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20dq%20%3D%20q_%7B3%7D%20-%20q_%7B1%7D%20%5CRightarrow%20dq%20%3D%202%2C59">
</p>
  <p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20LI%20%3D%20q_%7B1%7D%20-%201%2C5.dq%20%5CRightarrow%20LI%20%3D%202%2C82%20-%203%2C885%20%3D%20-1%2C065">
</p>
  <p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20LS%20%3D%20q_%7B3%7D%20&plus;%201%2C5.dq%20%5CRightarrow%20LS%20%3D%205%2C41%20&plus;%203%2C885%20%3D%209%2C295">
</p>
  <p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20min%20%3D%20x_%7B1%7D%20%3D%200%2C90">
</p>
  <p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20max%20%3D%20x_%7B30%7D%20%3D%208%2C45">
</p>

  - O modelo do Box-Plot deve ficar parecido com o seguinte:
<p align="center">
    <a href="https://plot.ly/~grabowski74/1/?share_key=ZUqE1YITuUpVyHXYcb9swf" target="_blank" title="Plot 1" style="display: block; text-align: center;"><img src="https://plot.ly/~grabowski74/1.png?share_key=ZUqE1YITuUpVyHXYcb9swf" alt="Plot 1" style="max-width: 100%;width: 600px;"  width="600" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
</p>

  - Podemos concluir que há uma concentração maior de valores menores que a mediana.
  
**b)** Agrupe os dados em classes, em seguida, construa um histograma de distribuição

**Resolução**

  - Idealmente, vamos atribuir o número de 5 classes(*k*) para esta resolução. Ainda precisamos dos valores do *Delta Total* e *Delta das classes*, que podem ser dados por:
   <p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20%5CDelta_%7Btot%7D%20%3D%20x_%7Bmax%7D%20-%20x_%7Bmin%7D%20%5CRightarrow%20%5CDelta_%7Btot%7D%20%3D%208%2C45%20-%200%2C90%20%3D%207%2C55">
</p>
  <p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20%5CDelta%20%3D%20%5Cfrac%7B%5CDelta_%7Btot%7D%7D%7Bk%7D%20%5CRightarrow%20%5CDelta%20%3D%20%5Cfrac%7B7%2C55%7D%7B5%7D%20%3D%201%2C51">
</p>

  - Assim, temos a seguinte distribuição:
  
  **Comprimentos** | **Frequência Absoluta(*ni*)** | **Frequência Relativa(*fi*)** | **Porcentagem(*%*)** | **Frequência Acumulada**
  --- | --- | --- | --- | ---
  ![](http://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%200%2C90%20%5Cvdash%202%2C41) | 5 | 0,166 | 16,6 % | 5
  ![](http://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%202%2C41%20%5Cvdash%203%2C92) | 7 | 0,234 | 23,4 % | 12
  ![](http://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%203%2C92%20%5Cvdash%205%2C43) | 11 | 0,366 | 36,6 % | 23
  ![](http://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%205%2C43%20%5Cvdash%206%2C94) | 3 | 0,100 | 10,0 % | 26
  ![](http://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%206%2C94%20%5Cvdash%208%2C45) | 4 | 0,134 | 13,4 % | 30
  **Total** | 30 | 1 | 100,0 % | -
  
  - O histograma deve ter aparência do seguinte modelo:
  <p align="center">
    <a href="https://plot.ly/~grabowski74/2/?share_key=EN1Lu293cT04VJFwUInnlw" target="_blank" title="Plot 2" style="display: block; text-align: center;"><img src="https://plot.ly/~grabowski74/2.png?share_key=EN1Lu293cT04VJFwUInnlw" alt="Plot 2" style="max-width: 100%;width: 600px;"  width="600" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    
</p>

## Questão 2
O número de divórcios numa certa idade, de acordo com a duração do casamento, está representado na tabela abaixo:
