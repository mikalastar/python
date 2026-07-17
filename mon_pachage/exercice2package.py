
#math
import math
n = int(input("Entrez un nombre entier positif: "))
print(math.factorial(n))

from math import sqrt
n = int(input("Entrez un nombre entier positif: "))
print(sqrt(n))

#random
import random
#randrange(start, stop, step) : renvoie un nombre aléatoire compris entre start et stop (exclus) avec un pas step
n= random.randrange(0, 101 , 2)
print(n)


#statistics
import statistics
md=statistics.mode([1, 2, 3, 4, 5,5, 6, 7, 8, 9,2,2,3,4,5,6,5])
#mode nous donne la valeur la plus fréquente dans une liste de nombres
print(md)
sd=statistics.stdev([1, 2, 3, 4, 5,5, 6, 7, 8, 9,2,2,3,4,5,6,5])
#stdev nous donne l'écart type d'une liste de nombres
print(sd)


import datetime
#datetime.datetime.now() #renvoie la date et l'heure actuelle
print(datetime.datetime.now())

from datetime import date 
# renvoie que la date actuelle
print(date.today())

from datetime import datetime
print(datetime.today())

from datetime import date
today =date.today()
print(today.strftime("%d/%m/%Y")) # permet de formater la date en jour/mois/année

from forex_python.converter import CurrencyRates
c = CurrencyRates(force_decimal=True)
print(c.convert('USD', 'INR', Decimal('10.45')))