from entities.auto import Auto
class Equipo:
    def __init__(self, nombre, pais, anio, auto: Auto):
        self._nombre = nombre
        self._pais = pais
        self._anio = anio
        self._auto = auto
        self._empleados = []

    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def pais(self):
        return self._pais
    
    @property
    def anio(self):
        return self._anio

    @property
    def auto(self):
        return self._auto   

    def agregar_empleado(self, empleado):
        self._empleados.append(empleado)
        
    
    

