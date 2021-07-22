#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
    turn = move_right
    k = False
    while wall_is_above() and wall_is_beneath():
        if wall_is_on_the_right():
            if k:
                break
            turn = move_left
        if wall_is_on_the_left():
            k = True
            turn = move_right
        turn()

    if not k:
        while not wall_is_above():
            move_up()
        while not wall_is_on_the_left():
            move_left()


if __name__ == '__main__':
    run_tasks()
