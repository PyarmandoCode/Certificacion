#----Trabajar con Cadenas------------
a="certificacion PCEP entrada PYTHON , LUEGO VIENE PCAP PYTHON"
print(a[2]) #Imprime el Segundo de Caracter
print(a[2:5]) #Imprime del caracter del 2 al 5
print(a[-5]) #Imprime Desde el ultimo caracter
print(a[-5:-2])
print(len(a)) #Cuantos caractees tiene la cadena
print(a.strip()) #Elimina los espacios en blanco en los lados
print(a.lower()) #Convierte la cadena a minusculas
print(a.upper()) #convierte la cadena a mayusuculas
print(a.replace("PCEP","PCAP"))# Reemplazar Caracteres
print(a.split(",")) #Dividir en subcadenas
print(a.capitalize()) #Coloca la primera letra en mayusculas
print(a.count("PYTHON")) #Contabiliza el numero de ocurrencias de una sub
print(a.find("PYTHON")) #Busqueda de Cadenas

# Alfanumericos (.isalnum())
# Alfabeticos (.isalpha())
# Numero (.isdigit())
# Letra May (.isupper())
# Letra Min (.islower())
# Espacios (.isspace())
# Numericos (.isnumeric()) - 2 %

x="23"
if x.isdigit():
    print("La Cadena contiene numeros en su contenido")






