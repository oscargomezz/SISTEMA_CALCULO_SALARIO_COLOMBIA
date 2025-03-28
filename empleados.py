import libreria
import os
import sys
from tabulate import tabulate
from colorama import Fore, Back, Style, init
init()

#-----------------------------------------------------------#
#Función con las opciones del CRUD para cualquier entidad   #
#-----------------------------------------------------------#
def menuActualizar(  ):
    titulo = "SELECCIONAR LA OPCIÓN A ACTUALIZAR"
    print(tabulate([['' + Fore.GREEN + "ALMACÉN MARKET \n" + Style.RESET_ALL + '' + Fore.LIGHTYELLOW_EX + "MENU: " + titulo + '' + Style.RESET_ALL + ''],],
                     tablefmt='fancy_grid',
                     stralign='center'))
    print(tabulate([ 
                     ['*' * (len(titulo) + 6)],
                     ["\t" + Back.YELLOW + "[1]" + Style.RESET_ALL + "  Nro. Identificación  "],
                     ["\t" + Back.YELLOW + "[2]" + Style.RESET_ALL + "  Nombre:    "],
                     ["\t" + Back.YELLOW + "[3]" + Style.RESET_ALL + "  Fecha Nacimiento "],
                     ["\t" + Back.YELLOW + "[4]" + Style.RESET_ALL + "  Dirección"],
                     ["\t" + Back.YELLOW + "[5]" + Style.RESET_ALL + "  Teléfonos  "],
                     ["\t" + Back.YELLOW + "[6]" + Style.RESET_ALL + "  Mail  "],
                     ["\t" + Back.YELLOW + "[7]" + Style.RESET_ALL + "  Estado  "],
                     ["\t" + Back.YELLOW + "[8]" + Style.RESET_ALL + "  Salario  "],
                     ["\t" + Back.YELLOW + "[9]" + Style.RESET_ALL + "  Regresar     "]
                     ],
                     tablefmt='fancy_grid',
                     stralign='left'))
    
def actualizar ( encabezado, vendedor ):        
    while True:                
        print("*** ACTUALIZANDO DATOS DEL vendedor ***")
        print("*" * 30)    
        libreria.mostrar(encabezado, vendedor)
        menuActualizar()
        respuesta = libreria.LeerCaracter("OPCION: ")
        match respuesta:
            case '1':
                vendedor[1] = libreria.leerCadena( "NRO. Identificación: ", 20 ).upper() #input("NRO. IDENTIFICACIÓN: ")
            case '2':
                vendedor[2] = libreria.leerCadena( "Nombre ", 100 ).title()        #input("NOMBRE: ")
            case '3':
                vendedor[3] = libreria.leerFecha("Fecha Nacimiento (YYYY-MM-DD): ")
            case '4':
                vendedor[4] = libreria.leerCadena("Dirección: ", 100) #input("DIRECCIÓN: ")
            case '5':
                vendedor[5] = libreria.leerCadena("Teléfonos: ", 50)
            case '6':
                vendedor[6] = libreria.leerMail("Mail: ")
            case '7':
                vendedor[7] = libreria.leerDiccionario(diccionarioEstados, "Estado: ")
            case '8':
                vendedor[8] = libreria.leerFlotante ("Salario:", 100000, 5000000)
            case '9':
                return vendedor
            case _:
                libreria.mensajeErrorEsperaSegundos("OPCIÓN NO VALIDA", 1)    
    

def insertar ( codigo ):
    libreria.limpiarPantalla()
    print("*** INSERTAR vendedor ***")
    print("*" * 30)
    print(f"CÓDIGO: {codigo}")
    identificacion  = libreria.leerCadena( "NRO. Identificación: ", 20 ).upper() #input("NRO. IDENTIFICACIÓN: ")
    nombres         = libreria.leerCadena( "Nombre: ", 100 ).title()        #input("NOMBRE: ")
    fechaNacimiento = libreria.leerFecha("Fecha Nacimiento (YYYY-MM-DD): ")
    direccion       = libreria.leerCadena("Dirección: ", 100) #input("DIRECCIÓN: ")
    telefonos       = libreria.leerCadena("Teléfonos: ", 50)
    mail            = libreria.leerMail("Mail: ")
    salario         = libreria.leerFlotante ("Salario:", 100000, 5000000)
    estado = 'A'
    #indices respetar 0         1            2           3              4          5        6     7         8
    vendedor     = [codigo, identificacion, nombres, fechaNacimiento, direccion, telefonos, mail, estado, salario]
    return vendedor

#VARIABLES GLOBALES Y CONSTANTES
print("Directorio actual:", os.getcwd())
rutaDirectorio = "datos/"
nombreArchivo   = os.path.join(rutaDirectorio, 'empleados.dat')
#nombreArchivo   = "empleados.dat"

diccionarioEstados = {
    'A': "Activa",
    'I': "Inactivo"
}

#ESTRUCTURAS DE DATOS A UTILIZAR 
vendedor    = []  #Lista una solo vendedor
empleados   = []  #Lista de Listas, muchos empleados
encabezado = [Fore.GREEN + Style.BRIGHT + "Código", "Identificación", "Nombres", "Nacimiento", "Dirección", "Telefonos", "Mail", "Estado", "Salario" + Style.RESET_ALL]

empleados = libreria.cargar(empleados, nombreArchivo)

#INICIO DEL PROGRAMA
def menu():
    while True:
        libreria.menuCrud( "GESTION empleados" )
        #opcion = input("OPCION: ")[0]
        opcion = libreria.LeerCaracter("OPCION: ")
        match opcion:
            case '1':            
                codigoBuscar = input("CÓDIGO: ").strip().upper()
                posicion = libreria.buscar(empleados, codigoBuscar)
                mensaje = "❌ YA EXISTE NO SE PERMITEN DUPLICADOS " + codigoBuscar
                if (posicion < 0):
                    vendedor = insertar( codigoBuscar )
                    empleados.append(vendedor)
                    libreria.guardar(empleados, nombreArchivo)
                    mensaje = "\U00002705 INSERTADO CORRECTAMENTE"
                libreria.mensajeEsperaSegundos( mensaje, 2 )
            case '2':            
                mensaje = " SIN INFORMACIÓN PARA LISTAR "
                if (empleados):
                    libreria.listar(encabezado, empleados)
                    mensaje = "\U00002705 FIN DE LISTAR <ENTER> Continuar"
                libreria.mensajeEsperaEnter( mensaje )
            case '3':           
                mensaje = " SIN INFORMACIÓN PARA CONSULTAR "
                if (empleados):
                    #sys.stdout.flush()            
                    codigoBuscar = input("\n INGRESE EL CÓDIGO A CONSULTAR: ").strip().upper()
                    posicion = libreria.buscar(empleados, codigoBuscar)
                    mensaje = "\u26A0 NO EXISTE EL REGISTRO " + codigoBuscar
                    if (posicion >= 0):
                        vendedor = empleados[posicion]
                        libreria.mostrar(encabezado, vendedor)
                        mensaje = "\U00002705 FIN DE CONSULTAR <ENTER> Continuar"            
                libreria.mensajeEsperaEnter( mensaje )
            case '4':          
                mensaje = " SIN INFORMACIÓN PARA ACTUALIZAR "
                if (empleados):            
                    codigoBuscar = input("CÓDIGO: ").strip().upper()
                    posicion = libreria.buscar(empleados, codigoBuscar)
                    mensaje = "\u26A0 NO EXISTE EL REGISTRO " + codigoBuscar
                    if (posicion >= 0):
                        vendedor = empleados[posicion]
                        vendedor = actualizar (encabezado, vendedor)    #retornar el registro actualizado
                        empleados[posicion] = vendedor
                        libreria.guardar(empleados, nombreArchivo) 
                        mensaje = "\U00002705 FIN DE ACTUALIZAR <ENTER> Continuar"            
                libreria.mensajeEsperaEnter( mensaje )
            case '5':          
                mensaje = " SIN INFORMACIÓN PARA ELIMINAR "
                if (empleados):            
                    codigoBuscar = input("CÓDIGO: ").strip().upper()
                    posicion = libreria.buscar(empleados, codigoBuscar)
                    mensaje = "\u26A0 NO EXISTE EL REGISTRO " + codigoBuscar
                    if (posicion >= 0):
                        vendedor = empleados[posicion]
                        libreria.mostrar(encabezado, vendedor)
                        mensaje = "\U00002705 NO ELIMINADO - FIN DE ELIMINAR <ENTER> Continuar"                     
                        respuesta = libreria.LeerCaracter("Seguro de Eliminar (Sí - No): ")
                        if (respuesta.lower() == 's'):
                            empleados.remove(empleados[posicion])     #o también con    del empleados[posicion] 
                            libreria.guardar(empleados, nombreArchivo)                   
                            mensaje = "\U00002705 REGISTRO ELIMINADO - FIN DE ELIMINAR <ENTER> Continuar"  
                libreria.mensajeEsperaSegundos( mensaje, 2 )
            case '6':
                libreria.mensajeEsperaSegundos( "GRACIAS POR UTILIZAR NUESTRO PROGRAMA, HASTA PRONTO! 😎", 1 )
                break
            case _:
                libreria.mensajeEsperaSegundos( "OPCION NO VALIDA, POR FAVOR, INTENTE NUEVAMENTE", 3 )
                libreria.limpiarPantalla()

if __name__ == "__main__":
    menu()