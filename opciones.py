#Utilicé este conjunto de menúes para dividir el código en módulos y poder leerlo mejor

import biblio
import prestamod

def obra(): #Este es un menu que engloba todas las funciones sobre "obra"

    optionObra = 0

    while optionObra != 1:

        print("1) Volver atrás\n2) Añadir obra\n3) Mostrar obras\n4) Buscar obra\n5) Modificar obra\n6) Borrar obra\n7) Borrar todo\n")
        op=input("\nIngresar una opción:\n")

        if op.isdigit():
            optionObra=int(op)

            if optionObra == 1:
                print("Usted ha regresado.\n")
            elif optionObra == 2:
                biblio.add_obra()
            elif optionObra == 3:
                biblio.show_obra()
            elif optionObra == 4:
                biblio.search_obra()
            elif optionObra == 5:
                biblio.modify_obra()
            elif optionObra == 6:
                biblio.delete_obra()
            elif optionObra == 7:
                biblio.deleteall_obra()
            else:
                print("Ingresar opción válida")
        else:
            print("Ingresar un número")

def user(): #Este es un menu que engloba todas las opciones del usuario

    optionUser = 0

    while optionUser != 1:

        print("1) Volver atrás\n2) Añadir User\n3) Mostrar Users\n4) Buscar User\n5) Modificar User\n6) Borrar User\n7) Borrar todo\n")
        op=input("\nIngresar una opción:\n")

        if op.isdigit():
            optionUser=int(op)

            if optionUser == 1:
                print("Usted ha regresado.\n")
            elif optionUser == 2:
                biblio.add_user()
            elif optionUser == 3:
                biblio.show_user()
            elif optionUser == 4:
                biblio.search_user()
            elif optionUser == 5:
                biblio.modify_user()
            elif optionUser == 6:
                biblio.delete_user()
            elif optionUser == 7:
                biblio.deleteall_user()
            else:
                print("Ingresar opción válida")
        else:
            print("Ingresar un número")

def presta(): #Este es un menu que engloba todas las opciones de préstamo

    optionPresta = 0

    while optionPresta != 1:

        print("1) Volver atrás\n2) Añadir Préstamo\n3) Devolucion Préstamo\n4) Mostrar Préstamos\n5) Borrar Préstamo\n6) Borrar todos los préstamos\n")
        op=input("\nIngresar una opción:\n")

        if op.isdigit():
            optionPresta=int(op)

            if optionPresta == 1:
                print("Usted ha regresado.\n")
            elif optionPresta == 2:
                prestamod.create_prestamo()
            elif optionPresta == 3:
                prestamod.fecha_devolcion()
            elif optionPresta == 4:
                prestamod.show_all_prestamos()
            elif optionPresta == 5:
                prestamod.delete_prestamo()
            elif optionPresta == 6:
                prestamod.delete_all_prestamos()
                print("Exitosamente borrado")
            else:
                print("Ingresar opción válida")
        else:
            print("Ingresar un número")