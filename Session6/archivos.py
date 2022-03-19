from cursos import data_cursos
    
def suma_horas(cursos):
    sumh=0
    try:
        tecn= input("Ingrese la tecnologia:")
        for item,curso,horas,tec in cursos:
            if item.isdigit() and tec==tecn :
                sumh+= int(horas)
    except Exception as err:
        print("Ocurrio un error:",err)
    else:
        print( "El Total de horas del ciclo es:",sumh)
    finally:
        return "Finalizo la funcion"        
                    
        
lst_cursos=data_cursos()
print(suma_horas(lst_cursos))        
    
#print(data_cursos())    
        