"""
Programa que calcula la edad de un perro y un gato
en años humanos.
"""
# Calcula la edad del perro y del gato en años humanos

def calculate_pet_ages(human_years):
    # Inicializamos las edades de los gatos y perros
    cat_years = 0
    dog_years = 0

    # Calcular la edad del gato
    if human_years == 1:
        cat_years = 15
    elif human_years == 2:
        cat_years = 15 + 9
    else:
        cat_years = 15 + 9 + (human_years - 2) * 4

    # Calcular la edad del perro
    if human_years == 1:
        dog_years = 15
    elif human_years == 2:
        dog_years = 15 + 9
    else:
        dog_years = 15 + 9 + (human_years - 2) * 5

    # Retornar los años humanos, años de gato y años de perro en tipo de dato lista
    return [human_years, cat_years, dog_years]


# Ejemplo de uso
#human_years = 12

human_years = int(input("Introduce el número de años humanos: "))

ages = calculate_pet_ages(human_years)
print(ages)
print(f"Human Years: {ages[0]} \nCat Years: {ages[1]} \nDog Years: {ages[2]}")

#Imprime o muesta el tipo de datos devuelto por la función
print(type(ages))
