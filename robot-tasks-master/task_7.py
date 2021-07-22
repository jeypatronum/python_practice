#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    while not wall_is_beneath():
        move_down(1)
    k = 0
    while wall_is_beneath():
        move_right()
        k += 1
    move_down(1)
    move_left(k)


if __name__ == '__main__':
    run_tasks()
