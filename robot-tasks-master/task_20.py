#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    move_right()
    turn = move_right
    for i in range(12):
        for j in range(26):
            fill_cell()
            turn()
        fill_cell()
        if turn == move_right:
            turn = move_left
        else:
            turn = move_right
        move_down()


if __name__ == '__main__':
    run_tasks()
