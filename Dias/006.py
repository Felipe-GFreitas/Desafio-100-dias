''' 
Exercicio envolvendo coisas sobre classe:
Criar uma classe para rempresentar uma SmartTV onde:
1-Ela tenha as caracteristicas : ligada (boolean), canal (int), e volume (int)
2-Nossa TV poderá ligar e desligar assim que mudar o estado ligada;
3-Nossa TV aumentará e diminuirá o volume sempre em +1 ou -1
4-Nossa TV poderá mudar de canal de 1 em 1 ou definindo o numero correspondente
'''

class SmartTv:
    def __init__(self) :
        self.ligada = False
        self.canal = 1
        self.volume = 15

    def ligar (self):
        self.ligada = not self.ligada
    
    def aumentar_volume(self):
        if self.ligada and self.volume <100:
            self.volume +=1
    
    def diminuir_volume(self):
        if self.ligada and self.volume >0:
            self.volume -=1
    
    def proximo_canal(self):
        if self.ligada and self.canal <201:
            self.canal +=1
    
    def canal_anterior(self):
        if self.ligada and self.canal >1 :
            self.canal -=1

    def mudar_canal(self,canal):
        if  self.ligada and 1 <= canal <=201:
            self.canal = canal
