import os
import pickle
import time
from colorama import Fore, Style

def guardar(lista, filename):
    try:
        # Obtener el directorio y verificar si existe
        directorio = os.path.dirname(filename)
        if not os.path.exists(directorio):
            print(f"🔧 Creando directorio: {directorio}")
            os.makedirs(directorio)  # Crear carpeta si no existe

        # Intentar abrir y escribir en el archivo
        print(f"📂 Intentando guardar en: {filename}")
        with open(filename, 'wb') as archivo:
            pickle.dump(lista, archivo)

        print(Fore.LIGHTYELLOW_EX + "\n\n✅ Archivo guardado correctamente." + Style.RESET_ALL)
    except Exception as e:
        print(f"❌ Error al guardar el archivo: {e}")
