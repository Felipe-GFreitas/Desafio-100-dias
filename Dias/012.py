'''
Esse exercicio originalmente estava em Java, mas tentei resolver usando 
Python :D
https://www.hackerrank.com/challenges/java-comparator/problem?isFullScreen=true
'''

class Checker:
    def compare(self, a, b):
        if a.score == b.score:
            return (a.name > b.name) - (a.name < b.name)
        else:
            return b.score - a.score


'''No caso originalmente era apenas para criar a classe check, e mantive apenas ela dai'''