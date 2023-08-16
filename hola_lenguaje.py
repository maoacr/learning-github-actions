import os


def main():
    nombre = os.getenv("USERNAME")
    print(f"¡Hola, {nombre}, este es el archivo del lenguaje favorito!")


if __name__ == "__main__":
    main()
