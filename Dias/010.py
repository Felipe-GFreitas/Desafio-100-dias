import math
import os
'''
Exercicio tirado do HackerRank
https://www.hackerrank.com/challenges/encryption/problem?isFullScreen=true
'''
def encryption(s):
    L = len(s)
    rows = int(math.floor(L**(0.5)))
    columns = int(math.ceil(L**(0.5)))
    output = ""
    for i in range(columns):
        k = i
        for j in range(k,L,columns):
            output+=s[j]
        output+=" "
    return output
# Exemplo de uso:
s = "ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots"
result = encryption(s)
print(result)