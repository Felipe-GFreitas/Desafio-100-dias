'''
Exercicio envolvendo matriz quadrada , retirado do HackerRank 
https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=false
'''
def diagonalDifference(arr):
    DiagonalEsquerda = 0
    DiagonalDireita = 0
    
    for i in range(len(arr)):
        DiagonalEsquerda += arr[i][i]
        DiagonalDireita += arr[i][len(arr) - i - 1]
    
    return abs(DiagonalEsquerda - DiagonalDireita)

# Exemplo de uso:
matrix = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]

diferenca = diagonalDifference(matrix)
print("Diferença absoluta entre as somas das diagonais:", diferenca)
