'''
Exercicio tirado de:
https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true
'''

def staircase(n):
    for i in range(1, n + 1):
        espaco = " " * (n - i)
        escada = "#" * i
        print(espaco + escada)

# Exemplo de uso:
n = 9
staircase(n)