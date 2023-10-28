import random

with open("logo.txt") as file:
    logo = file.read()
    print(logo)

pos = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

game_over = False
with_computer = False
draw = 0

play_style = input("\nIf you want to play with your friend enter '1'\nIf you want to play with computer enter '2':\n")

if play_style == "2":
    with_computer = True


def create_board():
    grid = "     \n" \
           f"              | {pos[0]} | {pos[1]} | {pos[2]} |\n" \
           f"              | {pos[3]} | {pos[4]} | {pos[5]} |\n" \
           f"              | {pos[6]} | {pos[7]} | {pos[8]} |"

    print("")
    print("           Player 1 symbol = X")
    print("           Player 2 symbol = O")
    print(grid)


def game():
    global game_over
    global draw
    while not game_over:
        p1_move = input("\nPlayer 1 select number:\n")
        if p1_move == pos[int(p1_move) - 1]:
            pos[int(p1_move) - 1] = "X"
            draw += 1

            if pos[0] == "X" and pos[1] == "X" and pos[2] == "X":
                game_over = True
                create_board()
                print("              PLAYER 1 WON!")
            elif pos[3] == "X" and pos[4] == "X" and pos[5] == "X":
                game_over = True
                create_board()
                print("              PLAYER 1 WON!")
            elif pos[6] == "X" and pos[7] == "X" and pos[8] == "X":
                game_over = True
                create_board()
                print("              PLAYER 1 WON!")
            elif pos[0] == "X" and pos[3] == "X" and pos[6] == "X":
                game_over = True
                create_board()
                print("              PLAYER 1 WON!")
            elif pos[1] == "X" and pos[4] == "X" and pos[7] == "X":
                game_over = True
                create_board()
                print("              PLAYER 1 WON!")
            elif pos[2] == "X" and pos[5] == "X" and pos[8] == "X":
                game_over = True
                create_board()
                print("              PLAYER 1 WON!")
            elif pos[0] == "X" and pos[4] == "X" and pos[8] == "X":
                game_over = True
                create_board()
                print("              PLAYER 1 WON!")
            elif pos[2] == "X" and pos[4] == "X" and pos[6] == "X":
                game_over = True
                create_board()
                print("              PLAYER 1 WON!")

            elif draw == 9:
                game_over = True
                create_board()
                print("                  DRAW")
                break

            else:
                create_board()

                if with_computer:
                    try_again = True
                    while try_again:
                        p2_move = random.choice(pos)
                        if p2_move != "X" and p2_move != "O":
                            try_again = False
                else:
                    p2_move = input("\nPlayer 2 select number:\n")

                if p2_move == pos[int(p2_move) - 1]:
                    pos[int(p2_move) - 1] = "O"
                    draw += 1
                    if pos[0] == "O" and pos[1] == "O" and pos[2] == "O":
                        game_over = True
                        create_board()
                        print("              PLAYER 2 WON!")
                    elif pos[3] == "O" and pos[4] == "O" and pos[5] == "0":
                        game_over = True
                        create_board()
                        print("              PLAYER 2 WON!")
                    elif pos[6] == "O" and pos[7] == "O" and pos[8] == "O":
                        game_over = True
                        create_board()
                        print("              PLAYER 2 WON!")
                    elif pos[0] == "O" and pos[3] == "O" and pos[6] == "O":
                        game_over = True
                        create_board()
                        print("              PLAYER 2 WON!")
                    elif pos[1] == "O" and pos[4] == "O" and pos[7] == "O":
                        game_over = True
                        create_board()
                        print("              PLAYER 2 WON!")
                    elif pos[2] == "O" and pos[5] == "O" and pos[8] == "O":
                        game_over = True
                        create_board()
                        print("              PLAYER 2 WON!")
                    elif pos[0] == "O" and pos[4] == "O" and pos[8] == "O":
                        game_over = True
                        create_board()
                        print("              PLAYER 2 WON!")
                    elif pos[2] == "O" and pos[4] == "O" and pos[6] == "O":
                        game_over = True
                        create_board()
                        print("              PLAYER 2 WON!")
                    else:
                        create_board()
                        game()


create_board()
game()
