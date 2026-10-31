"""
Sistema de gestión de biblioteca.
Unidad 2: diccionarios (dict) y conjuntos (set).
Ejecutar con: python main.py
"""

from utilidades import (
    registrar_libro,
    buscar_libro,
    mostrar_catalogo_ordenado,
    registrar_socio,
    analizar_prestamos,
)

def cargar_datos_ejemplo():
    """Carga datos iniciales para facilitar las pruebas."""
    catalogo = {
        "L003": {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"},
        "L001": {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes"},
        "L002": {"titulo": "Breves respuestas a las grandes preguntas", "autor": "Stephen Hawking"},
    }
    socios = {"SOC001", "SOC002", "SOC003", "SOC004"}
    prestamos_novela = {"SOC001", "SOC002", "SOC004"}
    prestamos_ciencia = {"SOC002", "SOC003"}
    return catalogo, socios, prestamos_novela, prestamos_ciencia

def mostrar_menu():
    print("\n===== SISTEMA DE GESTIÓN DE BIBLIOTECA =====")
    print("1. Registrar libro")
    print("2. Buscar libro por código")
    print("3. Mostrar catálogo ordenado")
    print("4. Registrar socio")
    print("5. Analizar préstamos por género")
    print("6. Mostrar socios registrados")
    print("0. Salir")

def main():
    catalogo, socios, prestamos_novela, prestamos_ciencia = cargar_datos_ejemplo()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            codigo = input("Código del libro: ").strip().upper()
            titulo = input("Título: ").strip()
            autor = input("Autor: ").strip()
            try:
                registrar_libro(catalogo, codigo, titulo, autor)
                print("Libro registrado correctamente.")
            except ValueError as error:
                print(f"No se pudo registrar: {error}")

        elif opcion == "2":
            codigo = input("Código del libro que desea buscar: ").strip().upper()
            libro = buscar_libro(catalogo, codigo)
            if libro:
                print(f"Código: {codigo} | Título: {libro['titulo']} | Autor: {libro['autor']}")
            else:
                print("No se encontró un libro con ese código.")

        elif opcion == "3":
            mostrar_catalogo_ordenado(catalogo)

        elif opcion == "4":
            identificador = input("Identificador del socio: ").strip().upper()
            if registrar_socio(socios, identificador):
                print("Socio registrado correctamente.")
            else:
                print("El socio ya estaba registrado o el identificador está vacío.")

        elif opcion == "5":
            resultado = analizar_prestamos(prestamos_novela, prestamos_ciencia)
            print("\n--- Análisis de préstamos ---")
            print("Leen novela y ciencia:", sorted(resultado["ambos"]) or "Ninguno")
            print("Solo leen novela:", sorted(resultado["solo_novela"]) or "Ninguno")
            print("Socios distintos con préstamos:", sorted(resultado["total"]) or "Ninguno")
            print(f"Total de socios distintos con préstamos: {len(resultado['total'])}")

        elif opcion == "6":
            print("Socios registrados:", sorted(socios) or "No hay socios registrados.")

        elif opcion == "0":
            print("Gracias por utilizar el sistema.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
