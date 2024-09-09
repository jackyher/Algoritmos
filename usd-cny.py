# Este programa convierte dólares estadounidenses (USD) a yuanes chinos (CNY)

def usd_to_cny(usd):
    # Convertir USD a CNY utilizando la tasa de conversión
    cny = usd * 6.75

    # Formatear el resultado a 2 decimales y en float (.2f) y convertirlo en una cadena (f")
    return f"{cny:.2f} Chinese Yuan"


# Solicitar al usuario que ingrese el monto en USD
usd_amount = int(input("Introduce la cantidad en USD: "))

# Convertir USD a CNY y mostrar el resultado
result = usd_to_cny(usd_amount)
print(result)

#print(usd_to_cny(15))  # '101.25 Chinese Yuan'
#print(usd_to_cny(465))  # '3138.75 Chinese Yuan'