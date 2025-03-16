class ManejoCadenas:

    @staticmethod
    def partirCadena(cadena, listaCadena):
        tamañoCadena1 = len(cadena)
        for letra in range(tamañoCadena1):
            listaCadena.extend(cadena[letra])
        
    @staticmethod
    def estarContenida(listaCadena1, listaCadena2):
        listaAux = [] 
        tamañoCadena1 = len(listaCadena1)
        tamañoCadena2 = len(listaCadena2)
        for i in range(tamañoCadena1):
            for j in range(tamañoCadena2):
                if listaCadena1[i] == listaCadena2[j]:
                    listaAux.extend(listaCadena2[j])

        print(f"\tLa listaCadena1 es: {listaCadena1}\n\tLa listaCadena2 es: {listaCadena2}\n\tLa listaAux es: {listaAux}")

        if listaCadena1 == listaCadena2:
            return ("Las cadenas son iguales")
        elif listaCadena1 == listaAux:
            return("La cadena 1 está contenida en la cadena 2")
        else:
            return ("La cadena1 no está contenida en la cadena2")
        
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


