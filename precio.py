reservas = []

def listar_reservas():
    if not reservas:
        print("No hay reservas en la lista")
        return
    else:
        for i, reserva in enumerate(reservas, start=1):
            print("-----------------------------------\n")
            print(f" \tReserva # {i}: ")
            print("-----------------------------------\n")
            print(f"Paquete: {', '.join(reserva["paquete"])}")
            print(f"Numeros de personas: {reserva["num_personas"]}")
            print(f"Precio total: {reserva["precio_total"]}")
            print(f"Detalles del pago: ")
            for clave, valor in reserva["detalle_pag"].items():
                print(f"- {clave} : {valor} \n")
            print(f"persona(s): ")
            for persona in reserva["personas"]:
                print(f"- Nombre: {persona["name"]}, Cedula: {persona["id_number"]}")
            print("-----------------------------------\n")
    

# Función para modificar una reserva
#def modificar_reserva(indice):

# Función para eliminar una reserva
def eliminar_reserva():
    if not reservas:
        print("No hay reservas para eliminar")
    else:
        print("Reservas disponible")
        listar_reservas()

        print("Selecciona la reserva a eliminar")

        indice = int(input("ingrese el numero de reserva que deseas eliminar: "))

        if 1 <= indice <= len(reservas):
            res_elimi = reservas.pop(indice -1)
            print(f"La reserva {res_elimi} ha sido eliminada con éxito.")
        else:
            print("indice no encontrado")



def generar_tiquete(paquete, numero_personas, precio_total, detalles_pago, people):
    # Crear una cadena de texto con la información del tiquete
    tiquete = "\n********** Tiquete de Reserva **********\n"
    tiquete += "Detalles del Paquete Seleccionado:\n"
    tiquete += "-----------------------------------\n"
    for detalle in paquete:
        tiquete += f"{detalle}\n"
    tiquete += f"\nNúmero de personas: {numero_personas}\n"
    tiquete += "Información de las personas:\n"
    tiquete += "-----------------------------------\n"
    
    # Añadir la información de cada persona
    for i, people in enumerate(people, start=1):
        tiquete += f"Persona {i}:\n"
        tiquete += f"  Nombre: {people['name']}\n"
        tiquete += f"  Cédula: {people['id_number']}\n"

    tiquete += f"Precio total: {precio_total}\n"
    tiquete += "\nDetalles de Pago:\n"
    tiquete += "-----------------------------------\n"
    for clave, valor in detalles_pago.items():
        tiquete += f"{clave}: {valor}\n"
    tiquete += "****************************************\n"
    
    return tiquete


def choose (paquetes):
     choose=int(input("Ingrese el numero correspondiente al paquete que desea: "))
     number=int(input("Digite la cantidad de personas que adquiriran el paquete: "))

     # Solicitar nombre y cédula de cada persona
     people = []
     for i in range(number):
         print(f"Información de la persona {i+1}:")
         name = input("Ingrese su nombre: ")
         id_number = input("Ingrese su cédula: ")
         people.append({"name": name, "id_number": id_number})
        
     paquete=paquetes[choose-1]
     if  choose == 1:
        valor= paquete[6]
        #Eliminar los puntos 
        valorc=valor.replace(".","")
        precio=int(valorc)*number
        #volver a agregar los puntos
        precioc="{:,}".format(precio).replace(",", ".")

        print("el precio a pagar es de: $", precioc)

        print("Seleccione la forma de pago: ")
        print("1. Tarjeta de crédito")
        print("2. Tarjeta de débito")
        print("3. Transferencia bancaria")
        print("4. Efectivo")

        forma_pago = int(input("Ingrese el número correspondiente a su forma de pago: "))
        formas_de_pago = ["Tarjeta de crédito", "Tarjeta de débito", "Transferencia bancaria", "Efectivo"]

        if 1 <= forma_pago <= 4:
            print(f"Usted ha seleccionado {formas_de_pago[forma_pago - 1]} como forma de pago.")
            
            # Variables para almacenar los detalles de pago
            detalles_pago = {}

            if forma_pago == 1:  # Tarjeta de crédito
                  while True:
                     numero_tarjeta = input("Ingrese el número de su tarjeta de crédito (16 dígitos): ")
                     if len(numero_tarjeta) == 16 and numero_tarjeta.isdigit():
                        break
                     else:
                        print("Número de tarjeta inválido. Debe tener 16 dígitos.")
                  
                  nombre_titular = input("Ingrese el nombre del titular de la tarjeta: ")
                  
                  while True:
                     fecha_expiracion = input("Ingrese la fecha de expiración (MM/AA): ")
                     if len(fecha_expiracion) == 5 and fecha_expiracion[:2].isdigit() and fecha_expiracion[3:].isdigit() and fecha_expiracion[2] == '/':
                        break
                     else:
                        print("Fecha de expiración inválida. Debe estar en el formato MM/AA.")
                  
                  while True:
                     cvv = input("Ingrese el código CVV (3 o 4 dígitos): ")
                     if len(cvv) in [3, 4] and cvv.isdigit():
                        break
                     else:
                        print("Código CVV inválido. Debe tener 3 o 4 dígitos.")

                  # Guardar detalles de pago
                  detalles_pago = {
                     "Forma de pago": "Tarjeta de crédito",
                     "Número de tarjeta": numero_tarjeta,
                     "Nombre del titular": nombre_titular,
                     "Fecha de expiración": fecha_expiracion,
                     "CVV": cvv
                  }

            elif forma_pago == 2:  # Tarjeta de débito
                  while True:
                     numero_tarjeta = input("Ingrese el número de su tarjeta de débito (16 dígitos): ")
                     if len(numero_tarjeta) == 16 and numero_tarjeta.isdigit():
                        break
                     else:
                        print("Número de tarjeta inválido. Debe tener 16 dígitos.")

                  nombre_titular = input("Ingrese el nombre del titular de la tarjeta: ")

                  while True:
                     fecha_expiracion = input("Ingrese la fecha de expiración (MM/AA): ")
                     if len(fecha_expiracion) == 5 and fecha_expiracion[:2].isdigit() and fecha_expiracion[3:].isdigit() and fecha_expiracion[2] == '/':
                        break
                     else:
                        print("Fecha de expiración inválida. Debe estar en el formato MM/AA.")

                  while True:
                     cvv = input("Ingrese el código CVV (3 o 4 dígitos): ")
                     if len(cvv) in [3, 4] and cvv.isdigit():
                        break
                     else:
                        print("Código CVV inválido. Debe tener 3 o 4 dígitos.")

                  # Guardar detalles de pago
                  detalles_pago = {
                     "Forma de pago": "Tarjeta de débito",
                     "Número de tarjeta": numero_tarjeta,
                     "Nombre del titular": nombre_titular,
                     "Fecha de expiración": fecha_expiracion,
                     "CVV": cvv
                  }

            elif forma_pago == 3:  # Transferencia bancaria
                  while True:
                     numero_cuenta = input("Ingrese el número de su cuenta bancaria: ")
                     if len(numero_cuenta) >= 10 and numero_cuenta.isdigit():
                        break
                     else:
                        print("Número de cuenta inválido. Debe tener al menos 10 dígitos.")

                  codigo_banco = input("Ingrese el código del banco (SWIFT o ABA): ")

                  nombre_beneficiario = input("Ingrese el nombre del beneficiario: ")

                  numero_referencia = input("Ingrese el número de referencia de la transferencia: ")

                  # Guardar detalles de pago
                  detalles_pago = {
                     "Forma de pago": "Transferencia bancaria",
                     "Número de cuenta": numero_cuenta,
                     "Código del banco": codigo_banco,
                     "Nombre del beneficiario": nombre_beneficiario,
                     "Número de referencia": numero_referencia
                  }

            elif forma_pago == 4:  # Efectivo
                  lugar_pago = input("Ingrese el lugar donde realizará el pago en efectivo: ")

                  while True:
                     fecha_limite = input("Ingrese la fecha límite para realizar el pago (DD/MM/AAAA): ")
                     if len(fecha_limite) == 10 and fecha_limite[:2].isdigit() and fecha_limite[3:5].isdigit() and fecha_limite[6:].isdigit() and fecha_limite[2] == '/' and fecha_limite[5] == '/':
                        break
                     else:
                        print("Fecha inválida. Debe estar en el formato DD/MM/AAAA.")

                  codigo_referencia = input("Ingrese el código de referencia de pago: ")

                  # Guardar detalles de pago
                  detalles_pago = {
                     "Forma de pago": "Efectivo",
                     "Lugar de pago": lugar_pago,
                     "Fecha límite de pago": fecha_limite,
                     "Código de referencia": codigo_referencia
                  }

            # Imprimir los detalles de pago
            print("\nDetalles de la forma de pago:")
            for clave, valor in detalles_pago.items():
                  print(f"{clave}: {valor}")
        else:
           print("Forma de pago no válida.")

     # Generar el tiquete con todos los detalles
     tiquete = generar_tiquete(paquete, number, precioc, detalles_pago, people)
    
     # Imprimir el tiquete
     print(tiquete)

     #agregar la reserva a la lista  de reservas
     reserva = {
         "paquete" : paquete,
         "num_personas" : number,
         "precio_total" : precioc,
         "detalle_pag" : detalles_pago,
         "personas" : people
     } 
     reservas.append(reserva)

     return precioc      

