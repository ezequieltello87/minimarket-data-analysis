-- 1. Ingresos totales y volumen por categoría de producto
SELECT 
    p.categoria,
    SUM(d.cantidad) AS unidades_vendidas,
    SUM(d.subtotal) AS ingresos_totales,
    ROUND(AVG(d.subtotal), 2) AS ticket_promedio_linea
FROM detalle_ventas d
JOIN productos p ON d.id_producto = p.id_producto
GROUP BY p.categoria
ORDER BY ingresos_totales DESC;

-- 2. Rendimiento de los 8 productos del catálogo
SELECT 
    p.nombre AS producto,
    p.categoria,
    SUM(d.cantidad) AS total_unidades,
    SUM(d.subtotal) AS recaudacion_total
FROM detalle_ventas d
JOIN productos p ON d.id_producto = p.id_producto
GROUP BY p.nombre, p.categoria
ORDER BY recaudacion_total DESC;

-- 3. Distribución de ventas por medio de pago
SELECT 
    medio_pago,
    COUNT(id_venta) AS cantidad_transacciones,
    SUM(monto_total) AS monto_recaudado,
    ROUND(AVG(monto_total), 2) AS promedio_ticket
FROM ventas
GROUP BY medio_pago
ORDER BY monto_recaudado DESC;

-- 4. Top 10 clientes con mayor volumen de compra
SELECT 
    c.id_cliente,
    c.nombre_cliente,
    COUNT(v.id_venta) AS total_compras,
    SUM(v.monto_total) AS gastado_total
FROM ventas v
JOIN clientes c ON v.id_cliente = c.id_cliente
GROUP BY c.id_cliente, c.nombre_cliente
ORDER BY gastado_total DESC
LIMIT 10;