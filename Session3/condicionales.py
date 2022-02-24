"""
CATEGORIA--
RECURSOS_HUMANOS=3
CONTABILIDAD=5
SISTEMAS=2
"""

codigo=input("Ingrese el codigo:")
categoria=int(input("Ingrese la categoria:"))
antiguedad=int(input("Ingrese la Antiguedad"))
respuesta=False
if categoria == 3 or categoria == 5:
    if antiguedad>=5:
        respuesta=True
elif categoria==2 and antiguedad>=10:
    respuesta=True
if respuesta:
    resultado="Reune las caracteristias para el puesto"
else:
    resultado="No Reunes las caracteristicas para el puesto"
print(f'El Empleado con codigo {codigo}' , resultado)                    
