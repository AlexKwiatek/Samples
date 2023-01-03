import include
import time
import item_list
from hero import PC_HERO

def hunting(player):
    time_limit = 20
    aim_meter = "-"*time_limit
    loose_list = ("puść","pusc","puśc","pusć","loose","p","l")
    aim_location = [time_limit-5]
    if player.str > 5:
        aim_location.append(time_limit-4)
    if player.str > 10:
        aim_location.append(time_limit-3)
    if player.str > 15:
        aim_location.append(time_limit-2)
    if player.str > 20:
        aim_location.append(time_limit-6)
    animal_location = 0

    aim_meter = list(aim_meter)
    for element in aim_location:
        aim_meter[element] = "U"
    command = " "

    print("Na łowiectwo skłania sie wiele czynników. Wielu ludzi mylnie myśli że kluczowe znaczenie ma tu zręczność")
    print("Prawda jest jednak taka, że w przeciwieństwie do szermierki, gdzie główną role gra rzeczywiście zręczność, w obsłudze łuku liczy się przede wszystkim siła")
    print("Im dłużej łuk jest naciągnięty, tym bardziej męczy ci się ramie, dlatego szerokość twojego celownika, zależy od tego jak dużo masz siły")
    print("Obecnie szerokość twojego celownika wynosi: " + str(len(aim_location)))
    print("Zwierze jest symbolizowane przez symbol 'Σ', twój celownik jest symbolizowany przez 'U'")
    print("Żeby strzelić wpisz 'Puść' ale zwykłe 'p' również wystarczy")
    print("Kliknij [ENTER] by zacząć")
    print('  '.join(aim_meter))
    input()
    start = time.time()
    while animal_location != time_limit-1:
        if animal_location in aim_location:
            aim_meter[animal_location] = "U"
        else:
            aim_meter[animal_location] = "-"

        #print(start)
        #print(time.time() - start)
        animal_location = int((time.time() - start)*2)# -4

        if animal_location >= time_limit:
            animal_location = time_limit-1

        if animal_location in aim_location:
            aim_meter[animal_location] = "X"
        else:
            aim_meter[animal_location] = "Σ"

        if command.lower() in loose_list:
            player.inventory.remove(item_list.itmi_arrow)
            if animal_location in aim_location:
                print("TRAFIENIE!")
                input()
                return "SUCCESS"
            else:
                print("Pudło! Zmarnowałeś strzałe!")
                #input()
        print('  '.join(aim_meter))
        if not item_list.itmi_arrow in player.inventory:
            print("Skończyły ci się strzały")
            return "FAILURE"
        command = input()
    print("Zwierze uciekło...")
