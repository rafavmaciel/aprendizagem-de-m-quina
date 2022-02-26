import matplotlib.pyplot as plt
from data_flor import FlorData
from classificador_flor import ClasificadorFlor


listaTreino = FlorData.listaTreino
listaTeste = FlorData.listaTeste
listaDistancias = []
cont = 0 
for i in listaTeste: 
    i1=ClasificadorFlor(i)
    dist = i1.calcularDistancia()
    listaDistancias.append(dist)
    if i1.analizarResultado() == True:
        cont = cont + 1
    print ('\n')
#print(listaDistancias)
print("taxa de acertos " + str(cont) +" de :"+str(len(FlorData.listaTeste))
)
