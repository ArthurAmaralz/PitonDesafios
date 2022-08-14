n = int(input("Digite um número inteiro: "))
adj = validador = 0
adj_ok = False

while n != 0:
    adj = n % 10
    validador = n % 100 // 10
    if adj == validador:
        adj_ok = True
    n = n // 10

if adj_ok:
    print("sim")
else:
    print("não")
