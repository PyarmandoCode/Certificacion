
sumtotal=0
while True:
    producto=input("Ingrese  el producto a comprar:")
    precio=float(input("Ingrese el precio  del producto:"))
    cantidad=int(input("Ingrese la cantidad a comprar:"))
    subtotal=precio*cantidad
    sumtotal=sumtotal+subtotal
    msj=input("Desea añadir mas productos a la cesta:?(S/N)")
    if msj.upper()=="N":
        print(f'Total a pagar {sumtotal}')
        break