#A
import unicodedata

import numpy as np
#U = string
municipios = np.loadtxt("50376.csv", delimiter=";", usecols = (0), skiprows=1, dtype="U")
fenomeno = np.loadtxt("50376.csv", delimiter=";", usecols = (1), skiprows=1, dtype="U")
#unicodedata.normalize('NFKD', fenomeno).encode('ASCII', 'ignore')
total = np.loadtxt("50376.csv", delimiter=";", usecols = (2), skiprows=1, dtype="i",
                   converters={2: lambda s:str(s.decode()).replace(".","")})


filtered_index5 = fenomeno == "nacidos vivos por residencia materna"

print(total[filtered_index5])

#Serie ordenada de fallecidos por el lugar de residencia
filtered_index2 = fenomeno == "fallecidos por el lugar de residencia"
fallecidos = np.sort(total[filtered_index2])

print(fallecidos)

#Media y DevEst de los 5 indicadores disponibles por Municipio

for fenom in np.unique(fenomeno):
    medias = str(np.round(np.mean(total[fenomeno == fenom]), decimals=2))
    ds = str(np.round(np.std(total[fenomeno == fenom]), decimals=2))
    print(fenom + ': Media ' + medias + ', Desv. Est. ' + ds)

