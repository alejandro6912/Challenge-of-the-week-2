#MAIN
# TOTAL INCOME CALCULATION
# Sums all order totals
# returns total
def calculate_income(orders):
    total = 0
    for id_ord in orders:
        total += orders[id_ord][3]
    return total
# FINAL REPORT
# Checks if there are orders, processes each order,
# counts orders per client and total products sold
# returns report printing as the menu
def generate_report(orders, clients, products):
    if not orders:
        return "No hay datos para generar reporte"
    total_orders = len(orders)
    total_income = calculate_income(orders)
    orders_per_client = {}
    products_sold = {}
    for id_ord in orders:
        id_cli, id_pro, quantity, _ = orders[id_ord]
        if id_cli in orders_per_client:
            orders_per_client[id_cli] += 1
        else:
            orders_per_client[id_cli] = 1
        if id_pro in products_sold:
            products_sold[id_pro] += quantity
        else:
            products_sold[id_pro] = quantity
    # Build report
    report = "\n###########\ REPORTE DEL DIA ###########\n"
    report += f"Total pedidos: {total_orders}\n"
    report += f"Total ingresos: {total_income}\n"
    report += "\nPedidos por cliente:\n"
    for id_cli in orders_per_client:
        report += f"{clients[id_cli][0]}: {orders_per_client[id_cli]}\n"
    report += "\nProductos vendidos\n"
    for id_pro in products_sold:
        report += f"{products[id_pro][1]}: {products_sold[id_pro]}\n"
    return report

# INTERACTIVE MENU
def menu(user):
    # Initialize empty dictionaries
    clients = {}
    products = {}
    orders = {}
    #Initialize variable case for the menu select option
    case = 0
    # Main loop until user exits
    while case != 7:
        print("\n###===MENÚ SISTEMA DE PEDIDOS ===###")
        print("1. Registrar cliente")
        print("2. Registrar producto")
        print("3. Crear pedido")
        print("4. Ver pedidos")
        print("5. Ver ingresos")
        print("6. Reporte del dia")
        print("7. Salir")
        # Input validation
        try:
            case = int(input("Seleccione una opción: "))
        except:
            print("Opcion invalida")
            continue
        # Option 1: Register client
        if case == 1:
            try:
                id_cli = int(input("ID del Cliente: "))
                name = input("Nombre: ")
                email = input("Email: ")
                clients, t = register_client(clients, id_cli, name, email)
                print(t)
            except:
                print("Error al ingresar datos")
        # Option 2: Register product
        elif case == 2:
            try:
                prod_id = int(input("ID del Producto: "))
                name = input("Nombre: ")
                price = float(input("Precio: "))
                products, t = register_product(products, prod_id, name, price)
                print(t)
            except:
                print("Error al ingresar datos")
        # Option 3: Create order
        elif case == 3:
            try:
                orde_id = int(input("ID del Pedido: "))
                id_cli = int(input("ID del Cliente: "))
                prod_id = int(input("ID del Producto : "))
                quan = int(input("Cantidad del Producto : "))
                orders, t = create_order(orders, orde_id, id_cli, prod_id, quan, clients, products)
                print(t)
            except:
                print("Error al ingresar datos")
        # Option 4: View orders
        elif case == 4:
            print(view_orders(orders, clients, products))
        # Option 5: View income
        elif case == 5:
            print("Total del dia:", calculate_income(orders))
        # Option 6: Generate report
        elif case == 6:
            print(generate_report(orders, clients, products))
        # Option 7: Exit
        elif case == 7:
            print("Saliendo del programa...")
        else:
            print("Opcion no permitida por favor intente de nuevo: ")
    return clients, products, orders
# PROGRAM EXECUTION
user ="1"
menu(user)
