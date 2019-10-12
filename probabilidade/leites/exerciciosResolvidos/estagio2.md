# Resolução de exercícios para o segundo estágio da disciplina Introdução à Probabilidade
Obs.: Idealmente, a aluno deve usar este arquivo apenas como referência e tentar resolver os exercicios 'on my own'

## Questão 1
De 120 estudantes, 60 estudam francês, 50 espanhol, e 20 estudam francês e espanhol. Se um estudante é escolhido ao acaso, encontre a probabilidade de que ele:

**a)** estude francês e espanhol.

**Resolução:**

  - Denotamos *A* como *estudante de francês* e *B* como *estudante de espanhol*, daí temos:
 <p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28A%5Ccap%20B%29%20%3D%20%5Cfrac%7B20%7D%7B120%7D%20%3D%20%5Cfrac%7B1%7D%7B6%7D">
</p>

**b)** estude pelo menos um dos idiomas.

**Resolução:**

  - Usaremos a propriedade de disjunção:
   <p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28A%5Ccup%20B%20%29%20%3D%20P%28A%29%20&plus;P%28B%29%20-%20P%28A%5Ccap%20B%29">
</p>
  <p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28A%5Ccup%20B%20%29%20%3D%20%5Cfrac%7B60%7D%7B120%7D%20&plus;%20%5Cfrac%7B50%7D%7B120%7D-%20%5Cfrac%7B1%7D%7B6%7D">
</p>
  <p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28A%5Ccup%20B%20%29%20%3D%20%5Cfrac%7B3%7D%7B4%7D">
</p>

**c)** não estude nem francês nem espanhol.

**Resolução:** 
  
  - Para isto, usaremos a Lei de De Morgan:
   <p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28%5Cbar%7BA%7D%5Ccap%20%5Cbar%7BB%7D%29%20%3D%20P%5Coverline%7B%28A%5Ccup%20B%29%7D">
</p>
  <p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%5Coverline%7B%28A%5Ccup%20B%29%7D%20%3D%201%20-%20P%28A%5Ccup%20B%29%20%3D%20%5Cfrac%7B1%7D%7B4%7D">
</p>

## Questão 2 
Um lote é composto por 10 artigos bons, 4 com defeitos menores e 2 com defeitos graves. Se 2 artigos são sorteados, sem reposição, determine a probabilidade de que:
  - Temos que:
    - B: Artigo bom;
    - M: Artigo com defeito menor;
    - G: Artigo com defeito grave.
    

**a)** ambos sejam bons.
 <p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28B%5Ccap%20B%29%20%3D%20%5Cfrac%7B10%7D%7B16%7D.%5Cfrac%7B9%7D%7B15%7D%20%3D%20%5Cfrac%7B3%7D%7B8%7D">
</p>

**b)** ambos tenham defeitos graves.
<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28G%5Ccap%20G%29%20%3D%20%5Cfrac%7B2%7D%7B16%7D.%5Cfrac%7B1%7D%7B15%7D%20%3D%20%5Cfrac%7B1%7D%7B120%7D">
</p>

**c)** ao menos um seja bom.
<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28B%29%20&plus;%20P%28M%5Ccap%20B%29%20&plus;%20P%28G%5Ccap%20B%29%20%3D%20%5Cfrac%7B10%7D%7B16%7D%20&plus;%20%5Cfrac%7B4%7D%7B16%7D.%5Cfrac%7B10%7D%7B15%7D&plus;%5Cfrac%7B2%7D%7B16%7D.%5Cfrac%7B10%7D%7B15%7D%20%3D%20%5Cfrac%7B7%7D%7B8%7D">
</p>

**d)** no máximo um seja bom.
<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%5Coverline%7B%28B%5Ccap%20B%29%7D%20%3D%201%20-%20P%28B%5Ccap%20B%29%20%3D%20%5Cfrac%7B5%7D%7B8%7D">
</p>

**e)** exatamente um seja bom.
<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28B%5Ccap%20M%29%20&plus;P%28B%5Ccap%20G%29%20&plus;P%28M%5Ccap%20B%29%20&plus;P%28G%5Ccap%20B%29%20%3D%20%5Cfrac%7B1%7D%7B2%7D">
</p>

**f)** nenhum tenha defeito grave.
<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28B%5Ccap%20B%29%20&plus;P%28B%5Ccap%20M%29%20&plus;P%28M%5Ccap%20B%29%20&plus;P%28M%5Ccap%20M%29%20%3D%20%5Cfrac%7B31%7D%7B40%7D">
</p>

**g)** nenhum seja bom.
  - Usaremos o complemento da letra c).
<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28%5Coverline%7Bc%7D%29%20%3D%201%20-%20P%28c%29%20%3D%20%5Cfrac%7B1%7D%7B8%7D">
</p>

## Questão 3
Em uma indústria, a experiência indica que há uma probabilidade de 90% de um operário novato, que tenha feito um curso prévio de treinamento, cumprir sua cota de produção; e que essa probabilidade para um novato que não tenha feito o curso prévio é de 45%. Sabe-se que 80% de todos os operários novatos frequentaram o curso prévio de treinamento. Selecionando-se um operário novato ao acaso, calcule:

**a)** A probabilidade de um operário novato não cumprir sua cota de produção.

**Resolução:**

  - Para isto, vamos usar probabilidade condicional:
  <p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28N_%7Bc%7D%29%20%3D%2080%5C%25">
</p>

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28N_%7Bs%7D%29%20%3D%2020%5C%25">
</p>

  - Sendo *C* o evento *"cumpriu a cota"*, temos que:
  <p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28C%29%20%3D%20P%28N_%7Bc%7D%29.P%28C%7CN_%7Bc%7D%29&plus;P%28N_%7Bs%7D%29.P%28C%7CN_%7Bs%7D%29">
</p>

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28C%29%20%3D%200.8*0.9&plus;0.2*0.45">
</p>

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28C%29%20%3D%200.81">
</p>

**b)** A probabilidade de ele ter feito o curso de treinamento, dado que ele não cumpriu a cota de produção.

**Resolução:**

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28N_%7Bc%7D%7CC%29%20%3D%20%5Cfrac%7BP%28%5Coverline%7BC%7D%7CN_%7Bc%7D%29.P%28N_%7Bc%7D%29%7D%7BP%28%5Coverline%7BC%7D%29%7D">
</p>

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28N_%7Bc%7D%7CC%29%20%3D%20%5Cfrac%7B0.1*0.8%7D%7B0.19%7D">
</p>

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28N_%7Bc%7D%7CC%29%20%3D%200.421">
</p>

## Questão 4
Suponha que a demanda por certa peça, numa loja de automóveis siga o seguinte modelo:
<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28X%3Dk%29%20%3D%5Cfrac%7Ba*2%5E%7Bk%7D%7D%7Bk%21%7D%2C%20k%20%3D%201%2C%202%2C%203%2C%204.">
</p>

**a)** Encontre o valor de *a*.

**Resolução:**

  - Para isto, vamos deduzir que o somatório das probabilidades seja igual a 1, então temos:
  <p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28X%3Dk%29%20%3D%20a%28%5Cfrac%7B2%5E%7B1%7D%7D%7B1%7D%20&plus;%20%5Cfrac%7B2%5E%7B2%7D%7D%7B2%7D%20&plus;%20%5Cfrac%7B2%5E%7B3%7D%7D%7B6%7D%20&plus;%20%5Cfrac%7B2%5E%7B4%7D%7D%7B24%7D%29%20%3D%201">
</p>

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20a%282%20&plus;%202%20&plus;%20%5Cfrac%7B4%7D%7B3%7D%20&plus;%20%5Cfrac%7B2%7D%7B3%7D%29%20%3D%201">
</p>

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20a%20%3D%20%5Cfrac%7B1%7D%7B6%7D">
</p>

**b)** Calcule a probabilidade da demanda ser inferior a duas peças.

**Resolução:**

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28X%20%3C%202%29%3D%5Cfrac%7B1*2%5E%7B1%7D%7D%7B6*1%21%7D%3D%5Cfrac%7B1%7D%7B3%7D">
</p>

**c)** Calcule a F.d.a. de X.

**Resolução:**

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20F%28X%29%20%3D%20%5Cleft%20%5C%7B%20%5Cbegin%7Bmatrix%7D%200%2C%20%26%20%5Cmbox%7Bse%20%7Dx%20%3C%201%2C%20%5C%5C%20%5Cfrac%7B1%7D%7B3%7D%2C%20%26%20%5Cmbox%7Bse%20%7D%201%5Cleq%20x%20%3C%202%2C%20%5C%5C%20%5Cfrac%7B1%7D%7B3%7D%2C%20%26%20%5Cmbox%7Bse%20%7D%202%5Cleq%20x%20%3C%203%2C%20%5C%5C%20%5Cfrac%7B2%7D%7B9%7D%2C%20%26%20%5Cmbox%7Bse%20%7D%203%5Cleq%20x%20%3C%204%2C%20%5C%5C%20%5Cfrac%7B1%7D%7B9%7D%2C%20%26%20%5Cmbox%7Bse%20%7D%20x%20%5Cgeq%204%20%5C%5C%20%5Cend%7Bmatrix%7D%20%5Cright.">
</p>

## Questão 5
Dada a função:

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20f%28x%29%20%3D%20%5Cleft%20%5C%7B%20%5Cbegin%7Bmatrix%7D%202e%5E%7B-2x%7D%2C%20%26%20%5Cmbox%7Bse%20%7Dx%20%5Cgeq%200%2C%20%5C%5C%200%2C%20%26%20%5Cmbox%7Bse%20%7D%20x%20%3C%200%20%5C%5C%20%5Cend%7Bmatrix%7D%20%5Cright.">
</p>

**a)** Mostre que esta função é uma *f.d.p.*.

**Resolução:**

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20%5Cint_%7B0%7D%5E%7B%5Cinfty%7D2e%5E%7B-2x%7Ddx%20%3D%202%20%5Cleft%20%5B%20%5Cfrac%7Be%5E%7B-2x%7D%7D%7B-2%7D%20%5Cright%20%5D_%7B0%7D%5E%7B%5Cinfty%7D">
</p>

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20%3D%202%5Cleft%20%5B%200%20&plus;%20%5Cfrac%7Be%5E%7B-0%7D%7D%7B2%7D%20%5Cright%20%5D%20%3D%201">
</p>

**b)** Obtenha a função de distribuição de *x* e calcule a probabilidade de *x > 10*.

**Resolução:**

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20F%28x%29%20%3D%5Cint_%7Bx%7D%5E%7B%5Cinfty%7D%202e%5E%7B-2x%7Ddx%20%3D%202%5Cleft%20%5B%20%5Cfrac%7Be%5E%7B-2x%7D%7D%7B-2%7D%20%5Cright%20%5D_%7Bx%7D%5E%7B%5Cinfty%7D%20%3D%202%5Cleft%20%5B%200%20&plus;%20%5Cfrac%7Be%5E%7B-2x%7D%7D%7B2%7D%20%5Cright%20%5D">
</p>

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20F%28x%29%20%3D%20e%5E%7B-2x%7D">
</p>

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20F%2810%29%20%3D%20P%28x%3E10%29%20%3D%20e%5E%7B-20%7D">
</p>

## Questão 6
Uma variável aleatória *x* tem distribuição triangular no intervalor [0, 1] se fua *f.d.p.* for dada por:

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20f%28x%29%20%3D%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%200%2C%20%26%20x%20%3C%200%20%5C%5C%20Cx%2C%20%26%200%5Cleq%20x%20%5Cleq%20%5Cfrac%7B1%7D%7B2%7D%20%5C%5C%20C%281-x%29%2C%20%26%20%5Cfrac%7B1%7D%7B2%7D%20%5Cleq%20x%20%5Cleq%201%20%5C%5C%200%2C%20%26%20x%20%3E%201%20%5Cend%7Bmatrix%7D%5Cright.">
</p>

**a)** Qual valor deve ter a constante *C*?

**Resolução:**

  - Para isto, vamos usar o somatório de integral:
  
  <p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20%5Cint_%7B-%5Cinfty%7D%5E%7B%5Cinfty%7Df%28x%29.dx%20%3D%20%5Cint_%7B-%5Cinfty%7D%5E%7B0%7D0.dx%20&plus;%20%5Cint_%7B0%7D%5E%7B%5Cfrac%7B1%7D%7B2%7D%7DCx.dx%20&plus;%20%5Cint_%7B%5Cfrac%7B1%7D%7B2%7D%7D%5E%7B1%7DC%281-x%29.dx%20&plus;%20%5Cint_%7B1%7D%5E%7B%5Cinfty%7D0.dx%20%3D%201">
</p>

 <p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20%5Cint_%7B-%5Cinfty%7D%5E%7B%5Cinfty%7Df%28x%29.dx%20%3D%20C%5Cleft%20%28%20%5Cleft%20%5B%20%5Cfrac%7Bx%5E2%7D%7B2%7D%20%5Cright%20%5D_%7B0%7D%5E%7B%5Cfrac%7B1%7D%7B2%7D%7D%20&plus;%20%5Cleft%20%5B%20x%20-%20%5Cfrac%7Bx%5E2%7D%7B2%7D%20%5Cright%20%5D_%7B%5Cfrac%7B1%7D%7B2%7D%7D%5E%7B1%7D%20%5Cright%20%29">
</p>

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20C%5Cleft%20%28%20%5Cfrac%7B1%7D%7B8%7D%20&plus;%201%20-%20%5Cfrac%7B1%7D%7B2%7D%20-%20%5Cfrac%7B1%7D%7B2%7D%20&plus;%20%5Cfrac%7B1%7D%7B8%7D%20%5Cright%20%29%20%3D%201">
</p>

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20C%20%3D%204">
</p>

**b)** Determine *P(x < 1/2)*, *P(x > 1/2)*, e *P(1/4 < x < 3/4)*.

**Resolução:**

  - Para P(x < 1/2):
  <p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28x%20%3C%201/2%29%20%3D%20%5Cint_%7B0%7D%5E%7B%5Cfrac%7B1%7D%7B2%7D%7Df%28x%29.dx%20%5CRightarrow%20%5Cint_%7B0%7D%5E%7B%5Cfrac%7B1%7D%7B2%7D%7D4x.dx%20%5CRightarrow%204%5Cleft%20%5B%20%5Cfrac%7Bx%5E2%7D%7B2%7D%20%5Cright%20%5D_%7B0%7D%5E%7B%5Cfrac%7B1%7D%7B2%7D%7D">
</p>
<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28x%20%3C%201/2%29%20%3D%20%5Cfrac%7B1%7D%7B2%7D">
</p>

  - Para P(x > 1/2), temos o complemento do item anterior, então:
  
  <p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28x%20%3E%201/2%29%20%3D%20%5Cfrac%7B1%7D%7B2%7D">
</p>

  - Para P(1/4 < x < 3/4):
  
  <p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%5Cleft%20%28%20%5Cfrac%7B1%7D%7B4%7D%20%3C%20x%20%3C%20%5Cfrac%7B3%7D%7B4%7D%20%5Cright%20%29%20%3D%20%5Cint_%7B%5Cfrac%7B1%7D%7B4%7D%7D%5E%7B%5Cfrac%7B3%7D%7B4%7D%7Df%28x%29.dx%20%5CRightarrow%20%5Cint_%7B%5Cfrac%7B1%7D%7B4%7D%7D%5E%7B%5Cfrac%7B1%7D%7B2%7D%7D4x.dx%20&plus;%20%5Cint_%7B%5Cfrac%7B1%7D%7B2%7D%7D%5E%7B%5Cfrac%7B3%7D%7B4%7D%7D4%281-x%29.dx">
</p>

  <p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%5Cleft%20%28%20%5Cfrac%7B1%7D%7B4%7D%20%3C%20x%20%3C%20%5Cfrac%7B3%7D%7B4%7D%20%5Cright%20%29%20%3D%20%5Cfrac%7B3%7D%7B4%7D">
</p>


## Questão 7
Suponha que estamos atirando dardos num alvo circular de raio 10cm, e seja *x* a distância do ponto atingido pelo dardo ao centro do alvo. A *f.d.p.* de *x* é:

 <p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20f%28x%29%3D%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%20kx%2C%20%26%200%20%5Cleq%20x%20%5Cleq%2010%20%5C%5C%200%2C%20%26%20c.c.%20%5Cend%7Bmatrix%7D%5Cright.">
</p>

**a)** Qual a probabilidade de acertar o centro do alvo, se esse for um círculo de 1cm de raio?

**Resolução:**

  - Como *P(x < 10) = 1*, temos que:
  
  <p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20%5Cint_%7B0%7D%5E%7B10%7Dkx.dx%20%3D%201%20%5CRightarrow%20k%5Cleft%20%5B%20%5Cfrac%7Bx%5E2%7D%7B2%7D%20%5Cright%20%5D_%7B0%7D%5E%7B10%7D%20%3D%201%20%5CRightarrow%20k%20%3D%200.02">
</p>

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20%5Ctherefore%20F%28x%29%20%3D%20%5Cint_%7B0%7D%5E%7Bx%7D0.02x.dx%20%3D%200%2C01x%5E2">
</p>

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20F%281%29%20%3D%20P%28x%5Cleq%201%29%20%3D%200%2C01">
</p>

**b)** Mostre que a probabilidade de acertar qualquer círculo concêntrico é proporcional â sua área.

**Resolução:**

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28x%20%3C%20r%29%20%3D%200.01r%5E2%20%3D%20%5Cfrac%7B%5Cpi%20r%5E2%7D%7B%5Cpi%2010%5E2%7D">
</p>

## Questão 8
Encontre o valor da constante *C* se

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20f%28x%29%3D%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%20%5Cfrac%7BC%7D%7Bx%5E2%7D%2C%20%26%20x%5Cgeq%2010%20%5C%5C%200%2C%20%26%20x%20%3C%2010%20%5Cend%7Bmatrix%7D%5Cright.">
</p>

for uma densidade, e encontre *P(x > 15)*.

**Resolução:**

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20%5Cint_%7B-%5Cinfty%7D%5E%7B%5Cinfty%7Df%28x%29.dx%20%3D%20%5Cint_%7B-%5Cinfty%7D%5E%7B10%7D0.dx%20&plus;%20%5Cint_%7B10%7D%5E%7B%5Cinfty%7D%5Cfrac%7BC%7D%7Bx%5E2%7D.dx">
</p>

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20C%5Cint_%7B10%7D%5E%7B%5Cinfty%7Dx%5E%7B-2%7D%3D%20C%5Cleft%20%5B%20-2x%5E%7B-3%7D%20%5Cright%20%5D_%7B10%7D%5E%7B%5Cinfty%7D">
</p>

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20%5Cfrac%7BC%7D%7B10%7D%20%3D1%20%5CRightarrow%20C%20%3D%2010">
</p>

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20%5Ctherefore%20P%28x%20%3E%2015%29%20%3D%20%5Cint_%7B15%7D%5E%7B%5Cinfty%7D%5Cfrac%7B10%7D%7Bx%5E2%7D.dx%20%3D%2010.%5Cleft%20%5B%20%5Cfrac%7B1%7D%7Bx%7D%20%5Cright%20%5D_%7B15%7D%5E%7B%5Cinfty%7D">
</p>

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28x%20%3E%2015%29%20%3D%20%5Cfrac%7B2%7D%7B3%7D">
</p>

## Questão 9 
Um fabricante afirma que apenas 5% de todas as válvulas que produz têm duração inferior a 20 horas. Uma indústria compra semanalmente um grande lote de válvulas desse fabricante, mas sob a seguinte condição:
  - ela aceita o lote se, em dez válvulas escolhidas ao acaso, no máximo uma tiver duração inferior a 20 horas;
  - caso contrário, o lote todo é rejeitado.

**a)** se o fabricante de fato tem razão, qual a probabilidade de um lote ser rejeitado?

**Resolução:**

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28v%29%20%3D%2095%5C%25">
</p>

  - Sendo *A* o evento *"o lote será aceito"*, temos:
  
  <p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28A%29%20%3D%20P%28v%29.P%28A%7Cv%29%20%5CRightarrow%20P%28A%29%20%3D%200.95x0.90">
</p>

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28A%29%20%3D%200.855">
</p>

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28%5Coverline%7BA%7D%29%20%3D%200.145">
</p>

  - Para encontrarmos a probabilidade esperada, vamos usar binomial:
  
  <p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20%5Ctherefore%20P%28x%20%5Cgeq%202%29%20%3D%201%20-%20P%28x%20%3C%202%29">
</p>

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28x%20%5Cgeq%202%29%20%3D%201%20-%20%5Cleft%20%5B%20%5Cleft%20%28%200%2C95%20%5Cright%20%29%5E%7B10%7D%20&plus;%20%5Cbinom%7B10%7D%7B9%7D.%5Cleft%20%28%200.05%20%5Cright%20%29%5E1.%280.95%29%5E9%20%5Cright%20%5D">
</p>

<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28x%20%5Cgeq%202%29%20%3D%200.086">
</p>
  
