import random
import time
import math
import item_list
from hero import PC_HERO

def fishing():
    failure_list = (
        "Ummmm, złowiłeś but",
        "Złowiłeś klatke na kraby",
        "Złowiłeś zardzewiały napierśnik",
        "Złowiłeś duży brązowy medialion z wyrytą na nim żółtą twarzą"
    )
    pull_set = (
        "ciagnij","ciągnij","pull"
    )
    print("Łowienie ryb wymaga przede wszystkim cierpliwości ale i dobrego refleksu")
    print("Musisz wpisać 'Ciągnij' w ciągu dwóch sekund od momentu w którym pojawi się informacja że ryba bierze")
    print("Jeśli masz dużą zręczność, dasz rade złąpać rybe nawet w przypadku drobnej pomyłki")
    print("Pamiętaj że masz ograniczoną ilość przynęty!")
    print("Gdy będziesz gotowy, kliknij [ENTER]")
    input()
    miss_window = 2 + math.floor(PC_HERO.dex/10)
    print("\n...")
    while item_list.itmi_bait in PC_HERO.inventory:
        time.sleep(random.randrange(1,5))
        event = random.randrange(1,4)
        if event == 1:
            print("Coś pociąga wędke!")
            start = time.time()
            command = input()
            elapsed = time.time()
            #print(elapsed - start)
            if command.lower() in pull_set and (elapsed - start) < miss_window:
                catch = random.randrange(1,3)
                if catch == 1:
                    print("Udało się! Złowiłeś rybę!")
                    input()
                    return "SUCCESS"
                else:
                    print(random.choice(failure_list))
            else:
                print("Cokolwiek to było, zdążyło uciec...")
            print("Zarzucasz jeszcze raz...")
            PC_HERO.inventory.remove(item_list.itmi_bait)
        else:
            print("...")
    print("Skończyła ci się przynęta.")
    input()
    return "FAILURE"
