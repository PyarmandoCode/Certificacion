import csv

def origen_datos():
    with open('Session5/data/productos.csv','r') as informacion:
        csv_leer = csv.reader(informacion)
        #todo convertir el objeto a una lista
        lista_productos = list(csv_leer)
        return lista_productos
    
    
print(origen_datos()  ) 
        