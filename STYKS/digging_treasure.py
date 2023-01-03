import include
import math
import random
from hero import PC_HERO

def digging(player):
    chances = 5 + math.floor(player.dex/5)
    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
    ]
    dictionary = {
        'A':0,
        'B':1,
        'C':2,
        'D':3,
        'E':4,
    }
    rev_dictionary = {
        0:'A',
        1:'B',
        2:'C',
        3:'D',
        4:'E'
    }
    allowed_letters = ("A","B","C","D","E")
    #Choose spot
    X = random.randrange(0,4)
    Y = random.randrange(0,4)

    board[X][Y] = "X"
    if X > 0: #Spot to the left
        board[X-1][Y] = "="
    if X < 4: #Spot to the right
        board[X+1][Y] = "="
    if Y < 4: #Spot to the down
        board[X][Y+1] = "="
    if Y > 0: #Spot to the up
        board[X][Y-1] = "="
    if X > 0 and Y > 0: #Corner
        board[X-1][Y-1] = "="
    if X < 4 and Y < 4: #Corner
        board[X+1][Y+1] = "="
    if X < 4 and Y > 0: #Corner
        board[X+1][Y-1] = "="
    if X > 0 and Y < 4: #Corner
        board[X-1][Y+1] = "="


    fake_board = [
        ['?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?'],
    ]

    print("\n\nZakopany przedmiot znajduje się gdzieś tutaj, ale trudno powiedzieć gdzie.")
    print("Aby odkopać fragment ziemi, wpis jego wiersz (litera) i kolumne (cyfra)")
    print("X oznacza poszukiwany przedmiot, = oznacza komórke graniczącą z nim")
    print("Masz na to " + str(chances) + " szans")
    input()
    rownum = 0
    print("     1    2    3    4    5")
    for row in fake_board:
        print(rev_dictionary[rownum] + ": ", end="")
        print(row)
        rownum += 1

    while chances > 0:
        command = input()

        command = list(command)
        if not command[0].upper() in allowed_letters:
            return
        try:
            int(command[1])
        except:
            return
        command[0] = dictionary[command[0].upper()]
        command[1] = int(command[1]) - 1
        if command[1] > 4 or command[1] < 0:
            return
        #print(command)

        fake_board[command[0]][command[1]] = board[command[0]][command[1]]
        rownum = 0
        print("     1    2    3    4    5")
        for row in fake_board:
            print(rev_dictionary[rownum] + ": ", end="")
            print(row)
            rownum += 1
        if command[0] == X and command[1] == Y:
            print("\nZNALEZIONE!")
            input()
            return "SUCCESS"

        chances -= 1
        if chances > 0:
            print("\nMasz jeszcze " + str(chances) + " szans zanim szpadel się złamie")
    print("Szpadel się złamał!")
    return "FAILURE"
