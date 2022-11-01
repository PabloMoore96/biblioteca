#Acá se encuentran todas las funciones para préstamo

import biblio

from time import strftime
from datetime import datetime #Tuve que llamar el módulo datetime para crear el diccionario
#------------------------------------------------------------------- Prestamo---------------------------------------------------------------------------------------------

presta=[] #Use una lista que encierra diccionarios, en vez de un diccionario que encierra listas

def create_prestamo(): #Funcion para crear un nuevo préstamo
    biblio.show_users()
    username = input("Diga el nombre del usuario. ")

    biblio.show_obra()
    obra_nombre = input("Ingresar la obra. ")

    user_exist = False
    obra_exist = False
    for user in biblio.users:
        if user["nombre"] == username:
            user_exist = True
            for obra in biblio.obras:
                if obra["titulo"] == obra_nombre:
                    obra_exist = True
                    value = {
                        "usuario": user["nombre"],
                        "obra": obra["titulo"],
                        "fechaini": datetime.now(),
                        "fechadev": ""
                    }

                    presta.append(value)
    
    if not user_exist:
        print("Usuario no existente")
        
    if not obra_exist:
        print("Obra no existente") 

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
            fecha_fin = datetime(1000, 1, 1)
            
            while fecha_fin < item["fechaini"]:
                day, month, year = input("Ingresar fecha mayor o igual a la actual: dia mes año (ejemplo: 12/5/2022)\n").split("/")
                fecha_fin = datetime(int(year), int(month), int(day))            

            item["fechadev"] = fecha_fin.strftime('%d/%m/%y')

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

def delete_prestamo(tipo, value): #Borra cada préstamo que sea seleccionado
    temporal_presta = []
    global presta

    if tipo == "usuario":
        for item in presta:
            if item["usuario"] != value:
                temporal_presta.append(item)

    if tipo == "obra":
        for item in presta:
            if item["obra"] != value:
                temporal_presta.append(item)

    presta = temporal_presta

def delete_all_prestamos(): #Limpia la lista de préstamo
    presta.clear()
    
        