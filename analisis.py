import pandas as pd
import matplotlib.pyplot as plt
# 1. Cargar datos del CSV
df = pd.read_csv('ventas.csv')
print(df.head())

# 2. Calcular ventas totales por mes
df['fecha'] = pd.to_datetime(df['fecha'])
df['mes'] = df['fecha'].dt.to_period('M')

"""
Consultar la diferencia entre agg y apply, y que resudos retornan un dataset nuevo, un array
"""
ventas_por_mes = df.groupby('mes').apply(lambda d: (d['cantidad_vendida'] * d['precio']).sum())

ventas_por_mes = ventas_por_mes.sort_index()

print('Ventas por mes:')
print(ventas_por_mes)

# 3. Determinar producto más vendido y con mayor ingresos

df['ingreso'] = df['cantidad_vendida'] * df['precio']

ventas_prod = df.groupby('producto').agg({
    'cantidad_vendida': 'sum',
    'ingreso': 'sum'
})

#Retorna el nombre del producto mas vendido
mas_vendido = ventas_prod['cantidad_vendida'].idxmax()

#Retorna el nombre del producto que genera mas ingresos
mayor_ingreso = ventas_prod['ingreso'].idxmax()

print(f'Producto más vendido en unidades: {mas_vendido} (total {ventas_prod.loc[mas_vendido, 'cantidad_vendida']})')

print(f'Producto con mayores ingresos: {mayor_ingreso} (total {ventas_prod.loc[mayor_ingreso, 'ingreso']:.2f} $)')

# 4. Graficar ventas por mes
plt.figure(figsize=(7, 5))
plt.bar(range(len(ventas_por_mes)), ventas_por_mes.values, color='skyblue', edgecolor='navy', alpha=0.7)
plt.xlabel('Mes')
plt.ylabel('Ventas Totales ($)')
plt.title('Ventas Totales por Mes')
plt.xticks(range(len(ventas_por_mes)), [str(mes) for mes in ventas_por_mes.index], rotation=45)
plt.grid(axis='y', alpha=0.3)

# Agregar valores en las barras
for i, valor in enumerate(ventas_por_mes.values):
    plt.text(i, valor + max(ventas_por_mes.values) * 0.01, f'${valor:,.0f}', 
             ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('imagenes_guardadas/ventas_mes.png')
plt.show()

# 5. Graficar los cinco productos más vendidos
top_5_productos = ventas_prod.nlargest(5, 'ingreso')

# Invertir el orden para que el producto con más ingresos aparezca arriba
top_5_productos = top_5_productos.iloc[::-1]

plt.figure(figsize=(10, 6))
bars = plt.barh(range(len(top_5_productos)), top_5_productos['ingreso'], 
                color=['#FFEAA7', '#96CEB4', '#45B7D1', '#4ECDC4', '#FF6B6B'])  # Invertir colores para coincidir con el orden
plt.xlabel('Ingresos Totales ($)')
plt.ylabel('Producto')
plt.title('Top 5 Productos por Ingresos')
plt.yticks(range(len(top_5_productos)), top_5_productos.index)

# Agregar valores en las barras
for i, (producto, ingreso) in enumerate(zip(top_5_productos.index, top_5_productos['ingreso'])):
    plt.text(ingreso + max(top_5_productos['ingreso']) * 0.01, i, f'${ingreso:,.0f}', 
             va='center', fontweight='bold')

plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('imagenes_guardadas/mas_vendidos.png')
plt.show()
