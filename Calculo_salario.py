'''
Desarrollar un programa en el lenguaje de programación PYTHON que calcule el salario neto de un empleado 
en Colombia, teniendo en cuenta los descuentos obligatorios y beneficios establecidos por la ley.
'''

# Se importa la libereria predefinida para el taller practico
import Biblioteca

# Se inicia limpiando la pantalla
Biblioteca.limpiarPantalla()

# Encabezado del programa
Biblioteca.Cabecera("PROGRAMA PARA CALCULAR EL SALARIO NETO A PAGAR DE UN EMPLEADO")

# Se establecen constantes
SALARIO_MINIMO = 1423500
VALOR_AUXILIO_TRANSPORTE = 200000
PORCENTAJE_SALUD = 0.04
PORCENTAJE_PENSION = 0.04

# Se inicializan las variables
Nombre_empleado = " "
Dias_trabajados = 0
Salario_basico = 0
Salario_devengado = 0
Salario_neto = 0
Auxilio_transporte = 0
Descuento_salud = 0
Descuento_pension = 0

Continuar = True
while (Continuar):

    # Funcion para ingresar una cadena de texto
    Nombre_empleado = Biblioteca.Leer_texto("Ingrese los nombres y apellidos del empleado: ")

    # Funcion para ingresar y validar el salario basico
    Salario_basico = Biblioteca.Ingresar_validar_salario()

    # Funcion para ingresar los dias trabajados
    Dias_trabajados = Biblioteca.Leer_numero_entero("Ingrese los dias laborados por el empleado: ")

    # Funcion para calcular el salario devengado
    Salario_devengado = Biblioteca.Calcular_salario_devengado(Salario_basico, Dias_trabajados)

    # Funcion para aplicar el auxilio de transporte
    Auxilio_transporte = Biblioteca.Aplicar_auxilio_transporte(Salario_basico, SALARIO_MINIMO, VALOR_AUXILIO_TRANSPORTE, Dias_trabajados)

    # Funcion para calcular el descuento por salud
    Descuento_salud = Biblioteca.Calcular_descuento_salud(Salario_devengado, PORCENTAJE_SALUD)

    # Funcion para calcular el descuento por pension
    Descuento_pension = Biblioteca.Calcular_descuento_pension(Salario_devengado, PORCENTAJE_PENSION)

    # Funcion para calcular el salario neto del empleado
    Salario_neto = Biblioteca.Calcular_salario_neto(Salario_devengado, Auxilio_transporte, Descuento_salud, Descuento_pension)

    # Funcion para mostrar los resultados de la nomina
    Biblioteca.Mostrar_nomina_empleado(Nombre_empleado, Salario_devengado, Auxilio_transporte, Descuento_salud, Descuento_pension, Salario_neto)

    # Funcion para preguntar si desea continuar ingresando datos en el programa
    Continuar = Biblioteca.Desea_continuar("¿Desea ingresar otro empleado? Por favor responda con Si o No: ")

# Funcion para dar un mensaje y salir con una tecla
Biblioteca.Mensaje_de_espera_enter("Gracias por usar nuestro programa. Para salir digite la tecla ENTER")

# Se finaliza limpiando la pantalla
Biblioteca.limpiarPantalla()