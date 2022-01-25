#print("Hola Mundo")


edad = 28
nombre_persona="Armando Ruiz"
precio=29.8
estado=True

lista_cursos=["PYTHON","DJANGO","FLASK"]
empleados={'A100':'ARMANDO','A200':'JOSE','A300':'RAUL'}
sueldos=(1900,200,1800)


#DocString
"""
print(type(edad))
print(type(nombre_persona))
print(type(precio))
print(type(estado))
print(type(lista_cursos))
print(type(empleados))
print(type(sueldos))
"""

persona_info= {
    'nombre':'Armando',
    'apellido':'Ruiz',
    'pais':'Perú',
    'ciudad':'Lima'
}

first_name,last_name,country = 'Armando','Ruiz','Perú'

#Oeradores Matematicos
"""
print(5/3) # Division Decimal
print(5//3) # Division Enterera
print(23 % 2) # Residuo de la Division
"""
#Operadores Logicos
# != Diferente
# == Igual
# not Negacion

"""
print(not 3>2) # Falso
print(not not False) #Verdadero
print(3>2 and 4>3) #Verdadero
print(3<2 or 4<3) #Falso
print(True == True) #Verdadero
"""

#Conversiones ==CAST
"""
print(str(23)) # '23'
print(float(23)) #23.0
print(str(True)) #'True'
print(bool(0)) # True
"""

#Concatenacion
mentor="Armando"
curso="Python"
edad=45
salario=1700
precio=2.78854545458

#print(mentor+curso)
#print("%s %s" %(mentor,curso))
#print("%s %d" %(mentor,edad))
#print("El Mentor {} Tiene {}".format(mentor,edad) )
#print("El producto que desea comprar {} cuesta {}".format(mentor,precio))
#print("El producto cuesta %.2f" %(precio))

#Separadores Tabularadores Y Saltos Linea
#print("hola","mundo",sep='<->')
#print("hola",end="")
#print("mundo")

#print("Salto de Linea \n\n")
#print("\t tabulador \n\n")
#print("comillas. comillas dentro: \"Hola\" ")

#Entrada de datos por consola 
n1=int(input("ingrese el numero uno:"))
n2=int(input("ingrese el numero dos:"))
sumar=n1+n2
print(sumar)

