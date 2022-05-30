import os, random
print(f"Welcome to Tic-Tac-Toe. You play with X, while the both plays with O. Here are the possible positions. After each move of the bot, please choose which position you want to place the X, and press Enter\n     │1│2│3│\n     │4│5│6│\n     │7│8│9│\n\nclick on the terminal and press Enter to continue...")
input()
first_pos = "bot"
score=[0,0]

def clear():
    #clearing the console
    #THIS SCRIPT DOESN'T WORK IN PYCHARM IF YOU HAVEN'T SELECTED "EMULATE TERMINAL IN OUTPUT CONSOLE"
    #TO GET THERE, RIGHT CLICK ON THE CODE AND PRESS "MODIFY RUN CONFIGURATION"
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def check_row(which_row, check_player):
    #check if a row is filled with the same
    global field
    check_one = field[which_row * 3] == check_player
    check_two = field[which_row * 3 + 1] == check_player
    check_tre = field[which_row * 3 + 2] == check_player
    return check_one and check_two and check_tre

def check_col(which_col, check_player):
    #check if a column is filled with the same
    global field
    check_one = field[which_col] == check_player
    check_two = field[which_col + 3] == check_player
    check_tre = field[which_col + 6] == check_player
    return check_one and check_two and check_tre

def check_diag(check_player):
    #check the diagonals
    global field
    check_one = field[0] == check_player and field[4] == check_player and field[8] == check_player
    check_two = field[2] == check_player and field[4] == check_player and field[6] == check_player
    return check_one or check_two

def draw_field():
    #draw the game field
    #the symbol   means empty space
    print("\n   Tic-Tac-Toe\n")
    for symbol, bs in enumerate(field):
        if field[symbol] == 0:
            field_display[symbol] = " "
        elif field[symbol] == 1:
            field_display[symbol] = "X"
        elif field[symbol] == 2:
            field_display[symbol] = "O"
    print(f"     │{field_display[0]}│{field_display[1]}│{field_display[2]}│\n     │{field_display[3]}│{field_display[4]}│{field_display[5]}│     player points: {score[0]}\n     │{field_display[6]}│{field_display[7]}│{field_display[8]}│     bot points: {score[1]}")

def check_winner(keep_score):
    global first_pos
    #check if someone wins and return True or False
    #keep_score shows whether you should keep score, because this function is also called "hypothetically" when the bot checks if it might win or lose next round
    #in which case don't affect the score yet
    player_won = -1
    for j in range(1, 3):
        for i in range(3):
            if check_row(i, j):
                player_won = j
                break
            if check_col(i, j):
                player_won = j
                break
        if check_diag(j):
            player_won = j
            break
    if player_won == 1:
        print("\nThe player wins! Press Enter to try again. Next time the bot is first.")
        first_pos = "bot"
        if keep_score:
            score[0] += 1
        return True
    elif player_won == 2:
        print("\nThe bot wins! Press Enter to try again. Next time the player is first.")
        first_pos = "player"
        if keep_score:
            score[1] += 1
        return True
    else:
#if it's a draw, the next first round is randomly given
        if not 0 in field:
            if random.random()>=0.5:
                first_pos = "player"
            else:
                first_pos = "bot"
            print(f"\nDraw! Press Enter to try again. Next time the {first_pos} is first.")
            return True
        else:
            if keep_score:
                print("\n" + message + ": ", end="")
            return False

# bot's "AI"
def bot_move():
    valid_move = False
    winning_move = False
    #attack mode
    #here it checks if there's a move which can win him the game (like 2 out of 3 Os placed in a row/col/diag)
    for i in range(9):
        if field[i] != 0:
            continue
        else:
            field[i] = 2
            if check_winner(False) and random.random() >= 0.1: #if there's such a move, there's a 10% chance he won't notice
                winning_move = True
                break
            else:
                field[i] = 0
    #defense mode
    #if it hasn't found such a move, here it checks if there's a move which IF it does NOT make, YOU might win the game
    if winning_move != True:
        for i in range(9):
            if field[i] != 0:
                continue
            else:
                field[i] = 1
                if check_winner(False) and random.random() >= 0.1: #if there's such a move, there's a 10% chance he won't notice
                    field[i] = 2
                    winning_move = True
                    break
                else:
                    field[i] = 0

    #if it hasn't figured out anything, make a random move
    if winning_move != True:
        while not valid_move:
            move_position = random.randint(1, 9)
            if field[move_position-1] == 0:
                field[move_position - 1] = 2
                valid_move = True

#main loop
while True: # this loop represents one round
    #clearing the field from last round
    field = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    field_display = ["", "", "", "", "", "", "", "", ""]
    message = "Choose a position"
    if first_pos == "bot":
        bot_move()
    while True: # this loop represents one move
        clear() #clear the terminal
        draw_field() #draw the field
        if not check_winner(True): #if no one has won, wait for player move
            action=input()
            #here I make sure you can't enter BS and break the code
            if action!="1" and action!="2" and action!="3" and action!="4" and action!="5" and action!="6" and action!="7" and action!="8" and action!="9":
                message = "Such a position doesn't exist. Try again"
            elif field[int(action)-1] != 0:
                message = "That position is occupied! Try again"
            else:
            #if it passes the checks and the move is possible, do it
                message = "Choose a position"
                field[int(action) - 1] = 1
                #if this move hasn't won the player the game, do bot's move
                if not check_winner(False):
                    bot_move()
        else: #if someone has won, wait for input and do the next iteration of the "game round" loop
            input()
            break
