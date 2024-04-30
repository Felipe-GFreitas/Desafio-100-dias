''' Criar um 
Desenvolva um programa que, com base em uma temperatura em graus celsius, 
a converta e exiba em Kelvin (K), Réaumur (Re), Rankine (Ra) e Fahrenheit.
'''

def conversao_temperatura():
    celsius=float(input('Digite a temperatuda em graus celsius: '))
    kelvin=(celsius+273.15)
    reaumur=(celsius*0.8)
    rankine=(celsius*1.8) + 491.67
    fahrenheit= (celsius*1.8)+32
    return print(f'A temperatura em kelvin {kelvin:.2f}, réamur{reaumur:.2f}, rankine{rankine:.3f}, fahrenheit{fahrenheit:.2f}')

conversao_temperatura()
