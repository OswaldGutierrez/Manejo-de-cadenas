class ManejoLenguajes():

    @staticmethod
    def agruparCadenas(cadena1, cadena2):
        cadena3 = input("Cadena 3: ")
        cadena4 = input("Cadena 4: ")
        lenguajeA = [cadena1, cadena3]
        lenguajeB = [cadena2, cadena4]
        return lenguajeA, lenguajeB

    @staticmethod
    def multiplicarLenguajes(lenguaje1, lenguaje2):
        try:
            if isinstance(lenguaje1, list) and isinstance(lenguaje2, list):
                if all(isinstance(i, str) for i in lenguaje1 + lenguaje2):
                    listaResult = []
                    for i in range(len(lenguaje1)):
                        for j in range(len(lenguaje2)):
                            result = lenguaje1[i] + lenguaje2[j]
                            listaResult.append(result)
                    return listaResult           
        except Exception as e:
            print(f"Ocurrió un error {e}")

    @staticmethod
    def multiplicarCuadrados(lenguaje):
        try:
            if isinstance(lenguaje, list):
                if all(isinstance(i, str) for i in lenguaje):
                    listaResult = []
                    for i in range(len(lenguaje)):
                        for j in range(len(lenguaje)):
                            result = lenguaje[i] + lenguaje[j]
                            listaResult.append(result)
                    return listaResult
        except Exception as e:
            print(f"Ocurrió un error {e}")

    @staticmethod
    def multiplicarCubo(lenguaje):
        if isinstance(lenguaje, list):
            if all(isinstance(i, str) for i in lenguaje):
                listAux = []
                listaResult = []
                for j in range(len(lenguaje)):
                    for k in range(len(lenguaje)):
                        result = lenguaje[j] + lenguaje[k]
                        listAux.append(result)
                for l in range(len(lenguaje)):
                    for m in range(len(listAux)):
                        result2 = lenguaje[l] + listAux[m]
                        listaResult.append(result2)
        return listaResult

       

if __name__ == "__main__":

    print("---------------------------Punto 1----------------------------------")
    c1 = "1"
    c2 = "2"
    lenguajeA, lenguajeB = ManejoLenguajes.agruparCadenas(c1, c2)
    print(lenguajeA, lenguajeB)

    print("---------------------------Punto 2----------------------------------")
    lengALengB = ManejoLenguajes.multiplicarLenguajes(lenguajeA, lenguajeB)
    print(lengALengB)

    print("---------------------------Punto 3----------------------------------")
    lengAlengBCuadrado = ManejoLenguajes.multiplicarCuadrados(lengALengB)
    print(lengAlengBCuadrado)

    print("---------------------------Punto 4----------------------------------")
    LenguajeACubo = ManejoLenguajes.multiplicarCubo(lenguajeA)
    lenguajePunto4 = ManejoLenguajes.multiplicarLenguajes(LenguajeACubo, lenguajeB)
    print(lenguajePunto4)