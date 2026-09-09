import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configuración de semilla para reproducibilidad
np.random.seed(42)

# 1. Definir Catálogo de Productos
productos = pd.DataFrame([
    {"id_producto": 1, "nombre": "Leche Entera 1L", "categoria": "Lácteos", "costo": 800, "precio": 1100},
    {"id_producto": 2, "nombre": "Pan Lactal 500g", "categoria": "Panadería", "costo": 1200, "precio": 1800},
    {"id_producto": 3, "nombre": "Gaseosa Cola 2.25L", "categoria": "Bebidas", "costo": 1500, "precio": 2200},
    {"id_producto": 4, "nombre": "Agua Mineral 1.5L", "categoria": "Bebidas", "costo": 500, "precio": 900},
    {"id_producto": 5, "nombre": "Chocolate Bariloche 100g", "categoria": "Chocolates", "costo": 1000, "precio": 1600},
    {"id_producto": 6, "nombre": "Alfajor Triple", "categoria": "Golosinas", "costo": 400, "precio": 750},
    {"id_producto": 7, "nombre": "Queso Cremoso 500g", "categoria": "Lácteos", "costo": 2500, "precio": 3800},
    {"id_producto": 8, "nombre": "Cerveza LAGER 473ml", "categoria": "Bebidas", "costo": 900, "precio": 1500},
])

# 2. Generar Fechas y Simular Transacciones (6 meses)
fecha_inicio = datetime(2026, 1, 1)
dias_simulacion = 180

ventas_list = []
detalle_list = []
id_venta_counter = 10001
id_detalle_counter = 50001

for dia in range(dias_simulacion):
    fecha_actual = fecha_inicio + timedelta(days=dia)
    
    # Efecto Cambio de Layout a partir del día 90: Caen los tickets, sube el gasto
    if dia < 90:
        cant_tickets = np.random.randint(80, 120)
        multiplicador_canasta = 1.0
    else:
        cant_tickets = np.random.randint(45, 65) # Caída brusca de clientes
        multiplicador_canasta = 1.4 # Venden más por ticket a los que se quedan
        
    medios_pago = ["Efectivo", "Debito", "Mercado Pago", "Credito"]
    prob_pago = [0.3, 0.3, 0.3, 0.1]
    
    for _ in range(cant_tickets):
        # Hora de la venta
        hora = np.random.choice([np.random.randint(8, 13), np.random.randint(16, 21)])
        fecha_hora_venta = fecha_actual.replace(hour=hora, minute=np.random.randint(0, 60))
        
        # Cliente
        id_cliente = np.random.choice([f"CLI-{np.random.randint(100, 300)}", None], p=[0.6, 0.4])
        medio_pago = np.random.choice(medios_pago, p=prob_pago)
        
        # Simular Cazadores de Ofertas en Promo Chocolates (Días 30 a 45)
        es_cazador_promo = (30 <= dia <= 45) and (np.random.rand() < 0.35)
        
        if es_cazador_promo:
            prods_compra = [5] # Solo Chocolate
            cantidades = [3]  # Llevan 3x2
        else:
            n_items = max(1, int(np.random.poisson(2.5) * multiplicador_canasta))
            prods_compra = np.random.choice(productos["id_producto"], size=min(n_items, len(productos)), replace=False)
            cantidades = np.random.randint(1, 4, size=len(prods_compra))
            
        monto_total_venta = 0
        
        for prod_id, cant in zip(prods_compra, cantidades):
            prod_info = productos[productos["id_producto"] == prod_id].iloc[0]
            precio_unitario = prod_info["precio"]
            
            # Aplicar descuento 3x2 si aplica
            if es_cazador_promo and prod_id == 5:
                subtotal = precio_unitario * 2 # Pagan 2 llevan 3
            else:
                subtotal = precio_unitario * cant
                
            monto_total_venta += subtotal
            
            detalle_list.append({
                "id_detalle": id_detalle_counter,
                "id_venta": id_venta_counter,
                "id_producto": prod_id,
                "cantidad": cant,
                "precio_unitario": precio_unitario,
                "subtotal": subtotal
            })
            id_detalle_counter += 1
            
        ventas_list.append({
            "id_venta": id_venta_counter,
            "fecha_hora": fecha_hora_venta,
            "id_cliente": id_cliente,
            "medio_pago": medio_pago,
            "monto_total": monto_total_venta
        })
        id_venta_counter += 1

# Crear DataFrames y Exportar
df_ventas = pd.DataFrame(ventas_list)
df_detalle = pd.DataFrame(detalle_list)

df_ventas.to_csv("ventas_minimarket.csv", index=False)
df_detalle.to_csv("detalle_minimarket.csv", index=False)
productos.to_csv("productos_minimarket.csv", index=False)

print("¡Dataset generado con éxito!")
print(f"Total Ventas (Encabezados): {len(df_ventas)} registros")
print(f"Total Detalles de Venta: {len(df_detalle)} líneas de productos")