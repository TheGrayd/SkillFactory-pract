
fild = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]
player_1 = [0, 1, 2,
            3, 4, 5,
            6, 7, 8]
player_2 = [0, 1, 2,
            3, 4, 5,
            6, 7, 8]

print("Ввидите имя:")
name_player_1 = input()
print("Ввидите имя:")
name_player_2 = input()

def print_fild():
    print(fild[0], end = " ")
    print(fild[1], end = " ")
    print(fild[2])

    print(fild[3], end = " ")
    print(fild[4], end = " ")
    print(fild[5])

    print(fild[6], end = " ")
    print(fild[7], end = " ")
    print(fild[8])
print_fild()
for i in range(len(fild)):
    symbol_p1 = "X"
    print("Ходит", name_player_1)
    turn = int(input()) - 1
    player_1[turn] = 1
    symbol_p2 = "O"
    print("Ходит", name_player_2)
    turn = int(input()) - 1
    player_2[turn] = 2

    if player_1[0] == player_1 [1] and player_1[1] == player_1[2] and player_1[2] == player_1[0]\
            or player_1[3] == player_1[4] and player_1[4] == player_1[5] and player_1[5] == player_1[3]\
            or player_1[6] == player_1[7] and player_1[7] == player_1[8] and player_1[8] == player_1[6]\
            or player_1[0] == player_1[3] and player_1[3] == player_1[6] and player_1[6] == player_1[0]\
            or player_1[1] == player_1[4] and player_1[4] == player_1[7] and player_1[7] == player_1[1]\
            or player_1[2] == player_1[5] and player_1[5] == player_1[8] and player_1[8] == player_1[2]\
            or player_1[0] == player_1[4] and player_1[4] == player_1[8] and player_1[8] == player_1[0]\
            or player_1[2] == player_1[4] and player_1[4] == player_1[6] and player_1[6] == player_1[2]:

        print(name_player_1, "Победил")
    elif player_2[0] == player_2[1] and player_2[1] == player_2[2] and player_2[2] == player_2[0]\
            or player_2[3] == player_2[4] and player_2[4] == player_2[5] and player_2[5] == player_2[3]\
            or player_2[6] == player_2[7] and player_2[7] == player_2[8] and player_2[8] == player_2[6]\
            or player_2[0] == player_2[3] and player_2[3] == player_2[6] and player_2[6] == player_2[0]\
            or player_2[1] == player_2[4] and player_2[4] == player_2[7] and player_2[7] == player_2[1]\
            or player_2[2] == player_2[5] and player_2[5] == player_2[8] and player_2[8] == player_2[2]\
            or player_2[0] == player_2[4] and player_2[4] == player_2[8] and player_2[8] == player_2[0]\
            or player_2[2] == player_2[4] and player_2[4] == player_2[6] and player_2[6] == player_2[2]:

        print(name_player_2, "Победил")

    else:

        print("Ничья")