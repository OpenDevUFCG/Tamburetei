#Questao 1040 do URI

#Recebe entrada e separa
n = input().split()

#Lista para armazenar valores da entrada
valores = list()

#Convertendo cada valor da entrada para float com um loop for.
#Outra opcao seria converter cada valor um a um
for e in n:
    numero = round(float(e), ndigits=1)
    valores.append(numero)

#Calculando a media ponderada dos valores de acordo com os pesos dado na questao
med = ((valores[0]*2)+(valores[1]*3)+(valores[2]*4)+(valores[3]*1))/10
print('Media: {:.1f}'.format(med))

#Avaliando a situacao do aluno que possui a media
if med >= 7:
    print('Aluno aprovado.')
if med < 5:
    print('Aluno reprovado.')
if 5 <= med < 7:
    print('Aluno em exame.')
    ex = round(float(input()), ndigits=1)
    print('Nota do exame: {:.1f}'.format(ex))
    medf = (med+ex)/2
    if medf >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(medf))


