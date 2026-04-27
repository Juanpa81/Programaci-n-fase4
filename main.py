# Archivo Principal (main.py)
# Aquí se ejecuta TODO el sistema

# Importamos las clases de otros archivos
from cliente import Cliente
from servicio import Sala, Equipo, Asesoria
from reserva import Reserva


# Inicio del Programa

print("=== SISTEMA SOFTWARE FJ ===")

try:
    # 1. Crear cliente (correcto)
    cliente1 = Cliente("Juan", "123")

    # 2. Crear servicios
    sala1 = Sala("Sala de reuniones", 50000, 10)
    equipo1 = Equipo("Computador", 30000, "Tecnología")
    asesoria1 = Asesoria("Asesoría IT", 80000, "Ingeniero")

    # 3. Crear reserva correcta
    reserva1 = Reserva(cliente1, sala1, 2)
    reserva1.confirmar()

    # 4. Crear reserva con error (para probar excepciones)
    reserva2 = Reserva(cliente1, equipo1, -1)

except Exception as e:
    print("Se presentó un error:", e)
   # Este bloque siempre se ejecuta
finally:
    print("El sistema sigue funcionando")
