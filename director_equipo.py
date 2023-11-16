from entities.empleado import Empleado
class DirectorDeEquipo(Empleado):
    def __init__(self, nombre_empleado, cedula_empleado, fecha_de_nacimiento_empleado, pais_de_nacimiento_empleado, salario_empleado):
        super().__init__(nombre_empleado, cedula_empleado, fecha_de_nacimiento_empleado, pais_de_nacimiento_empleado, salario_empleado)