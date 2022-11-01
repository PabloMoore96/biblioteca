#Aca se encuentran todas las funciones para Usuario y Obra
# -----------------------------------------------------------------------User--------------------------------------------------------------------------
import prestamod

users=[]
def add_user(): #Agregar un usuario
    nombre=input("Ingrese nombre de usuario: \n")
    apellido=input("Ingrese apellido del usuario: \n")
    dni=input("Ingrese su número DNI \n")
    while not dni.isnumeric():
        dni=input("Ingrese su número DNI correctamente: \n")
    dni=int(dni)
    data = {
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni
    }
    users.append(data)
    print(users)

def show_users():
    for item in users:
        print("-----------------------------\n")
        print(f"Nombre: {item['nombre']}\n")
        print(f"Apellido: {item['apellido']}\n")
        print(f"DNI: {item['dni']}\n")

def search_user(): #Busca en el diccionario la key con el mismo valor y la muestra en pantalla

    nom=input("Ingresar el nombre a buscar:\n")
    ape=input("Ingresar el apellido a buscar: \n")

    for item in users:
        if(nom == item['nombre'] and ape == item['apellido']):
            print("-----------------------------\n")        
            print(f"Nombre: {item['nombre']}\n")
            print(f"Apellido: {item['apellido']}\n")
            print(f"DNI: {item['dni']}\n")

def delete_user(): #Usa la funcion mostrar y elimina la clave con el valor ingresado
    show_users()
    nom=input("Ingresar nombre de contacto a eliminar: \n") #Usé la función mostrar contacto, pero acá declare la variable nom, y que borre la key con el mismo valor del diccionario
    ape=input("Ingresar apellido de contacto a eliminar: \n")
    for item in users:
        if(nom == item['nombre'] and ape == item['apellido']):
            users.remove(item)
            prestamod.delete_prestamo("usuario", nom)

def modify_user(): #Usa la funcion eliminar usuario y agregar usuario consecutivamente
    delete_user()
    add_user()

def deleteall_user(): #Limpia el diccionario
    users.clear()
    prestamod.delete_all_prestamos()

# --------------------------------------------------------------------Obras-------------------------------------------------------------------------------
obras=[]

def add_obra(): #Agregar una obra
    titulo=input("Ingrese Título:  \n")
    autor=input("Ingrese Autor/a: \n")
    edit=input("Ingrese editorial \n")
    
    data = {
        "titulo": titulo,
        "autor": autor,
        "editorial": edit
    }
    obras.append(data)
    print(obras)

def show_obra(): #Muestra el diccionario con cada uno de los elementos correspondientes a la key
    for item in obras:
        print("-----------------------------\n")
        print(f"Título: {item['titulo']}\n")
        print(f"Autor: {item['autor']}\n")
        print(f"Editorial: {item['editorial']}\n")

def search_obra(): #Busca en el diccionario la key con el mismo valor y la muestra en pantalla

    elem=input("Ingresar el elemento a buscar: \n")
    for item in users:
        if(elem == item['titulo']):
            print("-----------------------------\n")
            print(f"Título: {item['titulo']}\n")
            print(f"Autor: {item['autor']}\n")
            print(f"Editorial: {item['editorial']}\n")

def delete_obra(): #Usa la funcion mostrar y elimina la clave con el valor ingresado
    show_obra()
    titulo=input("Ingresar el titulo a eliminar: \n") #Usé la función mostrar contacto, pero acá declare la variable nom, y que borre la key con el mismo valor del diccionario
    for item in obras:
        if(titulo == item['titulo']):
            obras.remove(item)
            prestamod.delete_prestamo("obra", titulo)

def modify_obra(): #Usa la funcion eliminar obra y agregar obra consecutivamente
    delete_obra()
    add_obra()

def deleteall_obra(): #Limpia el diccionario
    obras.clear()
    prestamod.delete_all_prestamos()


