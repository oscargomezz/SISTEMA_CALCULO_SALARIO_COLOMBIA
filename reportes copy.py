import matplotlib.pyplot as plt
import pandas as pd
import os
import libreria

def histograma_por_salarios(pagos, encabezado_pagos):
    df = pd.DataFrame(pagos, columns=encabezado_pagos)

    # Agrupar los pagos por empleado
    pagos_por_empleado = df.groupby('Cédula')['Salario neto'].sum()

    # Crear figura y ejes
    fig, ax = plt.subplots(figsize=(10, 6))

    # Graficar barras
    barras = pagos_por_empleado.plot(kind='bar', ax=ax, color='skyblue', edgecolor='black')

    # Etiquetas y título
    ax.set_xlabel('ID Empleado')
    ax.set_ylabel('Pagos en COP')
    ax.set_title('Pagos por Empleado')
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Colocar etiquetas de los valores sobre cada barra
    for barra in barras.patches:
        altura = barra.get_height()
        if altura > 0:
            ax.annotate(f'{altura:,.0f}',  # Formato con separador de miles
                        (barra.get_x() + barra.get_width() / 2, altura),
                        ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

    # Mostrar gráfico
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# ESTRUCTURAS DE PAGOS
pagos = []  
encabezado_pagos = ["ID", "Cédula", "Días", "Salario básico", "Salario devengado", "Auxilio transporte", "Descuento salud", "Descuento pension", "Salario neto"]

empleados   = []  #Lista de Listas, muchos empleados
encabezado = ["ID", "Cédula", "Nombres", "Nacimiento", "Dirección", "Telefonos", "Mail", "Activo" , "Salario"]

# Cargar datos
ruta_directorio = "datos/"
nombre_archivo_pagos = os.path.join(ruta_directorio, 'pagos.dat')
pagos = libreria.cargar(pagos, nombre_archivo_pagos)

def menu():
    if pagos is not None:
        while True:
            print("\nMenú de Gráficas")
            print("1. Histogramas Pagos por empleado")
            print("4. Salir")
            opcion = input("Selecciona una opción: ")
            if opcion == '1':
                histograma_por_salarios(pagos, encabezado_pagos)
            elif opcion == '4':
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()
