from entities.empleado import Empleado
class Piloto(Empleado):
    def __init__(self, nombre_empleado, cedula_empleado, fecha_de_nacimiento_empleado, pais_de_nacimiento_empleado, salario_empleado, tipo_empleado, score_piloto, nro_auto, puntaje, lesion):
        super().__init__(nombre_empleado, cedula_empleado, fecha_de_nacimiento_empleado, pais_de_nacimiento_empleado, salario_empleado, tipo_empleado)
        self._score_piloto = score_piloto
        self._nro_auto = nro_auto
        self._puntaje = puntaje
        self._lesion = lesion

    @property
    def score_piloto(self):
        return self._score_piloto
    @property
    def nro_auto(self):
        return self._nro_auto
    @property
    def puntaje(self):
        return self._puntaje
    @property
    def lesion(self):
        return self._lesion
    













