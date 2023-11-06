class Auto:
    def __init__(self, modelo_de_auto, anio_de_auto, score_de_auto):
        self._modelo_de_auto = modelo_de_auto
        self._anio_de_auto = anio_de_auto
        self._score_de_auto = score_de_auto
    
    @property
    def modelo_de_auto(self):
        return self._modelo_de_auto
    @property
    def anio_de_auto(self):
        return self._anio_de_auto
    @property
    def score_de_auto(self):
        return self._score_de_auto