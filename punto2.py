# -*- coding: utf-8 -*-
"""Punto2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11B9Buq4zc2OBB8ybrbdeNYyGGg9ApYzz
"""

# Función que verifica si una palabra es un palíndromo.
def palindromo(palabra):
  # Convierte la palabra a minúsculas y la invierte.
    palabra = palabra.lower()
    list_caracteres = list(palabra)
    list_caracteres.reverse()
     # Compara la palabra original con la invertida.
    if list_caracteres == list(palabra):
        print('Es un palindromo') #Si son iguales es palindroma
    else:
        print('No es un palindromo') # Si no, no es palindroma

# Solicita la palabra al usuario y verifica si es un palíndromo.
palabra = input('Ingrese una palabra: ')
palindromo(palabra)