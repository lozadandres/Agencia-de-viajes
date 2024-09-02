from origenydestino import validarorigenydestino
from paquetes import paquetesListado, printpaquete
from precio import choose, listar_reservas, eliminar_reserva

def main():

    while True:
        print("\n1. Reservar paquetes")
        print("2. Gestión de Reservas")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            
            #consultar origen y destino
            origenDestino=validarorigenydestino()
            #Arreglo apra guardar el origen y destino ingresados por el cliente
            destino=origenDestino[1]
            #Buscar paquetes disponibles al usuario de acuerdo al destino ingresado
            paquetes=paquetesListado(destino)

            #Imprimir los paquetes correspondientes
            printpaquete(paquetes)

            #seleccionar y Calcular precio
            choose(paquetes)
      
        elif opcion == "2":
            search_option_vuel = input("Seleccione: 1. Listar reservas, 2. Modificar reserva, 3. Eliminar reserva: ")
            if search_option_vuel == "1":
                print("seccion de listar paquetes reservados: ")
                listar_reservas()
            elif search_option_vuel == "2":
                print("seccion de modificacion de reserva: ")
            elif search_option_vuel == "3":
                print("seccion de eliminacion de reserva: ")
                eliminar_reserva()
            
        elif opcion == "0":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
