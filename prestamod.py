#Acá se encuentran todas las funciones para préstamo

import biblio

from time import strftime
from datetime import datetime #Tuve que llamar el módulo datetime para crear el diccionario
#------------------------------------------------------------------- Prestamo---------------------------------------------------------------------------------------------

presta=[] #Use una lista que encierra diccionarios, en vez de un diccionario que encierra listas

def create_prestamo(): #Funcion para crear un nuevo préstamo
    biblio.show_obra()
    biblio.show_user()

    fechaini = datetime.now()

    user = input("Diga el nombre del usuario. ")
    obra = input("Ingresar la obra. ")
    
    value = {
        
        "usuario": user,
        "obra": obra,
        "fechaini": fechaini,
        "fechadev": ""
    }

    presta.append(value)

def show_all_prestamos(): #Muestra todos los prestamos hechos
    for item in presta:
        print("-----------------------------\n")
        print(f"Usuario: {item['usuario']}\n")
        print(f"Obra: {item['obra']}\n")
        print(f"Fecha de prestación: {item['fechaini'].strftime('%d/%m/%y')}\n")
        print(f"Fecha de devolución: {item['fechadev']}\n")

def fecha_devolcion(): #Crea la fecha de devolución
    show_all_prestamos() #Llama a la funcion mostrar para funcionar

    user=input("Ingresar usuario\n")
    obra=input("Ingresar obra\n")
    
    for item in presta:
        if item["usuario"] == user and item["obra"] == obra:
            fechafin = datetime(1000, 1, 1)
            
            while fechafin < item["fechaini"]:
                day, month, year = input("Ingresar fecha mayor o igual a la actual: dia mes año (ejemplo: 12/5/2022)\n").split("/")
                fechafin = datetime(int(year), int(month), int(day))            

            item["fechadev"] = fechafin.strftime('%d/%m/%y')

            print(item["fechadev"])

def delete_prestamo(): #Borra cada préstamo que sea seleccionado

    show_all_prestamos()
    index = 0
    for item in presta:
        index = index + 1
        print(index, item['usuario'], item['obra'])

    selected = input("Seleccionar cual préstamo pendiente desea eliminar. ")
    selected = int(selected) - 1

    presta.pop(selected)

def delete_all_prestamos(): #Limpia la lista de préstamo
    presta.clear()
    
        