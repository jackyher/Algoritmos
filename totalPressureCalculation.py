# Este programa calcula la presión total que ejercen dos gases en un recipiente, utilizando
# las masas de los gases, sus masas molares, el volumen del recipiente y la temperatura.

def calcular_presion_total(M1, M2, m1, m2, V, T):
    # Constante de gas en dm^3⋅atm⋅K^−1⋅mol^−1
    R = 0.082

    # Convertir la temperatura de Celsius a Kelvin
    T_kelvin = T + 273.15

    # Aplicar la fórmula para la presión total
    P_total = ((m1 / M1) + (m2 / M2)) * R * T_kelvin / V

    return P_total


# Ejemplo de uso:
M1 = 10.0  # Molar mass 1 en g/mol
M2 = 20.0  # Molar mass 2 en g/mol
m1 = 5.0  # Masa del gas 1 en g
m2 = 3.0  # Masa del gas 2 en g
V = 2.0  # Volumen en dm^3
T = 25.0  # Temperatura en grados Celsius

presion = calcular_presion_total(M1, M2, m1, m2, V, T)
print(f"La presión total es: {presion} atm")
