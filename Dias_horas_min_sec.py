n = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = int(n // 86400)
horas = int((n-(dias*86400)) // 3600)
minutos = abs(int(((n-(dias*86400)) // 60) - (60*horas)))
segundos = abs(int(((n-(dias*86400)) % 3600) - (60*minutos)))

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")