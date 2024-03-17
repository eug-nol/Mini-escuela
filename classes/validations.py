class Validations():
    def __init__(self):
        pass
    
    def validate_anio_curso(self, anio):
        if not anio.isnumeric():
            raise ValueError("El año ingresado no es válido.")
        return True
    
    def validate_division_curso(self, division):
        if not division.isalpha() & len(division) <= 2:
            raise ValueError("La división ingresada no es válida, deben ser hasta dos caracteres alfabéticos.")
        return True
    
    def validate_legajo(self, legajo):
        if not legajo.isnumeric() & len(legajo) != 5:
            raise ValueError("El legajo ingresado no es válido.")
        return True
        
    def validate_dni(self, dni):
        if not dni.isnumeric() & len(dni) != 8:
            raise ValueError("El DNI ingresado no es válido.")
        return True
    
    def validate_apellido_y_nombre(self, apellido_y_nombre):
        if len(apellido_y_nombre) > 50:
            raise ValueError("El nombre es demasiado largo.")
        return True
    
            
    