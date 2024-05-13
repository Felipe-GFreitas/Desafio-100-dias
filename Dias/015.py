'''
Dia 15, exercicio do HackerRank, basicamente é inverter uma array
https://www.hackerrank.com/challenges/arrays-ds/problem?isFullScreen=true
'''
def reverseArray(A):
    reversed_A = []
    for i in range(len(A) - 1, -1, -1):
        reversed_A.append(A[i])
    return reversed_A
