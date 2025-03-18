from manejoCadenas import ManejoCadenas as mc



def abrirMenu():
    cadena1 = input("Cadena 1: ")
    cadena2 = input("Cadena 2: ")
    salirMenu = True

    while salirMenu:
        opcionMenu = int(input("""\nElija una de las siguientes opciones:
            1. Determinar si la primera cadena está contenida o es igual a la segunda cadena
            2. Imprimir el módulo de las cadenas ingresadas.
            3. Invertir ambas cadenas.
            4. Imprimir el resultado de la expresión: (((cadena1)^I)^2((cadena2)^3)^I)^I
            5. Imprimir los prefijos.
            6. Imprimir los sufijos.
            7. Trabajar con lenguajes.
            8. 
            ¿Qué opción va elegir?    """))

        match opcionMenu:
            case 1:
                listaCadena1 = mc.partirCadena(cadena1)
                listaCadena2 = mc.partirCadena(cadena2)
                print(mc.estarContenida(listaCadena1, listaCadena2))
            case 2:
                mc.moduloCadenas(cadena1)
                mc.moduloCadenas(cadena2)
            case 3:
                print(mc.invertirCadenas(cadena1))
                print(mc.invertirCadenas(cadena2))
            case 4:
                print(mc.imprimirResultadoExpresion(cadena1, cadena2))
            case 5:
                mc.imprimirPrefijos(cadena1)
                mc.imprimirPrefijos(cadena2)
            case 6:
                mc.imprimirSufijos(cadena1)
                mc.imprimirSufijos(cadena2)
            case _:
                print("FINALIZADO")
                salirMenu = False




if __name__ == "__main__":
    abrirMenu()
    

