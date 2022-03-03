alumnos = {}
alumnos = dict()

alumnos = {'A3454':'GOMEZ','A3456':'PEREZ','A3458':'SALINAS'}

#print(alumnos)
#print(alumnos['A3456'])


person  = {
     'first_name' : 'Asabeneh' ,
     'last_name' : 'Yetayeh' ,
     'age' : 250 ,
     'country' : 'Finland' ,
     'is_marred' : True ,
     'skills' :[ 'JavaScript' , 'React ' , 'Nodo' , 'MongoDB' , 'Python' ],
     'dirección' :{
         'calle' : 'Calle espacial' ,
        'código postal' : '02210'
    }
    }

#print(person['skills'][1])
#print(person['address']['street'])

#todo accediendo a los valores del diccionario
alumnos = {'A3454':'GOMEZ','A3456':'PEREZ','A3458':'SALINAS'}
#print(alumnos['A3458'])
#print(alumnos.get('A3454'))
#print(person.get('first_name'))

#todo modificando valores de un diccionario
person['country']='Mexico'
person['skills'].append('HTML')
#print(person)

#todo chekear los valores de un diccionario
alumnos = {'A3454':'GOMEZ','A3456':'PEREZ','A3458':'SALINAS'}
#print('A3454' in alumnos) #True
#print('A3458' in alumnos) #True

#todo eliminar elementos de un diccionario

#alumnos.pop('A3454')
#alumnos.popitem()
#del alumnos['A3454']


#todo ejercicio diccionario
"""
agenda={}
salir=False

while (not salir):
    nombre=input("Ingrese un nombre:")
    telefono = input("Ingrese un telefono")
    if nombre not in agenda:
        agenda[nombre]=telefono
        print("Añadido a la agenda")
    else:
        print("El Nombre ya esta repetido")    
    respuesta= input("Quieres salir del proceso:")
    if respuesta.upper() == "S":
        salir=True
  
print(agenda)            
"""

alumnos = {'A3454':'GOMEZ','A3456':'PEREZ','A3458':'SALINAS'}
for item in alumnos.items():
    print(item)
    