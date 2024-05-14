'''Exercicio feito em Python 
https://www.hackerrank.com/challenges/migratory-birds/problem

'''


def migratoryBirds(arr):
    passaros_Cont = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

    for passaro in arr:
        passaros_Cont[passaro] += 1

    maisPassaro = 1
    for i in range(2, 6):
        if passaros_Cont[i] > passaros_Cont[maisPassaro]:
            maisPassaro = i

    return maisPassaro

# Exemplo de uso:
arr = [3, 5, 2, 1, 3, 4]
print(migratoryBirds(arr))  
