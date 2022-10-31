#Aca se encuentran todas las funciones para Usuario y Obra
# -----------------------------------------------------------------------User--------------------------------------------------------------------------
user={}
def add_user(): #Agregar un usuario
    nombre=input("Ingrese nombre de usuario: \n")
    apellido=input("Ingrese apellido del usuario: \n")
    dni=input("Ingrese su número DNI \n")
    while not dni.isnumeric():
        dni=input("Ingrese su número DNI correctamente: \n")
    dni=int(dni)
    user.update({nombre+" "+apellido: dni})
    print(user)


    return user

def show_user():

    for key, values in user.items(): #Muestra el diccionario con cada uno de los elementos correspondientes a la key
        print(f"Nombre y Apellido: {key}\nDni:{values}")
        print("")

def search_user(): #Busca en el diccionario la key con el mismo valor y la muestra en pantalla

    nom=input("Ingresar el nombre y el apellido del usuario a buscar:\n")
    for key, values in user.items():
        if(nom == key):
            print(f"Nombre y Apellido: {key} \nDNI: {values}")
            print("")

def delete_user(): #Usa la funcion mostrar y elimina la clave con el valor ingresado
    show_user()
    nom=input("Ingresar contacto a eliminar: \n") #Usé la función mostrar contacto, pero acá declare la variable nom, y que borre la key con el mismo valor del diccionario
    user.pop(nom)

def modify_user(): #Usa la funcion eliminar usuario y agregar usuario consecutivamente
    delete_user()
    add_user()

def deleteall_user(): #Limpia el diccionario
    user.clear()

# --------------------------------------------------------------------Obras-------------------------------------------------------------------------------
obras={}

def add_obra(): #Agregar una obra
    titulo=input("Ingrese Título:  \n")
    autor=input("Ingrese Autor/a: \n")
    edit=input("Ingrese editorial \n")
    
    obras.update({titulo: ["Autor/a:", autor, "Editorial:", edit]})

    return obras

def show_obra(): #Muestra el diccionario con cada uno de los elementos correspondientes a la key

    for key, values in obras.items():
        print(f"{key} - {values[0]} {values[1]}, {values[2]} {values[3]}")
        print("")


def search_obra(): #Busca en el diccionario la key con el mismo valor y la muestra en pantalla

    elem=input("Ingresar el elemento a buscar: \n")
    for key, values in obras.items():
        if(elem == key):
            print(f"{key} - {values[0]} {values[1]}, {values[2]} {values[3]}")
            print("")

def delete_obra(): #Usa la funcion mostrar y elimina la clave con el valor ingresado
    show_obra()
    elem=input("Ingresar el elemento a buscar: \n") #Usé la función mostrar contacto, pero acá declare la variable nom, y que borre la key con el mismo valor del diccionario
    obras.pop(elem)

def modify_obra(): #Usa la funcion eliminar obra y agregar obra consecutivamente
    delete_obra()
    add_obra()

def deleteall_obra(): #Limpia el diccionario
    obras.clear()


