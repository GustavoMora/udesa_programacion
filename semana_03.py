import random

# Ejercicio 1: Crear un álbum vacío
def crear_album(figus_total):
    return [0] * figus_total

# Ejercicio 2: Verificar si el álbum está incompleto
def album_incompleto(A):
    return 0 in A

# Ejercicio 3: Comprar una figurita individual
def comprar_figu(figus_total):
    return random.randint(0, figus_total - 1)

# Ejercicio 4: Contar cuántas figuritas se necesitan para llenar el álbum
def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    figus_compradas = 0
    while album_incompleto(album):
        figu = comprar_figu(figus_total)
        album[figu] = 1
        figus_compradas += 1
    return figus_compradas

# Ejercicio 6: Experimento con figuritas individuales
def experimento_figus(n_repeticiones, figus_total):
    resultados = []
    for _ in range(n_repeticiones):
        resultado = cuantas_figus(figus_total)
        resultados.append(resultado)
    return sum(resultados) / len(resultados)

# Ejercicio 8: Comprar un paquete de figuritas
def comprar_paquete(figus_total, figus_paquete):
    paquete = []
    for _ in range(figus_paquete):
        figu = random.randint(0, figus_total - 1)
        paquete.append(figu)
    return paquete

# Ejercicio 9: Contar cuántos paquetes se necesitan para llenar el álbum
def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    paquetes_comprados = 0
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        for figu in paquete:
            album[figu] = 1
        paquetes_comprados += 1
    return paquetes_comprados

# Código ejecutable para los ejercicios 5 y 10
if __name__ == "__main__":
    # Ejercicio 5: 1000 repeticiones para álbum de 6 figuritas
    n_repeticiones = 1000
    figus_total = 6
    resultados_figus = [cuantas_figus(figus_total) for _ in range(n_repeticiones)]
    promedio_figus = sum(resultados_figus) / len(resultados_figus)
    
    # Ejercicio 10: 100 repeticiones para álbum de 860 figuritas con paquetes
    n_repeticiones = 100
    figus_total = 860
    figus_paquete = 5
    resultados_paquetes = [cuantos_paquetes(figus_total, figus_paquete) for _ in range(n_repeticiones)]
    promedio_paquetes = sum(resultados_paquetes) / len(resultados_paquetes)