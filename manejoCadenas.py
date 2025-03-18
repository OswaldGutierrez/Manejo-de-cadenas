class ManejoCadenas:
      
    @staticmethod
    def ingresarCadenas(opc):
        try:
            salir = True
            while salir:
                if opc == 1:
                    cadena1 = input("Cadena 1: ").strip()
                    cadena2 = input("Cadena 2: ").strip()
                else:
                    cadena1 = input("Cadena 3: ").strip()
                    cadena2 = input("Cadena 4: ").strip()
                if cadena1 and cadena2:
                    salir = False
                    return cadena1, cadena2
                else:
                    print("Ingrese algún valor")
        except Exception as e:
            print(f"Ocurrio un error al ingresar las cadenas: {e}")

    @staticmethod
    def estarContenida(cadena1, cadena2):
        try:
            if cadena1 == cadena2:
                return ("Las cadenas son iguales")
            else:
                cantVeces = cadena2.count(cadena1)
                if cantVeces == 0:
                    return (f"La cadena: {cadena1} no está contenido en la cadena: {cadena2}")
                else:
                    return (f"La cadena: {cadena1} si está contenida en la cadena: {cadena2}")

        except Exception as e:
            print(f"Ocurrió un error {e}")
         
    @staticmethod   
    def moduloCadenas(cadena):
        tamañoCadena = len(cadena)
        print(f"El tamaño de la cadena {cadena} es: {tamañoCadena}") 

    @staticmethod
    def invertirCadenasEnLista(cadena, listaCadena):
        tamañoCadena = len(cadena) - 1
        for i in range(tamañoCadena, -1, -1):
            listaCadena.extend(cadena[i])

    @staticmethod
    def invertirCadenas(cadena):
        cadenaAux = ""
        tamañoCadena = len(cadena) - 1
        for i in range(tamañoCadena, -1, -1):
            cadenaAux = cadenaAux + cadena[i]
        return (cadenaAux)

    @staticmethod
    def imprimirResultadoExpresion(cadena1, cadena2):
        cadena1Inv = ManejoCadenas.invertirCadenas(cadena1)
        op1 = cadena1Inv * 2
        op2aux = cadena2 * 3
        op2aux2 = ManejoCadenas.invertirCadenas(op2aux)
        resultParcial = op1 + op2aux2
        result = ManejoCadenas.invertirCadenas(resultParcial)
        return (result)

    @staticmethod
    def imprimirSufijos(cadena):
        tamañoCadena = len(cadena)
        cadenaSufijos = ""
        for i in range(tamañoCadena):
            cadenaSufijos = cadenaSufijos + cadena[i]
            print(cadenaSufijos)

    @staticmethod
    def imprimirPrefijos(cadena):
        tamañoCadena = len(cadena)
        cadenaInvertida = ManejoCadenas.invertirCadenas(cadena)
        cadenaPrefijos = ""
        for i in range(tamañoCadena):
            cadenaPrefijos = cadenaInvertida[i] + cadenaPrefijos
            print(cadenaPrefijos)


