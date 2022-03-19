unacadena=" python certificacion "
otrocadena='preparacion para el examen'

print(unacadena[2]) # todo susbtraer la segunda posicion de la cadena
#todo tmar del caracter 2 al 5 incluido
print(unacadena[2:5])
print(unacadena[-5:-2])
#todo longitud de la cadena
size= len(unacadena.strip()) #todo eliminar espacios en blanco
print(size)
#todo mayusculas y minusculas
print(unacadena.lower()) #todo minuscula
print(unacadena.upper()) #todo mayuscula

#todo remplazar caracteres de una cadena
version_python="PYTHON 3.10"
print(version_python.replace("3.10","3.10.3"))
mensaje="python pcap"
#todo colcoar mayusculas a la primera letra
print(mensaje.capitalize())

#todo contabilizr el numero de ocurrencias de una subcadena
cadena="siguiente cadena de texto cadena"
print(cadena.count("cadena"))

#todo me devuelve el index de una subcadena a buscar
print(cadena.find("cadena"))

#todo crear particiones de una cadena
sub=cadena.partition("cadena")
print(sub)

# Alfanumericos (.isalnum())
# Alfabeticos (.isalpha())
# Numero (.isdigit())
# Letra May (.isupper())
# Letra Min (.islower())
# Espacios (.isspace())
# Numericos (.isnumeric())


x="23"
if x.isdigit():
    print("la cadena contiene numeros en su contenido")
else:
    print("no contiene digitos en su contenido")    


