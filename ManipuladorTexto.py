num = int(input('Digite o valor: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade: ', u)
print('Dezena: ', d)
print('Centena: ', c)
print('Milhar: ', m)


name = str(input('Seu nome: '))

print(name.upper())
print(name.lower())
print(len(name.replace(' ','')))
print(len(name.split()[0]))






frase = 'o que vale é o que importa'

print(len(frase))
print(frase[::2])
print(frase.count('a'))
print(frase.count('o', 0, 12))
print(frase.find('e')) ### Valor = -1, não encontrou resultado
print(frase.replace('vale', 'troll'))
print(frase.upper())
print(frase.lower())
print(frase.strip()) ### retira espaços desnecessarios
print(frase.split()) ### corta a frase em palavras
print('-'.join(frase))
dividido = frase.split()
print(dividido[2][2])