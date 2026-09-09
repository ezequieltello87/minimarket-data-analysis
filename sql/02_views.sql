-- Vista maestra para análisis y consumo en Power BI
CREATE OR REPLACE VIEW vw_ventas_detalle_completo AS
SELECT 
    d.id_detalle,
    v.id_venta,
    v.fecha_hora,
    v.medio_pago,
    v.monto_total AS venta_monto_total,
    c.id_cliente,
    c.nombre_cliente,
    p.id_producto,
    p.nombre AS producto_nombre,
    p.categoria,
    d.cantidad,
    d.precio_unitario,
    d.subtotal
FROM detalle_ventas d
JOIN ventas v ON d.id_venta = v.id_venta
LEFT JOIN clientes c ON v.id_cliente = c.id_cliente
JOIN productos p ON d.id_producto = p.id_producto;