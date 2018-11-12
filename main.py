import random
import time
from threading import *
from tkinter import *

main_window = Tk()
main_window.resizable(False, False)
main_window.geometry('600x600+300+200')

size = 10
labels = {}
snakeHead = [int(size / 2), int(size / 2)]
body = [0, int(size / 2), int(size / 2)]
food = [0, 0, 'Havenot']
step = 0
inc = [False, 0, 0]
direction = 'UP'
work = True


def speed_timer():
    global direction
    global inc
    global body
    global work

    while work:
        speed = body[0] + 1
        sleep_time = float(1 / speed)
        time.sleep(sleep_time)
        tick()
        move_to(direction)
        if inc[0]:
            print('start incSize')
            i = inc[1]
            j = inc[2]
            if labels.get((i, j))['text'] == 'o':
                labels.get((i, j))['text'] = 'O'
            if labels.get((i, j))['text'] == '+':
                labels.get((i, j))['text'] = 'X'
            if labels.get((i, j))['text'] == '.':
                labels.get((i, j))['text'] = '+'
                body[0] += 1
                body.append(i)
                body.append(j)
                inc[0] = False
                print('stop incSize')


def create_field(field_size):
    global labels

    for i in range(field_size):
        for j in range(field_size):
            label = Label(main_window, text='.', bg='white')
            label.place(x=10 * i, y=10 * j, width=10, height=10)
            labels[i, j] = label


def place_snake_body():
    global labels
    global body

    if body[0] != 0:
        labels.get((body[1], body[2]))['text'] = '+'
        labels.get((body[-2], body[-1]))['text'] = '.'
        for x in range(1, body[0] + 1):
            i = body[-2 * x - 2]
            j = body[-2 * x - 1]
            body[-2 * x] = i
            body[-2 * x + 1] = j


def tick():
    global step

    step += 1
    if step == 10:
        step = 0
        if food[2] == 'Havenot':
            place_food()


def place_food():
    global size
    global food
    global inc

    i = random.randint(0, size)
    j = random.randint(0, size)
    food = [i, j, 'Have']
    try:
        labels.get((food[0], food[1]))['text'] = 'F'
        inc[0] = True
        inc[1] = i
        inc[2] = j
    except TypeError:
        food[2] = 'Havenot'


def up_arrow_key(event):
    global direction

    direction = 'UP'


def down_arrow_key(event):
    global direction

    direction = 'DOWN'


def left_arrow_key(event):
    global direction

    direction = 'LEFT'


def right_arrow_key(event):
    global direction

    direction = 'RIGHT'


def return_arrow_key(event):
    global inc

    inc[0] = False


def place_snake_head(snake_head):
    global body
    global labels
    global size

    if snake_head[0] < 0:
        snake_head[0] = size - 1
    if snake_head[0] > size - 1:
        snake_head[0] = 0
    if snake_head[1] < 0:
        snake_head[1] = size - 1
    if snake_head[1] > size - 1:
        snake_head[1] = 0
    labels.get((snake_head[0], snake_head[1]))['text'] = 'o'


def move_to(current_direction):
    global snakeHead
    global labels
    global food
    global size
    global work

    i = snakeHead[0]
    j = snakeHead[1]

    if current_direction == 'UP':
        labels.get((i, j))['text'] = '.'
        if (j - 1) < 0:
            jtmp = size - 1
        else:
            jtmp = j - 1
        if labels.get((i, jtmp))['text'] == 'F':
            food[2] = 'Havenot'
        if (
            labels.get((i, jtmp))['text'] == 'X' or
            labels.get((i, jtmp))['text'] == '+'
        ):
            print('Game Over')
            work = False
        body[1] = i
        body[2] = j
        snakeHead[1] -= 1
        place_snake_head(snakeHead)
        place_snake_body()

    if current_direction == 'DOWN':
        labels.get((i, j))['text'] = '.'
        if (j + 1) > size - 1:
            jtmp = 0
        else:
            jtmp = j + 1
        if labels.get((i, jtmp))['text'] == 'F':
            food[2] = 'Havenot'
        if (
            labels.get((i, jtmp))['text'] == 'X' or
            labels.get((i, jtmp))['text'] == '+'
        ):
            print('Game Over')
            work = False
        body[1] = i
        body[2] = j
        snakeHead[1] += 1
        place_snake_head(snakeHead)
        place_snake_body()

    if current_direction == 'LEFT':
        labels.get((i, j))['text'] = '.'
        if (i - 1) < 0:
            itmp = size - 1
        else:
            itmp = i - 1
        if labels.get((itmp, j))['text'] == 'F':
            food[2] = 'Havenot'
        if (
            labels.get((itmp, j))['text'] == 'X' or
            labels.get((itmp, j))['text'] == '+'
        ):
            print('Game Over')
            work = False
        body[1] = i
        body[2] = j
        snakeHead[0] -= 1
        place_snake_head(snakeHead)
        place_snake_body()

    if current_direction == 'RIGHT':
        labels.get((i, j))['text'] = '.'
        if (i + 1) > size - 1:
            itmp = 0
        else:
            itmp = i + 1
        if labels.get((itmp, j))['text'] == 'F':
            food[2] = 'Havenot'
        if (
            labels.get((itmp, j))['text'] == 'X' or
            labels.get((itmp, j))['text'] == '+'
        ):
            print('Game Over')
            work = False
        body[1] = i
        body[2] = j
        snakeHead[0] += 1
        place_snake_head(snakeHead)
        place_snake_body()


main_window.bind('<Up>', up_arrow_key)
main_window.bind('<Down>', down_arrow_key)
main_window.bind('<Left>', left_arrow_key)
main_window.bind('<Right>', right_arrow_key)
main_window.bind('<Return>', return_arrow_key)

create_field(size)

mainT = Thread(target=speed_timer)
mainT.setDaemon(True)
mainT.start()

main_window.mainloop()
