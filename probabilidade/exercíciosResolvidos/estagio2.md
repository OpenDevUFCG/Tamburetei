# Resolução de exercícios para o segundo estágio da disciplina Introdução à Probabilidade
Obs.: Idealmente, a aluno deve usar este arquivo apenas como referência e tentar resolver os exercicios 'on my own'

## Questão 1
De 120 estudantes, 60 estudam francês, 50 espanhol, e 20 estudam francês e espanhol. Se um estudante é escolhido ao acaso, encontre a probabilidade de que ele:

**a)** estude francês e espanhol.

**Resolução:**

  - Denotamos *A* como *estudante de francês* e *B* como *estudante de espanhol*, daí temos:
 <p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28A%5Ccap%20B%29%20%3D%20%5Cfrac%7B20%7D%7B120%7D%20%3D%20%5Cfrac%7B1%7D%7B6%7D">
</p>

**b)** estude pelo menos um dos idiomas.

**Resolução:**

  - Usaremos a propriedade de disjunção:
   <p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28A%5Ccup%20B%20%29%20%3D%20P%28A%29%20&plus;P%28B%29%20-%20P%28A%5Ccap%20B%29">
</p>
  <p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28A%5Ccup%20B%20%29%20%3D%20%5Cfrac%7B60%7D%7B120%7D%20&plus;%20%5Cfrac%7B50%7D%7B120%7D-%20%5Cfrac%7B1%7D%7B6%7D">
</p>
  <p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28A%5Ccup%20B%20%29%20%3D%20%5Cfrac%7B3%7D%7B4%7D">
</p>

**c)** não estude nem francês nem espanhol.

**Resolução** 
  
  - Para isto, usaremos a Lei de De Morgan:
   <p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%28%5Cbar%7BA%7D%5Ccap%20%5Cbar%7BB%7D%29%20%3D%20P%5Coverline%7B%28A%5Ccup%20B%29%7D">
</p>
  <p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Csmall%20P%5Coverline%7B%28A%5Ccup%20B%29%7D%20%3D%201%20-%20P%28A%5Ccup%20B%29%20%3D%20%5Cfrac%7B1%7D%7B4%7D">
</p>
