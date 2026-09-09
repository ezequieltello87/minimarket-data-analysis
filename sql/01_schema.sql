-- ==========================================================
-- SCRIPT DE CREACIÓN DE ESQUEMA - MINIMARKET
-- ==========================================================

-- 1. Crear tabla de Clientes
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente VARCHAR(50) PRIMARY KEY,
    nombre_cliente VARCHAR(150)
);

-- 2. Crear tabla de Productos
CREATE TABLE IF NOT EXISTS productos (
    id_producto INT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    categoria VARCHAR(100),
    precio_unitario NUMERIC(10, 2) NOT NULL
);

-- 3. Crear tabla de Ventas (Cabecera)
CREATE TABLE IF NOT EXISTS ventas (
    id_venta INT PRIMARY KEY,
    fecha_hora TIMESTAMP NOT NULL,
    id_cliente VARCHAR(50),
    medio_pago VARCHAR(50),
    monto_total NUMERIC(10, 2) NOT NULL,
    CONSTRAINT fk_cliente FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

-- 4. Crear tabla de Detalle de Ventas
CREATE TABLE IF NOT EXISTS detalle_ventas (
    id_detalle SERIAL PRIMARY KEY,
    id_venta INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario NUMERIC(10, 2) NOT NULL,
    subtotal NUMERIC(10, 2) NOT NULL,
    CONSTRAINT fk_venta FOREIGN KEY (id_venta) REFERENCES ventas(id_venta),
    CONSTRAINT fk_producto FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);