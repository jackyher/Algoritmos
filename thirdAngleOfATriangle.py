# Este programa calcula el tercer ángulo de un triángulo a partir de dos proporcionados

def third_angle(angle1, angle2):
    # La suma de los ángulos interiores de un triángulo es siempre 180 grados
    return 180 - (angle1 + angle2)

# Ejemplos de uso
angle1 = int(input("Introduce el primer ángulo: "))
angle2 = int(input("Introduce el segundo ángulo: "))

third = third_angle(angle1, angle2)
print(f"El tercer ángulo es: {third}")