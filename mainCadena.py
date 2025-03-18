from manejoCadenas import ManejoCadenas as mc
from manejarTxt import ManejarTxt as mt


def abrirMenuCadenas():
    try:
        cadena1, cadena2 = mc.ingresarCadenas(1)

        mt.escribirTxt(cadena1, cadena2)
        
        salirMenu = True
        while salirMenu:
            opcionMenu = int(input("""\nElija una de las siguientes opciones:
                1. Determinar si la primera cadena está contenida o es igual a la segunda cadena
                2. Imprimir el módulo de las cadenas ingresadas.
                3. Invertir ambas cadenas.
                4. Imprimir el resultado de la expresión: (((cadena1)^I)^2((cadena2)^3)^I)^I
                5. Imprimir los prefijos.
                6. Imprimir los sufijos.
                7. Salir 
                ¿Qué opción va elegir?    """))
            match opcionMenu:
                case 1:
                    print(mc.estarContenida(cadena1, cadena2))
                case 2:
                    mc.moduloCadenas(cadena1)
                    mc.moduloCadenas(cadena2)
                case 3:
                    print(mc.invertirCadenas(cadena1))
                    print(mc.invertirCadenas(cadena2))
                case 4:
                    print(mc.imprimirResultadoExpresion(cadena1, cadena2))
                case 5:
                    print(f"Prefijos de la cadena {cadena1}")
                    mc.imprimirPrefijos(cadena1)
                    print(f"Prefijos de la cadena {cadena2}")
                    mc.imprimirPrefijos(cadena2)
                case 6:
                    print(f"Sufijos de la cadena {cadena1}")
                    mc.imprimirSufijos(cadena1)
                    print(f"Sufijos de la cadena {cadena2}")
                    mc.imprimirSufijos(cadena2)
                case _:
                    print("FINALIZADO")
                    salirMenu = False
        
    except Exception as e:
        print(f"Ocurrió un error: {e}")


if __name__ == "__main__":
    abrirMenuCadenas()
    

