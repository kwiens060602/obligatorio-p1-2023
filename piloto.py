from entities.empleado import Empleado
class Piloto(Empleado):
    def __init__(self, nombre_empleado, cedula_empleado, fecha_de_nacimiento_empleado, pais_de_nacimiento_empleado, salario_empleado, score_piloto, nro_auto, lesion=False, suplente=False):
        super().__init__(nombre_empleado, cedula_empleado, fecha_de_nacimiento_empleado, pais_de_nacimiento_empleado, salario_empleado)
        self._score_piloto = score_piloto
        self._nro_auto = nro_auto
        self._lesion = lesion

    @property
    def score_piloto(self):
        return self._score_piloto
    @property
    def nro_auto(self):
        return self._nro_auto
    @property
    def lesion(self):
        return self._lesion
    















