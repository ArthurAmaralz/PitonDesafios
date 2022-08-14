larg = int(input("digite a largura:"))
alt = int(input("digite a altura:"))
cont = 0

while alt > 0:
    val = larg
    while larg > 0:
        if larg == val or larg == 1 or alt == 1 or cont == 0:
            print("#", end="")
        else:
            print(end=" ")
        larg -= 1
    print()
    larg = val
    alt -= 1
    cont +=1
