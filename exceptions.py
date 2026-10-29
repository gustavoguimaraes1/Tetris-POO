# GamerError é a exceção geral do projeto.
# InvalidBlockError será usada quando criarem um bloco com coordenada negativa.
# InvalidRotationError será usada quando tentarem iniciar um tetrimino com rotação fora de 0, 1, 2, 3.


class GamerError(Exception):
    pass

class InvalidBlockError(GamerError):
    pass

class InvalidRotationError(GamerError):
    pass