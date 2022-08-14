n = int(input("Fatorial de: "))

resul = 1
for n in range(1,n+1):
    resul *= n

print(resul)

'''
#Ou define a função 

def fatorial(n):
    fat = 1

    while n > 1:
        fat = n * fat
        n -= 1
    return fat

def numero_binomial(n, k):
    return fatorial(n) / (fatorial(k) * fatorial(n-k))

'''