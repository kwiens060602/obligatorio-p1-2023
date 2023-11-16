class Empleado:
    def __init__(self, nombre_empleado, cedula_empleado, fecha_de_nacimiento_empleado, pais_de_nacimiento_empleado, salario_empleado):
       self._nombre_empleado = nombre_empleado
       self._cedula_empleado = cedula_empleado 
       self._fecha_de_nacimiento = fecha_de_nacimiento_empleado
       self._pais_de_nacimiento_empleado = pais_de_nacimiento_empleado
       self._salario_empleado = salario_empleado 
      
       
    @property
    def nombre_empleado(self):
        return self._nombre_empleado
    @property
    def cedula_empleado(self):
        return self._cedula_empleado
    @property
    def fecha_de_nacimiento(self):
        return self._fecha_de_nacimiento
    @property
    def salario(self):
        return self._salario_empleado
    
       