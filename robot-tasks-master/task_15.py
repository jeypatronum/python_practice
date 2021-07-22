#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    if wall_is_above():
        turn_ud = move_down
    elif wall_is_beneath():
        turn_ud = move_up

    if wall_is_on_the_right():
        turn_lr = move_left
    elif wall_is_on_the_left():
        turn_lr = move_right

    for i in range(9):
        turn_ud()
        turn_lr()


if __name__ == '__main__':
    run_tasks()
