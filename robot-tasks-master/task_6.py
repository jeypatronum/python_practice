#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_3():
    while not wall_is_beneath():
        move_right(1)
    while True:
        if wall_is_beneath():
            move_right(1)
        else:
            break


if __name__ == '__main__':
    run_tasks()
