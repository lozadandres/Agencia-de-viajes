# Agencia-de-viajes

Proyecto_APP_Agencia_de_Viajes
Instructivo de la Aplicación de Agencia de Viajes Descripción General Esta aplicación permite a los usuarios de una agencia de viajes reservar paquetes turísticos, gestionar sus reservas, y obtener detalles de pago personalizados. A través de un menú interactivo, los usuarios pueden seleccionar diferentes opciones de viaje y gestionar sus reservas. La aplicación está compuesta por varios módulos (main.py, origenydestino.py, paquetes.py, precio.py), cada uno con funciones específicas para cumplir con los requerimientos del negocio.

main.py Este es el archivo principal de la aplicación. Contiene el flujo principal del programa, donde se presenta un menú al usuario para reservar paquetes de viajes o gestionar reservas existentes.

Variables y Funciones en main.py main():

Función principal que inicia el programa. Muestra un menú de opciones al usuario y procesa la entrada seleccionada. opcion:

Variable que captura la opción seleccionada por el usuario del menú principal. Usada en la estructura de control if-elif para ejecutar diferentes secciones del programa. Menú de Opciones:

"1": Reservar paquetes: Permite al usuario seleccionar un destino y reservar un paquete de viaje. "2": Gestión de Reservas: Ofrece opciones para listar, modificar, o eliminar reservas. "0": Salir: Termina el programa. validarorigenydestino():

Función importada de origenydestino.py. Solicita al usuario seleccionar un origen y un destino para su viaje. Verifica que el destino sea diferente al origen seleccionado. paquetesListado(destino):

Función importada de paquetes.py. Toma el destino seleccionado por el usuario y devuelve una lista de paquetes disponibles para ese destino. printpaquete(paquetes):

Función importada de paquetes.py. Imprime en pantalla los detalles de los paquetes disponibles para el destino seleccionado. choose(paquetes):

Función importada de precio.py. Permite al usuario elegir un paquete, calcular el precio total, solicitar los detalles de los pasajeros, y realizar el pago. listar_reservas():

Función importada de precio.py. Muestra todas las reservas existentes. eliminar_reserva():

Función importada de precio.py. Permite al usuario eliminar una reserva seleccionada de la lista de reservas. origenydestino.py Este módulo se encarga de gestionar la selección de origen y destino para el viaje. Incluye funciones para validar la entrada del usuario, asegurando que los datos ingresados sean correctos.

Variables y Funciones en origenydestino.py validacionorigen():

Función para solicitar al usuario el número de la ciudad de origen. Valida que el número ingresado sea válido (entre 1 y 5) y maneja errores de entrada. validadestino():

Similar a validacionorigen(), pero solicita al usuario el número de la ciudad de destino. También valida la entrada. validarorigenydestino():

Combina las funciones anteriores (validacionorigen y validadestino) para asegurar que el origen y el destino seleccionados sean diferentes. Retorna una lista con el origen y destino seleccionados. paquetes.py Este módulo contiene las funciones relacionadas con los paquetes turísticos. Proporciona las listas de paquetes disponibles y funciones para mostrar esta información al usuario.

Variables y Funciones en paquetes.py paquetesListado(ciudadId):

Recibe un número de ciudad (ciudadId) y devuelve una lista de paquetes disponibles para esa ciudad. Cada ciudad tiene una lista de paquetes predefinidos: bogota: Lista de paquetes disponibles en Bogotá. medellin: Lista de paquetes disponibles en Medellín. cartagena: Lista de paquetes disponibles en Cartagena. barranquilla: Lista de paquetes disponibles en Barranquilla. cali: Lista de paquetes disponibles en Cali. printpaquete(paquetes1):

Imprime en pantalla cada paquete de la lista recibida (paquetes1). Utiliza un bucle for para recorrer y mostrar todos los elementos de cada paquete. precio.py Este módulo maneja todo lo relacionado con las reservas, los precios, y los detalles del pago. Contiene funciones para listar, modificar, y eliminar reservas, así como para gestionar los detalles de pago.

Variables y Funciones en precio.py reservas:

Lista global que almacena todas las reservas realizadas por los usuarios. listar_reservas():

Verifica si hay reservas en la lista. Si hay reservas, las muestra con todos sus detalles; de lo contrario, indica que no hay reservas disponibles. eliminar_reserva():

Permite al usuario eliminar una reserva de la lista. Solicita al usuario el número de reserva a eliminar y lo valida. generar_tiquete(paquete, numero_personas, precio_total, detalles_pago, people):

Genera un tiquete de reserva con toda la información de la reserva seleccionada. Incluye detalles del paquete, número de personas, precio total, detalles de pago, y la información de cada pasajero. choose(paquetes):

Gestiona la selección de un paquete por parte del usuario. Solicita el número de personas y recopila la información de cada pasajero. Calcula el precio total del paquete en función de la cantidad de personas. Maneja la selección de la forma de pago y recopila los detalles necesarios. Genera el tiquete y lo imprime. Agrega la reserva a la lista global reservas. Detalles de pago:

Se gestionan diferentes formas de pago: tarjeta de crédito, tarjeta de débito, transferencia bancaria, y efectivo. Para cada forma de pago, se recopilan diferentes detalles (por ejemplo, número de tarjeta, nombre del titular, código CVV, etc.) y se almacenan en un diccionario detalles_pago. Estructura del Programa El programa se estructura en base a funciones, donde cada una cumple un propósito específico:

Reserva de Paquetes:

Validación de origen y destino. Listado e impresión de paquetes disponibles según el destino. Selección del paquete y cálculo del precio. Registro de pasajeros y gestión del pago. Gestión de Reservas:

Listado de todas las reservas. Opción para eliminar una reserva existente.
