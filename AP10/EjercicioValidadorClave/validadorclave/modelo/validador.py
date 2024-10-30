# TODO: Implementa el código del ejercicio aquí

from validadorclave.modelo.errores import (
    ErrorLongitudInvalida,
    ErrorFaltaMayuscula,
    ErrorFaltaMinuscula,
    ErrorFaltaNumero,
    ErrorFaltaCaracterEspecial,
    ErrorFaltaCalisto
)

class ReglaValidacion:
    def __init__(self, longitud_esperada: int):
        self.longitud_esperada = longitud_esperada

    def validar_longitud(self, clave: str) -> bool:
        return len(clave) >= self.longitud_esperada

    def contiene_mayuscula(self, clave: str) -> bool:
        return any(c.isupper() for c in clave)

    def contiene_minuscula(self, clave: str) -> bool:
        return any(c.islower() for c in clave)

    def contiene_numero(self, clave: str) -> bool:
        return any(c.isdigit() for c in clave)

    def es_valida(self, clave: str) -> bool:
        raise NotImplementedError

class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(8)

    def contiene_caracter_especial(self, clave: str) -> bool:
        caracteres_especiales = "@_#$%"
        return any(c in caracteres_especiales for c in clave)

    def es_valida(self, clave: str) -> bool:
        if not self.validar_longitud(clave):
            raise ErrorLongitudInvalida
        if not self.contiene_mayuscula(clave):
            raise ErrorFaltaMayuscula
        if not self.contiene_minuscula(clave):
            raise ErrorFaltaMinuscula
        if not self.contiene_numero(clave):
            raise ErrorFaltaNumero
        if not self.contiene_caracter_especial(clave):
            raise ErrorFaltaCaracterEspecial
        return True

class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(6)

    def contiene_calisto(self, clave: str) -> bool:
        return clave.lower().count('calisto') == 1 and clave.find('CALISTO') == -1

    def es_valida(self, clave: str) -> bool:
        if not self.validar_longitud(clave):
            raise ErrorLongitudInvalida
        if not self.contiene_numero(clave):
            raise ErrorFaltaNumero
        if not self.contiene_calisto(clave):
            raise ErrorFaltaCalisto
        return True

class Validador:
    def __init__(self, regla: ReglaValidacion):
        self.regla = regla

    def es_valida(self, clave: str) -> bool:
        return self.regla.es_valida(clave)