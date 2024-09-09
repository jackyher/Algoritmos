# Este programa calcula la cantidad de litros de agua que beberá un ciclista por hora

import math

def litres(time):
    # Multiplicar el tiempo por 0.5 para obtener los litros, y redondear hacia abajo
    return math.floor(time * 0.5)

# Ejemplos de uso
time = float(input("Introduce el tiempo en horas: "))
litres_drunk = litres(time)
print(f"Nathan beberá {litres_drunk} litros de agua.")
