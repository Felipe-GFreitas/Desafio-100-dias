'''
https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true
'''
def timeConversion(s):
    # Separar as partes da string de tempo
    hour, minute, second = map(int, s[:-2].split(':'))
    meridian = s[-2:]
    
    # Converter para o formato de 24 horas
    if meridian == 'PM' and hour < 12:
        hour += 12
    elif meridian == 'AM' and hour == 12:
        hour = 0
    
    # Formatar a string de tempo no formato de 24 horas
    return f'{hour:02d}:{minute:02d}:{second:02d}'

# Exemplo de uso:
s = "07:05:45PM"
result = timeConversion(s)
print(result)  # Saída: 19:05:45
