


skills= ["PYTHON","DJANGO","FLASK","VUE"]
person_info ={
    "firstaname":"Armando",
    "lastname":"Ruiz",
    "country":"Perú",
    "city":"Lima"
}

#res= [1,2] + [3,4]
#res= {1,3}+{5,6}

#Declarar multiples variables en una linea

first_name,last_name,country = 'Juan','Perez','Colombia'

#costo = float(input("Costo de la cena: $"))
#servicio = costo * 0.062
#propina = costo *0.1
#print("Costo total de la comida: $", costo+servicio+propina)
#total = costo+servicio+propina
#print("El Costo total de la comida {}".format(total))
#print(f'El Costo total de la comida {total}')

#todo concatenacion
""" %s string
%d integer
%f float
"""
first_name="Armando"
last_name="Ruiz"
country="Perú"
city="Lima"
age=46
salary=7200.934444
is_married=True

#print("%s tiene %d" %(first_name,age))
#print("el sueldo redondeado es %.2f" %salary)

#print("pepino","tomate","lechuga")
#print("pepino","tomate","lechuga",sep="")
#print("pepino","tomate","lechuga",sep=" ,")

print("\n¿Como te llamas")
nombre=input()
ciudad=input("¿Donde Vives")
edad=int(input("¿Cuantos años tienes?"))
altura=float(input("¿Cuanto mides en Metros:"))

print(f'\nLa persona de nombre {nombre} vive en {ciudad} .'
    f'\nTiene {edad} años y mide {altura} m')







