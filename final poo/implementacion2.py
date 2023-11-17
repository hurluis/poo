class Tetromino:
    def __init__(self, forma):
        self.forma = forma
        self.rotacion = 0

    def rotar(self):
        self.rotacion = (self.rotacion + 1) % 4

    def imprimir_representacion(self):
        forma_rotada = self.rotar_forma(self.forma, self.rotacion)
        for fila in forma_rotada:
            print(''.join(['@' if celda else '.' for celda in fila]))

    def rotar_forma(self, forma, rotaciones):
        forma_rotada = forma.copy()
        for _ in range(rotaciones):
            forma_rotada = list(zip(*reversed(forma_rotada)))
        return forma_rotada

    def __eq__(self, otro):
        return self.forma == otro.forma and self.rotacion == otro.rotacion

    def __str__(self):
        return f"Tetromino({self.forma}, rotacion={self.rotacion})"


# Ejemplo de uso y pruebas unitarias
if __name__ == "__main__":
    # Definir dos tetrominos para realizar pruebas
    tetromino_T = Tetromino([[0, 1, 0], [1, 1, 1], [0, 0, 0]])
    tetromino_Z = Tetromino([[1, 1, 0], [0, 1, 1], [0, 0, 0]])

    # Mostrar la representación de los tetrominos
    print("Tetromino T:")
    tetromino_T.imprimir_representacion()

    print("\nTetromino Z:")
    tetromino_Z.imprimir_representacion()

    # Rotar el Tetromino T y mostrar la representación nuevamente
    tetromino_T.rotar()
    print("\nTetromino T después de una rotación:")
    tetromino_T.imprimir_representacion()

    # Pruebas de igualdad y semejanza
    tetromino_Z_rotado = Tetromino([[0, 1, 1], [1, 1, 0], [0, 0, 0]])
    print("\n¿Los Tetrominos T son iguales?")
    print(tetromino_T == tetromino_T)

    print("\n¿Los Tetrominos Z son semejantes?")
    print(tetromino_Z == tetromino_Z_rotado)