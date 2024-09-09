# Este programa calcula el costo total con oferta de 3*2 en función de la cantidad de mangos

def mango(quantity, price):
    # Calcular cuántos mangos se pagan (por cada 3, se pagan 2)
    paid_mangoes = (quantity // 3) * 2 + (quantity % 3)

    # Calcular el costo total multiplicando los mangos que se pagan por el precio por unidad
    total_cost = paid_mangoes * price

    return total_cost


# Ejemplos de uso
print(mango(2, 3))  # 6
print(mango(3, 3))  # 6
print(mango(5, 3))  # 12
print(mango(9, 5))  # 30
