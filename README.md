# 🛒 Análisis Transaccional y Segmentación de Clientes en Retail

## 📋 Descripción del Proyecto
Este proyecto simula un pipeline completo de ingeniería y análisis de datos para una cadena de supermercados. El objetivo principal es transformar datos transaccionales crudos (provenientes de archivos CSV) en información de negocio procesable mediante un flujo ETL robusto en Python, almacenamiento estructurado en PostgreSQL, consultas analíticas avanzadas en SQL y un dashboard interactivo.

---

## 🏗️ Arquitectura y Flujo de Datos (ETL)
El proyecto sigue el estándar moderno de análisis de datos:
1. **Extracción**: Lectura de archivos CSV crudos (`data/raw/`).
2. **Transformación**: Limpieza de datos, manejo de nulos, estandarización de textos y tipados utilizando **Python (Pandas)**.
3. **Carga**: Inyección automatizada del DataFrame limpio hacia tablas relacionales en **PostgreSQL** mediante **SQLAlchemy**.
4. **Explotación**: Creación de vistas analíticas en SQL y visualización ejecutiva en **Power BI**[cite: 9].

```text
[ CSV Crudo ] ──> [ Python (Pandas ETL) ] ──> [ PostgreSQL ] ──> [ Vistas SQL & RFM ] ──> [ Power BI Dashboard ]
```
---

## 🛠️ Stack Tecnológico
* **Lenguaje:** Python 3.x
* **Manipulación y ETL:** Pandas
* **Base de Datos:** PostgreSQL
* **Conexión y ORM:** SQLAlchemy, Psycopg2
* **Visualización de Datos:** Power BI

---

## 📂 Estructura del Repositorio
```text
├── dashboard/               # Archivo .pbix del reporte ejecutivo
├── data/
│   ├── raw/                 # Datos transaccionales originales (CSV)
│   └── processed/           # Datos limpios y normalizados listos para consumo
├── scripts/
│   ├── etl_limpieza.ipynb   # Notebook de auditoría, limpieza y validación
│   └── cargar_a_postgres.py # Script de automatización para inserción en DB
├── sql/
│   ├── 01_schema.sql        # Creación de tablas, llaves primarias y foráneas
│   ├── 02_views.sql         # Creación de la vista maestra para Power BI
│   └── 03_analysis.sql      # Consultas SQL analíticas (Top clientes, categorías, etc.)
└── README.md