from manejoCadenas import ManejoCadenas as mc

class ManejoLenguajes():

    @staticmethod
    def formarLenguajes(cadena1, cadena2):
        cadena3, cadena4 = mc.ingresarCadenas(2)
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
            print(f"Ocurrió un error al multiplicar al cuadrado: {e}")

    @staticmethod
    def multiplicarCubo(lenguaje):
        try:
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
        except Exception as e:
            print(f"Ocurrió un error al multriplicar al cubo: {e}")

    @staticmethod
    def calcularComplemento(conjunto, conjUniverso):
        try:
            if isinstance(conjunto, list) and isinstance(conjUniverso, list):
                if all(isinstance(i, str) for i in conjunto + conjUniverso):
                    conjuntoComplemento = []
                    for elemento in conjUniverso:
                        if elemento not in conjunto:
                            conjuntoComplemento.append(elemento)
            return conjuntoComplemento
        except Exception as e:
            print(f"Ocurrió un error al calcular el complemento: {e}")
              
    @staticmethod
    def calcularIntercepcion(conjunto1, conjuntoAInterceptar):
        try:
            if isinstance(conjunto1, list) and isinstance(conjuntoAInterceptar, list):
                if all(isinstance(i, str) for i in conjunto1 + conjuntoAInterceptar):
                    conjuntoIntercepcion = []
                    for elemento in conjuntoAInterceptar:
                        if elemento in conjunto1:
                            conjuntoIntercepcion.append(elemento)
            return conjuntoIntercepcion
        except Exception as e:
            print(f"Ocurrió un error al calcular la intercepción: {e}")
    
    @staticmethod
    def calcularUnion(conjunto1, conjunto2):
        try:
            if isinstance(conjunto1, list) and isinstance(conjunto2, list):
                if all(isinstance(i, str) for i in conjunto1 + conjunto2):
                    conjuntoUnion = set()
                    for elemento in conjunto1 + conjunto2:
                        conjuntoUnion.add(elemento)
            return list(conjuntoUnion)
        except Exception as e:
            print(f"Ocurrió un error al calcular la unión: {e}")
       

if __name__ == "__main__":

    print("---------------------------Punto 1----------------------------------")
    c1 = "1"
    c2 = "2"
    lenguajeA, lenguajeB = ManejoLenguajes.formarLenguajes(c1, c2)
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

    print("---------------------------Punto 5----------------------------------")
    lenguajeAComplemento = ManejoLenguajes.calcularComplemento(lenguajeA, lenguajeB)
    lenguajePunto5 = ManejoLenguajes.calcularIntercepcion(lenguajeAComplemento, lenguajeB)
    print(lenguajePunto5)

    print("---------------------------Punto 6----------------------------------")
    lenguajeBComplemento = ManejoLenguajes.calcularComplemento(lenguajeB, lenguajeA)
    print(f"Bc = {lenguajeBComplemento}")
    segundoParentesis = ManejoLenguajes.calcularIntercepcion(lenguajeBComplemento, lenguajeA)
    print(f"Bc n A = {segundoParentesis}")
    solucionParcial = ManejoLenguajes.calcularUnion(lenguajePunto5, segundoParentesis)
    print("(Ac n B) U (Bc n A) = ", solucionParcial)
    lenguajePunto6 = ManejoLenguajes.calcularIntercepcion(solucionParcial, lenguajeA)
    print(lenguajePunto6)