from manejoLenguajes import ManejoLenguajes as ml
from manejarTxt import ManejarTxt as mt

def abrirMenuLenguajes():
    try:
        salirMenu = True

        cadena1, cadena2 = mt.leerTxt()

        while salirMenu:
            opcionMenuLenguaje = int(input("""¿Qué operación desea realizar?
                1. Formar lenguajes A y B
                2. Calcular A.B
                3. Calcular (A.B)^2
                4. Calcular A^3.B
                5. Calcular Ac n B
                6. Calcular ((Ac n B) U (Bc n A)) n A
                7. Salir    """))
            match opcionMenuLenguaje:
                case 1:
                    lenguajeA, lenguajeB = ml.formarLenguajes(cadena1, cadena2)
                    print(f"Lenguaje A: {lenguajeA}\nLenguaje B: {lenguajeB}")
                case 2:
                    lenguajeALenguajeB = ml.multiplicarLenguajes(lenguajeA, lenguajeB)
                    print(f"A.B = {lenguajeALenguajeB}")
                case 3:
                    lenguajeALenguajeBCuadrado = ml.multiplicarCuadrados(lenguajeALenguajeB)
                    print(f"(A.B)^2 = {lenguajeALenguajeBCuadrado}")
                case 4:
                    lenguajeACubo = ml.multiplicarCubo(lenguajeA)
                    lenguajePunto4 = ml.multiplicarLenguajes(lenguajeACubo, lenguajeB)
                    print(f"A^3.B = {lenguajePunto4}")
                case 5:
                    LenguajeAComplemento = ml.calcularComplemento(lenguajeA, lenguajeB)
                    lenguajePunto5 = ml.calcularIntercepcion(LenguajeAComplemento, lenguajeB)
                    print(f"Ac n B = {lenguajePunto5}")
                case 6:
                    lenguajeBComplemento = ml.calcularComplemento(lenguajeB, lenguajeA)
                    segundoParentesis = ml.calcularIntercepcion(lenguajeBComplemento, lenguajeA)
                    conjuntoUnion = ml.calcularUnion(lenguajePunto5, segundoParentesis)
                    lenguajePunto6 = ml.calcularIntercepcion(conjuntoUnion, lenguajeA)
                    print(f"((Ac n B) U (Bc n A)) n A = {lenguajePunto6}")
                case 7:
                    print("Hasta luego!")
                    salirMenu = False
                case _:
                    print("Ingrese una opción válida")

    except Exception as e:
        print(f"Ocurrió un error {e}")


if __name__ == "__main__":
    abrirMenuLenguajes()