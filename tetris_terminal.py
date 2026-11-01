# Interface de terminal

from tetris import Tetris

def colored_board(game: Tetris) -> str:
    board = []

    for row in range(game.height):
        row_str = []

        for col in range(game.width):
            color = game.color_at(col, row)

            if color is None:
                row_str.append("  ")

            else:
                r = int(color[1:3], 16)
                g = int(color[3:5], 16)
                b = int(color[5:7], 16)

                row_str.append(
                    f"\033[38;2;{r};{g};{b}m██\033[0m"
                )

        board.append(''.join(row_str))

    return '\n'.join(board)

def bordas(game: Tetris):

    print("\033[2J\033[H", end="")

    largura = game.width * 2

    print("╔" + "=" * largura + "╗")

    for linha in colored_board(game).split("\n"):
        print("║" + linha + "║")

    print("╚" + "=" * largura + "╝")

    print()
    print("A - esquerda")
    print("D - direita")
    print("S - descer")
    print("W - girar")
    print("X - queda")
    print("Q - sair")
    

def main() -> None:
    game = Tetris()

    while not game.game_over:
        bordas(game)

        comando = input("> ").lower()

        match comando:
            case 'a':
                game.move_left()
            case 'd':
                game.move_right()
            case 's':
                game.move_down()
            case 'w':
                game.rotate()
            case 'x' | '':
                game.drop()
            case 'q':
                break

if __name__== '__main__':
    main()