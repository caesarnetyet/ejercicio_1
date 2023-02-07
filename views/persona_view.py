
import tabulate

from controller.persona_controller import PersonaController


def vista_persona(persona_controller: PersonaController):

    while True:
        print("1.- Agregar cliente ")
        print("2.- Modificar cliente ")
        print("3.- Eliminar cliente ")
        print("4.- Ver clientes ")
        print("5.- Salir ")
        opcion = int(input("Ingresa una opcion: "))
        if opcion == 1:
            persona_controller.insertar_cliente()
        elif opcion == 2:
            id_ = input("Ingresa el id del producto a modificar")
            persona_controller.modificar_cliente(id_)
        elif opcion == 3:
            id_ = input("Ingresa el id del producto a eliminar")
            persona_controller.eliminar_cliente(id_)
        elif opcion == 4:
            clientitos = persona_controller.clientes.todos()
            header = clientitos[0].keys()
            rows = [x.values() for x in clientitos]
            print(tabulate.tabulate(rows, header))
        elif opcion == 5:
            break
        else:
            print("Opcion invalida")