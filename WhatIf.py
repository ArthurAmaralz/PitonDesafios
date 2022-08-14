### if nome in 'ana claudia jessica juliana':

### Questão JOKEPO ###

from random import randint
iten = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('''
[0] Pedra
[1] Papel
[2] Tesoura''')
esc = int(input('Escolha: '))
print(f'A maquina jogou: {iten[comp]}')
print(f'Vc jogou:        {iten[esc]}')

if comp == 0:
    if esc == 1:
        print('Você ganhou!')
    elif esc == 2:
        print('Vc venceu!')
    elif esc == 0:
        print('Empate')
    else:
        print('Invalido!')

elif comp == 1:
    if esc == 0:
        print('Vc perdeu!')
    elif esc == 2:
        print('Vc ganhou!')
    elif esc == 1:
        print('Empate')
    else:
        print('Invalido!')

elif comp == 2:
    if esc == 1:
        print('Vc perdeu!')
    elif esc == 0:
        print('Vc venceu!')
    elif esc == 2:
        print('Empate')
    else:
        print('Invalido!')

### Questão conversão ###

num = int(input('Digite o valor: '))
p = int(input('Você deseja converter ele em:\n1 - para binario\n2 - para octal\n3 - para hexadecimal\n'))
if p == 1:
    print(f'O valor de {num} em binario é: {bin(num)[2:]}')
elif p == 2:
    print(f'O valor de {num} em octal é: {oct(num)[2:]}')
else:
    print(f'Ovalor de {num} em hexadecimal é: {hex(num)[2:]}')

### Questão financiamento ###

val = float(input('Qual o valor da casa?R$ '))
sal = float(input('Qual o seu salario?R$ '))
temp = float(input('Quantos anos deseja pagar? '))
if val/(temp*12) <= sal*0.3:
    print(f'Seu emprestimo foi aprovado em {temp*12:.0f} meses, no valor de R$ {val/(12*temp):.2f}')
else:
    print(f'Infelizmente seu emprestimo não foi aprovado,\nPois a prestação foi de R$ {val/(12*temp):.2f} e supera os 30% do seu salario')