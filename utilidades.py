"""Funciones auxiliares para el sistema de biblioteca."""

def registrar_libro(catalogo, codigo, titulo, autor):
    """Registra un libro si los datos son válidos y el código no existe."""
    if not codigo or not titulo or not autor:
        raise ValueError("el código, título y autor son obligatorios")
    if codigo in catalogo:  # búsqueda en diccionario: O(1) promedio
        raise ValueError("ya existe un libro con ese código")
    catalogo[codigo] = {"titulo": titulo, "autor": autor}  # inserción: O(1) promedio
    return True

def buscar_libro(catalogo, codigo):
    """Devuelve los datos del libro o None si no existe."""
    return catalogo.get(codigo)  # búsqueda por clave: O(1) promedio

def mostrar_catalogo_ordenado(catalogo):
    """Imprime los libros por código ascendente."""
    if not catalogo:
        print("El catálogo está vacío.")
        return
    # Ordenar con sorted: O(n log n); un TreeMap mantiene las claves ordenadas.
    for codigo in sorted(catalogo):
        libro = catalogo[codigo]
        print(f"{codigo} | {libro['titulo']} | {libro['autor']}")

def registrar_socio(socios, identificador):
    """Agrega un socio y evita duplicados. Devuelve False si ya existía."""
    if not identificador:
        return False
    if identificador in socios:  # pertenencia en conjunto: O(1) promedio
        return False
    socios.add(identificador)  # inserción en conjunto: O(1) promedio
    return True

def analizar_prestamos(prestamos_novela, prestamos_ciencia):
    """Calcula intersección, diferencia y unión de los conjuntos."""
    return {
        "ambos": prestamos_novela & prestamos_ciencia,  # intersección: O(min(n,m)) promedio
        "solo_novela": prestamos_novela - prestamos_ciencia,  # diferencia: O(n) promedio
        "total": prestamos_novela | prestamos_ciencia,  # unión: O(n+m) promedio
    }
