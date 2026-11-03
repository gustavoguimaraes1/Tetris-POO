# Tetris em Python

Projeto desenvolvido para a disciplina de **Programação Orientada a Objetos**, utilizando Python.

O objetivo do trabalho é implementar o jogo **Tetris** aplicando conceitos de orientação a objetos, mantendo a lógica do jogo separada das interfaces utilizadas para interação com o jogador.

## Integrantes

- Arthur Vinicius
- Estefane Pallaro
- Gustavo Augusto
- Helena Vinhote

## Professor

**Éfren Lopes de Souza**

## Sobre o projeto

O projeto implementa o funcionamento básico do Tetris em um tabuleiro de **10 colunas por 18 linhas**.

As sete peças tradicionais do jogo estão presentes:

- I
- J
- L
- O
- S
- T
- Z

O jogador pode mover, rotacionar e derrubar os tetriminos enquanto o sistema verifica colisões com as paredes, o chão e os blocos já posicionados.

Quando uma linha é completamente preenchida, ela é removida e as linhas superiores descem.

O jogo termina quando uma nova peça não consegue ser posicionada no topo do tabuleiro.

## Estrutura do projeto

```text
Tetris/
│
├── block.py
├── exceptions.py
├── tetriminos.py
├── tetris.py
├── tetris_terminal.py
├── tetris_gui.py
└── README.md
```

### `block.py`

Define a classe `Block`.

Cada objeto `Block` representa um dos quatro blocos que formam um tetrimino.

As coordenadas utilizadas são:

```text
x = coluna
y = linha
```

Caso seja criado um bloco com uma coordenada negativa, é lançada a exceção `InvalidBlockError`.

---

### `exceptions.py`

Contém as exceções utilizadas pelo projeto:

```python
GamerError
InvalidBlockError
InvalidRotationError
```

`GamerError` funciona como exceção base do jogo.

`InvalidBlockError` é utilizada para impedir blocos com coordenadas negativas.

`InvalidRotationError` é utilizada quando uma peça é iniciada com uma rotação diferente de:

```text
0
1
2
3
```

---

### `tetriminos.py`

Contém a classe abstrata `Tetrimino` e as sete peças do jogo:

```text
TetriminoI
TetriminoJ
TetriminoL
TetriminoO
TetriminoS
TetriminoT
TetriminoZ
```

Cada tetrimino possui quatro objetos `Block`.

A classe `Tetrimino` calcula automaticamente as quatro rotações possíveis de uma peça.

A rotação de 90° no sentido horário utiliza a transformação:

```text
(box_size - 1 - y, x)
```

Cada subclasse precisa definir apenas:

- sua forma original;
- sua cor.

---

### `tetris.py`

Contém a classe principal:

```python
Tetris
```

Ela controla as regras e o estado do jogo.

Entre suas responsabilidades estão:

- criar o tabuleiro;
- sortear os tetriminos;
- posicionar novas peças;
- mover para esquerda;
- mover para direita;
- mover para baixo;
- realizar rotação;
- realizar queda direta;
- detectar colisões;
- fixar peças;
- remover linhas completas;
- calcular pontuação;
- controlar o número de linhas;
- controlar o nível;
- detectar o fim de jogo.

A lógica do jogo permanece independente das interfaces.

---

### `tetris_terminal.py`

Interface para jogar diretamente pelo terminal.

O tabuleiro utiliza caracteres e códigos ANSI para mostrar as peças com suas respectivas cores.

### Controles

| Tecla | Ação |
|---|---|
| `A` | mover para esquerda |
| `D` | mover para direita |
| `S` | mover para baixo |
| `W` | girar |
| `X` | queda direta |
| `Q` | sair |

---

### `tetris_gui.py`

Interface gráfica desenvolvida utilizando **Tkinter**.

A interface possui um visual inspirado em consoles portáteis clássicos e apresenta:

- tabuleiro gráfico;
- peças coloridas;
- próxima peça;
- SCORE;
- LEVEL;
- LINES;
- botão de pausa;
- botão de reinício;
- queda automática das peças;
- sombra indicando a posição de queda da peça.

### Controles

| Tecla | Ação |
|---|---|
| `←` | mover para esquerda |
| `→` | mover para direita |
| `↓` | mover para baixo |
| `↑` | girar |
| `Espaço` | queda direta |

## Recursos adicionais

Além dos requisitos principais do trabalho, foram implementados alguns recursos adicionais.

### Ghost Piece

Uma sombra mostra onde a peça atual ficará caso seja derrubada.

### Próxima peça

A interface gráfica mostra antecipadamente o próximo tetrimino.

### Pontuação

Cada linha eliminada aumenta a pontuação do jogador.

### Level

O nível é calculado de acordo com a quantidade de linhas eliminadas.

### Pausa

A interface gráfica permite pausar e continuar o jogo.

### Easter Egg

Existe um pequeno easter egg escondido na interface gráfica.

Ele faz referência a jogos antigos e ao professor da disciplina.

## Conceitos de POO utilizados

Durante o desenvolvimento foram utilizados diferentes conceitos de Programação Orientada a Objetos.

### Encapsulamento

Atributos internos são protegidos e acessados através de propriedades.

Exemplo:

```python
@property
def x(self):
    return self._x
```

### Herança

As sete peças herdam da classe base:

```python
Tetrimino
```

### Classes abstratas

`Tetrimino` é uma classe abstrata e serve como estrutura para todas as peças.

### Polimorfismo

Cada tetrimino implementa sua própria forma e sua própria cor utilizando os mesmos métodos definidos pela classe base.

### Exceções

O projeto possui exceções específicas para situações inválidas durante a criação dos objetos.

## Requisitos

É necessário possuir **Python 3** instalado.

Para verificar:

```bash
python --version
```

ou:

```bash
python3 --version
```

O projeto utiliza apenas bibliotecas da própria instalação padrão do Python.

A interface gráfica utiliza:

```python
tkinter
```

## Executando pelo terminal

Dentro da pasta do projeto:

```bash
python tetris_terminal.py
```

Caso seu sistema utilize `python3`:

```bash
python3 tetris_terminal.py
```

## Executando a interface gráfica

```bash
python tetris_gui.py
```

ou:

```bash
python3 tetris_gui.py
```

## Arquitetura

O projeto foi dividido em duas partes principais.

### Modelo

```text
block.py
exceptions.py
tetriminos.py
tetris.py
```

Esses arquivos possuem as classes, objetos e regras responsáveis pelo funcionamento do Tetris.

### Interfaces

```text
tetris_terminal.py
tetris_gui.py
```

As interfaces apenas exibem o estado do jogo e enviam os comandos do jogador para a classe `Tetris`.

Dessa forma, a mesma lógica pode ser utilizada tanto no terminal quanto na interface gráfica.

## Objetivo acadêmico

O projeto foi desenvolvido com o objetivo de aplicar na prática conceitos estudados durante a disciplina de Programação Orientada a Objetos, principalmente:

- classes;
- objetos;
- atributos;
- métodos;
- encapsulamento;
- propriedades;
- herança;
- abstração;
- polimorfismo;
- exceções;
- modularização.

---

**Universidade Federal do Oeste do Pará — UFOPA**

**Bacharelado em Inteligência Artificial**

**Programação Orientada a Objetos**

**Obrigado, Professor!**
