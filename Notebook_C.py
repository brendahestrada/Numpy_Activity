#C
import numpy as np


countries = np.loadtxt("gov_10a_exp_page_linear.csv", delimiter=",", usecols =(7), skiprows=1, dtype="U")
year = np.loadtxt("gov_10a_exp_page_linear.csv", delimiter=",", usecols =(8), skiprows=1, dtype="U")
total_exp = np.loadtxt("gov_10a_exp_page_linear.csv", delimiter=",", usecols =(9), skiprows=1, dtype="f")

#print(np.unique(year))
#Que país obtuvo mayor gasto en el 2021?

#Cual es el historial de gasto de España?
hist_ES = total_exp[countries == 'ES']

import matplotlib.pyplot as plot

fig, ax = plot.subplots()
ax.plot(hist_ES)


#Grafica por pais del gasto en el 2020
last_exp = total_exp[year == '2020']
(unique, ctrys) = (np.unique(countries), last_exp)
print(f'País: {unique}\nGasto en el 2020: {ctrys}')

#plt.hist(last_exp, bins= unique)
#plt.title("Gasto del año 2020")
#plt.show()

#Cual es la media y la mediana del gasto por país?


for country in np.unique(countries):
    medias = str(np.mean(total_exp[countries == country]))
    medianas = str(np.median(total_exp[countries == country]))
    print(country + ': Media ' + medias + ', Mediana ' + medianas )

