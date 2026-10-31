# O TetriminoShape significa que sempre uma forma vai ter 4 objetos Block na sua composição.
# O ABC significa que a classe vai abstrata, ou seja, a ideia não é criar diretamente, mas ele será base das outras formas.
# initial_rotation significa a rotação do tetrimino.
# rotações: 0 = inicial, 1 = 90º, 2 = 180º, 3 = 270º.
# original_shape é a forma original da peça, ela tem a função abstrata.
# _box.size a sua lógica representa pegar o maior valor do bloco e fora do bloco pegar o maior valor dos 4 blocos.
# _rotate.shape é staticmethod, pois não precisa usar o self, pois ele só precisa do shape e o box_size para transformar uma nova forma de rotação.
# Além disso a lógica dele é definir as formas de 90º no sentido horário, assim transformando cada bloco em (box_size - 1 - y, x).
# Os shapes são as rotações das formmas, na qual giram 90º graus.
# Os Left e Right são funções de movimento para a esquerda e direita, a porcentagem 4 faz esse ciclo. (Lembrando que é só 0, 1, 2, 3 de movimento).
# A função color é abstrata, pois vai ser usada nas cores dos tetriminos.
# O __str__ é usado para desenhar a peça em texto, assim ocupando a caixa inteira.


from abc import ABC, abstractmethod
from block import Block
from exceptions import InvalidRotationError

TetriminoShape = tuple[Block, Block, Block, Block]

class Tetrimino(ABC):


    def __init__(self, initial_rotation: int = 0):
        if initial_rotation < 0 or initial_rotation >= 4:
            raise InvalidRotationError()

        self._rotation = initial_rotation

        original_shape = self._original_shape()

        self._box_size = 1 + max(
            max(block.x, block.y)
            for block in original_shape
        )

        shape0 = original_shape
        shape1 = self._rotate_shape(shape0, self._box_size)
        shape2 = self._rotate_shape(shape1, self._box_size)
        shape3 = self._rotate_shape(shape2, self._box_size)

        self._shapes = (
            shape0,
            shape1,
            shape2,
            shape3
        )

    @abstractmethod
    def _original_shape(self) -> TetriminoShape:
        pass

    @staticmethod
    def _rotate_shape(shape, box_size) -> TetriminoShape:
        return tuple(
            Block(box_size - 1 - block.y, block.x)
            for block in shape
        )

    @property
    def shape(self) -> TetriminoShape:
        return self._shapes[self._rotation]

    @property
    def box_size(self) -> int:
        return self._box_size

    @property
    def current_rotation(self) -> int:
        return self._rotation

    def right_rotate(self):
        self._rotation = (self._rotation + 1) % 4

    def left_rotate(self):
        self._rotation = (self._rotation - 1) % 4

    @property
    @abstractmethod
    def color(self) -> str:
        pass

    def __str__(self) -> str:
        linhas = []

        for y in range(self._box_size):
            linha = ""

            for x in range(self._box_size):
                ocupado = any(
                    block.x == x and block.y == y
                    for block in self.shape
                )

                if ocupado:
                    linha += "⬜"
                else:
                    linha += "⬛"

            linhas.append(linha)

        return "\n".join(linhas)


# Classes dos Tetriminos
# TretiminoI
# TetriminoJ
# TetriminoL
# TetriminoO
# TetriminoS
# TetriminoT
# TetriminoZ

class TetriminoI(Tetrimino):

    def _original_shape(self) -> TetriminoShape:
        return (
            Block(0, 1),
            Block(1, 1),
            Block(2, 1),
            Block(3, 1)
        )
    @property
    def color(self) -> str:
        return "#00f0f0"

class TetriminoJ(Tetrimino):

    def _original_shape(self) -> TetriminoShape:
        return (
            Block(0, 0),
            Block(0, 1),
            Block(1, 1),
            Block(2, 1)
        )
    @property
    def color(self) -> str:
        return "#0000f0"

class TetriminoL(Tetrimino):

    def _original_shape(self) -> TetriminoShape:
        return (
            Block(2, 0),
            Block(0, 1),
            Block(1, 1),
            Block(2, 1)
        )
    @property
    def color(self) -> str:
        return "#f0a000"

class TetriminoO(Tetrimino):

    def _original_shape(self) -> TetriminoShape:
        return (
            Block(0, 0),
            Block(1, 0),
            Block(0, 1),
            Block(1, 1)
        )
    @property
    def color(self) -> str:
        return "#f0f000"

class TetriminoS(Tetrimino):

    def _original_shape(self) -> TetriminoShape:
        return (
            Block(1, 0),
            Block(2, 0),
            Block(0, 1),
            Block(1, 1)
        )
    @property
    def color(self) -> str:
        return "#00f000"

class TetriminoT(Tetrimino):

    def _original_shape(self) -> TetriminoShape:
        return (
            Block(1, 0),
            Block(0, 1),
            Block(1, 1),
            Block(2, 1)
        )
    @property
    def color(self) -> str:
        return "#a000f0"

class TetriminoZ(Tetrimino):

    def _original_shape(self) -> TetriminoShape:
        return (
            Block(0, 0),
            Block(1, 0),
            Block(1, 1),
            Block(2, 1),
        )
    @property
    def color(self) -> str:
        return "#f00000"