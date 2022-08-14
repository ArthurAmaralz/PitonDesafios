n = int(input("Digite um número inteiro: "))
count = 0

for div in range(1,n+1):
    if n % div == 0:
        count += 1

if count > 2:
    print("não primo")
else:
    print("primo")