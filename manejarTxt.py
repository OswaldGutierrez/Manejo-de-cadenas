class ManejarTxt:

    def escribirTxt(cadena1, cadena2):     
        try:
            with open("1. Cadenas.txt", "w", encoding="UTF8") as archivo:
                archivo.write(f"{cadena1}\n{cadena2}")
        except Exception as e:
            print(f"Ocurrió un error al escribir en el archivo {e}")
    
    def leerTxt():
        try:
            with open("1. Cadenas.txt", "r", encoding="UTF8") as archivo:
                cadena1 = archivo.readline().strip()
                cadena2 = archivo.readline()
            return cadena1, cadena2
        except Exception as e:
            print(f"Ocurrió un error al leer el archivo: {e}")
