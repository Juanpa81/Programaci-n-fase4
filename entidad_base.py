
# Clase base del Sistema


class EntidadBase:
    """
    Clase base para todas las entidades del sistema.
    Maneja el ID único.
    """

    def __init__(self, id_entidad: str):
        if not id_entidad:
            raise ValueError("El ID no puede estar vacío")

        self._id_entidad = id_entidad

    @property
    def id_entidad(self):
        return self._id_entidad

    def obtener_info_base(self):
        return {
            "id": self._id_entidad
        }
