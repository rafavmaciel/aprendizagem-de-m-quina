from data_flor import FlorData
class ClasificadorFlor:
    def __init__(self, teste):
        self.listaTreino = FlorData.listaTreino
        self.teste = teste
        self.listaResultado= []


    def calcularDistancia(self):
        for lista in self.listaTreino:
            calculo = 0 
            for i in range(len(lista)-1):
                calculo =  calculo + (lista[i] - self.teste[i])**2
                if i == 3:
                    calculo = calculo **(0.5)
                    self.listaResultado.append(calculo)
        #print(self.listaResultado)
        return self.listaResultado

    def analizarResultado(self):
        mininmo = min(self.listaResultado)
        posicaoLista = self.listaResultado.index(mininmo)
        print ("o algoritimo classifica essa flor como  " + self.listaTreino[posicaoLista][4] + "  seu mínimo é : " + str(mininmo) )
        print('categoria no banco: '+self.teste[4])
        if self.listaTreino[posicaoLista][4]==self.teste[4]:
            return True

    


