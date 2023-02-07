from controller.producto_controller import ProductoController
import tabulate


def vista_producto(productos_controller: ProductoController):


    while True:
        print("1.- Agregar producto")
        print("2.- Modificar producto")
        print("3.- Eliminar producto")
        print("4.- Ver productos")
        print("5.- Salir")
        opcion = int(input("Ingresa una opcion: "))
        if opcion == 1:
            productos_controller.insertar_producto()
        elif opcion == 2:
            id_ = input("Ingresa el id del producto a modificar")
            productos_controller.modificar_producto(id_)
        elif opcion == 3:
            id_ = input("Ingresa el id del producto a eliminar")
            productos_controller.eliminar_producto(id_)
        elif opcion == 4:
            productitos = productos_controller.productos.todos()
            header = productitos[0].keys()
            rows = [x.values() for x in productitos]
            print(tabulate.tabulate(rows, header))
        elif opcion == 5:
            break
        else:
            print("Opcion invalida")