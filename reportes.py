

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import libreria
import os

'''
def graficar_histograma(datos, columna_factura, columna_total):
  df = pd.DataFrame(datos, columns=['Factura', 'Total'])
  fig, ax = plt.subplots(1, 2, figsize=(12, 6))

  # Histograma de Producción de Energía
  df.groupby(columna_factura)[columna_total].sum().plot(kind='bar', ax=ax[0], color='skyblue', edgecolor='black')
  ax[0].set_title('VENTAS POR FACTURA')
  ax[0].set_xlabel('Facturas')
  ax[0].set_ylabel('Total Ventas')
  ax[0].grid(axis='y', linestyle='--', alpha=0.7)

  # Colocar valores encima de las barras de producción
  for barra in ax[0].patches:
    ax[0].annotate(f'{barra.get_height():.0f}',
           (barra.get_x() + barra.get_width() / 2, barra.get_height()),
           ha='center', va='bottom')    
   
  plt.tight_layout()
  plt.show()
'''

def histotramaPorSalarios (pagos, encabezadoPagos):
    #encabezadoPagos = ['Nro.Factura', 'Código Producto', 'Precio Unitario', 'Cantidad', 'IVA', 'Descuento', 'total']
    df = pd.DataFrame (pagos, columns=encabezadoPagos)

    pagos_por_empleado = df.groupby('ID')['Salario neto'].sum()

    pagos_por_empleado.plot(kind='bar')

    plt.xlabel('PAGOS')
    plt.ylabel('Pagos en COP')
    plt.title('Pagos X Empleado')

    plt.show()


#ESTRUCTURAS DE PAGOS
pago    = []  #Lista una solo pago
pagos   = []  #Lista de Listas, muchos pagos
encabezadoPagos = ["ID", "Cédula", "Días", "Salario básico", "Salario devengado", "Auxilio transporte", "Descuento salud", "Descuento pension", "Salario neto"]


rutaDirectorio = "datos/"
nombreArchivopagos   = os.path.join(rutaDirectorio, 'pagos.dat')
pagos   = libreria.cargar(pagos, nombreArchivopagos)

def menu():
    if pagos is not None:
        while True:
            print("\nMenú de Gráficas")
            print("1. Histogramas Pagos por empleado")
            print("4. Salir")
            opcion = input("Selecciona una opción: ")
            if opcion == '1':
                histotramaPorSalarios (pagos, encabezadoPagos)
            elif opcion == '2':
                break
            elif opcion == '3':
                break
            elif opcion == '4':
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()
