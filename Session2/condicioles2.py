#Averigurar si un empleado es candidato o no aun puesto en la empresa

codigo=input("Ingrese el codigo del empleado:")
categoria=int(input("Ingrese categoria:"))
antiguedad=int(input("Ingrese antiguedad:"))
respuesta=False
if categoria == 3 or categoria == 5:
    if antiguedad>=5:
        respuesta=True
elif categoria == 2 and antiguedad>=10:
    respuesta=True
if respuesta:
    resultado='reune las caracteristicas para el puesto'
else:
    resultado='no reune las caracteristicas para el puesto'
print(f'\nEl Empleado con clave {codigo} ' + resultado)      

#Dado el sueldo actual del empleado , si este es menor a $8000
#se incrementa un 12% en caso contrario , el incremento
#es del %8 una vez determinado y calculado el aumento imprimir todos los resultados

sueldo=float(input("Ingrese el sueldo del empleado: $"))
if sueldo<8000:
    aumento= sueldo * 0.12
else:
    aumento= sueldo * 0.08
nuevo_sueldo= sueldo+aumento
#print("Aumento",aumento)
#print("Nuevo Sueldo",nuevo_sueldo)    
print(f'\nAumento=${aumento:.2f} y nuevo sueldo = ${nuevo_sueldo:.2f}')    

#Python es un Lenguaje Interpretado
