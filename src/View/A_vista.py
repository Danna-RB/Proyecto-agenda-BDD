def Mostrarmenu():

    print(" AGENDA ---------  ") 
    print("1. Agendar contacto") 
    print("2. Buscar contacto")  
    print("3. Eliminar contacto") 
    print("4. Mostrar contactos") 
    print("5. Salir")


def Pedirdatos():

    print("Contacto nuevo: ")  

    id = input("ID: ")  
    nombre = input("Nombre: ") 
    apellido = input("Apellido: ")  
    fecha = input("Fecha nacimiento: ") 
    sexo = input("Sexo: ")  
    telefono = input("Telefono: ") 

    return id, nombre, apellido, fecha, sexo, telefono  # retorna todos los datos


def Pedirid():

    id = input("Ingrese ID: ")  # pide el ID
    return id  # retorna el ID


def Mostrarcontacto(r):

    if r:  #si existe registro
        print("ID:", r[0])  #muestra ID
        print("Nombre:", r[1])  #muestra nombre
        print("Apellido:", r[2])  #muestra apellido
        print("Fecha:", r[3])  #muestra fecha
        print("Sexo:", r[4])  #muestra sexo
        print("Telefono:", r[5])  #muestra telefono
    else:
        print("Contacto no encontrado") 


def Mostrarlista(registros):

    for r in registros:  # recorre todos los registros
        print("")
        print("ID:", r[0])  # muestra ID
        print("Nombre:", r[1])  # muestra nombre
        print("Apellido:", r[2])  # muestra apellido
        print("Telefono:", r[5])  # muestra telefono


