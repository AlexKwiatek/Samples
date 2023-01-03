import include
import random
import math
import time
from hero import PC_HERO

def armwrestling(player,enemy):
    time_var = 3
    win_value = 30
    failure_margin = 5
    value = math.floor(win_value/2)
    print("\nW siłowaniu na rękę liczy się przede wszystkim siła. Do tego dochodzi jeszcze czynnik losowy oraz... dobra koordynacja mięśniowa!")
    print("Do tej ostatniej potrzebujesz dobrego oka! Przy każdym ruchu wyświetlać się będzie pasek pokazujący kto ma przewage w danej rundzie")
    print("Jeśli zdążysz wpisać położenie paska w postaci liczb od 1 do " + str(win_value) + " w ciągu " + str(time_var) + " sekund, dostaniesz dodatkowy bonus!")
    print("Możesz się odrobine pomylić, ale wtedy dostaniesz mniej punktów")
    print("\n")
    print("[" + "=" * value + "-" * (win_value-value) + "]")
    print("Gdy będziesz gotowy kliknij [ENTER]")
    input()
    while True:
        start = time.time()
        print("[" + "=" * value + "-" * (win_value-value) + "]")
        command = input()
        try:
            int(command)
        except:
            print("Musisz wpisać liczbe!")
            return
        elapsed = time.time()
        #print(elapsed - start)
        if elapsed - start < 3 and math.fabs(int(command) - value) < failure_margin:
            player_roll = (failure_margin - math.fabs(int(command) - value))*2 + player.str + random.randrange(1,10)
            print("Dobrze ci idzie!")
        else:
            player_roll = player.str + random.randrange(1,10)
        enemy_roll = enemy.str + random.randrange(1,10)
        # DEBUG MODE
        #print(enemy_roll)
        #print(player_roll)
        value -= math.floor(enemy_roll)
        value += math.floor(player_roll)
        if value > win_value:
            print("WYGRANA!")
            #input()
            return "SUCCESS"
        if value < 0:
            print("PRZEGRANA")
            #input()
            return "FAILURE"
