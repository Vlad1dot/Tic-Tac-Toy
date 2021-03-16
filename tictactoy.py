digit_list = [str(x) for x in range(1,10)]
xo = "XO"

def print_field(x):
    print("---------")
    print("| {} {} {} |".format(x[0], x[1], x[2]))
    print("| {} {} {} |".format(x[3], x[4], x[5]))
    print("| {} {} {} |".format(x[6], x[7], x[8]))
    print("---------")

def game_status(x):
    temporary_wins = []
    if abs(x.count("X") - x.count("O")) > 1:
        return "Impossible"
    if x[0] == x[1] == x[2] and x[0] in xo:
        temporary_wins.append(x[0])
    if x[3] == x[4] == x[5] and x[3] in xo:
        temporary_wins.append(x[3])
    if x[6] == x[7] == x[8] and x[6] in xo:
        temporary_wins.append(x[6])
    if x[0] == x[3] == x[6] and x[0] in xo:
        temporary_wins.append(x[6])
    if x[1] == x[4] == x[7] and x[1] in xo:
        temporary_wins.append(x[1])
    if x[2] == x[5] == x[8] and x[2] in xo:
        temporary_wins.append(x[2])
    if x[0] == x[4] == x[8] and x[0] in xo:
        temporary_wins.append(x[0])
    if x[6] == x[4] == x[2] and x[6] in xo:
        temporary_wins.append(x[6])
    if len(temporary_wins) == 1:
        return temporary_wins[0] + " wins"
    elif len(temporary_wins) > 1:
        return "Impossible"
    if (x.count("X") + x.count("O")) == 9:
        return "Draw"
    return "Game not finished"

def check_cell_bad(x_, y_, position):
    locate = (x_ - 1) * 3 + y_ - 1
    if position[locate] == "O" or position[locate] == "X":
        return True
    else:
        return False

def move_position(x_, y_, position, choice):
    locate = (x_ - 1) * 3 + y_ - 1
    next_position = position
    next_position[locate] = "X" if choice == True else "O"
    return next_position

print('Welcome to Tic-Tac-Toy!')
position = [" " for _ in range(9)]
print_field(position)
gamer = True
while True:
    while True:
        move_ = input("Enter the coordinates: ").split()
        if len(move_) != 2:
            print("You should enter numbers!")
            continue
        move_x = move_[0]
        move_y = move_[1]
        if move_x not in digit_list and move_y not in digit_list:
            print("You should enter numbers!")
            continue
        elif int(move_x) > 3 or int(move_y) > 3:
            print("Coordinates should be from 1 to 3!")
            continue
        elif check_cell_bad(int(move_x), int(move_y), position):
            print("This cell is occupied! Choose another one!")
            continue
        else:
            position = move_position(int(move_x), int(move_y), position, gamer)
            gamer = not gamer
            print_field(position)
            break
    if "win" in game_status(position) or "Draw" in game_status(position):
        break

print(game_status(position))
