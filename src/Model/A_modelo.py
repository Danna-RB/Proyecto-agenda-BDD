archivoDatos = "src/Persistencia/agenda.agp" 

def Guardar_Registro(id, nombre, apellido, fecha, sexo, telefono):
    
    registro = f"{id};{nombre};{apellido};{fecha};{sexo};{telefono}\n"

    with open(archivoDatos, "a") as archivo: 
        archivo.write(registro) 

def Leer_Registros():

    registros = []  #lista donde se guardan todos los registros

    try:
        with open(archivoDatos, "r") as archivo:

            for linea in archivo: 
                datos = linea.strip().split(";")  #elimina salto de linea y separa los datos por ;
                registros.append(datos)  #guarda el registro 

    except FileNotFoundError:  #si el archivo no existe
        pass

    return registros  #retorna todos los r


def buscarRegistro(id_buscar):

    registros = Leer_Registros() 

    for r in registros: 
        if r[0] == id_buscar: 
            return r  

    return None  


def eliminarRegistros(id_eliminar):

    registros = Leer_Registros() 
    nuevos = []  #lista para guardar registros que no se eliminan

    eliminado = False  # para saber si se elimino algo

    for r in registros: 
        if r[0] != id_eliminar: 
            nuevos.append(r)
        else:
            eliminado = True  

    with open(archivoDatos, "w") as archivo:  #abre el archivo en modo sobrescritura
        for r in nuevos:  #recorre los registros restantes
            linea = ";".join(r) + "\n"  #vuelve a crear la l
            archivo.write(linea)  #escribe el registro

    return eliminado