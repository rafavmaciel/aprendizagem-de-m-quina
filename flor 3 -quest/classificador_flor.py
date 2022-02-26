import math
from data_flor import FlorData
class ClasificadorFlor:
    def __init__(self, teste):
        self.listaTreino = FlorData.listaTreino
        self.teste = teste
        self.listaResultado= []


    def calcularDistancia(self,n):
        for lista in self.listaTreino:
            calculo = 0 
            for i in range(len(lista)-1):
                calculo =  calculo + abs((lista[i] - self.teste[i])**n)
                if i == 3:
                    calculo = calculo **(1/n)
                    self.listaResultado.append(calculo)
       
        return self.listaResultado

    def analizarResultado(self):
        mininmo = min(self.listaResultado)
        posicaoLista = self.listaResultado.index(mininmo)
        print ("o algoritimo classifica essa flor como  " + self.listaTreino[posicaoLista][4] + "  seu mínimo é : " + str(mininmo) )
        print('categoria no banco: '+self.teste[4])
        if self.listaTreino[posicaoLista][4]==self.teste[4]:
            return True

    


