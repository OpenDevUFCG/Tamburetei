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
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20md%28x%29%20%3D%20%28x_%7B15%7D&plus;x_%7B16%7D%29/2%20%5CRightarrow%20md%28x%29%20%3D%204%2C135">
</p>

  - Para a atribuição de *q1* e *q3* devemos analisar o elemento mediano da primeira e segunda metade do aglomerado ordenado de dados respectivamente:
    
<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20q_%7B1%7D%20%3D%20x_%7B8%7D%20%3D%202%2C82">
</p>
<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20q_%7B3%7D%20%3D%20x_%7B23%7D%20%3D%205%2C41">
</p>

  - Além destas, devemos encontrar as medidas: *LI*(Limite inferior), *LS*(Limite superior), *dq*(Diferença interquartílica), *min*(Valor mínimo), *max*(valor máximo):
  <p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20dq%20%3D%20q_%7B3%7D%20-%20q_%7B1%7D%20%5CRightarrow%20dq%20%3D%202%2C59">
</p>
  <p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20LI%20%3D%20q_%7B1%7D%20-%201%2C5.dq%20%5CRightarrow%20LI%20%3D%202%2C82%20-%203%2C885%20%3D%20-1%2C065">
</p>
  <p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20LS%20%3D%20q_%7B3%7D%20&plus;%201%2C5.dq%20%5CRightarrow%20LS%20%3D%205%2C41%20&plus;%203%2C885%20%3D%209%2C295">
</p>
  <p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20min%20%3D%20x_%7B1%7D%20%3D%200%2C90">
</p>
  <p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20max%20%3D%20x_%7B30%7D%20%3D%208%2C45">
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
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20%5CDelta_%7Btot%7D%20%3D%20x_%7Bmax%7D%20-%20x_%7Bmin%7D%20%5CRightarrow%20%5CDelta_%7Btot%7D%20%3D%208%2C45%20-%200%2C90%20%3D%207%2C55">
</p>
  <p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20%5CDelta%20%3D%20%5Cfrac%7B%5CDelta_%7Btot%7D%7D%7Bk%7D%20%5CRightarrow%20%5CDelta%20%3D%20%5Cfrac%7B7%2C55%7D%7B5%7D%20%3D%201%2C51">
</p>

  - Assim, temos a seguinte distribuição:
  
  **Comprimentos** | **Frequência Absoluta(*ni*)** | **Frequência Relativa(*fi*)** | **Porcentagem(*%*)** | **Frequência Acumulada**
  --- | --- | --- | --- | ---
  ![](https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%200%2C90%20%5Cvdash%202%2C41) | 5 | 0,166 | 16,6 % | 5
  ![](https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%202%2C41%20%5Cvdash%203%2C92) | 7 | 0,234 | 23,4 % | 12
  ![](https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%203%2C92%20%5Cvdash%205%2C43) | 11 | 0,366 | 36,6 % | 23
  ![](https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%205%2C43%20%5Cvdash%206%2C94) | 3 | 0,100 | 10,0 % | 26
  ![](https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%206%2C94%20%5Cvdash%208%2C45) | 4 | 0,134 | 13,4 % | 30
  **Total** | 30 | 1 | 100,0 % | -
  
  - O histograma deve ter aparência do seguinte modelo:
  <p align="center">
    <a href="https://plot.ly/~grabowski74/2/?share_key=EN1Lu293cT04VJFwUInnlw" target="_blank" title="Plot 2" style="display: block; text-align: center;"><img src="https://plot.ly/~grabowski74/2.png?share_key=EN1Lu293cT04VJFwUInnlw" alt="Plot 2" style="max-width: 100%;width: 600px;"  width="600" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    
</p>

## Questão 2
O número de divórcios numa certa idade, de acordo com a duração do casamento, está representado na tabela abaixo:

**Anos de casamento** | **Número de divórcios**
--- | ---
![](https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%200%20%5Cvdash%206) | 2800
![](https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%206%20%5Cvdash%2012) | 1400
![](https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%2012%20%5Cvdash%2018) | 600
![](https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%2018%20%5Cvdash%2024) | 150
![](https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%2024%20%5Cvdash%2030) | 50
**Total** | 5000

**a)** Construa o histograma da distribuição.

**Resolução**
  - O esboço do histograma deve seguir o seguinte modelo:
  
 <p align="center">
    <a href="https://plot.ly/~grabowski74/4/?share_key=frofwwSVKTIVUeYrZAlBj6" target="_blank" title="Plot 4" style="display: block; text-align: center;"><img src="https://plot.ly/~grabowski74/4.png?share_key=frofwwSVKTIVUeYrZAlBj6" alt="Plot 4" style="max-width: 100%;width: 600px;"  width="600" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    
</p>

**b)** Qual a duração média dos casamentos?

**Resolução**
  - Para isto, devemos calcular a média com a seguinte fórmula:
  <p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20%5Cbar%7Bx%7D%20%3D%20%5Cfrac%7B1%7D%7Bn%7D%5Csum_%7Bi%3D1%7D%5E%7Bk%7Dn_%7Bi%7D.s_%7Bi%7D">
</p>
 <p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20%5Cbar%7Bx%7D%20%3D%20%5Cfrac%7B1%7D%7B5000%7D%282800.3%20&plus;%201400.9%20&plus;%20600.15%20&plus;%20150.21%20&plus;%2050.27%29">
   <p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20%5Cbar%7Bx%7D%20%5Csimeq%206%2C97">
</p>

**c)** Encontre a variância e o desvio padrâo de duração de casamentos.

**Resolução**
  - Para a variância, usaremos a seguinte fórmula:
  <p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20var%28x%29%20%3D%20%5Csum_%7Bi%3D1%7D%5E%7Bk%7Df_%7Bi%7D%28x_%7Bi%7D-%5Cbar%7Bx%7D%29%5E2">
</p>
   <p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20var%28x%29%20%3D%200%2C56.%283-6%2C97%29%5E2%20&plus;0%2C28.%289-6%2C97%29%5E2&plus;0%2C12.%2815-6%2C97%29%5E2&plus;0%2C03.%2821-6%2C97%29%5E2%20&plus;%200%2C01.%2827-6%2C97%29%5E2">
</p>
  <p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20var%28x%29%20%3D%2027%2C61">
</p>

  - Para o desvio padrão, temos a seguinte fórmula:
   <p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20dp%28x%29%20%3D%20%5Csqrt%7Bvar%28x%29%7D">
</p>
    <p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20dp%28x%29%20%3D%205%2C25">
</p>
    

## Questão 3
Uma companhia de seguros analisou a frequência com que 2000 segurados usaram o hospital.

**Dados** | **Homens** | **Mulheres** | **Total**
--- | --- | --- | ---
**Usaram o hospital** | 100 | 150 | 250
**Não usaram o hospital** | 900 | 850 | 1750
**Total** | 1000 | 1000 | 2000

**a)** Calcule a proporção de homens entre os indíviduos que usaram o hospital.

**Resolução**
  - Para isto, vamos usar regra de três simples:
  <p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20%5Cfrac%7B250%7D%7B100%5C%25%7D%20%3D%20%5Cfrac%7B100%7D%7Bx%7D%20%5CRightarrow%20250x%20%3D%20100%20%5CRightarrow%20x%20%3D%2040%5C%25">
</p>

**b)** Calcule a proporção de homens entre os indivíduos que não usaram o hospital.

**Resolução**
  - Novamente, vamos usar regra de três simples:
  <p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20%5Cfrac%7B1750%7D%7B100%5C%25%7D%20%3D%20%5Cfrac%7B900%7D%7Bx%7D%20%5CRightarrow%201750x%20%3D%20900%20%5CRightarrow%20x%20%3D%2051%2C42%5C%25">
</p>

**c)** O uso do hospital independe do sexo do segurado? Justifique a sua resposta utilizando uma medida adequada de associação.

**Resolução**
  - Para isto, precisamos encontrar o coeficiente de associação *T*, que é dado pela fórumla:
  <p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20T%20%3D%20%5Csqrt%7B%5Cfrac%7B%5Cfrac%7Bx%5E2%7D%7Bn%7D%7D%7B%28r-1%29%28s-1%29%7D%7D">
</p>
  
  - Onde:
  <p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20x%5E2%20%3D%20%5Csum_%7Bi%3D1%7D%5E%7Br%7D%5Csum_%7Bj%3D1%7D%5E%7Bs%7D%5Cfrac%7B%28n_%7Bij%7D-n_%7Bij%7D%5E%7B*%7D%29%5E2%7D%7Bn_%7Bij%7D%5E%7B*%7D%7D">
</p>
  <p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20x%5E2%20%3D%20%5Cfrac%7B%28100-125%29%5E2%7D%7B125%7D&plus;%5Cfrac%7B%28150-125%29%5E2%7D%7B125%7D%20&plus;%20%5Cfrac%7B%28900-875%29%5E2%7D%7B875%7D&plus;%5Cfrac%7B%28850-875%29%5E2%7D%7B875%7D">
</p>
  <p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20x%5E2%20%3D%2011%2C43">
</p>

  - Daí temos:
  
    <p align="center">
      <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20T%20%3D%20%5Csqrt%7B%5Cfrac%7B%5Cfrac%7B11%2C43%7D%7B2000%7D%7D%7B1%7D%7D%5CRightarrow%20T%20%3D%200%2C07">
    </p>
    
  - Portanto, com o resultado obtido, definimos que há uma **associação fraca**.
  
  ## Questão 4
  Numa amostra de cinco operários de uma dada empresa foram observadas duas variáveis: *X = anos de experiência num dado cargo* e *Y = tempo, em minutos, gasto na execução de uma certa tarefa relacionada com esse cargo*. 
  
  *X* | 1 | 2 | 4 | 4 | 5
  --- | --- | --- | --- | --- | ---
  *Y* | 7 | 8 | 3 | 2 | 2
  
  Você diria que a variável *X* pode ser usada para explicar a variação de *Y*? Justifique a sua resposta utilizando uma medida adequada de associação.
  - Cálculos auxiliares:
   <p align="center">
      <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20%5Csum%20x%20%3D%2016%3B%20%5Csum%20y%20%3D%2022%3B%20%5Csum%20xy%20%3D%2053%3B%5Csum%20x%5E2%3D62%3B%20%5Csum%20y%5E2%3D130">
    </p>
    
**Resolução:**
  - Vamos usar a seguinte fórmula:
  <p align="center">
      <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20corr%28x%2C%20y%29%20%3D%20%5Cfrac%7B%5Csum_%7Bi%3D1%7D%5E%7Bn%7Dx_%7Bi%7Dy_%7Bi%7D%20-%20n%5Cbar%7Bx%7D%5Cbar%7By%7D%7D%7B%5Csqrt%7B%28%5Csum_%7Bi%3D1%7D%5E%7Bn%7Dx_%7Bi%7D%5E2%20-%20n%5Cbar%7Bx%7D%5E2%29%28%5Csum_%7Bi%3D1%7D%5E%7Bn%7Dy_%7Bi%7D%5E2%20-%20n%5Cbar%7By%7D%5E2%29%7D%7D">
    </p>
    <p align="center">
      <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20corr%28x%2C%20y%29%20%3D%20%5Cfrac%7B53%20-%285x3%2C2x4%2C4%29%7D%7B%5Csqrt%7B%5B62%20-%205x%283%2C2%29%5E2%5D%5B130%20-%205x%284%2C4%29%5E2%5D%7D%7D">
    </p>
    <p align="center">
      <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20%7Ccorr%28x%2C%20y%29%7C%20%3D%20%5Cfrac%7B-17%2C4%7D%7B18%2C9%7D%20%5CRightarrow%20%7Ccorr%28x%2Cy%29%7C%20%3D%200%2C92">
    </p>
    
  - Portanto, dizemos que há uma **associação forte** entre as variáveis.
