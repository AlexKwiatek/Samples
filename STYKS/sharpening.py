import include
import random
import math
import time
from hero import PC_HERO

def sharpening():
    direction_list = [
        "left","right","up","down"
    ]
    direction_dict = {
        "left":"Lewo",
        "right":"Prawo",
        "up":"Przód",
        "down":"Tył"
    }
    score = 0
    elapsed = 0
    time_limit = PC_HERO.str + random.randrange(5,10)
    print("### Ostrzenie miecza to trudna sztuka. Silny człowiek jest w stanie dłużej utrzymać miecz przy kole, ale potrzeba dobrego refleksu by ostrze nie wypadło ci z ręki")
    print("### Myśle że będziesz w stanie utrzymać je przez " + str(time_limit) + " sekund")
    print("### Na ekranie pojawią się komendy kierunków [Lewo,Prawo,Tył,Przód]. Wpisuj je najszybciej jak potrafisz a ulepszysz swój miecz")
    print("\nGdy będziesz gotowy, kliknij [ENTER]")
    input()
    start = time.time()

    while elapsed < time_limit:
        direction = random.choice(direction_list)
        print("\n### " + direction_dict[direction] + " ###")

        response = input("Wpisz Kierunek: ") #get the user's response
        if direction == "left" and response.lower() in include.left_set:
            success = 1
        elif direction == "right" and response.lower() in include.right_set:
            success = 1
        elif direction == "up" and response.lower() in include.forward_set:
            success = 1
        elif direction == "down" and response.lower() in include.backward_set:
            success = 1
        else:
            print("BŁĄD!")
            success = 0

        elapsed = time.time() - start #update the time elapsed
        if time_limit > elapsed:
            if success == 1:
                score += 1
                print("Udało się...")
            print("Pozostało czasu: " + str(math.floor(time_limit - elapsed)))
        else:
            print("KONIEC CZASU!")
        print("Ulepszenia: " + str(score))
    input()
    return score
