import matplotlib.pyplot as plt
from data_flor import FlorData
from classificador_flor import ClasificadorFlor
from collections import Counter

listaTreino = FlorData.listaTreino
listaTeste = FlorData.listaTeste
listaDistancias = []

# for i in listaTeste: 
#     i1=ClasificadorFlor(i)
#     dist = i1.calcularDistancia()
#     listaDistancias.append(dist)
#     i1.analizarResultado()
#     print ('\n')
# print(listaDistancias)




# 3NN
for i in listaTeste: 
    lista3NN = []
    i1=ClasificadorFlor(i)
    dist = i1.calcularDistancia()
    listaDistancias.append(dist)
    for i in range(3): 
        lista3NN.append(i1.analizarResultado3NN())
    counts = Counter(lista3NN)
    print (counts)
    print ('\n')

