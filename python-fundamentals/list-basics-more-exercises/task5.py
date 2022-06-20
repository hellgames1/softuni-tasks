""""
Task 5 - Tic-Tac-Toe
"""
row_1 = input().split()
row_2 = input().split()
row_3 = input().split()

row_1 = [int(x) for x in row_1]
row_2 = [int(x) for x in row_2]
row_3 = [int(x) for x in row_3]
field = row_1 + row_2 + row_3

def check_row(which_row, check_player):
    global field
    check_one = field[which_row * 3] == check_player
    check_two = field[which_row * 3 + 1] == check_player
    check_tre = field[which_row * 3 + 2] == check_player
    return check_one and check_two and check_tre

def check_col(which_col, check_player):
    global field
    check_one = field[which_col] == check_player
    check_two = field[which_col + 3] == check_player
    check_tre = field[which_col + 6] == check_player
    return check_one and check_two and check_tre

def check_diag(check_player):
    global field
    check_one = field[0] == check_player and field[4] == check_player and field[8] == check_player
    check_two = field[2] == check_player and field[4] == check_player and field[6] == check_player
    return check_one or check_two

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
    print("First player won")
elif player_won == 2:
    print("Second player won")
else:
    print("Draw!")