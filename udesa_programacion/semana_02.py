#ejercicios de la semana 2

# Ejercicio 1: Invertir listas
print("\n Ejercicio 1:")
l1 = [1,2,3,4,5]
l2 = ['Bogota', 'Rosario', 'San Fernando', 'San Miguel']

def invertir_lista(lista):
    return lista[::-1]

#verificamos la función
print(f"Lista 1: {l1}")
print("La lista invertida seria:", invertir_lista(l1))

print(f"La lista 2: {l2}")
print("La lista invertida seria:", invertir_lista(l2))

# Ejercicio 2: Conjetura de Collatz
#1) Empezamos con un número entero positivo
#2) Lo evaluamos, si el número es par entonces lo dividimos entre 2. Si es impar, entonces se multiplica por 3 y se le suma 1.
#3) Al resultado lo volvemos a evaluar y nuevamente aplicamos las operaciones correspondientes hasta que obtengamos un 1.
#4) Retornar la cantidad de pasos realizados.

def collatz(n):
    pasos = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        pasos += 1
    return pasos

print("\n Ejercicio 2:")
max_num = 10 * 10**15
n = int(input("Ingrese un numero entero positivo:"))

if n <= 0:
    print("Por favor, ingrese un numero entero positivo")
elif n > max_num:
    print(f"el numero es demasiado grande. Ingresa un valor menor a {max_num}")
else:
    pasos = collatz(n)
    print(f"el numero {n} llego a 1 en {pasos} pasos.")

# Ejercicio 3: Diccionarios

# Diccionario de ejemplo
d = {
    "manzana": ["fruta", "roja", "dulce"],
    "banana": ["fruta", "amarilla", "alargada"],
    "tomate": ["fruta", "roja", "ácida"],
    "lechuga": ["verdura", "verde", "hoja"],
    "limón": ["fruta", "cítrico", "amarillo"]
}

def contar_definiciones(d):
    return {clave: len(definiciones) for clave, definiciones in d.items()}

def cantidad_de_claves_letra(d, l):
    return sum(1 for clave in d if clave.startswith(l))

print("\nEjercicio 3:")

resultado1 = contar_definiciones(d)
print("\nCantidad de definiciones por clave:")
print(resultado1)  

letra = 'l'
resultado2 = cantidad_de_claves_letra(d, letra)
print(f"\nCantidad de claves que comienzan con '{letra}': {resultado2}") 

letra = 'm'
resultado3 = cantidad_de_claves_letra(d, letra)
print(f"\nCantidad de claves que comienzan con '{letra}': {resultado3}")  # Debería ser 1

# Ejercicio 4: Fosforos

print("\n Ejercicio 4:")

def propagar(L):
    L = L[:]  
    for i in range(len(L)):
        if L[i] == 1: 
            # Propaga a la izquierda
            j = i - 1
            while j >= 0 and L[j] == 0:
                L[j] = 1
                j -= 1
            # Propaga a la derecha
            j = i + 1
            while j < len(L) and L[j] == 0:
                L[j] = 1
                j += 1
    return L

ejemplo1 = [0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0]
print("\n Propagación de fuego")
print("Antes :", ejemplo1)
resultado1 = propagar(ejemplo1)
print("Después:", resultado1) 

# 🔥 Otro ejemplo
ejemplo2 = [0, 0, 0, 1, 0, 0]
print("\nAntes :", ejemplo2)
resultado2 = propagar(ejemplo2)
print("Después:", resultado2)