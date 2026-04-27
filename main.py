
# Archivo Principal - Pruebas del Sistema


from sistema import SistemaGestion
from cliente import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada

def main():

    print("=== Iniciando Sistema Software FJ ===\n")

    sistema = SistemaGestion()

    
    # 1. Crear Clientes
    
    print("Creando clientes...")

    cliente1 = Cliente("Juan", "123")
    cliente2 = Cliente("Ana", "456")

    sistema.registrar_cliente(cliente1)
    sistema.registrar_cliente(cliente2)

    
    # 2. Crear Servicios
    
    print("Creando servicios...")

    sala = ReservaSala("S1", "Sala Principal", 50000, 10, True)
    equipo = AlquilerEquipo("E1", "Laptop", 20000, "Computador", 5)
    asesoria = AsesoriaEspecializada("A1", "Consultoría IT", 80000, "Tecnología", "senior")

    sistema.registrar_servicio(sala)
    sistema.registrar_servicio(equipo)
    sistema.registrar_servicio(asesoria)

    
    # 3. Rerservas Correctas
    
    print("Creando reservas válidas...")

    r1 = sistema.crear_reserva(cliente1, sala, 2, personas=5)
    r1.confirmar()
    r1.procesar()

    r2 = sistema.crear_reserva(cliente2, equipo, 3, cantidad=2)
    r2.confirmar()

    
    # 4. Reservas con Error
    
    print("Probando errores...")

    try:
        r3 = sistema.crear_reserva(cliente1, sala, 2, personas=50)
        r3.confirmar()
    except Exception as e:
        print("Error controlado:", e)

    try:
        r4 = sistema.crear_reserva(cliente2, asesoria, 10)
        r4.confirmar()
    except Exception as e:
        print("Error controlado:", e)

    
    # 5. Cancelacion
    
    print("Cancelando reserva...")
    r2.cancelar("Cliente no asistió")

    
    # 6. Reporte Final
    
    print("\nREPORTE FINAL:")
    print(sistema.reporte_resumen())


# Ejecutar
if __name__ == "__main__":
    main()
