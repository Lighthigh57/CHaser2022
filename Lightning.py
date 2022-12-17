import random
import Command

# PlayerName = Light

priority = []
"""priority = 優先度"""

run = None
"""instance of Command class"""

last = 0
"""last direction"""

Check_Zone = 0
"""Interval of Map_Check"""

Safety_Heart = 0
"""ModeChange border"""

item = 0


def main():
    global run
    global priority

    turn = 0
    dir_last = 0
    while True:
        priority = [0 for _ in range(9)]
        dir_last = checker(dir_last, run.get_ready())
        turn += 1


def solve_diagonal(target, com):
    """斜めに物が見えた時の処理"""
    global priority
    y = 1 if target < 3 else 7  # Where this is for Y
    x = 3 if target == 0 or target == 6 else 5  # Where this is for X

    if com == "avoid":  # if this is enemy
        priority[x] = -2
        priority[y] = -2
    else:  # if this is item
        priority[x] += 1
        priority[y] += 1


def checker(current, ready_value) -> int:
    """敵いたら潰します(笑)"""
    global run
    global priority
    global item

    for i in range(0, 9):  # Safe Command
        if ready_value[i] == 3:  # Can I get now?
            if i % 2 == 1:
                priority[i] += 2
            else:
                solve_diagonal(i, "get")
    # Danger Command
    for i in range(0, 9):
        if ready_value[i] == 1:  # Can I put there now?
            if i % 2 == 0:
                solve_diagonal(i, "avoid")
            else:
                run.move("put", i)
                break
        if ready_value[i] == 2:  # There is a block?
            priority[i] = -2

    p_max = priority[1]  # maximum value
    now_max = [1]  # direction index who it has maximum

    # find maximum value in priority list(look like search sort)
    for i in range(3, 8, 2):
        if p_max < priority[i]:
            p_max = priority[i]
            now_max = [i]
        elif p_max == priority[i]:
            now_max += [i]

    if len(now_max) != 1:  # remove last place
        if (current == 1) and (7 in now_max):
            now_max.remove(7)
        elif (current == 3) and (5 in now_max):
            now_max.remove(5)
        elif (current == 5) and (3 in now_max):
            now_max.remove(3)
        elif (current == 7) and (1 in now_max):
            now_max.remove(1)
    if p_max < 0:  # I should go to Danger Zone!!!
        run.move("look", 1)
        return 0
    else:
        goto = now_max[random.randint(0, len(now_max) - 1)]
        run.move("walk", goto)
    return goto


if __name__ == "__main__":
    run = Command.Command()  # Set Command instance
    main()
