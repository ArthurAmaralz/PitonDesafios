def maior_primo(n):
    count = 0
    # Aqui testo se o primeiro valor é primo
    for div in range(1, n + 1):
        if n % div == 0:
            count += 1
    # Caso ele não seja, entra em loop até encontrar o maior primo antecessor ao valor atribuido a função
    if count > 2:
        while count > 2:
            n -= 1 # No loop ele vai decrementando até encontrar o primo antecesso
            count = 0 # Zerando o contador para não interferir no loop
            for div in range(1, n + 1):
                if n % div == 0:
                    count += 1
    return n

