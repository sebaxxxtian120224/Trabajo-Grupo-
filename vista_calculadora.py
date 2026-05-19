from calculadora import * 
def mostrar_menu():
    print("1. Area de Triangulo")
    print("2.IMC")
    print("3.Cambio")
    print("4.Hora de llegada")
    print ("5.Salir")
    return int (input("Seleccione una opción"))

def opcion_1():#Sara

def opcion_2(): #Pinzón
    peso = float(input("Peso En Lb"))
    altura = float(input("Altura"))
    print("Resultado:", calcular_BMI(peso,altura))

def opcion_3():#Gadiel

def opcion_4():#Samacá

def iniciar_programa():
    while True:
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