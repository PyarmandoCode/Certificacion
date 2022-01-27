#-------Bucle For--------

for x in range(10):
   print(x,"PYTHON PCEP")

for x in range(1,11):
    if x % 2 == 0:
        print(x)

for x in range(2,10,2):
    print(x)      

#Break = Salir del Loop , Bucle , iterador
#Continue = Siga el proceso hasta el final      

for i in range(1,10):
    if i == 7:
        break
    else:
        print(i)
        continue 
print("Salir del Bucle")    

#Contadores y Acumuladores
c=0
sum=0
for i in range(5):
    valor=int(input("Ingresar Valores:"))
    c +=1         #c=c+1
    sum +=valor   #sum=sum+valor
print("Imprimiendo Totales")
print("Cantidad de valores ingesados",c)
print("Suma de esos valores",sum)

#Calcule e imprima la planilla del mes de enero del 2022 para
#Una empresa de 10 empleados
nomina=0
for i in range(1,11):
    sueldo=float(input(f'Ingrese el sueldo {i}: $'))
    nomina +=sueldo
print('\nLa Planilla total que debe pagarse es : $', nomina)    

#-------Bucle While---------------#

i=0
sum=0
while i<=100:#True
    i = i + 1
    sum=sum+i
    print(i)
print(f"La Suma de los numeros  es {sum}")    
print("Fin")    

#Escribir un Programa que contenga una contraseña inventada, que le pregunte al usuario
#La contraseña , y no le permita ingresar hasta que sea Valida
passw="PCEP"
cont=0
usuario=input("Ingrese el nmbre del Usuario:")
while True:
    con=input("Ingrese su contraseña:")
    if con==passw:
        print(f'Bienvenido al Sistema {usuario}')
        break
    else:
        cont = cont + 1
        print(f'Contraseña Errada Intento {cont}')
        if cont == 3:
            print("Supero los intentos, vuelva a intentarlo dentro de 24 horas")
            break


#Esta Libreria del Nucleo de PYTHON me permite generar numeros aleatorios(AZAR)
import random
numero_secreto=random.randint(1,100)
intentos=0
#print(numero_secreto)
while True:
    numero = int(input('Cual Es EL Numero Secreto:?'))
    intentos +=1
    if numero==numero_secreto:
        print("Acertastes !!!!!")
        print(f'Numero de intentos {intentos}')
        break
    else:
        if numero_secreto>numero:
            print(f'El Numero secreto es mayor que {numero}')
        else:
            print(f'El Numero secreto es menor que {numero}')
                







