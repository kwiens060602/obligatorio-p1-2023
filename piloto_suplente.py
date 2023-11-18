from entities.empleado import Empleado
class PilotoSuplente(Empleado):
    def __init__(self, nombre_empleado, cedula_empleado, fecha_de_nacimiento_empleado, pais_de_nacimiento_empleado, salario_empleado, score_piloto, nro_auto, puntaje_carrera, lesion=False, suplente=True):
        super().__init__(nombre_empleado, cedula_empleado, fecha_de_nacimiento_empleado, pais_de_nacimiento_empleado, salario_empleado)
        self._score_piloto = score_piloto
        self._nro_auto = nro_auto
        self._lesion = lesion
        self._suplente = suplente
        self._puntaje_carrera = puntaje_carrera

    @property
    def score_piloto(self):
        return self._score_piloto
    @property
    def nro_auto(self):
        return self._nro_auto
    @property
    def lesion(self):
        return self._lesion
    @property
    def suplente(self):
        return self._suplente
    @property
    def puntaje_carrera(self):
        return self._puntaje_carrera
    
    @puntaje_carrera.setter
    def puntaje_carrera(self, puntaje_carrera_nuevo):
        self._puntaje_carrera = puntaje_carrera_nuevo
        
    