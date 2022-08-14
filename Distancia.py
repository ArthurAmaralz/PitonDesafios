x1 = int(input("digite o x1º numero: "))
y1 = int(input("digite o y1º numero: "))
x2 = int(input("digite o x2º numero: "))
y2 = int(input("digite o y2º numero: "))

d = ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)

if d >= 10:
    print("longe")
else:
    print("perto")
