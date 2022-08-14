larg = int(input("digite a largura:"))
alt = int(input("digite a altura:"))

while alt > 0:
    val = larg
    while larg > 0:
        print("#", end="")
        larg -= 1
    print()
    larg = val
    alt -= 1
