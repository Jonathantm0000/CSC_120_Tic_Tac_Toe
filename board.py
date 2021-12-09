rows = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
turn = 'o'


def printboard():
    for x in range(len(rows)):
        print(rows[x])


def placexo(move1, move2, xoturn):
            if rows[move1-1][move2-1] == '-':
                rows[move1-1][move2-1] = xoturn
            else:
                print("that tile is taken")


def wincheck(currentplayer):
    if rows[0][0] == rows[0][1] == rows[0][2]:
        print("Game over ", currentplayer, "wins")
    elif rows[1][0] == rows[1][1] == rows[1][2]:
        print("Game over ", currentplayer, "wins")
    elif rows[2][0] == rows[2][1] == rows[2][2]:
        print("Game over ", currentplayer, "wins")
    elif rows[0][0] == rows[1][0] == rows[2][0]:
        print("Game over ", currentplayer, "wins")
    elif rows[0][1] == rows[1][1] == rows[2][1]:
        print("Game over ", currentplayer, "wins")
    elif rows[0][2] == rows[1][2] == rows[2][2]:
        print("Game over ", currentplayer, "wins")
    elif rows[0][0] == rows[1][1] == rows[2][2]:
        print("Game over ", currentplayer, "wins")
    elif rows[2][0] == rows[1][1] == rows[0][2]:
        print("Game over ", currentplayer, "wins")


win = False
while not win:
    turncount = 0
    printboard()
    if turn == 'x':
        turn = 'o'
    else:
        turn = 'x'

    print("It is", turn, "turn")
    movec = int(input("Enter the column you want"))
    mover = int(input("Enter the row you want"))
    if movec < 1 | movec > 4:
        print("Enter a column from 1-3")
        movec = int(input("Enter the column you want"))

    if mover < 1 | mover > 4:
        print("Enter a column from 1-3")
        mover = int(input("Enter the row you want"))

    placexo(movec, mover, turn)
    wincheck(turn)
    turncount = turncount + 1
    if turncount == 9:
        win = True
        print("This game is a draw")
