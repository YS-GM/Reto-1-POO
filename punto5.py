
"""Punto5
"""

def elementos_iguales(lista):
    # Lista para almacenar las cadenas con los mismos caracteres
    resultado = []

    # Recorre la lista de cadenas
    for palabra in lista:
        # Compara cada palabra con el resto de las palabras en la lista
        for otra_palabra in lista:
            if palabra != otra_palabra and sorted(palabra) == sorted(otra_palabra):
                if palabra not in resultado:
                    resultado.append(palabra)
                break

    return resultado

# Solicitar al usuario una lista de palabras
entrada = input('Ingrese una lista de palabras separadas por comas: ')
palabras = [palabra.strip() for palabra in entrada.split(',')]  # Convertir la entrada en una lista de palabras

# Filtrar las palabras con los mismos caracteres
resultado = elementos_iguales(palabras)

# Mostrar el resultado
print('Palabras con los mismos caracteres:', resultado)
