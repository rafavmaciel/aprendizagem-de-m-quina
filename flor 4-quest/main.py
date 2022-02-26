from data_flor import FlorData
from classificador_flor import ClasificadorFlor
listaTeste = FlorData.listaTeste

def processarSemPeso():
    cont = 0 
    for teste in listaTeste:
        i1=ClasificadorFlor(teste)
        i1.calcularDistancia()
        if i1.analizarResultado() == True:
            cont = cont + 1
        i1.classificarSeteVizinhos()
        print ('\n')
    print(cont)
def processarComPeso():
    for teste in listaTeste:
        i1=ClasificadorFlor(teste)
        i1.calcularDistancia()
        i1.analizarResultadoComPeso()
        i1.classificarVizinhosComPeso()
        print ('\n')
processarSemPeso()
