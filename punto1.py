"""Punto1"""

# Función que realiza operaciones básicas según el operador proporcionado.
def operaciones_basicas(numero1,numero2,operador):
    if operador == "+":
        return numero1 + numero2
    elif operador == "-":
        return numero1 - numero2
    elif operador == "*":
        return numero1 * numero2
    elif operador == "/":
        if numero2 == 0:
          return "No se puede dividir por cero"
        else:
          return numero1 / numero2
    else:
        return "operador invalido"

# Solicita la entrada de los números y el operador.
numero1 = float(input('Ingrese el primer numero: '))
numero2 = float(input('Ingrese el segundo numero: '))
operador = input('Ingrese el operador (+, -, *, /): ')

# Ejecuta la función y muestra el resultado.
resultado = operaciones_basicas(numero1,numero2,operador)
print(resultado)
