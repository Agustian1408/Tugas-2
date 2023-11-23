def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():#diulangi selama tidak digoal
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else: turn_left()