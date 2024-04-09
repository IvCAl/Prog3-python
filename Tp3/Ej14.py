def menu(has_added_producto: bool, total_due: float) -> int:
    if has_added_producto:
        op = int(input(f'1. Comprar otro producto\n'
                       f'2. Finalizar compra (${total_due:.2f})\n'
                       '0. Salir\n'
                       'Ingrese su opción: '))
    else:
        op = int(input('1. Comprar producto\n'
                       '0. Salir\n'
                       'Ingrese su opción: '))
    return op

def show_productos(productos: dict):
    for code, producto in productos.items():
        print(f'Código: {code}, Nombre: {producto[0]}, Precio: {producto[1]} ')

def check_producto_code(key: int, productos: dict) -> bool:
    return key in productos

def buy_producto(producto_info: tuple) -> float:
    units_to_buy = int(input(f'Ingrese cuántas unidades de {producto_info[0]} quiere comprar: '))
    total = units_to_buy * producto_info[1]
    return total
        
productos = {
    1234: ['Arroz', 1399.99],
    1235: ['Leche', 899.99],
    1236: ['Oro 18 kilates x kg', 2300.00],
    1237: ['Media semilla de palta', 3000.00]
}

total_due = float()
has_added_producto = False

while True:
    show_productos(productos)
    
    option = menu(has_added_producto, total_due)
    
    if option == 0:
        print('Saliendo...')
        break
    
    elif option == 1:
        code = int(input('\nIngrese el código del producto a comprar: '))
        
        if check_producto_code(code, productos):
            total_due += buy_producto(productos.get(code))
            has_added_producto = True
        else:
            print(f'El código {code} ingresado es inválido.')
    
    elif option == 2 and has_added_producto:
        print(f'Gracias por su compra')
        break
    
    else:
        print('Opción inválida. Por favor, seleccione una opción válida.')