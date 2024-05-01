'''
Tarefa: Dado um número inteiro N, imprima seu primeiro Dado um número inteiro, N, imprima seu primeiro 10 múltiplos. 
Cada múltiplo N x i que deve ser impresso em uma nova linha no formato: N x i = result.
Formato de entrada:
Um único número inteiro, N.
Restrições:
2 < N <  20
Formato de saída:
Imprimir 10 linhas de saída; cada linha contém o resultado  de N x i na forma:
N x i = result.
'''

def dez_multiplos_N():
    numero = int(input('Digite um número entre 2 e 20: '))
    if 2 < numero < 20:
        print(f"Os primeiros 10 múltiplos de {numero} são:")
        for indice in range(1, 11):
            print(f"{numero} * {indice} = {numero * indice}")
    return print("Número inválido. Por favor, digite um número entre 2 e 20.")

dez_multiplos_N()