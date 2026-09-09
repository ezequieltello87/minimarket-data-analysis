
# 🛒 Análisis Transaccional y Segmentación de Clientes en Retail

## 📋 Descripción del Proyecto
Este proyecto simula un pipeline completo de ingeniería y análisis de datos para una cadena de supermercados. El objetivo principal es transformar datos transaccionales crudos (provenientes de archivos CSV) en información de negocio procesable mediante un flujo ETL robusto en Python, almacenamiento estructurado en PostgreSQL, consultas analíticas avanzadas en SQL y un dashboard interactivo.

---

## 🏗️ Arquitectura y Flujo de Datos (ETL)
El proyecto sigue el estándar moderno de análisis de datos:
1. **Extracción**: Lectura de archivos CSV crudos (`data/raw/`).
2. **Transformación**: Limpieza de datos, manejo de nulos, estandarización de textos y tipados utilizando **Python (Pandas)**.
3. **Carga**: Inyección automatizada del DataFrame limpio hacia tablas relacionales en **PostgreSQL** mediante **SQLAlchemy**.
4. **Explotación**: Creación de vistas analíticas en SQL y visualización ejecutiva en **Power BI**.

```text
[ CSV Crudo ] ──> [ Python (Pandas ETL) ] ──> [ PostgreSQL ] ──> [ Vistas SQL & RFM ] ──> [ Power BI Dashboard ]