from controller.venta_controller import VentaController


def vista_ventas(ventas_controller: VentaController):
    import tabulate

    ventas_controller.cargar_ventas()

    while True:
        print("1. - Insertar venta")
        print("2. - Ver ventas")
        print("3. - Salir")
        opcion = int(input("Ingresa una opcion: "))
        if opcion == 1:
            ventas_controller.insertar_venta()
        elif opcion == 2:
            # Diccionario de ventas
            ventecitas = ventas_controller.ventas.todos()
            header = ventecitas[0].keys()
            rows = [x.values() for x in ventecitas]
            print(tabulate.tabulate(rows, header))
        elif opcion == 3:
            break
        else:
            print("Opcion no valida")
