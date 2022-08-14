import random

a1 = input('1º aluno: ')
a2 = input('2º aluno: ')
a3 = input('3º aluno: ')
a4 = input('4º aluno: ')

list = [a1, a2, a3, a4]
rand = random.choice(list)
ord = random.shuffle(list)

print('O aluno sorteado foi o: ',rand)
print('list ordenada dos escolinhos: \n', list)


import math
from math import sqrt,floor

num = int(input('Digite um valor: '))
raiz = math.sqrt(num)

print('A raiz de', num, 'é', raiz)

