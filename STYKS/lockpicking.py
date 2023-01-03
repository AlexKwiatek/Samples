import include
import math
import item_list
import random
from hero import PC_HERO

def lockpick(combination):
    spot = 0
    print("Aby otwierać zamek odkryj kombinacje [Lewo/Prawo]")
    print("Aby się cofnąć wpisz POWRÓT")
    break_chance = 50 - PC_HERO.dex
    if break_chance < 0:
        break_chance = 0
    print("Szansa złamania wytrycha: " + str(break_chance) + "%")
    while True:
        move = input()
        if move.lower() in include.left_set: # Lewo
            move = "L"
        elif move.lower() in include.right_set: # Prawo
            move = "P"
        elif move.lower() in include.back_set:
            return "FAILURE"
        if move == combination[spot]:
            spot += 1
            if spot == len(combination):
                print("Zamek puścił")
                return "SUCCESS"
            else:
                print("Brzmi nieźle")
        else:
            spot = 0
            if random.randrange(1,100) < break_chance:
                PC_HERO.inventory.remove(item_list.itke_lockpick)
                print("Wytrych się złamał")
                if not item_list.itke_lockpick in PC_HERO.inventory:
                    print("Nie masz już wytrychów")
                    return "FAILURE"
            else:
                print("Cholera... spróbuje jeszcze raz")

