"""
Álvaro Marcos Rodríguez
primos.py modulo de manejo de numeros primos

Manejo de números primos - APA 2026
Tests unitarios de las funciones incluidas en este módulo:
>>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)
>>> mcm(90, 14)
630
>>> mcd(924, 780)
12
>>> mcm(42, 60, 70, 63)
1260
>>> mcd(840, 630, 1050, 1470)
210
"""


def esPrimo(numero):
    """
    Mira si un número natural mayor que uno es primo.
    """
    if not isinstance(numero, int) or numero < 2:
        raise TypeError("El argumento debe ser un número natural mayor que uno.")
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            return False
    return True


def primos(numero):
    """
    Retorna una tupla con todos los números primos menores que un numero.
    """
    return tuple(n for n in range(2, numero) if esPrimo(n))


def descompon(numero):
    """
    Retorna una tupla con la descomposición en factores primos de un numero.
    """
    factores = []
    divisor = 2
    while numero > 1:
        while numero % divisor == 0:
            factores.append(divisor)
            numero //= divisor
        divisor += 1
    return tuple(factores)


def mcm(*numeros):
    """
    Retorna el mínimo común múltiplo de un número arbitrario de argumentos.
    """
    factores_max = {}
    for numero in numeros:
        factores = descompon(numero)
        for factor in set(factores):
            potencia = factores.count(factor)
            if factor not in factores_max or potencia > factores_max[factor]:
                factores_max[factor] = potencia
    resultado = 1
    for factor, potencia in factores_max.items():
        resultado *= factor ** potencia
    return resultado


def mcd(*numeros):
    """
    Retorna el máximo común divisor de un número arbitrario de argumentos.
    """
    lista_factores = [descompon(numero) for numero in numeros]
    factores_comunes = set(lista_factores[0])
    resultado = 1
    for factor in factores_comunes:
        potencia_min = min(factores.count(factor) for factores in lista_factores)
        if potencia_min > 0:
            resultado *= factor ** potencia_min
    return resultado


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)