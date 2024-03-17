import os
from os import system
import time
import msvcrt
from classes.validations import Validations
from classes import db_cursos
from classes import db_alumnos


validator = Validations()
def print_options():
    print('''MINI ESCUELA - Opciones
          Seleccione el comando que desea ejecutar
          1 - Listado de alumnos por curso
          2 - Listado completo de alumnos
          3 - Listado de cursos
          
          4 - Agregar alumno
          5 - Editar alumno
          6 - Eliminar alumno
          
          7 - Agregar curso
          8 - Editar curso
          9 - Eliminar curso
          
          10 - Salir''')
    
def run():
    print_options()
    command = input("Ingrese su nro de opción elegida: ")
    
    if command == "1":
        list_alumnos_curso()
    elif command == "2":
        list_alumnos()
    elif command == "3":
        list_cursos()
    elif command == "4":
        create_alumno()
    elif command == "5":
        edit_alumno()
    elif command == "6":
        quit_alumno()
    elif command == "7":
        create_curso()
    elif command == "8":
        pass
    elif command == "9":
        pass
    elif command == "10":
        os._exit(1)
    else:
        print("Comando inválido")
        time.sleep(1)
        run()
    
    if __name__ == "__main__":
        run()



 
def list_alumnos_curso():
    system("cls")
    print("Ingrese el curso del que desea visualizar la lista de alumnos")
    a = int(check("Año del curso: ", "anio_curso"))
    d = check("División: ", "division_curso")
    
    listar_alumnos = db_alumnos.DataBase_Alumnos()
    all_alumnos = listar_alumnos.getall_alumnos()
    
    print(f"Alumnos de {a}°'{d}'")
    
    for i in all_alumnos:
        if i.anio_curso == a:
            if i.division_curso == d:
                legajo = i._legajo
                dni = i._dni
                apellido_y_nombre = i._apellido_y_nombre
                print(f"{legajo} - {dni} ------------------- {apellido_y_nombre}")
            
    print("Presione cualquier tecla para continuar...")
    msvcrt.getch() #para volver al inicio
        
        
def list_alumnos():
    system("cls")
    
    listar_alumnos = db_alumnos.DataBase_Alumnos()
    all_alumnos = listar_alumnos.getall_alumnos()
    
    for i in all_alumnos:
        legajo = i._legajo
        dni = i._dni
        apellido_y_nombre = i._apellido_y_nombre
        anio_curso = i._anio_curso
        division_curso = i._division_curso
        print(f"{legajo} - {dni} ------------------- {apellido_y_nombre} --- {anio_curso}°{division_curso}")
        
    print("Presione cualquier tecla para continuar...")
    msvcrt.getch() 
    

def list_cursos():
    system("cls")
    
    listar_cursos = db_cursos.DataBase_Cursos()
    all_cursos = listar_cursos.getall_cursos()
    
    for i in all_cursos:
        anio = i.anio
        division = i.division
        print(f"{anio}° {division}")
    
    listar_cursos.close()
    
    print("Presione cualquier tecla para continuar...")
    msvcrt.getch() 
    
    
def create_alumno():
    system("cls")
    
    print('''Agregando un alumno
        Ingrese los datos correspondientes
        ''')
    legajo = check("Legajo: ", "legajo")
    dni = check("DNI: ", "dni")
    apellido_y_nombre = check("Apellido y nombre: ", "apellido_y_nombre")
    anio_curso = check("Año de curso: ", "anio_curso")
    division_curso = check("División: ", "division_curso")
    
    try:
        alumno_nuevo = db_alumnos.DataBase_Alumnos()
        alumno_nuevo.insert_alumno(int(legajo), int(dni), apellido_y_nombre, int(anio_curso), division_curso)
        print("Se agregó correctamente el alumno")
    except:
        print("No se ha podido agregar al alumno")
    
    alumno_nuevo.close()
    
    print("Presione cualquier tecla para continuar...")
    msvcrt.getch()


def edit_alumno():
    system("cls")
    
    list_alumnos_curso()
    legajo = int(input("Ingrese el legajo del alumno que quiere editar: "))
    
    alumno_elegido = db_alumnos.DataBase_Alumnos()
    alumno_editado = alumno_elegido.get_alumno(legajo)
    
    alumno_elegido.show_alumno(alumno_editado)
    opcion = input("Qué desea editar? [L]egajo, [D]NI, [N]ombre y apellido, [A]ño, [C]urso (división) \n")
    #alumno_elegido.update_alumno(legajo, alumno_editado)
    
    if opcion.upper() == "L":
        alumno_editado.legajo = int(check("Legajo nuevo: ", "legajo"))
        alumno_elegido.update_alumno(alumno_editado)
            
    elif opcion.upper() == "D":
        alumno_editado.dni = int(check("DNI nuevo: ", "dni"))
        alumno_elegido.update_alumno(alumno_editado)
        
    elif opcion.upper() == "N":
        alumno_editado.apellido_y_nombre = check("Apellido y nombre nuevos: ", "apellido_y_nombre")
        alumno_elegido.update_alumno(alumno_editado)
    
    elif opcion.upper() == "A":
        alumno_editado.anio_curso = int(check("Año de cursado nuevo: ", "anio_curso"))
        alumno_elegido.update_alumno(alumno_editado)
    
    elif opcion.upper() == "C":
        alumno_editado.division_curso = int(check("División de cursado nueva: ", "division_cursado"))
        alumno_elegido.update_alumno(alumno_editado)
    
    else:
        print("La opción ingresada no es válida, inténtelo de nuevo")
        edit_alumno()
    
    print("El alumno ha sido actualizado exitosamente")
    print(f"{alumno_editado.legajo} - {alumno_editado.dni} ------------------- {alumno_editado.apellido_y_nombre} --- {alumno_editado.anio_curso}°{alumno_editado.division_curso}")
    
    alumno_elegido.close()
    
    print("Presione cualquier tecla para continuar...")
    msvcrt.getch()
    

def quit_alumno():
    system("cls")
    
    legajo = int(input("Ingrese el legajo que quiere eliminar: "))
    alumno_elegido = db_alumnos.DataBase_Alumnos()
    
    try:
        alumno_eliminado = alumno_elegido.get_alumno(legajo)
        alumno_elegido.show_alumno(alumno_eliminado)
        confirmacion = input("¿Desea eliminar este alumno? S/N ")
        if confirmacion.upper() == "S":
            alumno_elegido.delete_alumno(alumno_eliminado)
            print("Se ha eliminado correctamente al alumno.")
    except:
        print("No se ha encontrado el alumno. Presione cualquier tecla para intentarlo otra vez, o 'M' para volver al menu principal")
        op = input()
        if op.upper() != "M":
            quit_alumno()
    
    alumno_elegido.close()
    
    print("Presione cualquier tecla para continuar...")
    msvcrt.getch()
    
    
    
def create_curso():
    print('''Agregando un curso
          Ingrese los datos correspondientes
          ''')
    anio_curso = check("Año: ", "anio_curso")
    division_curso = check("División: ", "division_curso")
    
    try:
        curso_nuevo = db_cursos.DataBase_Cursos()
        curso_nuevo.insert_curso(int(anio_curso), division_curso)
        print("Se agregó correctamente el curso")
    except:
        print("No se ha podido agregar el curso")
        
    print("Presione cualquier tecla para continuar...")
    msvcrt.getch()


def check(message, data_name):
    print()
    data_input = input(f"{message} ")
    try:
        getattr(validator, f"validate_{data_name}")(data_input)
        return data_input
    except ValueError as err:
        print(err)
        check(message, data_name)

run()