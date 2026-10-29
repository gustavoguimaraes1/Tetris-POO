# O TetriminoShape significa que sempre uma forma vai ter 4 objetos Block na sua composição.
# O ABC significa que a classe vai abstrata, ou seja, a ideia não é criar diretamente, mas ele será base das outras formas.


from abc import ABC, abstractmethod
from block import Block
from exceptions import InvalidRotationError

TetriminoShape = [Block, Block, Block, Block]

class Tetrimino(ABC):
    pass

