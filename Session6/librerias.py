import random
import math
import statistics
from datetime import date

curso=random.choice(['PYTHON','FLASK','DJANGO'])
print(curso)

#print(random.random())
#print(random.randrange(100))
#print(random.randint(10,100))

hoy= date.today()
print(hoy)
print(hoy.year)
print(hoy.day)
print(hoy.month)

print(math.pi)
print(math.sqrt(12))
print(math.cos(math.pi/4))

datos =[15,18,23,45,45,17,19,20]
print(statistics.mean(datos))
print(statistics.median(datos))
print(statistics.mode(datos))
print(statistics.variance(datos))




