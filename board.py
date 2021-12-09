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


win = False
while not win:
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
