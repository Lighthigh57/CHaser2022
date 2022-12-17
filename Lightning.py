import random
import Command

# PlayerName = Light

priority = []
"Direction priority"

run = None
"instance of Command class"

last = 0
"last direction"

Check_Zone = 0
"Interval of Map_Check"

Safety_Heart = 0
"ModeChange border"

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
    global run

    y = 1 if target < 3 else 7  # Where this is for Y
    x = 3 if target == 0 or target == 6 else 5  # Where this is for X

    if com == "avoid":  # if this is enemy
        run.move("put", x if random.randint(0, 1) == 0 else y)

    else:  # if this is item
        priority[x] += 1
        priority[y] += 1


def around_check(ready_value):
    for i in range(0, 9):
        if ready_value[i] == 1:  # Can I put there now?
            if i % 2 == 0:
                solve_diagonal(i, "avoid")
                did_command = True
            else:
                _ = run.move("put", i)
                break


def trap_check(dir: int):
    result = run.move("look", dir)
    if result[4] == 2:
        priority[dir] = -2
    else:
        priority[dir] += 2


def checker(current, ready_value) -> int:
    """敵いたら潰します(笑)"""
    global run
    global priority
    global item

    did_command = False
    for i in range(0, 9):  # Safe Command
        if ready_value[i] == 3:  # Can I get now?
            if i % 2 == 1:
                if i == 1 and ready_value[0] == ready_value[2] == 2:
                    if not run.ready_OK:
                        ready_value = run.get_ready()
                        around_check(ready_value)
                    trap_check(1)
                elif (i == 3 or i == 5) and ready_value[i-3] == ready_value[i+3] == 2:
                    if not run.ready_OK:
                        ready_value = run.get_ready()
                        around_check(ready_value)
                    trap_check(i)
                elif i == 7 and ready_value[6] == ready_value[2] == 8:
                    if not run.ready_OK:
                        ready_value = run.get_ready()
                        around_check(ready_value)
                    trap_check(6)
                else:
                    priority[i] += 2
            else:
                solve_diagonal(i, "get")
    # Danger Command
    for i in range(0, 9):
        if ready_value[i] == 1:  # Can I put there now?
            if i % 2 == 0:
                solve_diagonal(i, "avoid")
                did_command = True
            else:
                _ = run.move("put", i)
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

    goto = 0
    if not did_command:
        if p_max < 0:  # I should go to Danger Zone!!!
            run.move("look", 1)
        else:
            goto = now_max[random.randint(0, len(now_max) - 1)]
            _ = run.move("walk", goto)

    return goto


if __name__ == "__main__":
    run = Command.Command()  # Set Command instance
    main()
