from typing import List, Dict, Any


class State:

    CANCIONES = 0
    DIRECTORIO_GUARDAR = 1
    TIPO_FORMATO = 2

    __canciones: List[str]
    __directorio_guardar: str
    __tipo_formato: str

    def set_state(self, canciones: List[str] = None, directorio_guardar: str = None, tipo_formato: str = None):
        if canciones is not None:
            self.__canciones = canciones
        elif directorio_guardar is not None:
            self.__directorio_guardar = directorio_guardar
        elif tipo_formato is not None:
            self.__tipo_formato = tipo_formato

    def get_state(self) -> Dict[str, Any]:
        return {
            self.CANCIONES: self.__canciones,
            self.DIRECTORIO_GUARDAR: self.__directorio_guardar,
            self.TIPO_FORMATO: self.__tipo_formato
        }
