
import opciones

if __name__=="__main__": #Menú Principal

    option = 0
    while option!=4:
        print("1) Obras\n2) Usuarios\n3) Préstamos\n4) Salir\n")
        op=input("\nSeleccionar opción: \n")

        if (op.isdigit()):
            option=int(op)
            if option == 1:
                print("Ha seleccionado Obras: ")
                opciones.obra()


            elif option == 2:
                print("Ha seleccionado Usuarios: ")
                opciones.user()

            
            elif option == 3:
                print("Ha seleccionado Prestamos: ")
                opciones.presta()
            elif option == 4:
                print("Gracias por usar el programa! ")

            else:
                print("Opción Incorrecta.")
        else:
            ("Opción Incorrecta.")
