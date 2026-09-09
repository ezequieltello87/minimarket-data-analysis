import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine, text

# 1. Configurar la conexión a PostgreSQL
# Reemplaza 'tu_usuario', 'tu_contraseña', 'localhost', '5432' y 'tu_base_de_datos' con tus credenciales reales
usuario = "postgres"
password = "admin"
host = "localhost"
puerto = "5432"
db_name = "practica"  # O el nombre de tu base de datos

cadena_conexion = f"postgresql://{usuario}:{password}@{host}:{puerto}/{db_name}"
engine = create_engine(cadena_conexion)

# 2. Limpiar tablas existentes para evitar duplicados o llaves duplicadas (Opcional pero recomendado tras una interrupción)
print("Limpiando tablas en PostgreSQL...")
with engine.connect() as connection:
    connection.execute(text("TRUNCATE TABLE detalle_ventas, ventas, productos, clientes CASCADE;"))
    connection.commit()

# 3. Cargar archivos procesados
raiz_proyecto = Path().resolve().parent if Path().resolve().name == 'scripts' else Path().resolve()
ruta_processed = raiz_proyecto / 'data' / 'processed'

df_productos = pd.read_csv(ruta_processed / 'productos_clean.csv')
df_ventas = pd.read_csv(ruta_processed / 'ventas_clean.csv')
df_detalle = pd.read_csv(ruta_processed / 'detalle_clean.csv')

# 4. Cargar 'clientes' (extraídos de ventas únicas, asegurando 'Consumidor Final')
clientes_unicos = df_ventas['id_cliente'].dropna().unique()
df_clientes = pd.DataFrame({
    'id_cliente': clientes_unicos,
    'nombre_cliente': clientes_unicos
})

print("Cargando clientes...")
df_clientes.to_sql('clientes', engine, if_exists='append', index=False)

# 5. Cargar 'productos'
print("Cargando productos...")
df_productos.to_sql('productos', engine, if_exists='append', index=False)

# 6. Cargar 'ventas'
print("Cargando ventas...")
df_ventas.to_sql('ventas', engine, if_exists='append', index=False)

# 7. Cargar 'detalle_ventas'
print("Cargando detalle de ventas...")
df_detalle.to_sql('detalle_ventas', engine, if_exists='append', index=False)

print("¡Carga completada exitosamente en PostgreSQL sin errores!")