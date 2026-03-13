from Model import A_modelo
from View import A_vista  

def iniciar ():
    while True:  #ciclo infinito del programa
        A_vista.Mostrarmenu()  #muestra menu
        opcion = input("Seleccione opcion: ")  #pide opcion
        if opcion == "1":  #guardar contacto
            datos = A_vista.Pedirdatos()  #pide datos a la vista
            A_modelo.Guardar_Registro(*datos)  #guarda los datos en el modelo

            print("Contacto guardado") 
        elif opcion == "2":  #buscar contacto

            id = A_vista.Pedirid()  #pide ID
            r = A_modelo.buscarRegistro(id)  #busca registro
            A_vista.Mostrarcontacto(r)  #muestra resultado
        elif opcion == "3":  #eliminar contacto

            id = A_vista.Pedirid()  #pide ID
            eliminado = A_modelo.eliminarRegistros(id)  #elimina registro

            if eliminado:  #si se eliminó
                print("Contacto eliminado")
            else:
                print("No se encontró el contacto")
        elif opcion == "4": #mostrar todos

            registros = A_modelo.Leer_Registros()  #obtiene registros
            A_vista.Mostrarlista(registros)  #muestra lista
        elif opcion == "5":  #salir

            print("Saliendo del programa")  #mensaje
            break  #termina programa
        else:
            print("Opcion invalida")  #error