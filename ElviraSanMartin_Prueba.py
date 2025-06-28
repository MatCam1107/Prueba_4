reservas = {}

stock_maximo = 20

def reservar_zapatillas():
    print("-- Reservar Zapatillas --")
    try:
        if len(reservas) >= stock_maximo:
            print("No hay más stock disponible.")
            return

        nombre = input("Nombre del comprador: ").strip()

        if not nombre:
            print("Error: el nombre no puede estar vacío.")
            return

        if nombre in reservas:
            print("Error: ya existe una reserva a este nombre.")
            return

        clave = input("Digite la palabra secreta para confirmar la reserva: ").strip()

        if clave != "EstoyEnListaDeReserva":
            print("Error: palabra clave incorrecta. Reserva no realizada.")
            return

        reservas[nombre] = 1
        print(f"Reserva realizada exitosamente para {nombre}.")

    except:
        print("Ocurrió un error al intentar realizar la reserva: " )

def buscar_reserva():
    print("-- Buscar Zapatillas Reservadas --")
    try:
        nombre = input("Nombre del comprador a buscar: ").strip()

        if not nombre:
            print("Error: nombre vacío.")
            return

        if nombre in reservas:
            tipo_reserva = "estándar" if reservas[nombre] == 1 else "VIP"
            print(f"Reserva encontrada: {nombre} - {reservas[nombre]} par(es) ({tipo_reserva}).")
            if reservas[nombre] == 1:
                respuesta = input("¿Desea pagar adicional para VIP y reservar 2 pares? (s/n): ").strip().lower()
                if respuesta == "s":
                    reservas[nombre] = 2
                    print("Reserva actualizada a VIP (2 pares).")
                else:
                    print("Manteniendo reserva actual.")
            else:
                print("Ya cuenta con reserva VIP.")
        else:
            print("No se encontró ninguna reserva con ese nombre.")

    except:
        print("Ocurrió un error al buscar la reserva: ")


def ver_stock():
    print("-- Ver Stock de Reservas --")
    try:
        pares_reservados = sum(reservas.values())
        reservas_disponibles = stock_maximo - pares_reservados
        print(f"Pares reservados: {pares_reservados}")
        print(f"Pares disponibles: {reservas_disponibles}")
    except Exception:
        print("Ocurrió un error al mostrar el stock.")


def main():
    while True:
        print("\nTOTEM AUTOATENCIÓN RESERVA STRIKE")
        print("1.- Reservar zapatillas")
        print("2.- Buscar zapatillas reservadas")
        print("3.- Ver stock de reservas")
        print("4.- Salir")

        try:
            opcion = int(input("Seleccione una opción (1-4): "))
            
            if opcion == 1:
                reservar_zapatillas()
            elif opcion == 2:
                buscar_reserva()
            elif opcion == 3:
                ver_stock()
            elif opcion == 4:
                print("Programa terminado...")
                break
            else:
                print("Debe ingresar una opción válida!!")
        
        except ValueError:
            print("Debe ingresar una opción válida!!")


main()