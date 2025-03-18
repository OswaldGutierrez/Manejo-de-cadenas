import mainCadena as mc
import mainLenguaje as ml

def ejecutarPrograma():
    salirMenu = True
    while salirMenu:
        opcionMenu = int(input("""Elija una opción
                        1. Trabajar con cadenas.
                        2. Trabajar con lenguajes.
                        3. Salir    """))
        match opcionMenu:
            case 1:
                print("Por favor, ingrese las cadenas.")
                mc.abrirMenuCadenas()
            case 2: 
                ml.abrirMenuLenguajes()
            case 3:
                print("Ejecución finalizada")
                salirMenu = False
            case _:
                print("Ingrese una opción válida")


if __name__ == "__main__":
    ejecutarPrograma()