# Convierte imágenes en resoluciones con una relación de aspecto de 16:9 manteniendo la misma altura.

import math

def convert_to_16_9(x, y):
    # Calcular el nuevo valor de X manteniendo Y igual y ajustando a la relación 16:9
    new_x = math.ceil(y * (16 / 9))

    # Retornar la nueva resolución
    return (new_x, y)


# Ejemplo de uso
x = int(input("Introduce la resolución ancho (X): "))
y = int(input("Introduce la resolución alto (Y): "))

new_resolution = convert_to_16_9(x, y)
print(f"La nueva resolución ajustada a 16:9 es: {new_resolution[0]}x{new_resolution[1]}")
