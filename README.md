# biblioteca
 Parcial de prácticas profesionalizantes de Desarrollo de Software
Consideraciones Generales
 El trabajo debe ser realizado en forma individual, ser subido a la plataforma de
classrom en tiempo y forma
 El trabajo Parcial 2 es una instancia de evaluación y como tal para aprobarlo el mismo
debe ser defendido durante el horario de clase, tendrá que demostrar sólidos
conocimientos respecto del código fuente entregado. También traer datos para
Testear su sistema, ya que el tiempo de evaluación es reducido.
 El trabajo Parcial 2 tiene un UNICO recuperatorio, pero para hacer uso del mismo el
trabajo deberá cumplir con nuevos requerimientos en tiempo y forma.
 El trabajo NO será evaluado si el proyecto NO compila. Este proyecto se puede hacer a
partir del proyecto Agenda.
Consigna
Sistema de Biblioteca
Una biblioteca decide informatizar su proceso de préstamos de libros por lo que requiere
implementar un sistema informático.
Cada apartado del menú (obras, usuarios y préstamos) tienen su propio &quot;borrar todo; al borrar
todo en el apartado obras se borran las obras y préstamos, pero no la de usuarios; al borrar
todo en el apartado usuarios se borran los usuarios y préstamos, pero no la de obras; al borrar
todo en el apartado préstamos, sólo se borra los préstamos.
Sistema de BIBLIOTECA
El programa de biblioteca tendrá un menú con 4 módulos: Obras, Usuarios, Préstamos salir.
mínimamente utilizable; para Obras, Usuarios, Préstamos debe permitir añadir registros,
listarlos y borrar todos los registros.
 Obras
o Inicio Vuelve al Menu principal
o Añadir (Título: Autor: Editoria)
o Listar
o Buscar
o Modificar
o Borrar
o Borrar todo
 Usuarios
o Inicio: Vuelve al Menú principal
o Añadir (Nombre: Apellidos: DNI)
o Listar
o Buscar
o Modificar
o Borrar
o Borrar todo
 Préstamos: El menú de Préstamos permite crear un nuevo préstamo e indicar la fecha
de devolución, así como listar todos los préstamos y borrarlos.
 En la página de devolución de préstamos sólo deben mostrarse los préstamos
pendientes.
 La fecha de devolución debe ser posterior a la fecha de préstamo.
 Cuando un préstamo todavía no se haya devuelto, la celda de la fecha de devolución
debe mostrarse vacía (en vez de con 00-00-0000).
o Inicio Vuelve al Menu principal
o Préstamo (Usuario: Obra : Fecha de préstamo (dd-mm-aaaa)
o Devolución: Seleccione el préstamo e indique la fecha de devolución:
o Listar (Usuarios Título Préstamo Devolución) (usuario Título Préstamo Devolución (dd-mm-aaaa))
o Borrar Listado de préstamos, selección de préstamo a borrar
o Borrar todo: Borrar todo Listado de préstamos, eliminar todos los prestamos
 Salir: sale del sistema
