

import importlib
import libreria
import os
import sys
from tabulate import tabulate
from colorama import Fore, Back, Style, init

import empleados as E
import reportes as R
import pagos as P

#-----------------------------------------------------------#
#Función con las opciones del CRUD para cualquier entidad   #
#-----------------------------------------------------------#
def menu(  ): 
    titulo = "***** MENU PRINCIPAL ****"
    libreria.limpiarPantalla()    #os.system('cls')
    print(tabulate([['' + Fore.GREEN + "SISTEMA CALCULO SALARIO COLOMBIA \n" + Style.RESET_ALL + '' + Fore.LIGHTYELLOW_EX + "MENU: " + titulo + '' + Style.RESET_ALL + ''],],
                     tablefmt='fancy_grid',
                     stralign='center'))
    print(tabulate([ 
                     ['*' * (len(titulo) + 6)],
                     ["\t" + Back.YELLOW + "[1]" + Style.RESET_ALL + "  GESTIONAR EMPLEADOS  "],
                     ["\t" + Back.YELLOW + "[2]" + Style.RESET_ALL + "  GESTIONAR PAGOS    "],
                     ["\t" + Back.YELLOW + "[3]" + Style.RESET_ALL + "  REPORTES "],
                     ["\t" + Back.YELLOW + "[4]" + Style.RESET_ALL + "  GESTIONAR PARAMETROS  "],
                     ["\t" + Back.YELLOW + "[5]" + Style.RESET_ALL + "  SALIR     "]
                     ],
                     tablefmt='fancy_grid',
                     stralign='left'))
    
#PROGRAMA PRINCIPAL PARA NAVEGAR ENTRE OTROS ARCHIVOS
def main():
    while True:
        menu()
        opcion = libreria.LeerCaracter("OPCIÓN: ").upper()
        match opcion:
            case '1':
                importlib.reload(E)
                E.menu()
            case '2':
                importlib.reload(P)
                P.menu()
            case '3':
                importlib.reload(P)
                R.menu()
            case '4':
                print("llamar a parámetros")
                input()
            case '5':
                libreria.mensajeEsperaSegundos("GRACIAS POR UTILIZAR NUESTRO PROGRAMA, HASTA PRONTO! 😎", 4)
                libreria.limpiarPantalla()
                sys.exit()

if __name__ == "__main__":
    main()