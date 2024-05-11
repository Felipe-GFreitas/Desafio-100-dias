'''
Dia 14, um exercicio simples retirado do hackerank, (estou no momento utilizando a continuidade do site
para pegar os exercicios)
https://www.hackerrank.com/challenges/picking-numbers/problem?isFullScreen=true
'''


def pickingNumbers(a):
    a.sort()
    max_length = 0
    current_length = 0
    for i in range(len(a)):
        current_length = 1
        for j in range(i + 1, len(a)):
            if abs(a[j] - a[i]) <= 1:
                current_length += 1
            else:
                break
        max_length = max(max_length, current_length)
    return max_length