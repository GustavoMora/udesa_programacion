#Listado de ejercicios de la semana 2

# Ejercicio 1: Invertir listas
print("\n Ejercicio 1: Listas")

def invertir_lista(lista):
    lista_invertida = []

    for i in range(len(lista) - 1, -1, -1):  
        lista_invertida.append(lista[i])  
    
    return lista_invertida 

l1 = [1, 2, 3, 4, 5]
l2 = ["Bogotá", "Rosario", "San Fernando", "San Miguel"]

print("Lista original:", l1)
print("Lista invertida:", invertir_lista(l1))

print("\nLista original:", l2)
print("Lista invertida:", invertir_lista(l2))

# Ejercicio 2: Conjetura de Collatz
#1) Empezamos con un numero entero positivo
#2) Lo evaluamos, si el numero es par entonces lo dividimos entre 2. Si es impar, entonces se multiplica por 3 y se le suma 1.
#3) Al resultado lo volvemos a evaluar y nuevamente aplicamos las operaciones correspondientes hasta que obtengamos un 1.
#4) Retornar la cantidad de pasos realizados.

print("\n Ejercicio 2: Collatz")

def collatz(n):
    if n == 1:
        return 0 #al llegar a 1 terminan los pasos
    elif n % 2 == 0:
        return 1 + collatz(n / 2)  # n par
    else:
        return 1 + collatz(3 * n + 1)  # n impar

#test
n = 27
pasos = collatz(n)
print(f"El número {n} llegó a 1 en {pasos} pasos.")

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

print("\nEjercicio 3: Diccionarios")

resultado1 = contar_definiciones(d)
print("\nCantidad de definiciones por clave:")
print(resultado1)  

letra = 'l'
resultado2 = cantidad_de_claves_letra(d, letra)
print(f"\nCantidad de claves que comienzan con '{letra}': {resultado2}") 

letra = 'm'
resultado3 = cantidad_de_claves_letra(d, letra)
print(f"\nCantidad de claves que comienzan con '{letra}': {resultado3}")

# Ejercicio 4: Fosforos

print("\n Ejercicio 4: Fosforos")

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

f1 = [0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0]
print("\n Propagación de fuego")
print("Antes :", f1)
resultado1 = propagar(f1)
print("Después:", resultado1) 

f2 = [0, 0, 0, 1, 0, 0]
print("\nAntes :", f2)
resultado2 = propagar(f2)
print("Después:", resultado2)