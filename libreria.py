import os
import sys
import time
import re
from tabulate import tabulate
from colorama import Fore, Back, Style, init
import pickle
from datetime import datetime

from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Image
from reportlab.lib import colors
from reportlab.lib.units import inch
init()

import msvcrt


#valida que un codigo se encuentre en un diccionario
def leerCodigoValidado (lista, mensaje):
      while True:
          print(f"{mensaje}", end="", flush=True)
          codigoBuscar = input().upper()
          encontrado = buscar(lista, codigoBuscar)
          if encontrado >= 0:
            return codigoBuscar, encontrado
          else:
            print(Fore.YELLOW + Style.BRIGHT + "❌ Error: Código NO existe" + Style.RESET_ALL)
            #print("Error: Código NO existe", end="", flush=True)
            time.sleep(3) # Pausa breve de 1 segundo
            # Borrar las dos líneas anteriores (entrada + mensaje de error)
            sys.stdout.write("\033[F\033[K")  # Borra última línea (Error)
            sys.stdout.write("\033[F\033[K")  # Borra la línea de entrada
            sys.stdout.flush()

#-------------------------------------------------------------------#
#recibe un diccionario lo muestra y validad la opcion del usuario   #
#VALIDA que sea un valor numerio en el rango enviado por parametro  #
#-------------------------------------------------------------------#
def leerDiccionario (diccionario, mensaje):            
      tabla = [[clave, descripcion] for clave, descripcion in diccionario.items()]
      print(tabulate(tabla, headers=["Clave", "Descripción"], tablefmt="fancy_grid"))
      while True:
          opcion = LeerCaracter( mensaje ).upper()
          if opcion in diccionario:
                return opcion
          else:
            print("Error: Opción NO válida", end="", flush=True)
            time.sleep(1) # Pausa breve de 1 segundo
            print(end="\r\033[K") # Mueve el cursor al inicio de la linea y limpia la línea


###############################################
#función lee un solo carácter NO espera ENTER #
###############################################
def LeerCaracter (mensaje):
  return input(mensaje).strip().lower()
  #print(mensaje, end="", flush=True)
  #tecla = msvcrt.getch().decode('utf-8').lower()  # Captura la tecla presionada
  #print(tecla)  # Imprime la tecla en la consola para que el usuario la vea
  #return tecla
  #return msvcrt.getch().lower().decode('utf-8')  #getch captura un solo caracter No hay que dar enter

##############################################################################################
# Función que valida el ingreso de una cadena que no sea vacia y limitar un maximo caracteres#
# SI se quiere que retorne recortado usar return cadena[:maximoCaracteres]
##############################################################################################
def leerCadena( mensaje, maximoCaracteres ):
    while True:
        #print(f"{mensaje}", end="", flush=True)
        cadena = input( f"{mensaje} (Máx. {maximoCaracteres} caracteres): ").strip()
        if 0 < len(cadena) <= maximoCaracteres:  #Retorna la cadena válida
           return cadena[:maximoCaracteres] #cadena
        else:
            print(f"❌ Error: La cadena no debe estar vacía y debe tener máximo {maximoCaracteres} caracteres.", end="", flush=True)
            time.sleep(1)                 # Pausa breve de 1 segundo)
            print("\r\033[K", end="")     # \r Mueve cursor al inicio de la línea y limpia la línea con \033[K
            print("\033[F\033[K", end="") # Mueve cursor al final de la línea de arriba y limpia la línea
            continue
        
############################################################################
# Función que valida el ingreso de la fecha en un formato y rango correcto #
############################################################################
def leerFecha( mensaje ):
    while True:
        #print(f"{mensaje}", end="", flush=True)
        fecha_str = input( mensaje )
        try:
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
            return fecha.strftime("%Y-%m-%d")  #fecha  # Retorna un objeto datetime (fecha y hora)
        except ValueError:
            print("❌ Error: Formato incorrecto. Intente de nuevo.", end="", flush=True)
            time.sleep(1)                 # Pausa breve de 1 segundo)
            print("\r\033[K", end="")     # \r Mueve cursor al inicio de la línea y limpia la línea con \033[K
            print("\033[F\033[K", end="") # Mueve cursor al final de la línea de arriba y limpia la línea
            continue

############################################################################
# Función que valida el ingreso del mail en un formatro correcto           #
############################################################################
def leerMail ( mensaje ):
      while True:
          #print(f"{mensaje}", end="", flush=True) 
          email = input ( mensaje )
          #correo valido verifica antes y despues del @
          patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'          
          if re.match(patron, email.lower()):
            return email
          else:
            print("Error: Email NO es correcto", end="", flush=True)
            time.sleep(1) # Pausa breve de 1 segundo
            print(end="\r\033[K\033[F") # Mueve el cursor al inicio de la linea y limpia la línea

############################################################################
# Función que valida el ingreso de un decimal en un rango minimo y maximo  #
############################################################################
def  leerEntero (mensaje, minimo, maximo):
  while True:
    print(f"{mensaje} ({minimo}-{maximo}): ", end="", flush=True)
    valor = input().strip()
    # Verificar que no esté vacío ni tenga espacios intermedios
    if not valor or " " in valor:
      print(f"❌Error: {mensaje} no debe estar vacío ni contener espacios.", end="", flush=True)
      time.sleep(1)                 # Pausa breve de 1 segundo)
      print("\r\033[K", end="")     # \r Mueve cursor al inicio de la línea y limpia la línea con \033[K
      print("\033[F\033[K", end="") # Mueve cursor al final de la línea de arriba y limpia la línea
      continue
      # Verificar si es un número decimal válido
    try:
      numero = int(valor)
      if minimo <= numero <= maximo:  # numero >= minimo and numero <= maximo
        return numero
      else:
        print(f"❌Error: {mensaje} debe estar entre {minimo} y {maximo}.", end="", flush=True)
        time.sleep(1)                 # Pausa breve de 1 segundo
        print("\r\033[K", end="")     # Mueve cursor al inicio de la línea y limpia la línea
        print("\033[F\033[K", end="") # Mueve cursor al final de la línea de arriba y limpia la línea
    except ValueError:
      print("❌Error: {mensaje} inválida. ", end="", flush=True)
      time.sleep(1)                 # Pausa breve de 1 segundo
      print("\r\033[K", end="")     # Mueve cursor al inicio de la línea y limpia la línea
      print("\033[F\033[K", end="") # Mueve cursor al final de la línea de arriba y limpia la línea

############################################################################
# Función que valida el ingreso de un decimal en un rango minimo y maximo  #
############################################################################
def  leerFlotante (mensaje, minimo, maximo):
  while True:
    print(f"{mensaje} ({minimo}-{maximo}): ", end="", flush=True)
    valor = input().strip().replace(",", ".")
    # Verificar que no esté vacío ni tenga espacios intermedios
    if not valor or " " in valor:
      print(f"❌Error: {mensaje} no debe estar vacío ni contener espacios.", end="", flush=True)
      time.sleep(1)                 # Pausa breve de 1 segundo)
      print("\r\033[K", end="")     # \r Mueve cursor al inicio de la línea y limpia la línea con \033[K
      print("\033[F\033[K", end="") # Mueve cursor al final de la línea de arriba y limpia la línea
      continue
      # Verificar si es un número decimal válido
    try:
      numero = float(valor)
      if minimo <= numero <= maximo:  # numero >= minimo and numero <= maximo
        return numero
      else:
        print(f"❌Error: {mensaje} debe estar entre {minimo} y {maximo}.", end="", flush=True)
        time.sleep(1)                 # Pausa breve de 1 segundo
        print("\r\033[K", end="")     # Mueve cursor al inicio de la línea y limpia la línea
        print("\033[F\033[K", end="") # Mueve cursor al final de la línea de arriba y limpia la línea
    except ValueError:
      print("❌Error: {mensaje} inválida. ", end="", flush=True)
      time.sleep(1)                 # Pausa breve de 1 segundo
      print("\r\033[K", end="")     # Mueve cursor al inicio de la línea y limpia la línea
      print("\033[F\033[K", end="") # Mueve cursor al final de la línea de arriba y limpia la línea
      
    
############################################################################
# Función que valida el nombre de un mes ingresado #
############################################################################      
def leerMes(mensaje="Ingrese un mes"):
    meses_validos = {
        "ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO",
        "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"
    }

    while True:
        print(f"{mensaje}: ", end="", flush=True)
        valor = input().strip().upper()

        # Verificar que no esté vacío ni tenga espacios intermedios
        if not valor or " " in valor:
            print("❌ Error: El mes no debe estar vacío ni contener espacios.", end="", flush=True)
            time.sleep(2)
            print("\r\033[K", end="")
            print("\033[F\033[K", end="")
            continue

        # Verificar si el mes ingresado es válido
        if valor in meses_validos:
            return valor
        else:
            print("❌ Error: Mes inválido. Inténtelo de nuevo.", end="", flush=True)
            time.sleep(2)
            print("\r\033[K", end="")
            print("\033[F\033[K", end="")      
      

#La función devuelve el nombre del sistema operativo y aplica el comando respectivo
def limpiarPantalla ():    
    if os.name == 'nt':  # Para sistemas Windows
        os.system('cls')
    else:  # Para sistemas Unix/Linux/Mac
        os.system('clear')
    
def cabecera ( titulo ): 
    print(Fore.RED + f"\n   {titulo}    \n" + Style.RESET_ALL )


def mensajeEsperaSegundos( mensaje, segundos ):
    print(Fore.YELLOW + Style.BRIGHT + mensaje + Style.RESET_ALL)
    time.sleep( segundos )

def mensajeErrorEsperaSegundos( mensaje, segundos ):
    print(Fore.RED + Style.BRIGHT + mensaje + Style.RESET_ALL)
    time.sleep( segundos )

##################################################################
# Procedimiento que espera que el usuario presione Enter         #
##################################################################
def mensajeEsperaEnter( mensaje ):
    print("\n" + Fore.GREEN + Style.BRIGHT + mensaje + Style.RESET_ALL, end="")
    input()

#-----------------------------------------------------------#
#Función con las opciones del CRUD para cualquier entidad   #
#-----------------------------------------------------------#
def menuCrud( titulo ): 
    limpiarPantalla()    #os.system('cls')
    print(tabulate([['' + Fore.GREEN + "SISTEMA CALCULO SALARIO COLOMBIA \n" + Style.RESET_ALL + '' + Fore.LIGHTYELLOW_EX + "MENU: " + titulo + '' + Style.RESET_ALL + ''],],
                     tablefmt='fancy_grid',
                     stralign='center'))
    print(tabulate([ 
                     ['*' * (len(titulo) + 6)],
                     ["\t" + Back.YELLOW + "[1]" + Style.RESET_ALL + "  INSERTAR  "],
                     ["\t" + Back.YELLOW + "[2]" + Style.RESET_ALL + "  LISTAR    "],
                     ["\t" + Back.YELLOW + "[3]" + Style.RESET_ALL + "  CONSULTAR "],
                     ["\t" + Back.YELLOW + "[4]" + Style.RESET_ALL + "  ACTUALIZAR"],
                     ["\t" + Back.YELLOW + "[5]" + Style.RESET_ALL + "  ELIMINAR  "],
                     ["\t" + Back.YELLOW + "[6]" + Style.RESET_ALL + "  SALIR     "]
                     ],
                     tablefmt='fancy_grid',
                     stralign='left'))

#----------------------------------------------------------------------------#
#Función para listar cualquier lista, le debo enviar la lista y el encezado  #
#----------------------------------------------------------------------------#
def listar(encabezado, listas): 
    # Formatear columnas de numeros que no salga exponencial
    limpiarPantalla()
    
    encabezado_coloreado = [f"{Fore.GREEN}{Style.BRIGHT}{col}{Style.RESET_ALL}" for col in encabezado]
    
    print(tabulate(listas, headers=encabezado_coloreado, tablefmt='fancy_grid', stralign='left', floatfmt=",.0f"))
'''   
    headers = encabezado
    #headers =[Fore.GREEN + 'PLACA', 'MARCA', 'MODELO', 'COLOR', 'PRECIO' ]
    print(tabulate(listas,
                   headers = headers,
                   tablefmt='fancy_grid',
                   stralign='left',
                   floatfmt=",.0f"))
'''                   
#-------------------------------------------------------------------------------------#
# Función Mostrar un solo registro, con la cabecera y los datos de la entidad enviada #
#-------------------------------------------------------------------------------------#
def mostrar(encabezado, listas): 
    #os.system('cls')
    # Formatear columnas de numeros que no salga exponencial
    lista = [listas]   #CONVERTIMOS A LISTA DE LISTAS POR QUE TABULATE LO EXIGE
    
    # Imprimir encabezado en color sin modificar los datos internos
    encabezado_coloreado = [f"{Fore.GREEN}{Style.BRIGHT}{col}{Style.RESET_ALL}" for col in encabezado]
    
    print(tabulate(lista, headers=encabezado_coloreado, tablefmt='fancy_grid', stralign='left', floatfmt=",.0f"))
'''  
    headers = encabezado #dependiendo de la entidad, se envian por parametro
    print(tabulate(lista,
                   headers = headers,
                   tablefmt='fancy_grid',
                   stralign='left',
                   floatfmt=",.0f"))
'''                   

#-------------------------------------------------------------------------------------#
# Función Mostrar un solo registro, con la cabecera y los datos de la entidad enviada #
#-------------------------------------------------------------------------------------#
def mostrarEmpleado(encabezadoEmpleados, listas): 
    #os.system('cls')
    # Formatear columnas de numeros que no salga exponencial
    #lista = [listas]   #CONVERTIMOS A LISTA DE LISTAS POR QUE TABULATE LO EXIGE
    lista = listas if isinstance(listas[0], list) else [listas]
    headers = encabezadoEmpleados #dependiendo de la entidad, se envian por parametro
    print(tabulate(lista,
                   headers = headers,
                   tablefmt='fancy_grid',
                   stralign='left',
                   floatfmt=",.0f"))
    
#-----------------------------------------------------------#
# Función para buscar elemento en lista por su codigo PK,   #
# devolver indice si lo encuentra o -1 si no lo encuentra   #
#-----------------------------------------------------------#
def buscar(lista, codigoBuscar):
    posicion = -1
    for indice, registro in enumerate(lista):   #recorre toda la lista y extrae registro a registro con su indice
        #print(indice, " -- ", fila)  0.placa 1.marca 2.color......
        if str(registro[0]).upper() == str(codigoBuscar).upper():
            return indice
    return posicion


#---------------------------------------------------------#
# Función para guardar Información en Archivos - MODO  w, # 
# si existe lo borra, si no existe lo crea                #
#---------------------------------------------------------#
def guardar(lista, filename):
    archivo = open( filename, 'wb') #W se abre solo para escritua y si existe lo borra y crea uno nuevo y B indica que un archivo binario
    pickle.dump(lista, archivo)
    archivo.close()
    print(""+Fore.LIGHTYELLOW_EX+"\n\n>>> Guardando Información en los archivos correspondientes <<< " + Style.RESET_ALL)
    time.sleep(2)

#----------------------------------------------------------------------#
# Función para cargar Información en Archivos, MODO R, de solo lectura #
#----------------------------------------------------------------------#
def cargar(lista, filename):
    try:
        archivo = open(filename, 'rb')   #R se abre solo para lectura y B indica que un archivo binario
        lista = pickle.load(archivo)
        archivo.close()
        print("" + Fore.RED+"\n>>> Cargando Información : "+filename + '' + Style.RESET_ALL)
        time.sleep(1)
        return lista
    except:
        print("" + Fore.RED+"\n>>> Error al cargar el archivo o no se ha creado: " + filename + '' + Style.RESET_ALL)
        time.sleep(1)
    return lista


#GENERA Y ABRE LOS PDF GENERADOS


def abrirPDF( archivo_pdf):
    #directorio = "reportesPDF"
    #archivo_pdf = os.path.join(directorio, "empleados.pdf") 
    try:
        if sys.platform == "win32":  # Windows
            os.startfile(archivo_pdf)
        elif sys.platform == "darwin":  # macOS
            os.system(f"open {archivo_pdf}")
        elif sys.platform.startswith("linux"):  # Linux
            os.system(f"xdg-open {archivo_pdf}")
        else:
            print("⚠ No se pudo abrir el PDF automáticamente.")
    except Exception as e:
        print(f"❌ Error al abrir el PDF: {e}")


# Función para generar PDF con logo y tabla ajustada
def generarPDF(encabezado, empleados, archivo_pdf, titulo, logo):
    # Configuración de márgenes amplios
    margen = 40
    extra_margen_visual = 15
    ancho_total = 792  
    ancho_util = (ancho_total - (2 * margen)) - (2 * extra_margen_visual)

    doc = SimpleDocTemplate(archivo_pdf, pagesize=landscape(letter),
                          leftMargin=margen, rightMargin=margen,
                          topMargin=margen, bottomMargin=margen)

    elementos = []

    # Función para calcular el ancho necesario para cada columna
    def calcular_ancho_columnas(datos):
        # Anchos mínimos y máximos (en puntos)
        min_width = 40  # Ancho mínimo para cualquier columna
        max_width = 200  # Ancho máximo para cualquier columna
        
        # Inicializar anchos con el ancho de los encabezados
        anchos = [min_width] * len(datos[0])
        
        # Fuente para cálculos
        normal_font = 'Helvetica'
        bold_font = 'Helvetica-Bold'
        font_size = 9
        
        for col in range(len(datos[0])):
            max_text_width = 0
            
            for row in range(len(datos)):
                # Determinar si es encabezado (usamos fuente bold)
                font = bold_font if row == 0 else normal_font
                
                # Calcular ancho aproximado del texto
                text = str(datos[row][col])
                text_width = len(text) * font_size * 0.6  # Factor de ajuste empírico
                
                # Ajustar por fuente bold
                if row == 0:
                    text_width *= 1.15
                
                # Considerar saltos de línea
                line_count = text.count('\n') + 1
                if line_count > 1:
                    text_width = text_width / line_count * 1.5
                
                if text_width > max_text_width:
                    max_text_width = text_width
            
            # Ajustar el ancho calculado con límites
            anchos[col] = min(max(min_width, max_text_width + 20), max_width)  # +20 por padding
        
        # Normalizar los anchos para que sumen el ancho útil
        suma_actual = sum(anchos)
        factor_ajuste = ancho_util / suma_actual if suma_actual > 0 else 1
        anchos = [w * factor_ajuste for w in anchos]
        
        return anchos

    # Agregar logos
    try:
        # Logo de empleados
        img_logo = Image(logo, width=2.3*inch, height=1.75*inch)
        img_logo.hAlign = 'CENTER'
        elementos.append(img_logo)

    except:
        print("⚠️ No se encontraron los logos, el PDF se generará sin ellos.")

    # Espaciado antes del título
    elementos.append(Spacer(1, 20))

    # Título centrado
    tabla_titulo = Table(titulo, colWidths=[ancho_util])
    tabla_titulo.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 14),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 15),
        ('TOPPADDING', (0, 0), (-1, -1), 15),
    ]))
    elementos.append(tabla_titulo)

    # Preparar datos y calcular anchos automáticos
    datos = [encabezado]
    datos.extend(empleados)
    
    # Calcular anchos de columna automáticamente
    anchos_columnas = calcular_ancho_columnas(datos)

    # Crear tabla con anchos calculados
    tabla = Table(datos, colWidths=anchos_columnas)

    # Estilos de la tabla
    estilo = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4F81BD')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.lightgrey),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('WORDWRAP', (0, 0), (-1, -1), True),
    ])
    
    # Aplicar estilo alternado para filas
    for i, row in enumerate(datos):
        if i > 0:
            bg_color = colors.white if i % 2 == 1 else colors.HexColor('#DCE6F1')
            estilo.add('BACKGROUND', (0, i), (-1, i), bg_color)

    tabla.setStyle(estilo)
    
    # Añadir espacio antes de la tabla
    elementos.append(Spacer(1, 15))
    elementos.append(tabla)

    # Generar el PDF
    doc.build(elementos)
    print(f"PDF generado correctamente con columnas autoajustables: {archivo_pdf}")



############################################################################
#FUNCIONES CALCULO SALARIO
############################################################################

# Funcion para calcular el salario devengado
def Calcular_salario_devengado(Salario_basico, Dias_trabajados):
    Salario_devengado = (Salario_basico / 30) * Dias_trabajados
    return Salario_devengado

# Funcion para aplicar el auxilio de transporte
def Aplicar_auxilio_transporte(Salario_basico, SALARIO_MINIMO, VALOR_AUXILIO_TRANSPORTE, Dias_trabajados):
    if Salario_basico <= (SALARIO_MINIMO * 2):
        Auxilio_transporte = (VALOR_AUXILIO_TRANSPORTE / 30) * Dias_trabajados
        return Auxilio_transporte
    else:
        return 0
    
# Funcion para calcular el descuento por salud
def Calcular_descuento_salud(Salario_devengado, PORCENTAJE_SALUD):
    Descuento_salud = Salario_devengado * PORCENTAJE_SALUD
    return Descuento_salud

# Funcion para calcular el descuento por pension
def Calcular_descuento_pension(Salario_devengado, PORCENTAJE_PENSION):
    Descuento_pension = Salario_devengado * PORCENTAJE_PENSION
    return Descuento_pension

# Funcion para calcular el salario neto del empleado
def Calcular_salario_neto(Salario_devengado, Auxilio_transporte, Descuento_salud, Descuento_pension):
    Salario_neto = Salario_devengado + Auxilio_transporte - Descuento_salud - Descuento_pension
    return Salario_neto

############################################################################