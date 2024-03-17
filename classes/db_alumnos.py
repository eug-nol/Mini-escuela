import pymysql
from classes import alumno

class DataBase_Alumnos():
    def __init__(self):
        try:
            self.conn = pymysql.connect(host = 'localhost',
                                user = 'root',
                                password = '478Hola333oP*',
                                database = 'mini_escuela')
            self.cursor = self.conn.cursor() #con el cursor leemos la informacion
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print(f"No se pudo conectar con la base de datos. Error: {e}")
        
    
    def getall_alumnos(self):
        self.cursor.execute("SELECT * FROM alumnos;") 
        alumnos = self.cursor.fetchall() 
        lista_alumnos = [] 
        for i in alumnos:
            alu = alumno.Alumno(i[0],i[1],i[2],i[3],i[4])
            lista_alumnos.append(alu) #el indice marca la columna de la tabla, podemos ponerle tambien el nombre de la columna como indice
        return lista_alumnos
    
    def insert_alumno(self, legajo, dni, apellido_y_nombre, anio_curso, division_curso):
        sql =("INSERT INTO alumnos VALUES (%s, %s, %s, %s, %s);")
        values = (legajo, dni, apellido_y_nombre, anio_curso, division_curso)
        self.cursor.execute(sql, values)
        self.conn.commit()

    def get_alumno(self, legajo):
        sql = "SELECT * FROM alumnos WHERE legajo = %s;"
        value = legajo
        self.cursor.execute(sql, value)
        alu = self.cursor.fetchone()
        alumno_elegido = alumno.Alumno(alu[0], alu[1], alu[2], alu[3], alu[4])
        return alumno_elegido
    
    def show_alumno(self, alumno):
        print(f"{alumno.legajo} - {alumno.dni} ------------------- {alumno.apellido_y_nombre} --- {alumno.anio_curso}°{alumno.division_curso}")
    
    def update_alumno(self, alumno_editado):
        sql = "UPDATE alumnos SET legajo=%s, dni=%s, apellido_y_nombre=%s, anio_curso=%s, division_curso=%s WHERE legajo=%s;"
        values = (alumno_editado.legajo, alumno_editado.dni, alumno_editado.apellido_y_nombre, alumno_editado.anio_curso, alumno_editado.division_curso, alumno_editado.legajo)
        self.cursor.execute(sql, values)
        self.conn.commit()
    
    def delete_alumno(self, alumno_eliminado):
        sql = "DELETE FROM alumnos WHERE legajo=%s;"
        value = alumno_eliminado.legajo
        self.cursor.execute(sql, value)
        self.conn.commit()
    
    def close(self):
        self.cursor.close()