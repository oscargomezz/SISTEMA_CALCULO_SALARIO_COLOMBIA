import matplotlib.pyplot as plt
import pandas as pd
import os
import libreria

def histograma_todos_los_meses(pagos, encabezado_pagos):
    df = pd.DataFrame(pagos, columns=encabezado_pagos)

    # Crear una columna de etiqueta combinando Empleado y Mes/Año
    df['Etiqueta'] = df['Cédula'] + ' - ' + df['Mes'].str.title() + '/' + df['Año'].astype(str)

    # Agrupar por esa nueva etiqueta y sumar el salario neto
    pagos_por_etiqueta = df.groupby('Etiqueta')['Salario neto'].sum().sort_index()

    # Graficar
    fig, ax = plt.subplots(figsize=(14, 7))
    barras = pagos_por_etiqueta.plot(kind='bar', ax=ax, color='lightgreen', edgecolor='black')

    ax.set_xlabel('Empleado - Mes/Año')
    ax.set_ylabel('Pagos en COP')
    ax.set_title('Pagos por Empleado en Todos los Meses')
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Etiquetas de valores sobre las barras
    for barra in barras.patches:
        altura = barra.get_height()
        if altura > 0:
            ax.annotate(f'{altura:,.0f}',
                        (barra.get_x() + barra.get_width() / 2, altura),
                        ha='center', va='bottom', fontsize=8, fontweight='bold')

    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

# ESTRUCTURAS DE PAGOS
pagos = []  
encabezado_pagos = ["ID", "Cédula", "Días", "Mes", "Año", "Salario básico", "Salario devengado", "Auxilio transporte", "Descuento salud", "Descuento pension", "Salario neto"]

# Cargar datos
ruta_directorio = "datos/"
nombre_archivo_pagos = os.path.join(ruta_directorio, 'pagos.dat')
pagos = libreria.cargar(pagos, nombre_archivo_pagos)

# MENÚ PRINCIPAL
def menu():
    if pagos:
        while True:
            print("\nMenú de Gráficas")
            print("1. Ver gráfico de pagos por empleado para un mes específico")
            print("2. Ver gráfico combinado de pagos por empleado (todos los meses)")
            print("3. Salir")
            opcion = input("Selecciona una opción: ")
            if opcion == '1':
                mes = input("Ingrese el mes (ej. enero): ").strip().lower()
                año = input("Ingrese el año (ej. 2025): ").strip()
                histograma_por_salarios_mes(pagos, encabezado_pagos, mes, año)
            elif opcion == '2':
                histograma_todos_los_meses(pagos, encabezado_pagos)
            elif opcion == '3':
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")
    else:
        print("⚠️ No hay datos de pagos para mostrar.")

# Función para ver solo un mes
def histograma_por_salarios_mes(pagos, encabezado_pagos, mes, año):
    df = pd.DataFrame(pagos, columns=encabezado_pagos)
    df_filtrado = df[(df["Mes"].str.lower() == mes.lower()) & (df["Año"] == int(año))]

    if df_filtrado.empty:
        print(f"\n❌ No hay pagos registrados para {mes.title()} de {año}.")
        return

    pagos_por_empleado = df_filtrado.groupby('Cédula')['Salario neto'].sum()

    fig, ax = plt.subplots(figsize=(10, 6))
    barras = pagos_por_empleado.plot(kind='bar', ax=ax, color='skyblue', edgecolor='black')

    ax.set_xlabel('Cédula Empleado')
    ax.set_ylabel('Pagos en COP')
    ax.set_title(f'Pagos por Empleado - {mes.title()} {año}')
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    for barra in barras.patches:
        altura = barra.get_height()
        if altura > 0:
            ax.annotate(f'{altura:,.0f}',
                        (barra.get_x() + barra.get_width() / 2, altura),
                        ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    menu()
