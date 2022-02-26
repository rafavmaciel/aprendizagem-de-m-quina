from data_flor import FlorData
class ClasificadorFlor:
    def __init__(self, teste):
        self.listaTreino = FlorData.listaTreino
        self.teste = teste
        self.listaResultado= []
        self.vizinhosMinimos = []
        self. valorVizinhosMinimos = []
        self.listaDeClassificacaoComPeso = []

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
        for i in range(7):
            mininmo = min(self.listaResultado) #pega o mínimo 
            self.valorVizinhosMinimos.append(mininmo) # adiciona a lista de valores dos minimos 
            posicaoLista = self.listaResultado.index(mininmo) # pega o indice na lista  do valor minimo  
            self.vizinhosMinimos.append(self.listaTreino[posicaoLista]) # adiciona a lista de nomes dos minimos 
            del(self.listaResultado[posicaoLista]) # deleta o minimo atual 
            if self.listaTreino[posicaoLista][4]==self.teste[4]:
                return True
        print('')
        print('\n valor dos vizinhos mínios'+str(self.valorVizinhosMinimos)+"\n")
        print()
        print(str(self.vizinhosMinimos))

    def classificarSeteVizinhos(self):
        irisSetosa = 0
        irisVersicolor = 0
        irisVirginica = 0
        for vizinho in self.vizinhosMinimos:
            if str(vizinho[4]) == 'Iris-setosa':
                irisSetosa = irisSetosa + 1
            elif str(vizinho[4]) == 'Iris-versicolor':
                irisVersicolor = irisVersicolor + 1
            else:
                irisVirginica = irisVirginica + 1
        print('\n')
        print(' Resultado :')
        print('Iris-setosa ' + str(irisSetosa))
        print('Iris-versicolor ' + str(irisVersicolor))
        print('irisVirginica ' + str(irisVirginica))
        print('classe do teste de acordo com a base de dados :'+self.teste[4])


    def analizarResultadoComPeso(self):
        
        for i in range(7):
            mininmo = 1/min(self.listaResultado) #pega o mínimo 
            self.valorVizinhosMinimos.append(mininmo) # adiciona a lista de valores dos minimos 
            posicaoLista = self.listaResultado.index(mininmo) # pega o indice na lista  do valor minimo  
            self.vizinhosMinimos.append(self.listaTreino[posicaoLista]) # adiciona a lista de nomes dos minimos
            self.listaDeClassificacaoComPeso.append([mininmo,self.listaTreino[posicaoLista][4]]) 
            del(self.listaResultado[posicaoLista]) # deleta o minimo atual 
            
        print('\n valor dos vizinhos mínios com peso'+str(self.valorVizinhosMinimos)+'\n')
        print(str(self.listaDeClassificacaoComPeso))
    

    def classificarVizinhosComPeso(self):
        irisSetosa = 0
        irisVersicolor = 0
        irisVirginica = 0
        for vizinho in self.listaDeClassificacaoComPeso:
            if str(vizinho[1]) == 'Iris-setosa':
                irisSetosa = vizinho[0] + irisSetosa
            elif str(vizinho[1]) == 'Iris-versicolor':
                irisVersicolor = irisVersicolor + vizinho[0]
            else:
                irisVirginica = irisVirginica + vizinho[0]
        print('\n')
        print(' Resultado :')
        print('Iris-setosa ' + str(irisSetosa))
        print('Iris-versicolor ' + str(irisVersicolor))
        print('irisVirginica ' + str(irisVirginica))
        print('classe do teste de acordo com a base de dados :'+self.teste[4])


        


