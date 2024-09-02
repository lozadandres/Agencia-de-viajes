#Funcion de Registro

print("Bienvenido a la agencia de viajes DreamVentures la mejor agencia de viajes en Colombia, a continuacion se mostraran las cidades donde estamos ubicados: ")

print(" 1. Bogota \n 2. Medellin \n 3. Cartagena \n 4. Barranquilla \n 5. Cali")

def validacionorigen ():
    while True:
        try:
            origen = int(input("Digite el numero de su lugar de partida: "))
            if origen >=1 and origen<=5:
                break
            else:
                print("Por favor, introduce un número válido.")
        except ValueError:
            print("Por favor, introduce un número válido.")
    return origen

def validadestino ():
    while True:
        try:
            destino=int(input("Digite el numero de lugar de llegada: "))
            if destino >=1 and destino<=5:
                break
            else:
                print("Por favor, introduce un número válido.")
        except ValueError:
            print("Por favor, introduce un número válido.")
    return destino

def validarorigenydestino():       
    while True:
        try:
            origen = int(validacionorigen())
            destino = int(validadestino())
            
            if origen != destino:
                lista=[origen,destino]
                break
            else:
                print("El destino y el origen no pueden ser iguales")  
        except:
            print("El destino y el origen no pueden ser iguales")
    return lista
