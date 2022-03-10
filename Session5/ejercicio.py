from datos import *
from utilitarios import *
#from datetime import datetime


#print(datetime.year(datetime.now()))


def main():
    resp=""
    encontrar=False
    año_actual=2022
    listado=registro_pre()
    while True:
        dni = input("Ingresar al DNI:")
        for item in listado:
            if dni in item['dni']:
                edad = año_actual - item['nac']
                if edad>=18 and item['dosis'] == 3:
                    item['asiento']=generar_numero_asiento()
                    print(f'Se le asigno el asiento {item["asiento"]} a la persona {item["fullname"]} ')
                    encontrar=True
                    break
                else:
                    print("La Persona no cumple con uno de los requisitos")
                    encontrar=True
                    break
            else:
                encontrar=False
        if encontrar == False:
            print("No se encontro el DNI de esa la persona")
        resp = input("Desea Continuar con el proceso <S/N>:")
        if resp == "N":
            print(listado)
            break    
                        
                
#main()            
    
 