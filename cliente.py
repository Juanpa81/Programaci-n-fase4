
# Clase Cliente


import uuid

class Cliente:

    def __init__(self, nombre, cedula, activo=True):

        if not nombre or len(nombre.strip()) < 3:
            raise ValueError("Nombre inválido")

        if not cedula:
            raise ValueError("Cédula obligatoria")

        # ID que el sistema necesita
        self.id_entidad = str(uuid.uuid4())[:8].upper()

        self.nombre = nombre.strip()
        self.cedula = cedula
        self.activo = activo

    def desactivar(self):
        self.activo = False

    def activar(self):
        self.activo = True

    def __str__(self):
        estado = "Activo" if self.activo else "Inactivo"
        return f"{self.nombre} ({estado})"
