from abc import ABC, abstractmethod
import errores

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave):
        if len(clave) <= self._longitud_esperada:
            raise errores.NoCumpleLongitudMinimaError()

    def _contiene_mayuscula(self, clave):
        if not any(c.isupper() for c in clave):
            raise errores.NoTieneLetraMayusculaError()

    def _contiene_minuscula(self, clave):
        if not any(c.islower() for c in clave):
            raise errores.NoTieneLetraMinusculaError()

    def _contiene_numero(self, clave):
        if not any(c.isdigit() for c in clave):
            raise errores.NoTieneNumeroError()

    @abstractmethod
    def es_valida(self, clave):
        pass


class ReglaValidacionGanimedes(ReglaValidacion):
    def contiene_caracter_especial(self, clave):
        caracteres_especiales = ['@', '_', '#', '$', '%']
        if not any(c in caracteres_especiales for c in clave):
            raise errores.NoTieneCaracterEspecialError()


    def es_valida(self, clave):
        self._validar_longitud(clave)
        self._contiene_mayuscula(clave)
        self._contiene_minuscula(clave)
        self._contiene_numero(clave)
        self.contiene_caracter_especial(clave)
        return True


class ReglaValidacionCalisto(ReglaValidacion):
    def contiene_calisto(self, clave):
        if clave.find('calisto') == -1:
            raise errores.NoTienePalabraSecretaError()

    def es_valida(self, clave):
        self._validar_longitud(clave)
        self._contiene_numero(clave)
        self.contiene_calisto(clave)
        return True


class Validador:
    def _init_(self, regla):
        self.regla = regla

    def es_valida(self, clave):
        return self.regla.es_valida(clave)