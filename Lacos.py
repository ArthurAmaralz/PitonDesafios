### Questão maior/menor peso ###

lst=[]
for c in range(6):
    peso=float(input(f'Peso da {c+1}ª pessoa: '))
    lst+=[peso]
print('O Maior peso foi:', max(lst))
print('O Menor peso foi:', min(lst))


### Questão  soma valores pares ###

p = 0
for c in range(6):
    s = int(input(f'Digite o {c+1}º numero: '))
    if s % 2 == 0:
        p += s
print(p)

### Questão somar impares multiplos de 3 ###
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
print(s)

### Testes ###

for c in range(0,10, 2):
    print(c)
for c in range(10,0, -1):
    print(c)
i = int(input('Inicio: '))
f = int(input('Fim:'))
p = int(input('Pula:'))
for c in range (i, f+1, p):
    print(c)
s = 0
for c in range (0, 10):
    n = int(input('Valor: '))
    s += n
print(f'Valor total: {s}')