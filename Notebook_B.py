#B
import numpy as np

distrito = np.loadtxt("Speculation_Watch_list.csv", delimiter=";", usecols = (0), skiprows=1, dtype="U")
bloque = np.loadtxt("Speculation_Watch_list.csv", delimiter=";", usecols = (2), skiprows=1, dtype="U")
lote = np.loadtxt("Speculation_Watch_list.csv", delimiter=";", usecols = (3), skiprows=1, dtype="U")
precio = np.loadtxt("Speculation_Watch_list.csv", delimiter=";", usecols = (11), skiprows=1, dtype="i")

#Listado del total de viviendas vendidas:
(unique, counts) = np.unique(distrito, return_counts=True)
print(f'Distritos: {unique}\nViviendas vendidas: {counts}')

#Cual es el preico máximo y minimo por el que se vendieron viviendas en el bloque con mayores ventas?
BK = precio[distrito == "BK"]
print("El precio máximo por el que se vendió una vivienda es de ", np.amax(BK))
print("El precio mínimo por el que se vendió una vivienda es de ", np.amin(BK))

#El precio medio por distrito es:
for dist in np.unique(distrito):
    medias = str(np.round(np.mean(precio[distrito == dist]), decimals=2))
    print(dist + ': Media ' + medias)
