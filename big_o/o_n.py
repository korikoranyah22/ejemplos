# ============================================================
#   EJEMPLO PYTHON — COMPLEJIDAD O(n)
# ============================================================
#
# Este ejemplo muestra un algoritmo con complejidad lineal.
# O(n) significa que el tiempo de ejecución crece
# proporcionalmente al tamaño de la lista.
#
# Cuanto más grande sea "lista", más tiempo tardará,
# aumentando de manera directa: si duplicás la cantidad de
# elementos, aproximadamente se duplica la cantidad de pasos.
#
# ¿Por qué?
# Porque el algoritmo recorre la lista UNA VEZ, de principio a fin.
#
# La operación dominante es el bucle.
# ------------------------------------------------------------

def buscar(nombre, lista):
    # Recorremos cada elemento de la lista
    for item in lista:
        # Comparamos el elemento actual con el nombre buscado
        if item == nombre:
            # Si encontramos una coincidencia, devolvemos True
            return True

    # Si terminamos el recorrido sin encontrar coincidencias,
    # el resultado final es False
    return False

# Conclusión:
#   Este algoritmo realiza una cantidad de comparaciones que depende
#   directamente del tamaño de la lista: f(n) = n
#   Por eso su complejidad temporal es O(n).
