# ============================================================
#   EJEMPLO PYTHON — COMPLEJIDAD O(log n)
# ============================================================
#
# Búsqueda binaria: el ejemplo clásico de un algoritmo logarítmico.
#
# ¿Por qué es O(log n)?
#
# Porque en cada paso el algoritmo REDUCE A LA MITAD el tamaño
# del espacio de búsqueda.
#
# Si empezamos con 1.000.000 de elementos:
#   - 1er paso: quedan 500.000
#   - 2do paso: quedan 250.000
#   - 3er paso: quedan 125.000
#   - ...
#   - En ~20 pasos ya encontramos el resultado o confirmamos que no existe.
#
# En términos de Big O:
#   El número de pasos crece con log₂(n), no con n.
#
# Esto hace que los algoritmos O(log n) sean extremadamente eficientes,
# incluso con cantidades enormes de datos.
# ------------------------------------------------------------

def buscar_binario(arr, objetivo):
    inicio, fin = 0, len(arr) - 1

    # Mientras el rango de búsqueda tenga sentido
    while inicio <= fin:

        # Calculamos el punto medio
        medio = (inicio + fin) // 2

        # Comparamos el valor del medio con el objetivo
        if arr[medio] == objetivo:
            return True

        # Si el objetivo está a la derecha
        if arr[medio] < objetivo:
            inicio = medio + 1

        # Si el objetivo está a la izquierda
        else:
            fin = medio - 1

    # Si se agota la búsqueda sin hallarlo
    return False

# Conclusión:
#   La lista se divide a la mitad en cada iteración.
#   Ese patrón da lugar al crecimiento logarítmico.
#   Complejidad temporal: O(log n).
