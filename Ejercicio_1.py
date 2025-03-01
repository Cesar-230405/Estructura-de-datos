import cmath  # Módulo para trabajar con números complejos

# Subrutina para calcular las raíces
def calcular_raices(a, b, c):
    # Calculamos el discriminante (b^2 - 4ac)
    discriminante = b**2 - 4*a*c
    
    # Calculamos las dos raíces usando la fórmula cuadrática
    raiz1 = (-b + cmath.sqrt(discriminante)) / (2*a)
    raiz2 = (-b - cmath.sqrt(discriminante)) / (2*a)
    
    return raiz1, raiz2

# Función para realizar las corridas de prueba
def pruebas():
    # Caso a) a = 1, b = 6, c = 2
    a, b, c = 1, 6, 2
    raiz1, raiz2 = calcular_raices(a, b, c)
    print(f"Raíces de la ecuación {a}x^2 + {b}x + {c} = 0:")
    print(f"Raíz 1: {raiz1}")
    print(f"Raíz 2: {raiz2}\n")

    # Caso b) a = 0, b = -4, c = 1.6 (esto no es una ecuación cuadrática válida)
    a, b, c = 0, -4, 1.6
    if a == 0:
        print("La ecuación no es cuadrática, ya que a = 0.\n")
    else:
        raiz1, raiz2 = calcular_raices(a, b, c)
        print(f"Raíces de la ecuación {a}x^2 + {b}x + {c} = 0:")
        print(f"Raíz 1: {raiz1}")
        print(f"Raíz 2: {raiz2}\n")

    # Caso c) a = 3, b = 2.5, c = 7
    a, b, c = 3, 2.5, 7
    raiz1, raiz2 = calcular_raices(a, b, c)
    print(f"Raíces de la ecuación {a}x^2 + {b}x + {c} = 0:")
    print(f"Raíz 1: {raiz1}")
    print(f"Raíz 2: {raiz2}\n")

# Ejecutamos las pruebas
pruebas()