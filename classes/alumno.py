class Alumno():
    def __init__(self, legajo, dni, apellido_y_nombre, anio_curso, division_curso):
        self._legajo = legajo
        self._dni = dni
        self._apellido_y_nombre = apellido_y_nombre
        self._anio_curso = anio_curso
        self._division_curso = division_curso
    
    @property
    def legajo(self):
        return self._legajo
    
    @legajo.setter
    def legajo(self, legajo):
        self._legajo = legajo
    
    @property
    def dni(self):
        return self._dni
    
    @dni.setter
    def dni(self, dni):
        self._dni = dni
    
    @property
    def apellido_y_nombre(self):
        return self._apellido_y_nombre
    
    @apellido_y_nombre.setter
    def apellido_y_nombre(self, apellido_y_nombre):
        self._apellido_y_nombre = apellido_y_nombre
        
    @property
    def anio_curso(self):
        return self._anio_curso
    
    @anio_curso.setter
    def anio_curso(self, anio_curso):
        self._anio_curso = anio_curso
        
    @property
    def division_curso(self):
        return self._division_curso
    
    @division_curso.setter
    def division_curso(self, division_curso):
        self._division_curso = division_curso
        