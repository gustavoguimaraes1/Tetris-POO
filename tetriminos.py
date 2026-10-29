# O TetriminoShape significa que sempre uma forma vai ter 4 objetos Block na sua composição.
# O ABC significa que a classe vai abstrata, ou seja, a ideia não é criar diretamente, mas ele será base das outras formas.
# initial_rotation significa a rotação do tetrimino.
# rotações: 0 = inicial, 1 = 90º, 2 = 180º, 3 = 270º.
# original_shape é a forma original da peça, ela tem a função abstrata.
# _box.size a sua lógica representa pegar o maior valor do bloco e fora do bloco pegar o maior valor dos 4 blocos.



from abc import ABC, abstractmethod
from block import Block
from exceptions import InvalidRotationError

TetriminoShape = [Block, Block, Block, Block]

class Tetrimino(ABC):


    def __init__(self, initial_rotation: int = 0):
        if initial_rotation < 0 or initial_rotation > 4:
            raise InvalidRotationError()

        self._rotation = initial_rotation

        original_shape = self._original_shape()

        self._box.size = 1 + max(
            max(block.x, block.y)
            for block in original_shape
        )

    @abstractmethod
    def _original_shape(self) -> TetriminoShape:
        pass



