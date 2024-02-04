nombre = str(input("ingrese su nombre"))
while(nombre.isalpha() == False):
    nombre = input("ingrese su nombre")
edad = input("ingrese su edad")
while(edad.isnumeric() == False):
    edad = input("ingrese su edad")
direccion = input("ingrese su direccion")
while (direccion.isnumeric() == False and direccion.isalpha() == False):
    direccion = input("ingrese su direccion")
descripcion = input("ingrese su descripcion")
while (descripcion.isnumeric() == False and descripcion.isalpha() == False):
    descripcion = input("ingrese su descripcion")
