import random

def spellbreaking():

    print("Żeby dostroić się do Ognia Latarni, musisz wytężyć swój umysł i użyć siły woli do rozwiania struktury zaklęcia")
    print("Gdy zaklęcie będzie rozwiane, będziesz mógł wysłać wiadomość")
    print("Za każdym razem gdy uderzysz w symbol, wszystkie takie same symbole sąsiadujące z nim znikają tak samo, aż skończą się graniczące symbole")
    print("Jesteś w stanie skupić się jedynie na 10 uderzeń w strukture")
    print("Koordynaty uderzenia wpisujesz albo jedną cyfrą, oznaczającą horyzontalne położenie symbolu albo dwiema. W takim wypadku druga liczba to położenie wertykalne")
    print("Nie możesz uderzyć w symbol jeśli poniżej niego znajduje się inny symbol. Okienko pod atakowanym symbolem musi być puste!")
    print("Kliknij [ENTER] żeby zacząć")
    input()
    board = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]

    marks = ("Δ","Γ","ϴ","Λ","Π")
    len_y = len(board)
    len_x = len(board[0])

    def randomize_tile(len_y,len_x):
        temp_list = ["Δ","Γ","ϴ","Λ","Π"]
        if len_y > 0:
            if board[len_y-1][len_x] != " ":
                temp_list.append(board[len_y-1][len_x])
                temp_list.append(board[len_y-1][len_x])
        if len_y < 9:
            if board[len_y+1][len_x] != " ":
                temp_list.append(board[len_y+1][len_x])
                temp_list.append(board[len_y+1][len_x])
        if len_x > 0:
            if board[len_y][len_x-1] != " ":
                temp_list.append(board[len_y][len_x-1])
                temp_list.append(board[len_y][len_x-1])
        if len_x < 19:
            if board[len_y][len_x+1] != " ":
                temp_list.append(board[len_y][len_x+1])
                temp_list.append(board[len_y][len_x+1])
        mark = random.choice(temp_list)
        return mark

    def pop_tile(tile_y,tile_x):
        attacked_mark = board[tile_y][tile_x]
        if attacked_mark == " ":
            return
        board[tile_y][tile_x] = " "
        if tile_y > 0:
            if board[tile_y-1][tile_x] == attacked_mark:
                pop_tile(tile_y-1,tile_x)
        if tile_y < 9:
            if board[tile_y+1][tile_x] == attacked_mark:
                pop_tile(tile_y+1,tile_x)
        if tile_x > 0:
            if board[tile_y][tile_x-1] == attacked_mark:
                pop_tile(tile_y,tile_x-1)
        if tile_x < 19:
            if board[tile_y][tile_x+1] == attacked_mark:
                pop_tile(tile_y,tile_x+1)

    row = 1
    while row <= len_y:
        spot = 1
        while spot <= len_x:
            board[row-1][spot-1] = randomize_tile(row-1,spot-1)
            spot += 1
        row += 1

    shots = 10
    while shots != 0:
        row_num = 10
        for row in reversed(board):
            if row_num < 10:
                print(str(row_num) + ".  " + ' '.join(row))
            else:
                print(str(row_num) + ". " + ' '.join(row))
            row_num -= 1
        print("   |        |         |         |         |")

        points = 0
        for row in board:
            points += row.count(" ")
        print("PUNKTY: " + str(points))
        print("UDERZENIA: " + str(shots))

        command = input()
        if command == "":
            command = 1
        shots -= 1
        try:
            blablabla = command.split(' ', 1)
            print(blablabla)
            axis_y = int(blablabla[1]) - 1
            axis_x = int(blablabla[0]) - 1
        except:
            axis_x = int(command) - 1
            shot_row = 9
            while True:
                if shot_row == 0:
                     axis_y = 0
                     break
                elif board[shot_row-1][axis_x] == " ":
                     axis_y = shot_row
                     break
                else:
                    shot_row -= 1
        if axis_y > 9:
            axis_y = 9
        if axis_y < 0:
            axis_y = 0
        if axis_x > 19:
            axis_x = 19
        if axis_x < 0:
            axis_x = 0

        print(axis_y)
        print(axis_x)

        if axis_y == 0:
            pop_tile(axis_y,axis_x)
        elif board[axis_y-1][axis_x] == " ":
            pop_tile(axis_y,axis_x)
        else:
            print("Nieosiągalne pole!")

    row_num = 10
    for row in reversed(board):
        if row_num < 10:
            print(str(row_num) + ".  " + ' '.join(row))
        else:
            print(str(row_num) + ". " + ' '.join(row))
        row_num -= 1
    print("   |        |         |         |         |")

    points = 0
    for row in board:
        points += row.count(" ")
    print("PUNKTY: " + str(points))
    print("Skończyły ci się uderzenia!")
    input()
    return points