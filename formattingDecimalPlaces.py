# Este programa solicita al usuario que ingrese un número a través de la consola
# y luego muestra el número redondeado a dos decimales.

def redondear_a_dos_decimales(numero):
    return round(numero, 2)

# Solicitar el número al usuario
numero = float(input("Introduce un número: "))
print(f"El número redondeado a dos decimales es: {redondear_a_dos_decimales(numero)}")
