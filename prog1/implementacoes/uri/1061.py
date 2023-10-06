ini = input().split()
horaria_ini = [int(l) for l in input().split(" : ")]
fim = input().split()
horaria_fim = [int(l) for l in input().split(" : ")]
ini_dia, fim_dia = int(ini[1]), int(fim[1])
termino = fim_dia - ini_dia
horas, minutos, segundos = 0, 0, 0

if horaria_ini[2] < horaria_fim[2]:
    segundos = horaria_fim[2] - horaria_ini[2]
    if segundos == 60:
        minutos +=1
        segundos = 0

else:
    segundos = (60 - horaria_ini[2]) + horaria_fim[2]
    minutos -= 1
    if segundos == 60:
        minutos +=1
        segundos = 0

if horaria_ini[1] < horaria_fim[1]:
    minutos += horaria_fim[1] - horaria_ini[1]
    if minutos == 60:            
        horas +=1
        minutos = 0

else:
    minutos += (60 - horaria_ini[1]) + horaria_fim[1]
    horas -= 1
    if minutos == 60:
        horas +=1
        minutos = 0

if int(horaria_ini[0]) < int(horaria_fim[0]):
    horas += horaria_fim[0] - horaria_ini[0]
    if horas == 24:
        termino +=1
        horas = 0

else:
    horas += (24 - horaria_ini[0]) + horaria_fim[0]
    termino -= 1
    if horas == 24:
        termino +=1
        horas = 0

print(f'''{termino} dia(s)
{horas} hora(s)
{minutos} minuto(s)
{segundos} segundo(s)
''', end='')