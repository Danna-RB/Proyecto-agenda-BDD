from Model import A_modelo
from View import A_vista  

def iniciar ():
    while True: 
        A_vista.Mostrarmenu() 
        opcion = input("Seleccione opcion: ") 
        if opcion == "1":  #guardar contacto
            datos = A_vista.Pedirdatos()
            A_modelo.Guardar_Registro(*datos)

            print("Contacto guardado") 
        elif opcion == "2":  #buscar contacto

            id = A_vista.Pedirid()
            r = A_modelo.buscarRegistro(id)
            A_vista.Mostrarcontacto(r) 
        elif opcion == "3":  #eliminar contacto

            id = A_vista.Pedirid() 
            eliminado = A_modelo.eliminarRegistros(id)

            if eliminado:
                print("Contacto eliminado")
            else:
                print("No se encontró el contacto")
        elif opcion == "4": #mostrar todos

            registros = A_modelo.Leer_Registros() 
            A_vista.Mostrarlista(registros)
        elif opcion == "5":  #salir

            print("Saliendo del programa")
            break 
        else:
            print("Opcion invalida")