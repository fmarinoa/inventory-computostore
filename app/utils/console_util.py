import os

# Función para limpiar la consola
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
