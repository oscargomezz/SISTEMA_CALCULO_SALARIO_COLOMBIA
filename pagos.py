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
                     ["\t" + Back.YELLOW + "[4]" + Style.RESET_ALL + "  Regresar     "]
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
                return pago
            case _:
                libreria.mensajeErrorEsperaSegundos("OPCIÓN NO VALIDA", 1)    

    

def insertar ( codigo ):
    pago    = [codigo, empleado[1], 0, 0, empleado[8], 0, 0, 0, 0, 0]
    libreria.limpiarPantalla()
    print("*** INSERTAR PAGO ***")
    print("*" * 30)
    print(f"CÓDIGO: {codigo}")
    #print(f"Identificación: {empleado}")
    libreria.mostrar(encabezadoEmpleados, empleado)
    libreria.mostrar(encabezadoPagos, pago)
    #identificacion  = libreria.leerCadena( "NRO. Identificación: ", 20 ).upper() #input("NRO. IDENTIFICACIÓN: ")
    diaslaborados   = libreria.leerEntero("Días laborados: ", 1,31)
    mes = libreria.leerMes("Escriba el mes a pagar: ")
    #mes   = libreria.leerEntero("Número del mes laborado: ", 1,12)
    pago    = [codigo, empleado[1], diaslaborados, mes, empleado[8], 0, 0, 0, 0, 0]
    #libreria.mostrar(encabezadoPagos, pago)
    #salario         = libreria.leerFlotante( "Salario básico: ", 100000, 12000000)       #input("Salario básico: ")
    #pago    = [codigo, empleado[1], diaslaborados, salario, 0, 0, 0, 0, 0]
    #libreria.mostrar(encabezadoPagos, pago)
    # Funcion para calcular el salario devengado
    Salario_devengado = libreria.Calcular_salario_devengado(empleado[8], diaslaborados)

    # Funcion para aplicar el auxilio de transporte
    Auxilio_transporte = libreria.Aplicar_auxilio_transporte(empleado[8], SALARIO_MINIMO, VALOR_AUXILIO_TRANSPORTE, diaslaborados)

    # Funcion para calcular el descuento por salud
    Descuento_salud = libreria.Calcular_descuento_salud(Salario_devengado, PORCENTAJE_SALUD)

    # Funcion para calcular el descuento por pension
    Descuento_pension = libreria.Calcular_descuento_pension(Salario_devengado, PORCENTAJE_PENSION)

    # Funcion para calcular el salario neto del empleado
    Salario_neto = libreria.Calcular_salario_neto(Salario_devengado, Auxilio_transporte, Descuento_salud, Descuento_pension)

      #indices respetar   0           1         2         3          4                   5                   6               7                   8          9
    pago     =      [codigo, empleado[1], diaslaborados, mes, empleado[8], Salario_devengado, Auxilio_transporte, Descuento_salud, Descuento_pension, Salario_neto]
    libreria.mostrar(encabezadoPagos, pago)
    mensaje = "\U00002705 FIN DE LISTAR <ENTER> Continuar"
    libreria.mensajeEsperaEnter( mensaje )
    
    return pago





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
encabezadoPagos = [Fore.GREEN + Style.BRIGHT + "ID", "Cédula", "Días", "Mes", "Salario básico", "Salario devengado", "Auxilio transporte", "Descuento salud", "Descuento pension", "Salario neto" + Style.RESET_ALL]
#anchoColumnas = [50, 60, 30, 50, 80, 80, 80, 80, 60]

encabezadoPagos = [re.sub(r'\x1b\[[0-9;]*m', '', col) for col in encabezadoPagos]

pagos = libreria.cargar(pagos, nombreArchivoPagos)
empleados = libreria.cargar(empleados, nombreArchivoEmpleados)

#INICIO DEL PROGRAMA
def menu():
    while True:
        libreria.menuCrud( "GESTION PAGO EMPLEADOS" )
        #opcion = input("OPCION: ")[0]
        opcion = libreria.LeerCaracter("OPCION: ")
        match opcion:
            case '1': 
                global empleados
                global empleado                
                codigoEmpleado, posicionEmpleado = libreria.leerCodigoValidado(empleados, "Código Empleado: ")
                #posicionEmpleado = libreria.buscar(clientes, codigoCliente)
                mensaje = "✅ EMPLEADO ENCONTRADO, CARGANDO INFORMACIÓN..."
                libreria.mensajeEsperaSegundos( mensaje, 2 )
                if posicionEmpleado >= 0:
                    empleado = empleados[posicionEmpleado]   # Obtiene solo el empleado encontrado
                    #libreria.listar(encabezadoEmpleados, [empleado])
                    #libreria.mostrarEmpleado(encabezadoEmpleados, empleado)

                   # print(f"{empleado[1]} \t {empleado[2]}")
                   
                while True:
                    os.system("cls" if os.name == "nt" else "clear")  # Limpia pantalla 
                    libreria.mostrar(encabezadoEmpleados, empleado)
                    codigoBuscar = input("Ingresa el Código de pago, ejemplo(PAGO001): ").strip().upper()
                    posicion = libreria.buscar(pagos, codigoBuscar)
                    if posicion == -1:  # Si NO existe en la lista, lo aceptamos
                        if (posicion < 0):
                            pago = insertar( codigoBuscar )
                            pagos.append(pago)
                            libreria.guardar(pagos, nombreArchivoPagos)
                            mensaje = "\U00002705 INSERTADO CORRECTAMENTE"
                            libreria.mensajeEsperaSegundos( mensaje, 2 )
                            break
                    else:
                        print(f"❌ YA EXISTE NO SE PERMITEN DUPLICADOS ({codigoBuscar}). Intenta de nuevo.")    
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
                if (pagos):
                    #sys.stdout.flush()            
                    codigoBuscar = input("\n INGRESE EL CÓDIGO A CONSULTAR: ").strip().upper()
                    posicion = libreria.buscar(pagos, codigoBuscar)
                    mensaje = "\u26A0 NO EXISTE EL REGISTRO " + codigoBuscar
                    if (posicion >= 0):
                        pago = pagos[posicion]
                        libreria.mostrar(encabezadoPagos, pago)
                        mensaje = "\U00002705 FIN DE CONSULTAR <ENTER> Continuar"            
                libreria.mensajeEsperaEnter( mensaje )
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