import os
from colorama import Fore, Back, Style, init

# Funcion para limpiar la pantalla
def limpiarPantalla ():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Funcion para hacer cabeceras
def Cabecera(Titulo):
    print(Fore.YELLOW + f"\n {Titulo} \n")
    print(Style.RESET_ALL)

# Funcion para ingresar una cadena de texto
def Leer_texto(Etiqueta):
    while True:
        try:
            return str(input(Etiqueta))
        except ValueError:
            print(" ")
            print(str(Fore.RED + Style.BRIGHT + "ERROR. Ingrese un nombre valido. Por favor intentelo de nuevo" + Style.RESET_ALL))

# Funcion para ingresar y validar el salario basico
def Ingresar_validar_salario():
    while True:
        Salario = Leer_numero_entero("Ingrese el salario basico mensual del empleado: ")
        if 0 < Salario <= 8000000:
            return Salario
        print(Fore.RED + Style.BRIGHT + "ERROR. El salario debe estar entre $0 y $8.000.000." + Style.RESET_ALL)

# Funcion para ingresar un numero entero
def Leer_numero_entero(Etiqueta):
    while True:
        try:
            valor = input(Etiqueta).strip()
            if not valor.isdigit():
                raise ValueError
            return int(valor)
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "ERROR. Ingrese solo números enteros sin puntos ni comas." + Style.RESET_ALL)

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

# Funcion para mostrar los resultados de la nomina
def Mostrar_nomina_empleado(Nombre_empleado, Salario_devengado, Auxilio_transporte, Descuento_salud, Descuento_pension, Salario_neto):
    print(" ")
    print(Fore.YELLOW + Style.BRIGHT + "NOMINA" + Style.RESET_ALL)
    print(" ")
    print("NOMBRE EMPLEADO: " + Fore.GREEN + Style.BRIGHT + f"{Nombre_empleado}" + Style.RESET_ALL)
    print("SALARIO DEVENGADO: " + Fore.GREEN + Style.BRIGHT + f"$ {Salario_devengado:.0f}" + Style.RESET_ALL)
    print("AUXILIO DE TRANSPORTE: " + Fore.GREEN + Style.BRIGHT + f"$ {Auxilio_transporte:.0f}" + Style.RESET_ALL)
    print("DESCUENTO SALUD: " + Fore.GREEN + Style.BRIGHT + f"$ {Descuento_salud:.0f}" + Style.RESET_ALL)
    print("DESCUENTO PENSION: " + Fore.GREEN + Style.BRIGHT + f"$ {Descuento_pension:.0f}" + Style.RESET_ALL)
    print("SALARIO NETO: " + Fore.GREEN + Style.BRIGHT + f"$ {Salario_neto:.0f}" + Style.RESET_ALL)
    print(" ")
    print(Fore.YELLOW + Style.BRIGHT + f"EL TOTAL A PAGAR AL EMPLEADO ES $ {Salario_neto:.0f}" + Style.RESET_ALL)
    print(" ")

# Funcion para preguntar si desea continuar ingresando datos en el programa
def Desea_continuar(Etiqueta): 
    while True:
        Respuesta = input(Fore.YELLOW + Style.BRIGHT + f"{Etiqueta}" + Style.RESET_ALL).strip().lower()
        if Respuesta == "si":
            print(" ")
            return True
        elif Respuesta == "no":
            print(" ")
            return False
        else:
            print(" ")
            print(Fore.RED + Style.BRIGHT + "ERROR. Por favor, responda con 'Si' o 'No'" + Style.RESET_ALL)

# Funcion para dar un mensaje y salir con una tecla
def Mensaje_de_espera_enter(Mensaje):
    print("\n" + Fore.YELLOW + Style.BRIGHT + Mensaje + Style.RESET_ALL, end="")
    input()