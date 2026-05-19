def mostrar_menu():
    print("1. Area de Triangulo")
    print("2.IMC")
    print("3.Cambio")
    print("4.Hora de llegada")
    print ("5.Salir")
    return int (input("Seleccione una opción"))

def opcion_1():#Sara
# Aqui van las funciones
def area_triangulo(l1, l2, l3):
    s = (l1 + l2 + l3) / 2
    area = (s * (s - l1) * (s - l2) * (s - l3)) ** 0.5
    return area


def ejecutar_opcion_1():
    l1 = float(input("Ingrese Lado 1: ")) 
    l2 = float(input("Ingrese Lado 2: "))
    l3 = float(input("Ingrese Lado 3: "))

    print("Resultado:", area_triangulo(l1, l2, l3))


ejecutar_opcion_1()
def opcion_2():#Pinzón

def opcion_3():#Gadiel

def opcion_4():#Samacá

def iniciar_programa():
    while true:
        opcion=mostrar_menu()
        if opcion==1:
            opcion_1
        if opcion==2:
            opcion_2
        if opcion==3:
            opcion_3
        if opcion==4:
            opcion_4
        if opcion==5:
            print("Salir")
            break
        if opcion<1 or opcion> 5:
            print("No válida")
iniciar_programa