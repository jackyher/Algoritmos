# Este programa calcula los puntos de un jugador de NBA por partido si jugó los 48 minutos completos.

def nba_extrap(ppg, mpg):
    if mpg == 0:  # Si no jugó minutos, devolvemos 0
        return 0

    # Calcular los puntos extrapolados para 48 minutos
    extrapolated_ppg = (ppg / mpg) * 48

    # Redondear el resultado a la décima más cercana
    return round(extrapolated_ppg, 1)


# Solicitar al usuario que ingrese los datos
ppg = float(input("Introduce los puntos por juego (ppg): "))
mpg = float(input("Introduce los minutos por juego (mpg): "))

# Llamar a la función y mostrar el resultado
result = nba_extrap(ppg, mpg)
print(f"Los puntos extrapolados por 48 minutos son: {result}")

