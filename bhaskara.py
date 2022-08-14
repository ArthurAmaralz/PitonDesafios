a = int(input("digite o valor de A: "))
b = int(input("digite o valor de B: "))
c = int(input("digite o valor de C: "))

delta = float(b**2 - 4*a*c)

if delta > 0:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)
    if x1 > x2:
        print(f"as raízes da equação são {x2:.2f} e {x1:.2f} ")
    else:
        print(f"as raízes da equação são {x1:.2f} e {x2:.2f} ")

elif delta == 0:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    print(f"a raiz dupla desta equação é {x1:.2f}")

else:
    print("esta equação não possui raízes reais")
