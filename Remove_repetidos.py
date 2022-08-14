def remove_repetidos(lista):
    clone = []
    lista.sort()
    for x in lista:
        if x not in clone:
            clone.append(x)

    return clone

