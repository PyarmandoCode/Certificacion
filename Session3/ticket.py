total_plato=int(input("¿Total a Pagar...?"))
personas=int(input('¿Entre cuantas personas se dividira la cuenta...?'))
propina=int(input('¿Porcentaje de propina (Digite numero)...?'))
impuesto=0.19
porc_propina=propina/100
total_cuenta = print(f'''{'*'*30}
El total de la cuenta es:     
plato:\t\t ${total_plato}   
Impuesto:\t {impuesto*100} % (${impuesto*total_plato})
Propina:\t {propina}% (${porc_propina*total_plato})
Total a pagar:\t $ {total_plato + impuesto*total_plato + porc_propina*total_plato} 

Divido en:\t\t {personas} personas
Total por persona:\t ${round(((total_plato+impuesto+porc_propina)/personas),2)}
{'*'*30}
''')
                
