import csv

def data_cursos():
    with open('session6/data.csv','r') as data_:
        csv_leer=csv.reader(data_)
        lista_cursos=list(csv_leer)
        return lista_cursos