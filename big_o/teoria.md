# 📘 **Guía Completa de Complejidad Algorítmica y Notación Big O**

_Un tutorial claro, moderno y fácil de seguir — con ejemplos en Python_

## 🟣 **1. Introducción: por qué existe Big O**

Cuando escribimos un programa, muchas veces tenemos más de una forma de resolver el mismo problema.  
Pero… ¿cómo sabemos cuál es mejor? ¿Más rápido? ¿Más eficiente? ¿Más escalable?

Medir el tiempo “con un cronómetro” no alcanza, porque el tiempo depende de:

- el procesador
- la RAM
- otros procesos abiertos
- el sistema operativo
- el disco
- el azar del scheduler

Por eso necesitamos una forma **independiente del hardware** para medir la eficiencia de un algoritmo.  
Ahí entra **la notación Big O**.

Big O responde:

- ¿Qué pasa si la entrada crece enormemente?
- ¿Mi algoritmo escala o colapsa?
- ¿Cuál de dos soluciones es mejor a largo plazo?

---

## 🟣 **2. Qué es un algoritmo**

Un **algoritmo** es simplemente un conjunto de instrucciones paso a paso para resolver un problema.  
Dos algoritmos distintos pueden resolver exactamente lo mismo…  
pero uno puede tardar milisegundos y otro horas.

Big O no observa el resultado, sino **el proceso**.

---

## 🟣 **3. ¿Cómo se determina la eficiencia de un algoritmo?**

La eficiencia se basa en cuántas **operaciones básicas** realiza el algoritmo en función del tamaño de los datos (**n**).  
Las operaciones básicas son:

- Comparaciones
- Asignaciones
- Accesos a un array
- Iteraciones de un bucle
- Retornos

No importa cuánto tarde cada una en tiempo real:  
importa **cómo crecen en cantidad** cuando la entrada crece.

---

## 🟣 **4. Problemas comunes: memoria y código ineficiente**

Dos fuentes típicas de lentitud:

### 1) Uso excesivo de memoria

Si un programa ocupa mucha RAM, el sistema usa memoria virtual (disco).  
Y el disco es _lento_. Muy lento.

### 2) Ineficiencia del código

A veces la computadora no es lenta:  
el algoritmo simplemente está mal planteado.

Big O permite anticipar estos problemas incluso antes de programar.

---

## 🟣 **5. ¿Cómo medimos la eficiencia sin probar el programa?**

Big O analiza el crecimiento del número de operaciones.

En lugar de preguntar:

> “¿Cuánto tarda exactamente?”

Preguntamos:

> “¿Cómo crece el costo cuando n aumenta?”

Esto se llama **complejidad temporal asintótica**.

---

## 🟣 **6. Qué es Big O (definición simple)**

Big O describe la **tasa de crecimiento** de un algoritmo.  
Decimos que un algoritmo es **O(f(n))** cuando la cantidad de operaciones crece proporcionalmente a la función **f(n)**.

Ejemplos:

- Recorrer una lista → f(n) = n → **O(n)**
- Doble bucle anidado → f(n) = n² → **O(n²)**
- Búsqueda binaria → f(n) = log₂(n) → **O(log n)**

Lo importante no es el valor exacto de f(n), sino **el comportamiento cuando n se vuelve enorme**.

---

## 🟣 **7. Cómo calcular Big O (tutorial paso a paso)**

### ✔️ Paso 1 — Contar operaciones básicas

Observamos cuántas veces se ejecutan:

- bucles
- comparaciones
- accesos
- asignaciones

### ✔️ Paso 2 — Expresar ese conteo como una función f(n)

Ejemplos:

| Código                   | f(n)    |
| ------------------------ | ------- |
| Un bucle                 | n       |
| Doble bucle              | n²      |
| Búsqueda binaria         | log n   |
| n elementos + constantes | 3n + 10 |

### ✔️ Paso 3 — Quedarse con el término dominante

Regla:  
**Cuando n es grande, las constantes no importan.**

Ejemplos:

- f(n) = 3n + 4 → O(n)
- f(n) = n² + 50n → O(n²)
- f(n) = n log n + n → O(n log n)

---

## 🟣 **8. Ejemplos en Python**

### Ejemplo O(n)

```python
def buscar(nombre, lista):
    for item in lista:
        if item == nombre:
            return True
    return False
```

### Ejemplo O(n²)

```python
def pares(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            print(lista[i], lista[j])
```

### Ejemplo O(log n)

```python
def buscar_binario(arr, objetivo):
    inicio, fin = 0, len(arr) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if arr[medio] == objetivo:
            return True
        elif arr[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return False
```

---

## 🟣 **9. Tabla resumen**

| Complejidad | Interpretación  |
| ----------- | --------------- |
| O(1)        | Constante       |
| O(log n)    | Logarítmica     |
| O(n)        | Lineal          |
| O(n log n)  | Semi-cuadrática |
| O(n²)       | Cuadrática      |
| O(2ⁿ)       | Exponencial     |
| O(n!)       | Factorial       |

---

## 🟣 **10. Mini Machete**

```
O(1) → constante
O(log n) → logarítmica
O(n) → lineal
O(n log n) → intermedia
O(n²) → cuadrática
O(2ⁿ) → exponencial
O(n!) → factorial
```

---

## 🟣 **11. Conclusión**

Big O es una herramienta fundamental para diseñar software eficiente y escalable.  
Una vez que entendés cómo funciona, podés analizar cualquier algoritmo y anticipar su comportamiento sin necesidad de ejecutarlo.
