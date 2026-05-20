a=input("ingrese contraseña: ")
b=len(a)
if b >= 8 and "clave"not in a and "123" not in a:
    print("contraseña aceptada")
else:
    print("no cumple con los requisitos")