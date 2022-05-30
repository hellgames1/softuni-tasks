import os, random
print(f"Добре дошли в играта Морски Шах. Вие играете с X, а ботът с O. Ето възможните позиции. След всяко действие на бота, трябва да въведете на коя позиция искате да сложите X и да натиснете Enter\n     │1│2│3│\n     │4│5│6│\n     │7│8│9│\n\nкликнете върху конзолата и натиснете Enter за да започнете")
input()
first_pos = "бот"
score=[0,0]

def clear():
    #изчистване на конзолата
    #ТОЗИ СКРИПТ НЯМА ДА РАБОТИ В PYCHARM АКО НЕ СТЕ ИЗБРАЛИ "EMULATE TERMINAL IN OUTPUT CONSOLE" В ОПЦИИТЕ
    #ЗА ДА ДОСТИГНЕТЕ ДО ТАМ, НАТИСНЕТЕ ДЕСЕН БУТОН НА КОДА И ИЗБЕРЕТЕ MODIFY RUN CONFIGURATION
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def check_row(which_row, check_player):
    #провери дали някой ред е запълнен от едни и същи
    global field
    check_one = field[which_row * 3] == check_player
    check_two = field[which_row * 3 + 1] == check_player
    check_tre = field[which_row * 3 + 2] == check_player
    return check_one and check_two and check_tre

def check_col(which_col, check_player):
    #провери дали някоя колона е запълнена от едни и същи
    global field
    check_one = field[which_col] == check_player
    check_two = field[which_col + 3] == check_player
    check_tre = field[which_col + 6] == check_player
    return check_one and check_two and check_tre

def check_diag(check_player):
    #провери дали някой диагонал е запълнен от едни и същи
    global field
    check_one = field[0] == check_player and field[4] == check_player and field[8] == check_player
    check_two = field[2] == check_player and field[4] == check_player and field[6] == check_player
    return check_one or check_two

def draw_field():
    #изрисувай играта в конзолата
    #символът   означава празно пространство
    print("\n   Морски Шах\n")
    for symbol, bs in enumerate(field):
        if field[symbol] == 0:
            field_display[symbol] = " "
        elif field[symbol] == 1:
            field_display[symbol] = "X"
        elif field[symbol] == 2:
            field_display[symbol] = "O"
    print(f"     │{field_display[0]}│{field_display[1]}│{field_display[2]}│\n     │{field_display[3]}│{field_display[4]}│{field_display[5]}│     точки на играча: {score[0]}\n     │{field_display[6]}│{field_display[7]}│{field_display[8]}│     точки на бота: {score[1]}")

def check_winner(keep_score):
    global first_pos
    #провери дали някой бие и върни True или False
    #keep_score показва дали да се променят точките, тей като тази функция се извиква от бота когато проверява какъв може да е следващия ход
    #в такъв случай не искам да променя точките
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
        print("\nИграчът печели! Натиснете Enter за да опитате отново. Следващия път ботът е първи.")
        first_pos = "бот"
        if keep_score:
            score[0] += 1
        return True
    elif player_won == 2:
        print("\nБотът печели! Натиснете Enter за да опитате отново. Следващия път играчът е първи.")
        first_pos = "играч"
        if keep_score:
            score[1] += 1
        return True
    else:
#ако е равенство, в следващия рунд първия ход е произволен
        if not 0 in field:
            if random.random()>=0.5:
                first_pos = "играч"
            else:
                first_pos = "бот"
            print(f"\nРавенство! Натиснете Enter за да опитате отново. Следващия път {first_pos}ът е първи.")
            return True
        else:
            if keep_score:
                print("\n" + message + ": ", end="")
            return False

#"изкуствения интелект" на бота
def bot_move():
    valid_move = False
    winning_move = False
    #режим АТАКА
    #тук проверява ако има движение, което ще му спечели играта (примерно 2 от 3 кръгчета в един ред или диагонал са сложени и може да сложи третото)
    for i in range(9):
        if field[i] != 0:
            continue
        else:
            field[i] = 2
            if check_winner(False) and random.random() >= 0.1: #ако има такова движение, има 10% шанс да не го "забележи"
                winning_move = True
                break
            else:
                field[i] = 0
    #режим ЗАЩИТА
    #ако не е намерил такова движение, проверява ако има движение, което ако НЕ направи, ще може ТИ да спечелиш играта в следващия ход
    if winning_move != True:
        for i in range(9):
            if field[i] != 0:
                continue
            else:
                field[i] = 1
                if check_winner(False) and random.random() >= 0.1: #ако има такова движение, има 10% шанс да не го "забележи"
                    field[i] = 2
                    winning_move = True
                    break
                else:
                    field[i] = 0

    #ако не е открил такива движения, прави произволно
    if winning_move != True:
        while not valid_move:
            move_position = random.randint(1, 9)
            if field[move_position-1] == 0:
                field[move_position - 1] = 2
                valid_move = True

#главен цикъл
while True: # този цикъл обхваща един рунд
    #изчистване на полето от миналия рунд
    field = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    field_display = ["", "", "", "", "", "", "", "", ""]
    message = "Изберете позиция"
    if first_pos == "бот":
        bot_move()
    while True: # този цикъл обхваща един ход
        clear() #изчисти конзолата
        draw_field() #изрисувай полето
        if not check_winner(True): #ако никой не е спечелил, изчакай действие
            action=input()
            #тук отстранявам всички възможни глупости, които може да въведе някой и да счупи кода
            if action!="1" and action!="2" and action!="3" and action!="4" and action!="5" and action!="6" and action!="7" and action!="8" and action!="9":
                message = "Не съществува такава позиция! Опитайте пак"
            elif field[int(action)-1] != 0:
                message = "Тази позиция е заета! Опитайте пак"
            else:
            #ако мине проверките и ходът е възможен, прави го
                message = "Изберете позиция"
                field[int(action) - 1] = 1
                #ако играчът не е спечелил играта с този ход, следва хода на бота
                if not check_winner(False):
                    bot_move()
        else: #ако някой е спечелил, изчакай Enter и излез от цикъла за ходовете и завърти за следващия рунд
            input()
            break
