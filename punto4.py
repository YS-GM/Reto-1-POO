"""Punto4
"""

def primo(n):
   #Determina si un número es primo.
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filtrar_numero(lista):
    #Filtra los números primos de una lista.
    primos = [num for num in lista if primo(num)]
    return primos

# Solicitar al usuario que ingrese una lista de números
entrada = input('Ingrese una lista de números enteros separados por comas: ')
numeros = [int(num.strip()) for num in entrada.split(',')]  # Convertir la entrada en una lista de enteros

# Filtrar los números primos
primos_en_lista = filtrar_numero(numeros)

# Mostrar el resultado
print('Números primos en la lista:', primos_en_lista)
