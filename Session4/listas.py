#todo inicializando una lista
import re


cursos = list()
cursos_back=[]

web_skills =["HTML","CSS","JS","REACT","NODE","CSS"]

#todo contar elementos de la lista
#print(len(web_skills))

#todo visualizar los elementos de la lista
#print(web_skills)
#for item in web_skills:
#    print(item)
    
#print(web_skills[0])    
#print(web_skills[5])   
web_skills[5]="CSS3"
#print(web_skills)

#todo rebanar items
fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits=fruits[0:4] #all elemnts list
all_fruits=fruits[0:1] #print 2 elements de la list
all_fruits=fruits[1:]
all_fruits=fruits[-1] #el ultimo elemento de la lista
all_fruits=fruits[-4]
all_fruits=fruits[-3:-1] #
all_fruits=fruits[-3:]
#print(all_fruits)

#todo cheking items

fruits = ['banana', 'orange', 'mango', 'lemon'] 
existe='banana' in fruits #True Or False
#print(existe)

#if 'banana' in fruits:
#    print("")
#else:
#    print("")    

#todo insertar elementos a la lista    
fruits.append("Fresa")
fruits.insert(2,"Sandia")    

#todo elimina elementos de la lista
fruits.remove('banana')
estado=fruits.pop(3)
#del fruits[0]
#del fruits
fruits.clear() #todo elimina todos los elemntos de la lista

#todo copiar listas
fruits = ['banana', 'orange', 'mango', 'lemon'] 
fruits_copy=fruits.copy()

#print(fruits_copy)

#todo unir elementos de una lista
positivos_numero=[1,2,3,4,5]
zero=[0]
negativos_numeros=[-1,-2,-3,-4]
integers=negativos_numeros+zero+positivos_numero
#print(integers)

#todo uniendo utilizando extends
num1=[0,1,2,4,5]
num2=[4,5,6]
num1.extend(num2)
#print(num1)

#todo count
fruits = ['banana', 'orange', 'banana', 'lemon']
#print(fruits.count('banana'))

#todo index
fruits = ['banana', 'orange', 'banana', 'lemon']
#print(fruits.index('orange'))

# fruta=input("Ingrese la fruta buscar:")
# if fruta in fruits:
#     vindex=fruits.index(fruta)
#     fruits.pop(vindex)
# else:
#     print("No se encontro la fruta")    

#todo elementos sort()
ages = [22, 19, 24, 25, 26, 24, 25, 24]
valores= ["A","B","C",12,14,17]
fruits.sort()
fruits.reverse()
#valores.sort()
fruits.sort(reverse=True)

#todo help
#help(list)
#help('list.index')

#todo zip 


# preguntas = ['nombre', 'objetivo', 'sistema operativo']
# respuestas = ['Leonardo', 'aprender Python y Plone', 'Linux']
# for pregunta,respuesta in zip(preguntas,respuestas):
#     print('Cual es tu {0} , la respuesta es :{1}.'.format(pregunta,respuestas))
    
#todo añadir elementos a una lista dinamicamente

lista=list()
salir=False

while(not salir):
    numero=int(input("Dame un Numero"))
    if (numero == 0):
        salir=True
        #break
    else:
        lista.append(numero)

lista.sort()
print(lista)
            








