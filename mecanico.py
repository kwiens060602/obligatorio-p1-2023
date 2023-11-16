from entities.empleado import Empleado
class Mecanico(Empleado):
    def __init__(self, nombre_empleado, cedula_empleado, fecha_de_nacimiento_empleado, pais_de_nacimiento_empleado, salario_empleado, score_mecanico):
        super().__init__(nombre_empleado, cedula_empleado, fecha_de_nacimiento_empleado, pais_de_nacimiento_empleado, salario_empleado)
        self._score_mecanico = score_mecanico
        
    @property
    def score_mecanico(self):
        return self._score_mecanico