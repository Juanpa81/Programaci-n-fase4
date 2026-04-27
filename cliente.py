# Clase Cliente
# Sistema Software FJ


class Cliente:

    
    # Constructor
    # Se ejecuta cuando se crea un cliente
    
    def __init__(self, nombre, cedula):

        
        # Validaciones
        

        if not nombre:
            raise ValueError("El nombre no puede estar vacío")

        if not cedula:
            raise ValueError("La cédula no puede estar vacía")

        
        # Encapsulación (datos privados)
        

        self.__nombre = nombre
        self.__cedula = cedula

    
    # Metodo para obtener el nombre
    
    def get_nombre(self):
        return self.__nombre

   
    # Metodo para mostrar datos
    
    def mostrar(self):
        print("Nombre:", self.__nombre)
        print("Cédula:", self.__cedula)
