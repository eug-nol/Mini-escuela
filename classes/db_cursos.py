import pymysql
from classes import curso

class DataBase_Cursos():
    def __init__(self):
        try:
            self.conn = pymysql.connect(host = 'localhost',
                                user = 'root',
                                password = '478Hola333oP*',
                                database = 'mini_escuela')
            self.cursor = self.conn.cursor() #con el cursor leemos la informacion
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print(f"No se pudo conectar con la base de datos. Error: {e}")
        
    
    def getall_cursos(self):
        self.cursor.execute("SELECT * FROM cursos") #ejecuta la query
        cursos = self.cursor.fetchall() #la variable cursos almacena todo lo que leyó el cursor en la query
        lista_cursos = [] #la lista donde voy a guardar todos los cursos para mostrarlos
        for i in cursos:
            cur = curso.Curso(i[0],i[1])
            lista_cursos.append(cur) #el indice marca la columna de la tabla, podemos ponerle tambien el nombre de la columna como indice
        self.cursor.close()
        return lista_cursos

    def insert_curso(self, anio_curso, division_curso):
        sql =("INSERT INTO cursos VALUES (%s, %s);")
        values = (anio_curso, division_curso)
        self.cursor.execute(sql, values)
        self.conn.commit()
        self.cursor.close()