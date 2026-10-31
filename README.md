# CABRERA_JENNY_AlgEstDatos_U2

## Sistema de gestión de una biblioteca en Python

Proyecto de consola para practicar diccionarios (`dict`) y conjuntos (`set`) de Python.

## Requisitos
- Python 3 instalado.
- No requiere instalar paquetes externos.

## Cómo ejecutar
Abra PowerShell en la carpeta del proyecto y ejecute:

```powershell
python main.py
```

Si `python` no está reconocido en Windows, pruebe:

```powershell
py main.py
```

## Requerimientos funcionales

- **R1 – Catálogo de libros (`dict`):** cada código identifica un libro y permite registrar y buscar su título y autor. No se admiten códigos repetidos.
- **R2 – Catálogo ordenado:** `sorted()` muestra los libros por código. El ordenamiento cuesta O(n log n). Un TreeMap mantiene las claves ordenadas durante las operaciones, por lo que recorrerlo en orden no requiere ordenar todo el catálogo en cada consulta.
- **R3 – Socios (`set`):** el conjunto guarda identificadores únicos y evita duplicados.
- **R4 – Análisis de préstamos (`set`):** intersección para socios que leen novela y ciencia, diferencia para quienes solo leen novela y unión para todos los socios distintos con préstamos.

El programa incluye libros y socios de ejemplo al iniciar. Los datos se mantienen en memoria durante la ejecución y no se guardan en un archivo.

## Pruebas
Ejecute las pruebas automatizadas desde esta carpeta:

```powershell
python -m unittest -v
```

En Windows también puede usar `py -m unittest -v`.

## Complejidades principales

| Operación | Complejidad promedio |
|---|---|
| Buscar libro por código | O(1) |
| Registrar libro en diccionario | O(1) |
| Mostrar catálogo ordenado con `sorted()` | O(n log n) |
| Verificar/agregar socio en conjunto | O(1) |
| Intersección de conjuntos | O(min(n, m)) aproximada |
| Diferencia de conjuntos | O(n) aproximada |
| Unión de conjuntos | O(n + m) aproximada |

`n` y `m` representan la cantidad de elementos de cada estructura. Las operaciones de diccionarios y conjuntos tienen complejidad promedio O(1) para búsqueda/inserción debido a su implementación basada en tablas hash; en casos extremos de colisiones puede ser mayor.
