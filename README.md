# 📊 Análisis de Ventas

## 📋 Descripción del Proyecto

Este proyecto realiza un análisis completo de datos de ventas utilizando Python, pandas y matplotlib. El objetivo es procesar transacciones comerciales, calcular métricas clave y generar visualizaciones informativas

### 🎯 Funcionalidades Principales

- **Carga y procesamiento de datos** desde archivo CSV
- **Análisis temporal** de ventas por mes
- **Identificación de productos estrella** (más vendidos y con mayores ingresos)
- **Generación de gráficos** interactivos y estáticos
- **Exportación de visualizaciones** en formato PNG

## 🚀 Instalación y Configuración

### Prerrequisitos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### 1. Clonar el Repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd analisis_ventas
```

### 2. Crear Entorno Virtual

```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual
# En Windows:
venv\Scripts\activate

# En macOS/Linux:
source venv/bin/activate
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

## 📁 Estructura del Proyecto

```
analisis_ventas/
├── analisis.py          # Script principal de análisis
├── ventas.csv           # Datos de ventas (archivo de entrada)
├── requirements.txt     # Dependencias del proyecto
├── README.md           # Este archivo
├── venv/               # Entorno virtual (se crea automáticamente)
└── imagenes_guardadas/ # Directorio para gráficos exportados (se crea automáticamente)
```

## 🎮 Uso del Proyecto

### Ejecutar el Análisis

```bash
# Asegúrate de que el entorno virtual esté activado
python analisis.py
```

### Archivos de Entrada

El archivo `ventas.csv` debe contener las siguientes columnas:
- `fecha`: Fecha de la venta (formato YYYY-MM-DD)
- `producto`: Nombre del producto vendido
- `cantidad_vendida`: Cantidad de unidades vendidas
- `precio`: Precio unitario del producto

## 📈 Resultados Esperados

### 1. Análisis en Consola
- Resumen de los datos cargados
- Ventas totales por mes
- Producto más vendido en unidades
- Producto con mayores ingresos

### 2. Visualizaciones Generadas
- **Gráfico de barras**: Ventas totales por mes
- **Gráfico horizontal**: Top 5 productos por ingresos
- **Archivos PNG**: Exportados en `imagenes_guardadas/`

**Desarrollado con ❤️ usando Python, pandas y matplotlib**
