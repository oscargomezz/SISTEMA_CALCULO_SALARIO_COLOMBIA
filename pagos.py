import libreria
import os
import sys
import empleados as E
import re


from tabulate import tabulate
from colorama import Fore, Back, Style, init

init()



#-----------------------------------------------------------#
#Función con las opciones del CRUD para cualquier entidad   #
#-----------------------------------------------------------#
def menuActualizar(  ):
    titulo = "SELECCIONAR LA OPCIÓN A ACTUALIZAR"
    print(tabulate([['' + Fore.GREEN + "SISTEMA CALCULO SALARIO COLOMBIA \n" + Style.RESET_ALL + '' + Fore.LIGHTYELLOW_EX + "MENU: " + titulo + '' + Style.RESET_ALL + ''],],
                     tablefmt='fancy_grid',
                     stralign='center'))
    print(tabulate([ 
                     ['*' * (len(titulo) + 6)],
                     ["\t" + Back.YELLOW + "[1]" + Style.RESET_ALL + "  Nro. Identificación  "],
                     ["\t" + Back.YELLOW + "[2]" + Style.RESET_ALL + "  Días laborados: "],
                     ["\t" + Back.YELLOW + "[3]" + Style.RESET_ALL + "  Mes:    "],
                     ["\t" + Back.YELLOW + "[4]" + Style.RESET_ALL + "  Año:    "],
                     ["\t" + Back.YELLOW + "[5]" + Style.RESET_ALL + "  Regresar     "]
                     ],
                     tablefmt='fancy_grid',
                     stralign='left'))
    
def actualizar ( encabezadoPagos, pago ):        
    while True:                
        print("*** ACTUALIZANDO DATOS DEL PAGO ***")
        print("*" * 30)    
        libreria.mostrar(encabezadoPagos, pago)
        menuActualizar()
        respuesta = libreria.LeerCaracter("OPCION: ")
        match respuesta:
            case '1':
                pago[1] = libreria.leerCadena( "NRO. Identificación: ", 20 ).upper() #input("NRO. IDENTIFICACIÓN: ")
            case '2':
                pago[2] = libreria.leerFecha("Días laborados: ", 3)
            case '3':
                pago[3] = libreria.leerCadena( "Mes ", 1, 12 ) 
            case '4':
                pago[4] = libreria.leerEntero( "Año ", 2025, 2100 )          
            case '5':
                return pago
            case _:
                libreria.mensajeErrorEsperaSegundos("OPCIÓN NO VALIDA", 1)    
                

               

def filtrarEmpleadosActivos(empleados):
    sublista = []
    activo = 'S'
    for empleado in empleados:
        if empleado[7].upper() == activo:
            sublista.append(empleado)
    return sublista
        

def generarNominaMes ( empleados ):
    global empleado
    libreria.limpiarPantalla()
    print("*** INSERTAR NOVEDADES ***")
    print("*" * 30)
    mes             = libreria.leerMes("Escriba el mes a pagar: ")
    año             = libreria.leerEntero("Escriba el año a pagar: ",  2025, 2100)
    empleadosActivos = filtrarEmpleadosActivos(empleados)
    
    for empleado in empleadosActivos:
        
            
        if libreria.existePagoRegistrado(pagos, empleado, mes, año):
            
            mensaje = f"❌ El empleado con cédula {empleado[1]} ya tiene un pago registrado para {mes} de {año}"
            libreria.mensajeEsperaSegundos(mensaje, 12)
            continue
            
        codigo  = empleado[0]
        diaslaborados  = 30         

        Salario_devengado = libreria.Calcular_salario_devengado(empleado[8], diaslaborados)

            # Funcion para aplicar el auxilio de transporte
        Auxilio_transporte = libreria.Aplicar_auxilio_transporte(empleado[8], SALARIO_MINIMO, VALOR_AUXILIO_TRANSPORTE, diaslaborados)

            # Funcion para calcular el descuento por salud
        Descuento_salud = libreria.Calcular_descuento_salud(Salario_devengado, PORCENTAJE_SALUD)

            # Funcion para calcular el descuento por pension
        Descuento_pension = libreria.Calcular_descuento_pension(Salario_devengado, PORCENTAJE_PENSION)

            # Funcion para calcular el salario neto del empleado
        Salario_neto = libreria.Calcular_salario_neto(Salario_devengado, Auxilio_transporte, Descuento_salud, Descuento_pension)
        
        mensaje = "✅ PAGANDO NÓMINA COMPLETA ..."
                
        pago     =      [codigo, empleado[1], diaslaborados, mes, año ,empleado[8], Salario_devengado, Auxilio_transporte, Descuento_salud, Descuento_pension, Salario_neto]
        pagos.append(pago)
    return pagos                

#VARIABLES GLOBALES Y CONSTANTES
# Se establecen constantes
SALARIO_MINIMO = 1423500.00
VALOR_AUXILIO_TRANSPORTE = 200000.00
PORCENTAJE_SALUD = 0.04
PORCENTAJE_PENSION = 0.04

Salario_devengado = round(0.00, 2)
Salario_neto = round(0.00, 2)
Auxilio_transporte = round(0.00, 2)
Descuento_salud = round(0.00, 2)
Descuento_pension = round(0.00, 2)
mes = 0
año = 0




print("Directorio actual:", os.getcwd())
rutaDirectorio = "datos/"
nombreArchivoPagos   = os.path.join(rutaDirectorio, 'pagos.dat')
nombreArchivoEmpleados   = os.path.join(rutaDirectorio, 'empleados.dat')
#nombreArchivo   = "pagos.dat"

directorio_pdf = "reportesPDF"
archivo_pdf = os.path.join(directorio_pdf, "pagos.pdf") 


diccionarioEstados = {
    'A': "Activa",
    'I': "Inactivo"
}

#ESTRUCTURAS DE EMPLEADOS
empleado    = []  #Lista una solo empleado
empleados   = []  #Lista de Listas, muchos empleados
encabezadoEmpleados = [Fore.GREEN + Style.BRIGHT + "ID", "Cédula", "Nombres", "Nacimiento", "Dirección", "Telefonos", "Mail", "Activo", "Salario" + Style.RESET_ALL]#, "Salario " + Style.RESET_ALL]

encabezadoEmpleados = [re.sub(r'\x1b\[[0-9;]*m', '', col) for col in encabezadoEmpleados]


#ESTRUCTURAS DE PAGOS
pago    = []  #Lista una solo pago
pagos   = []  #Lista de Listas, muchos pagos
encabezadoPagos = [Fore.GREEN + Style.BRIGHT + "ID", "Cédula", "Días", "Mes", "Año", "Salario básico", "Salario devengado", "Aux. transporte", "Desc. Salud", "Desc. Pension", "Salario neto" + Style.RESET_ALL]
#anchoColumnas = [50, 60, 30, 50, 80, 80, 80, 80, 60]

encabezadoPagos = [re.sub(r'\x1b\[[0-9;]*m', '', col) for col in encabezadoPagos]

pagos = libreria.cargar(pagos, nombreArchivoPagos)
empleados = libreria.cargar(empleados, nombreArchivoEmpleados)



#INICIO DEL PROGRAMA
def menu():
    global empleados
    global empleado
    global pagos
    while True:

        libreria.menuCrudPagos( "GESTION PAGO EMPLEADOS" )
        #opcion = input("OPCION: ")[0]
        opcion = libreria.LeerCaracter("OPCION: ")
        match opcion:
            case '1': 

                pagos = generarNominaMes ( empleados )
                libreria.guardar(pagos, nombreArchivoPagos)
                libreria.listar(encabezadoPagos, pagos)
                respuesta = libreria.LeerCaracter("Imprimir PDF (S / N): ").upper()
                if respuesta == 'S':
                        titulo = [["PAGOS A EMPLEADOS"]]
                        logo = "imagenes/logo pagos.png"
                        #logo_empleados = "imagenes/logo empleados.png"
                        libreria.generarPDF (encabezadoPagos, pagos, archivo_pdf, titulo, logo)
                        libreria.abrirPDF (archivo_pdf)
                        mensaje = "\U00002705 FIN DE LISTAR <ENTER> Continuar"
                        libreria.mensajeEsperaEnter( mensaje )   
            case '2':
            
                mensaje = " SIN INFORMACIÓN PARA LISTAR "
                if (pagos):
                    libreria.listar(encabezadoPagos, pagos)
                    respuesta = libreria.LeerCaracter("Imprimir PDF (S / N): ").upper()
                    if respuesta == 'S':
                        titulo = [["PAGOS A EMPLEADOS"]]
                        logo = "imagenes/logo pagos.png"
                        #logo_empleados = "imagenes/logo empleados.png"
                        libreria.generarPDF (encabezadoPagos, pagos, archivo_pdf, titulo, logo)
                        libreria.abrirPDF (archivo_pdf)
                    mensaje = "\U00002705 FIN DE LISTAR <ENTER> Continuar"
                libreria.mensajeEsperaEnter( mensaje )
            case '3':
                mensaje = " SIN INFORMACIÓN PARA CONSULTAR "
                if pagos:
                    codigoEmpleado = input("\n INGRESA EL CÓDIGO DEL EMPLEADO A CONSULTAR: ").strip().upper()
                    
                    # Filtrar pagos del empleado
                    pagos_empleado = [p for p in pagos if p[0].upper() == codigoEmpleado]

                    if pagos_empleado:
                        libreria.mostrar_varios(encabezadoPagos, pagos_empleado)  # Muestra todos en una sola tabla
                        mensaje = "\U00002705 FIN DE CONSULTAR <ENTER> Continuar"

                        respuesta = libreria.LeerCaracter("¿Imprimir PDF (S / N)? ").upper()
                        if respuesta == 'S':
                            titulo = [["PAGOS A EMPLEADOS"]]
                            logo = "imagenes/logo pagos.png"
                            archivo_pdf_empleado = f"{rutaDirectorio}pagos_{codigoEmpleado}.pdf"

                            libreria.generarPDF(encabezadoPagos, pagos_empleado, archivo_pdf_empleado, titulo, logo)
                            libreria.abrirPDF(archivo_pdf_empleado)
                    else:
                        mensaje = f"❌ El empleado con código {codigoEmpleado} no tiene pagos registrados."
                
                libreria.mensajeEsperaEnter(mensaje)
            case '4':          
                mensaje = " SIN INFORMACIÓN PARA ACTUALIZAR "
                if (pagos):            
                    codigoBuscar = input("CÓDIGO: ").strip().upper()
                    posicion = libreria.buscar(pagos, codigoBuscar)
                    mensaje = "\u26A0 NO EXISTE EL REGISTRO " + codigoBuscar
                    if (posicion >= 0):
                        pago = pagos[posicion]
                        pago = actualizar (encabezadoPagos, pago)    #retornar el registro actualizado
                        pagos[posicion] = pago
                        libreria.guardar(pagos, nombreArchivoPagos) 
                        mensaje = "\U00002705 FIN DE ACTUALIZAR <ENTER> Continuar"            
                libreria.mensajeEsperaEnter( mensaje )
            case '5':          
                mensaje = " SIN INFORMACIÓN PARA ELIMINAR "
                if (pagos):            
                    codigoBuscar = input("CÓDIGO: ").strip().upper()
                    posicion = libreria.buscar(pagos, codigoBuscar)
                    mensaje = "\u26A0 NO EXISTE EL REGISTRO " + codigoBuscar
                    if (posicion >= 0):
                        pago = pagos[posicion]
                        libreria.mostrar(encabezadoPagos, pago)
                        mensaje = "\U00002705 NO ELIMINADO - FIN DE ELIMINAR <ENTER> Continuar"                     
                        respuesta = libreria.LeerCaracter("Seguro de Eliminar (Sí - No): ")
                        if (respuesta.lower() == 's'):
                            pagos.remove(pagos[posicion])     #o también con    del pagos[posicion] 
                            libreria.guardar(pagos, nombreArchivoPagos)                   
                            mensaje = "\U00002705 REGISTRO ELIMINADO - FIN DE ELIMINAR <ENTER> Continuar"  
                libreria.mensajeEsperaSegundos( mensaje, 2 )
            case '6':
                libreria.mensajeEsperaSegundos( "REGRESANDO A MENÚ PRINCIPAL...", 1 )
                break
            case _:
                libreria.mensajeEsperaSegundos( "OPCION NO VALIDA, POR FAVOR, INTENTE NUEVAMENTE", 3 )
                libreria.limpiarPantalla()

if __name__ == "__main__":
    menu()