#Dia 02-100

'''
Desenvolva um algoritmo que verifique se um número é um quadrado perfeito e retorne se é verdadeiro ou falso.
Regra adicional: faça esse número ser gerado aleatoriamente, mas o converta para o inteiro mais próximo.

'''

import random
def verifica_quadrado_perfeito():
    numero_aleatorio= round(random.random()*1000) #Gera um numero aleatorio entre 1 e 1000 e arredonda ele
    numero_inteiro= round(numero_aleatorio) #Basicamente converter para o inteiro mais proximo 
    raiz_quadrada = int(numero_inteiro**0,5) #Optei por não utilizar a lib match do python, mas ficaria mais pratico
    if raiz_quadrada*raiz_quadrada == numero_inteiro:
        return print(f'O {numero_inteiro} é um quadrado perfeito')
    else:
        return print(f'O {numero_inteiro} não é um quadrado perfeito')