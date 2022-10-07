import msvcrt
import os
from collections import deque
from random import randint

rows = 15
cols = 35

snake = deque()
snake.append((12,7))
apple = (3,7)
game_going = True


def game_over():
    global game_going
    game_going = False


def draw():
    matrix = []
    for y in range(rows):
        row = []
        for x in range(cols):
            if (x, y) in snake:
                row.append("▓▓")
            elif (x,y) == apple:
                row.append("@@")
            else:
                row.append("░░")
        matrix.append(row)
    for i in range(len(matrix)):
        print(*matrix[i], sep="")
    print(f"Points: {len(snake)} ",end="")


def snake_move(dir):
    global apple
    if dir == "left":
        if snake[0][0] - 1 < 0:
            snake.appendleft((cols-1, snake[0][1]))
        else:
            snake.appendleft((snake[0][0] - 1, snake[0][1]))
    elif dir == "up":
        if snake[0][1] - 1 < 0:
            snake.appendleft((snake[0][0], rows - 1))
        else:
            snake.appendleft((snake[0][0], snake[0][1] - 1))
    elif dir == "right":
        if snake[0][0] + 1 > cols - 1:
            snake.appendleft((0, snake[0][1]))
        else:
            snake.appendleft((snake[0][0] + 1, snake[0][1]))
    elif dir == "down":
        if snake[0][1] + 1 > rows - 1:
            snake.appendleft((snake[0][0], 0))
        else:
            snake.appendleft((snake[0][0], snake[0][1] + 1))
    if snake.count(snake[0]) > 1:
        game_over()
    if snake[0] != apple:
        snake.pop()
    else:
        apple = (randint(0, cols - 1), randint(0, rows - 1))


print("Welcome to Snake Game in Python Console! For game to work in pycharm, do this")
print("Right button on text editor -> Modify Run Configuration -> Emulate terminal in output console")
print("Make sure you resize the output window so that it fits the entire playfield!")
print("Game is controlled with W, A, S, D for movement. Press any of those keys to start!")

while game_going:
    char = msvcrt.getch().decode("utf-8")
    os.system('cls')
    if char == "a":
        snake_move("left")
    elif char == "w":
        snake_move("up")
    elif char == "d":
        snake_move("right")
    elif char == "s":
        snake_move("down")
    draw()
print("\nOoops. You bit yourself. GAME OVER")