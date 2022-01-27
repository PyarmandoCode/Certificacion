#----Palabras Reservadas------#
import keyword
#print(keyword.kwlist)
print(keyword.iskeyword("Pass"))

#--Tipos de Formato en PYTHON---#
#--Cast -- Convertir a otro tipo de datos
pizza=int(input("Hola , ¿Cuantas rebanadas de pizzas trajiste..?"))
comidas=int(input("¿Y Cuantas rebanadas de comieron..?"))
print(f'Si Trajiste {pizza} rebanadas de pizza y se comieron {comidas} , quedan {pizza - comidas} rebanadas')


