# Py2 — Ejercicios de Python 2

Repositorio de ejercicios prácticos en Python organizados por secciones temáticas, desde conceptos básicos hasta estructuras de datos, funciones y un proyecto integrador.

---

## Estructura del proyecto

```
py2/
├── requirements.txt                  # Enunciados de todos los ejercicios
├── README.md
├── CarpetitaMadre/
│   ├── calculadoracientifica.py      # Calculadora científica (proyecto extra)
│   ├── ex.py                         # Ejemplos de estructuras de datos
│   ├── ÑamSeccion1/                  # Ejercicios 0–4: Entrada/salida y condicionales básicos
│   │   ├── ñam.py   (Ej. 0)
│   │   ├── ñam1.py  (Ej. 1)
│   │   ├── ñam2.py  (Ej. 2)
│   │   ├── ñam3.py  (Ej. 3)
│   │   └── ñam4.py  (Ej. 4)
│   ├── ÑamSeccion2/                  # Ejercicios 5–9: Condicionales y menús interactivos
│   │   ├── ñam5.py  (Ej. 5)
│   │   ├── ñam6.py  (Ej. 6)
│   │   ├── ñam7.py  (Ej. 7)
│   │   ├── ñam8.py  (Ej. 8)
│   │   └── ñam9.py  (Ej. 9)
│   ├── ÑamSeccion3/                  # Ejercicios 10–14: Ciclos for y while
│   │   ├── ñam10.py (Ej. 10)
│   │   ├── ñam11.py (Ej. 11)
│   │   ├── ñam12.py (Ej. 12)
│   │   ├── ñam13.py (Ej. 13)
│   │   └── ñam14.py (Ej. 14)
│   ├── ÑamSeccion4/                  # Ejercicios 15–19: Listas
│   │   ├── ñam15.py (Ej. 15)
│   │   ├── ñam16.py (Ej. 16)
│   │   ├── ñam17.py (Ej. 17)
│   │   ├── ñam18.py (Ej. 18)
│   │   └── ñam19.py (Ej. 19)
│   └── ÑamSeccion5/                  # Ejercicios 20–24: Funciones
│       ├── ñam20.py (Ej. 20)
│       ├── ñam21.py (Ej. 21)
│       ├── ñam22.py (Ej. 22)
│       ├── ñam23.py (Ej. 23)
│       └── ñam24.py (Ej. 24)
└── ÑamSeccion6/
    └── gestion_biblioteca.py         # Proyecto integrador: Sistema de gestión de biblioteca
```

---

## Secciones

### Sección 1 — Entrada/Salida y Condicionales básicos (`ÑamSeccion1/`)

| Archivo | Ejercicio | Descripción |
|---------|-----------|-------------|
| `ñam.py` | 0 | Registro de usuario: solicita nombre, edad y ciudad; muestra mensaje personalizado con validación de edad positiva. |
| `ñam1.py` | 1 | Calculadora básica: pide dos números y una operación (`+`, `-`, `*`, `/`) con validación de división por cero. |
| `ñam2.py` | 2 | Validador de correo electrónico: verifica presencia y posición válida de `@` y `.`. |
| `ñam3.py` | 3 | Validador de contraseña segura: comprueba longitud mínima, mayúsculas, números y caracteres especiales. |
| `ñam4.py` | 4 | Convertidor de unidades: menú para Celsius→Fahrenheit, kilómetros→millas y kilogramos→libras. |

---

### Sección 2 — Condicionales y Menús interactivos (`ÑamSeccion2/`)

| Archivo | Ejercicio | Descripción |
|---------|-----------|-------------|
| `ñam5.py` | 5 | Clasificador de edad: niño, adolescente, adulto o adulto mayor según rangos definidos. |
| `ñam6.py` | 6 | Menú interactivo con opciones: saludar, despedirse y salir usando `if-elif-else`. |
| `ñam7.py` | 7 | Calculadora con menú: extiende el ejercicio 1 permitiendo múltiples operaciones en sesión. |
| `ñam8.py` | 8 | Conversor de nota numérica (0-100) a letra (A, B, C, D, F) con validación de rango. |
| `ñam9.py` | 9 | Simulador de descuentos por categoría (A=20%, B=15%, C=10%): calcula monto final y ahorro. |

---

### Sección 3 — Ciclos `for` y `while` (`ÑamSeccion3/`)

| Archivo | Ejercicio | Descripción |
|---------|-----------|-------------|
| `ñam10.py` | 10 | Muestra todos los números pares desde 1 hasta N usando `for`. |
| `ñam11.py` | 11 | Suma acumulada de números ingresados hasta que el usuario ingrese 0. |
| `ñam12.py` | 12 | Búsqueda de un nombre en una lista predefinida, indicando posición si se encuentra. |
| `ñam13.py` | 13 | Generador de tabla de multiplicar del 1 al 10 con opción de repetir. |
| `ñam14.py` | 14 | Ingresa 10 números y muestra la lista sin duplicados (sin usar `set`). |

---

### Sección 4 — Listas (`ÑamSeccion4/`)

| Archivo | Ejercicio | Descripción |
|---------|-----------|-------------|
| `ñam15.py` | 15 | Lista de compras: agregar, eliminar y mostrar productos con menú interactivo. |
| `ñam16.py` | 16 | Ejercicio de listas (ver enunciado en `requirements.txt`). |
| `ñam17.py` | 17 | Ejercicio de listas (ver enunciado en `requirements.txt`). |
| `ñam18.py` | 18 | Ejercicio de listas (ver enunciado en `requirements.txt`). |
| `ñam19.py` | 19 | Compara dos listas: muestra elementos comunes, únicos de cada una (sin `set`). |

---

### Sección 5 — Funciones (`ÑamSeccion5/`)

| Archivo | Ejercicio | Descripción |
|---------|-----------|-------------|
| `ñam20.py` | 20 | Función `saludar(nombre, hora)`: retorna saludo según hora del día (mañana/tarde/noche). |
| `ñam21.py` | 21 | Ejercicio de funciones (ver enunciado en `requirements.txt`). |
| `ñam22.py` | 22 | Ejercicio de funciones (ver enunciado en `requirements.txt`). |
| `ñam23.py` | 23 | Ejercicio de funciones (ver enunciado en `requirements.txt`). |
| `ñam24.py` | 24 | Función `factorial(n)` recursiva con validación para números negativos. |

---

### Sección 6 — Proyecto integrador (`ÑamSeccion6/`)

#### `gestion_biblioteca.py` — Sistema de gestión de biblioteca

Proyecto completo que aplica todos los conceptos anteriores. Gestiona un catálogo de libros mediante una lista de diccionarios.

**Funciones principales:**

| Función | Descripción |
|---------|-------------|
| `agregar_libro()` | Registra un nuevo libro validando que el año sea numérico y mayor a 1900. |
| `mostrar_libros()` | Muestra el catálogo completo con ID, título, autor, año y disponibilidad. |
| `buscar_libro()` | Busca por título o autor con coincidencias parciales. |
| `prestar_libro(id)` | Marca un libro como prestado si está disponible. |
| `devolver_libro(id)` | Marca un libro como disponible nuevamente. |
| `eliminar_libro(id)` | Elimina un libro solo si no está prestado. |
| `libros_por_autor(autor)` | Lista todos los libros de un autor específico. |
| `estadisticas()` | Muestra total de libros, disponibles y prestados. |
| `exportar_a_txt()` | Exporta el catálogo al archivo `biblioteca.txt`. |
| `menu_principal()` | Menú interactivo que integra todas las funciones. |

---

### Extra — Calculadora científica (`CarpetitaMadre/calculadoracientifica.py`)

Calculadora con menú interactivo que incluye:
- Operaciones básicas: suma, resta, multiplicación, división.
- Funciones avanzadas: potencia, raíz cuadrada, seno, coseno, tangente, logaritmo natural, logaritmo base 10, factorial.
- Constantes: π y e.

---

## Requisitos

- Python 3.14.3
- No se requieren librerías externas (solo `math` de la biblioteca estándar).

---

## Ejecución

Cada archivo es independiente y puede ejecutarse directamente:

```bash
python CarpetitaMadre/ÑamSeccion1/ñam.py
python ÑamSeccion6/gestion_biblioteca.py
```
