### Questão maior e menor ###

"""primeiro = int(input('Digite o primeiro número:'))
segundo = int(input('Digite o segundo número:'))
terceiro = int(input('Digite o terceiro número:'))
numeros = [primeiro, segundo, terceiro]

print('O maior valor digitado foi {}'.format(max(numeros)))
print('O menor numero digitado foi {}'.format(min(numeros)))"""

n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
if n1 > n2 or n2 < n3:
    if n1 > n3:
        print('O maior valor é: ', n1)
        if n2 < n3:
            print('O menor valor é:', n2)
        else:
            print('O menor valor é: ', n3)
    else:
        print('O maior valor é: ', n3)
        if n2 < n1:
            print('O menor valor é:', n2)
        else:
            print('O menor valor é: ', n1)
else:
    print('O maior valor é:', n2)
    if n1 > n3:
        print('O menor valor é: ', n3)
    else:
        print('O menor valor é: ', n1)

### Questão multa ###
vel = int(input('Qual a velocidade em Km/h? '))

if vel > 80:
    mul = (vel - 80) * 7
    print('Você foi multado! \n Valor da multa:', mul, 'R$')
else:
    print('Você não foi multado!')

### Questão Advinhar o resultado ###
import random

num = int(input('Escolha um numero entre 0 e 5: '))
val = random.randrange(0, 5)
if 0 <= num <= 5:
    if num == val:
        print('Parabens, vc acertou!')
    else:
        print('O valor sorteado foi:', val, '\n Tente novamente!')
