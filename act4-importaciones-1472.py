import pandas as pd
import matplotlib.pyplot as plt

print("jose solis NC 1472")

# 1. Crear diccionario con datos de incidencias de entrega
incidencias_entrega = {
    'id_incidencia': [701, 702, 703, 704, 705, 706],
    'id_guia': [111, 333, 555, 222, 666, 444],
    'fecha': ['2024-01-11', '2024-01-12', '2024-01-12', '2024-01-09', '2024-01-08', '2024-01-10'],
    'tipo_incidencia': ['Direccion incorrecta', 'Retraso por clima', 'Cliente ausente', 'Paquete danado', 'Entregado a vecino', 'Retraso trafico'],
    'gravedad': ['Media', 'Alta', 'Baja', 'Alta', 'Baja', 'Media'],
    'responsable': ['Chofer', 'Externo', 'Cliente', 'Almacen', 'Chofer', 'Externo'],
    'accion_correctiva': ['Reprogramar', 'Reprogramar', 'Dejar aviso', 'Reemplazo', 'Validar con cliente', 'Monitoreo'],
    'costo_extra': [0, 0, 0, 500, 0, 0],
    'tiempo_retraso_horas': [24, 48, 24, 0, 0, 4],
    'resuelta': [True, False, True, True, True, True]
}

print("Análisis Exploratorio de Datos EDA")
print("Exploratory Data Analysis) por Jose Solis NC 1472")
print("5. Crear el diccionario con 10 listas y 6 elementos")

# 2. Convertir diccionario en DataFrame
df = pd.DataFrame(incidencias_entrega)
print("\n--- TABLA ORIGINAL DE INCIDENCIAS DE ENTREGA ---")
print(df)

# 3. Exportar los datos a CSV
print("----Convertir el DataFrame en archivo CSV----")
df.to_csv(
    'incidencias_entrega_1472.csv',
    index=False,
    encoding='utf-8-sig'
)
print("\n✅ Archivo CSV creado correctamente")

print("----- 8. Leer los datos desde el archivo CSV -----")
print("incidencias_entrega_1472.csv")
# 4. Leer el archivo CSV
df = pd.read_csv('incidencias_entrega_1472.csv')
print("\n--- DATOS LEÍDOS DESDE CSV ---")
print(df)

print("-----9. Análisis Exploratorio de Datos (EDA)-----")
# 5. Primeros y últimos registros
print("----\n1. PRIMEROS REGISTROS (Head):----")
print(df.head(3)) # Muestra los primeros 3

print("----\n2. ÚLTIMOS REGISTROS (Tail):----")
print(df.tail(2)) # Muestra los últimos 2

# 6. Dimensiones y estructura
print("-----6. Dimensiones y estructura-----")
print(df) # mostrar toda la tabla o matriz
print("\n3. DIMENSIONES (Filas, Columnas):", df.shape)
print("\n4. NOMBRES DE COLUMNAS:\n", df.columns)
print("\n5. TIPOS DE DATOS:\n", df.dtypes)

print("\n6. INFORMACIÓN GENERAL:")
df.info()

# 7. Estadísticas y limpieza
print("-----\n7. ESTADÍSTICAS DESCRIPTIVAS:-----")
print(df.describe())

print("\n8. VALORES FALTANTES (Nulls):")
print(df.isnull().sum())

print("\n9. REGISTROS DUPLICADOS:")
print(df.duplicated().sum())

print("\n10. VALORES ÚNICOS POR COLUMNA:")
print(df.nunique())
print("Responsables únicos:", df['responsable'].unique())

# 8. Análisis específico
print(df)
print("--------------------------------------------------")
print("-----\n11. INCIDENCIAS POR RESPONSABLE:-----")
print(df['responsable'].value_counts())

print("\n12. PROMEDIO DE TIEMPO DE RETRASO (HORAS):", df['tiempo_retraso_horas'].mean())
print("13. TIEMPO DE RETRASO MÁXIMO (HORAS):", df['tiempo_retraso_horas'].max())
print("14. TIEMPO DE RETRASO MÍNIMO (HORAS):", df['tiempo_retraso_horas'].min())

# 9. Ordenamiento, filtrado y agrupación
print("9. Ordenamiento, filtrado y agrupación")
print("-----\n15. INCIDENCIAS ORDENADAS POR TIEMPO DE RETRASO (Mayor a menor):-----")
print(df.sort_values(by='tiempo_retraso_horas', ascending=False))

print("\n16. INCIDENCIAS CON TIEMPO DE RETRASO MAYOR A 10 HORAS:")
filtro = df[df['tiempo_retraso_horas'] > 10]
print(filtro)

print("\n17. RESUMEN POR RESPONSABLE:")
resumen = df.groupby('responsable').agg(
    incidencias=('id_incidencia', 'count'),
    retraso_promedio=('tiempo_retraso_horas', 'mean'),
    costo_maximo=('costo_extra', 'max')
)
print(resumen)

# 18. Gráfica de barras: Incidencias por responsable
print("18. Gráfica de barras: Incidencias por responsable")
conteo = df['responsable'].value_counts()
plt.figure(figsize=(8, 5))
plt.bar(conteo.index, conteo.values, color='skyblue')
plt.title('Incidencias por responsable jose 1472')
plt.xlabel('Responsable')
plt.ylabel('Cantidad de incidencias')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 19. Gráfica de barras: Tiempo de retraso por tipo de incidencia
plt.figure(figsize=(9, 5))
plt.bar(df['tipo_incidencia'], df['tiempo_retraso_horas'], color='lightgreen')
plt.title('Tiempo de retraso por tipo de incidencia jose 1472')
plt.xlabel('Tipo de incidencia')
plt.ylabel('Tiempo de retraso (horas)')
plt.xticks(rotation=25)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 20. Histograma: Distribución de tiempo de retraso
plt.figure(figsize=(8, 5))
plt.hist(df['tiempo_retraso_horas'], bins=5, color='orange', edgecolor='black')
plt.title('Distribución de tiempo de retraso EDA jose 1472')
plt.xlabel('Tiempo de retraso (horas)')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 21. Gráfica de dispersión: Tiempo de retraso vs Costo extra
plt.figure(figsize=(8, 5))
plt.scatter(df['tiempo_retraso_horas'], df['costo_extra'], color='red', s=100)
plt.title('Relación entre tiempo de retraso y costo extra EDA por jose 1472')
plt.xlabel('Tiempo de retraso (horas)')
plt.ylabel('Costo extra ($)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 22. Diagrama de caja: Distribución de tiempo de retraso
plt.figure(figsize=(7, 5))
plt.boxplot(df['tiempo_retraso_horas'], patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Distribución de tiempo de retraso (Boxplot) EDA jose 1472')
plt.ylabel('Tiempo de retraso (horas)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 23. Matriz de correlación
correlacion = df.corr(numeric_only=True)
print("\n--- MATRIZ DE CORRELACIÓN ---")
print(correlacion)

plt.figure(figsize=(9, 6))
plt.imshow(correlacion, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(correlacion.columns)), correlacion.columns, rotation=45)
plt.yticks(range(len(correlacion.columns)), correlacion.columns)
plt.title('Matriz de correlación de variables numéricas EDA jose 1472')
plt.tight_layout()
plt.show()

print("jose solis nc 1472")