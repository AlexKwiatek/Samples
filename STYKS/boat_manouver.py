import include
import random
import math
import time
from hero import PC_HERO

tile_list = (
    "x"," "," "," "
)

def create_river_row():
    row = [" "," "," "," "," "," "," "," "," "," "," "]
    row[0] = "x"
    row[1] = random.choice(tile_list)
    row[2] = random.choice(tile_list)
    row[3] = random.choice(tile_list)
    row[4] = random.choice(tile_list)
    row[5] = random.choice(tile_list)
    row[6] = random.choice(tile_list)
    row[7] = random.choice(tile_list)
    row[8] = random.choice(tile_list)
    row[9] = random.choice(tile_list)
    row[10] = "x"
    return row

def boat_manouver():
    rows = 0
    number_of_rows = 40
    row_map = []
    rows_to_see = 60

    print("Będziesz teraz kierować łodzią. Komendy są tylko dwie, L oraz P reprezentujące Lewo i Prawo")
    print("Twoim zadaniem jest wybrać następny ruch łodzi tak by nie znaleźć się w następnym ruchu na mieliźnie")
    print("Mielizny są symbolizowane symbolem 'x'")
    print("Gdy będziesz gotowy, kliknij [ENTER]")
    input()

    while rows < number_of_rows:
        row_map.append(create_river_row())
        rows += 1

    for element in range(5):
        row_map.insert(0,[" "," "," "," "," "," "," "," "," "," "," "])
        row_map.append([" "," "," "," "," "," "," "," "," "," "," "])

    row_map.append(["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"])

    for element in range(20):
        row_map.append([" "," "," "," "," "," "," "," "," "," "," "])

    player_position = 5
    current_row = 0


    while True:
        if row_map[0][player_position] == "x":
            print("ROZBIŁEŚ ŁÓDŹ")
            input()
            return "FAILURE"
        elif current_row == number_of_rows+10:
            print("Wypływasz na bezpieczne wody...")
            input()
            return "SUCCESS"
        else:
            row_map[0][player_position] = "0"

        for element in reversed(row_map[0:rows_to_see]):
            print(' '.join(element))

        command = input()
        if command.lower() == "l" and player_position != 1:
            player_position -= 1
        elif command.lower() == "p" and player_position != 9:
            player_position += 1

        row_map.remove(row_map[0])
        current_row += 1
