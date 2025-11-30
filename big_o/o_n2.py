# ============================================================
#   EJEMPLO PYTHON — COMPLEJIDAD O(n²)
# ============================================================
#
# Este algoritmo genera todos los pares posibles dentro de una lista.
# Usa DOS bucles anidados.
#
# El bucle externo se ejecuta n veces.
# El bucle interno se ejecuta (n - i) veces por cada iteración externa.
#
# Aunque matemáticamente la cantidad exacta es n(n-1)/2,
# en notación Big O nos quedamos con el término dominante: n².
#
# Más intuitivamente:
#   - Si duplicás el tamaño de la lista, el trabajo se multiplica por 4.
#   - Si triplicás el tamaño, el trabajo se multiplica por 9.
#
# O(n²) es una complejidad que escala muy mal.
# ------------------------------------------------------------

def pares(lista):
    # Recorremos la lista con el primer índice
    for i in range(len(lista)):
        # Recorremos nuevamente la lista con un segundo índice,
        # empezando desde el siguiente elemento
        for j in range(i + 1, len(lista)):
            # Producimos un par (o realizamos alguna operación)
            print(lista[i], lista[j])

# Conclusión:
#   Dos bucles anidados → crecimiento cuadrático.
#   Complejidad temporal: O(n²).
