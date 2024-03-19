def soma_horas(*horas):
    total_segundos = 0

    # Iterar sobre todas as horas fornecidas
    for hora in horas:
        # Converter as horas no formato "0000" para o formato "HH:MM:SS"
        if len(hora) == 4:
            hora = hora[:2] + ':' + hora[2:] + ':00'
        
        # Separar as horas, minutos e segundos de cada hora
        h, m, s = map(int, hora.split(':'))
        
        # Converter tudo para segundos e somar
        total_segundos += h * 3600 + m * 60 + s

    # Calcular o total de horas, minutos e segundos
    horas_totais = total_segundos // 3600
    minutos_totais = (total_segundos % 3600) // 60
    segundos_totais = total_segundos % 60

    # Retornar o resultado formatado
    return '{:02d}:{:02d}:{:02d}'.format(horas_totais, minutos_totais, segundos_totais)

# Exemplo de uso
horas = []
while True:
    hora = input("Digite uma hora (HHMM ou HH:MM:SS) ou deixe em branco para terminar: ")
    if hora == "":
        break
    horas.append(hora)

resultado = soma_horas(*horas)
print("A soma das horas é:", resultado)
