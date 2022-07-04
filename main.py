
game = [[" "," "," "],
        [" "," "," "],
        [" "," "," "]]


def print_board():
    print("   1     2     3 ")
    print(f"1  {game[0][0]}  |  {game[0][1]}  |  {game[0][2]} ")
    print("  ---------------")
    print(f"2  {game[1][0]}  |  {game[1][1]}  |  {game[1][2]} ")
    print("  ---------------")
    print(f"3  {game[2][0]}  |  {game[2][1]}  |  {game[2][2]} ")
    return

def player_turn(player):
    global game
    global running
    column_choice = int(input(f"{player}: What column would you like to place your X?(1,2,3) ")) - 1
    row_choice = int(input(f"{player}: What row would you like to place your X?(1,2,3) ")) - 1
    player_mark = ""
    if player == "Player1":
        player_mark = "X"
    elif player == "Player2":
        player_mark = "O"

    try:
        if game[row_choice][column_choice] == " ":
            game[row_choice][column_choice] = player_mark
        else:
            print("Invalid entry")
            player_turn(player)
    except:
        print("Invalid entry")
        player_turn(player)

    return


def check_winner(player, player_mark):
    # check rows
    if game[0] == [player_mark, player_mark, player_mark] \
            or game[1] == [player_mark, player_mark, player_mark] \
            or game[2] == [player_mark, player_mark, player_mark]:
        print(f"{player} WINS!")
        return True

    # check columns
    elif game[0][0] == player_mark and game[1][0] == player_mark and game[2][0] == player_mark\
            or game[0][1] == player_mark and game[1][1] == player_mark and game[2][1] == player_mark\
            or game[0][2] == player_mark and game[1][2] == player_mark and game[2][2] == player_mark:
        print(f"{player} WINS!")
        return True

    # check diagonals
    elif game[0][0] == player_mark and game[1][1] == player_mark and game[2][2] == player_mark\
            or game[0][2] == player_mark and game[1][1] == player_mark and game[2][0] == player_mark:
        print(f"{player} WINS!")
        return True

    # check stalemate
    elif " " not in game[0] and " " not in game[1] and " " not in game[2]:
        print("Stalemate")
        return True
    return False


def reset_game():
    global game
    game = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]
    return

running = True

while running:
    print_board()
    player_turn("Player1")
    if check_winner("Player1", "X"):
        play_again = input("Play again?(Y/N) ").lower()
        if play_again == "n":
            running = False
            break
        else:
            reset_game()
    print_board()
    player_turn("Player2")
    if check_winner("Player1", "X"):
        play_again = input("Play again?(Y/N) ").lower()
        if play_again == "n":
            running = False
            break
        else:
            reset_game()



