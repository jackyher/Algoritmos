# Este programa solicita al usuario que ingrese su edad a través de la consola y luego calcula
# y muestra el rango de edad mínimo y máximo para salir con alguien.

def rango_de_citas(edad):
    if edad <= 14:
        min_edad = int(edad - 0.10 * edad)
        max_edad = int(edad + 0.10 * edad)
    else:
        min_edad = int(edad / 2 + 7)
        max_edad = int((edad - 7) * 2)
    return f"{min_edad}-{max_edad}"

# Solicitar la edad al usuario
edad = int(input("Introduce tu edad: "))
print(f"Tu rango de citas es: {rango_de_citas(edad)}")

