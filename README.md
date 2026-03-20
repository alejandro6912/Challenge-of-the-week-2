# 📦 Sistema de Gestión de Pedidos (CLI)

Este programa es una aplicación de consola en Python diseñada para gestionar el flujo de ventas de un negocio. Permite administrar clientes, productos y órdenes mediante una interfaz de menú interactiva.

## 🚀 Funcionalidades Principales

El sistema está dividido en módulos lógicos para asegurar la integridad de los datos:

1.  **Registro de Clientes:** Almacena ID único, nombre y correo electrónico.
2.  **Catálogo de Productos:** Gestión de productos con sus respectivos precios unitarios.
3.  **Gestión de Órdenes:** 
    - Valida la existencia del cliente y el producto antes de crear el pedido.
    - Calcula automáticamente el total según la cantidad ingresada.
    - Evita duplicidad de IDs de pedido.
4.  **Reportes y Consultas:**
    - Visualización detallada de todas las órdenes.
    - Cálculo de ingresos totales del día.
    - Reporte estadístico (pedidos por cliente y cantidad de productos vendidos).

## 🛠️ Requisitos Técnicos

- **Lenguaje:** Python 3.x
- **Estructuras de Datos:** Utiliza diccionarios para garantizar una búsqueda eficiente de registros por ID.
- **Robustez:** Implementa bloques `try-except` para evitar cierres inesperados por entradas de datos incorrectas.

## 💻 Instalación y Uso

1. Copia el código en un archivo llamado `gestion_pedidos.py`.
2. Abre una terminal y ejecuta:
   ```bash
   python gestion_pedidos.py


Sigue las instrucciones del menú interactivo en pantalla.
📋 Ejemplo de Estructura de Datos (Memoria)
El programa organiza la información de la siguiente manera:
Clientes: {id: (nombre, email)}
Productos: {id: (id, nombre, precio)}
Pedidos: {id_pedido: (id_cliente, id_producto, cantidad, total)}
📊 Ejemplo de Reporte Generado
Al seleccionar la opción "Reporte del día", el sistema procesa los diccionarios para mostrar:
Total de ingresos monetarios.
Cantidad de pedidos por cada cliente registrado.
Conteo acumulado de unidades vendidas por producto.
