
def paquetesListado(ciudadId):

    bogota=[["1. Vuelos ida y regreso +", "Hotel Decameron +", "5 dias y 4 noches +", "Incluye: Desayuno, almuerzo y cena +", "Precio por persona:", "$", "900.000 "],["2. Vuelos ida y regreso +", "Hotel hilton +", "3 dias y 2 noches +", "incluye: Desayuno y almuerzo +", "Precio por persona:","$","1.200.000"], ["3. Vuelos ida y regreso +", "Hotel Dann Carton +", "4 dias y 3 noches +", "Incluye: Desayuno y cena +", "Precio por persona:","$", "850.000"]]
    medellin=[["1. Vuelos ida y regreso +", "Hotel Decameron +", "5 dias y 4 noches +", "Incluye: Desayuno, almuerzo y cena +", "Precio por persona:","$", "1.000.000 "],["2. Vuelos ida y regreso +", "Hotel hilton +", "3 dias y 2 noches +", "incluye: Desayuno y almuerzo +", "Precio por persona:","$","1.000.000"], ["3. Vuelos ida y regreso +","Hotel Dann Carton +", "4 dias y 3 noches +", "Incluye: Desayuno y cena +", "Precio por persona:","$","750.000"]]
    cartagena=[["1. Vuelos ida y regreso +","Hotel Dubai +", "4 dias y 3 noches +", "Incluye: Desayuno, almuerzo y cena +", "Precio por persona:","$","700.000"],["2. Vuelos ida y regreso +","Hotel hilton +", "3 dias y 2 noches +", "incluye: Desayuno y almuerzo +", "Precio por persona:","$","950.000"], ["3. Vuelos ida y regreso +","Hotel Decameron +", "5 dias y 4 noches +", "Incluye: Desayuno y cena +", "Precio por persona:","$","1.000.000"]]
    barranquilla=[["1. Vuelos ida y regreso +","Hotel Decameron +", "3 dias y 2 noches +", "Incluye: Desayuno, almuerzo y cena +", "Precio por persona:","$","900.000"],["2. Vuelos ida y regreso +","Hotel hilton +", "3 dias y 2 noches +", "incluye: Desayuno y almuerzo +", "Precio por persona:","$","1.200.000"], ["3. Vuelos ida y regreso +","Hotel Dann Carton +", "4 dias y 3 noches +", "Incluye: Desayuno y cena +", "Precio por persona:","$","850.000"]]
    cali=[["1. Vuelos ida y regreso +","Hotel intercontinental +", "5 dias y 4 noches +", "Incluye: Desayuno, almuerzo y cena +", "Precio por persona:","$","1.500.000"],["2. Vuelos ida y regreso +","Hotel hilton +", "3 dias y 2 noches +", "incluye: Desayuno y almuerzo +", "Precio por persona:","$","1.200.000"], ["3. Vuelos ida y regreso +","Hotel Dann Carton +", "4 dias y 3 noches +", "Incluye: Desayuno y cena +", "Precio por persona:","$","900.000"]]

    paquetes = [bogota,medellin,cartagena,barranquilla,cali]    

    paquetes1=paquetes[ciudadId-1]
    #print(response)

    return paquetes1

def printpaquete(paquetes1):
    print("Los paquetes disponibles son: ")
    for lista in paquetes1:
            for elemento in lista:
                print(elemento, end=" ")
            print()  # Salto de línea después de cada lista