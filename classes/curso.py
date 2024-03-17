class Curso():
    def __init__(self, anio, division):
        self._anio = anio
        self._division = division
    
    @property 
    def anio(self):
        return self._anio
    
    @anio.setter
    def anio(self, anio):
        self._anio = anio
    
    @property
    def division(self):
        return self._division
    
    @division.setter
    def division(self, division):
        self._division = division
    
    