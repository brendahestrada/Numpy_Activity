## Tecnologías para el Análisis de Datos Masivos
***
### A. Datos demográficos por Municipio y fenómeno de las Islas Baleares

```python
import numpy as np
import matplotlib.pyplot as plt
```

Series por nacidos vivos por residencia materna:

El municipio con menor número de nacidos vivos es de 1, mientras que el de mayor número es de 3345

```python
filtered_index5 = fenomeno == "nacidos vivos por residencia materna"
print(total[filtered_index5])

[  70   47  178   58  109    6   57    3   62   10   50  340   20  100
  109   41  208   35   14    5  434    3   35    1  186   39   91    4
  334   16   58   24  277  445   13  239   19  264   33    6   22   77
 3345   26  170  130   50   13   34  230   23   52  237   61   37    8
  303   92   63   86   33   28   32   94  104   13   49]

```

Serie ordenada de fallecidos por el lugar de residencia:

El municipio con mayor numero de fallecidos es de 3355, superior incluso, que al municipio con mayor número de nacidos vivos 

```python
filtered_index2 = fenomeno == "fallecidos por el lugar de residencia"
fallecidos = np.sort(total[filtered_index2])
print(fallecidos)

[   0    2    3    3    3    4    7    8   10   10   11   12   12   17
   23   24   25   28   28   29   30   30   30   30   31   39   41   42
   42   43   44   45   46   49   52   52   55   55   58   59   64   65
   65   71   85   91   94  103  108  108  110  128  131  134  141  151
  172  189  200  218  219  229  246  294  315  341 3355]

```

Media y DevEst de los 5 indicadores disponibles por Municipio:

El indicador con mayor variación es el de nacidos vivos por residencia materna, con una media de 141.12, lo que explica 
La gran diferencia entre los totales de los municicpios con rangos desde 1:3345
El indicador con menos variación en sus totales por municipio es el de muertes fetales tarías por residencia con una
desviación d 2.04 y una media de 0.6, lo que indica bajos totales.

```python
for fenom in np.unique(fenomeno):
    medias = str(np.round(np.mean(total[fenomeno == fenom]), decimals=2))
    ds = str(np.round(np.std(total[fenomeno == fenom]), decimals=2))
    print(fenom + ': Media ' + medias + ', Desv. Est. ' + ds)

crecimiento vegetativo: Media 13.37, Desv. Est. 32.63
fallecidos por el lugar de residencia: Media 127.75, Desv. Est. 405.29
matrimonios por el lugar en que han fijado residencia: Media 44.18, Desv. Est. 135.04
muertes fetales tardías por residencia materna: Media 0.6, Desv. Est. 2.04
nacidos vivos por residencia materna: Media 141.12, Desv. Est. 408.25
```

### B.  Análisis de la lista de ventas de multiples viviendas seleccionadas con alquiler regulado donde puede haber potencial para la especulación


```python
distrito = np.loadtxt("data/Speculation_Watch_list.csv", delimiter=";", usecols = (0), skiprows=1, dtype="U")
num_distrito = np.loadtxt("data/Speculation_Watch_list.csv", delimiter=";", usecols = (1), skiprows=1, dtype="i")
precio = np.loadtxt("data/Speculation_Watch_list.csv", delimiter=";", usecols = (11), skiprows=1, dtype="i")
```

Listado del total de viviendas vendidas:

Existe una gran diferencia entre el total de ventas del distrito QN y SI, respecto al resto. Mientras que entre estos didstritos
se transaccionaron únicamente 67 viviendas, el el resto de distritos se concentran la mayor parte de las ventas, teniendo
como líder del mercado a 'MN' con un total de 165 viviendas vendidas.

```python
(unique, counts) = np.unique(distrito, return_counts=True)
print(f'Distritos: {unique}\nViviendas vendidas: {counts}')

Distritos: ['BK' 'BX' 'MN' 'QN' 'SI']
Viviendas vendidas: [156 147 164  63   4]

```

Histograma del precio de todas las viviendas vendidas:

Podemos observar como mientras un total de 379 viviendas se encuentran en el rango de 500000 (que es mas de la mitad de las
viviendas vendidas, el precio mayor de las transacciones se centra unicamente en una casa con un total de 90000000)

```python
hist, bin_edges = np.histogram(precio)
print(hist)
print(bin_edges)
print(np.sum(hist))
_ = plt.hist(precio, bins='auto')  # arguments are passed to np.histogram
plt.title("Histogram del precio de las viviendas vendidas")
plt.show()

[379 107  30   5   7   1   2   1   1   1]
[  500000.  9450000. 18400000. 27350000. 36300000. 45250000. 54200000.
 63150000. 72100000. 81050000. 90000000.]
534
![Image text](Imagen1.png?raw=true)

```

Cual es el preico máximo y minimo por el que se vendieron viviendas en el bloque con mayores ventas?:

Podemos identificar que este distrito contiene la venta de la casa mas cara en todo nuestro data set, mientras que la mas
"barata" se vendió por unt otal de 2550000

```python
MN = precio[distrito == "MN"]
print("El precio máximo por el que se vendió una vivienda es de ", np.amax(MN))
print("El precio mínimo por el que se vendió una vivienda es de ", np.amin(MN))

El precio máximo por el que se vendió una vivienda es de  90000000
El precio mínimo por el que se vendió una vivienda es de  2550000

```
El precio medio por distrito es:

Podemos concluir que el distrito que integran las viviendas mas "exclusivas" y caras es definitivamente MN, con una media de precio
superior al resto y con el mayor numero de operaciones, mientras que la que concentra menor numero de ventas es SI, la cual 
tiene igualmente el número menor de transacciones de venta. Definitivamente el mejor distrito para el mercado inmobiliario es MN

```python
for dist in np.unique(distrito):
    medias = str(np.round(np.mean(precio[distrito == dist]), decimals=2))
    print(dist + ': Media ' + medias)

BK: Media 8691022.11
BX: Media 6659420.79
MN: Media 12382693.45
QN: Media 9266994.21
SI: Media 2206250.0

```

### C. Análisis del porcentaje del Total Anual del gasto total del gobierno respecto al Producto Interno Bruto

```python
countries = np.loadtxt("data/gov_10a_exp_page_linear.csv", delimiter=",", usecols =(7), skiprows=1, dtype="U")
year = np.loadtxt("data/gov_10a_exp_page_linear.csv", delimiter=",", usecols =(8), skiprows=1, dtype="U")
total_exp = np.loadtxt("data/gov_10a_exp_page_linear.csv", delimiter=",", usecols =(9), skiprows=1, dtype="f")

```

Cual es el historial de gasto de España?

Podmeos observar como durante el último año el porcentaje del gasto en España, se ha incrementado respuescto al PIB
pasando de un 42,1 en el 2019 a un 52.4 en el año 2020. El año en el que se reportó un gasto mas bajo fue con un total 
de 41,7 porciento respecto al PIB en el 2017

```python
hist_ES = total_exp[countries == 'ES']
fig, ax = plot.subplots()
ax.plot(hist_ES)

[<matplotlib.lines.Line2D at 0x7fcfe1145550>]
![Image text](https://http://raw.github.com/brendahestrada/Numpy_Activity/blob/main/Imagen2.png)

```

El gasto de los paises durante el último año con registro 2020:

El país con el porcentaje del gasto rspecto a su PIB es Francia, con un total del 61,6 porciento.

```python
last_exp = total_exp[year == '2020']
(unique, ctrys) = (np.unique(countries), last_exp)
print(f'País: {unique}\nGasto en el 2020: {ctrys}')

País: ['AT' 'BE' 'BG' 'CY' 'CZ' 'DE' 'DK' 'EA19' 'EE' 'EL' 'ES' 'EU27_2020' 'FI'
 'FR' 'HR' 'HU' 'IE' 'IS' 'IT' 'LT' 'LU' 'LV' 'MT' 'NL' 'NO' 'PL' 'PT'
 'RO' 'SE' 'SI' 'SK']
Gasto en el 2020: [56.7 59.2 41.8 45.1 47.2 50.8 53.5 53.5 45.9 59.8 52.4 52.9 57.5 61.6
 54.5 51.6 27.4 50.5 57.1 42.9 47.2 43.1 45.9 47.8 58.5 48.7 49.3 41.5
 52.1 51.3 45.6]

```

Cual es la media y la mediana del gasto por país?:

Observando los datos, podemos concluir que el país con una Mediana y Media superior que el resto es Francia, 
Mientras que el país con menor Media y Mediana es Irlanda.

```python
for country in np.unique(countries):
    medias = str(np.mean(total_exp[countries == country]))
    medianas = str(np.median(total_exp[countries == country]))
    print(country + ': Media ' + medias + ', Mediana ' + medianas )
    
AT: Media 51.579998, Mediana 51.15
BE: Media 54.466667, Mediana 53.7
BG: Media 37.72222, Mediana 36.9
CY: Media 41.71111, Mediana 42.2
CZ: Media 42.17778, Mediana 41.9
DE: Media 45.21111, Mediana 44.4
DK: Media 53.1, Mediana 53.0
EA19: Media 48.855556, Mediana 48.4
EE: Media 39.800003, Mediana 39.4
EL: Media 53.21111, Mediana 50.7
ES: Media 44.81111, Mediana 43.9
EU27_2020: Media 48.488888, Mediana 48.1
FI: Media 55.477776, Mediana 55.6
FR: Media 57.12222, Mediana 56.8
HR: Media 47.911114, Mediana 48.2
HU: Media 48.488888, Mediana 49.1
IE: Media 31.222221, Mediana 28.1
IS: Media 45.71111, Mediana 45.8
IT: Media 50.52222, Mediana 50.3
LT: Media 35.644447, Mediana 34.8
LU: Media 41.944443, Mediana 41.3
LV: Media 39.055557, Mediana 38.7
MT: Media 38.888885, Mediana 38.5
NL: Media 44.96, Mediana 45.449997
NO: Media 49.355553, Mediana 49.3
PL: Media 42.755554, Mediana 41.8
PT: Media 47.1, Mediana 48.2
RO: Media 36.022224, Mediana 36.0
SE: Media 50.3, Mediana 49.9
SI: Media 48.62222, Mediana 48.7
SK: Media 42.377777, Mediana 42.6

```
