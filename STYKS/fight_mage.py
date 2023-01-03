import include
import item_list
import random
import time
import math
from hero import PC_HERO
from fight import get_health_bar

def fight_mage(player,enemy):
    reaction_time = 3 + math.floor(player.dex/10)
    print("\nWalka z czarnoksiężnikiem niczym nie przypomina walki ze zwykłym przeciwnikiem.")
    print("Twój przeciwnik może teleportować się na krótkie dystanse i atakować cie różnymi atakami które musisz odeprzeć")
    print("- Δ oznacza płonącą kulę, żeby jej uniknąć, należy odskoczyć [Odskok]")
    print("- Γ oznacza podmuch wiatru, żeby go uniknąć musisz się czegoś złapać [Złap]")
    print("- ϴ oznacza magie krwi, mag próbuje przemocą wyrwać krew z twojego ciała. Musisz się przed tym schować [Schowaj]")
    print("- Λ oznacza oślepiający promień, musisz wykonać unik [Unik]")
    print("- Π oznacza moment w którym czarownik musi wziąć oddech by zebrać energie. To właśnie wtedy możesz zaatakować [Atak]")
    if hasattr(player,"weapon"):
        if player.weapon == item_list.itwp_sword_silver:
            print("Twój srebrny miecz może jednak rozproszyć każde zaklęcie. Wystarczy że wpiszesz [Tnij]")
    print("Poza odpowiedzią na atak maga, musisz wpisać jego lokalizacje. Mag teleportuje się po okręgu między 8 punktami")
    print("Każdy ma swój numer zgodnie ze wskazówkami zegara")

    print("\n--------------")
    print("    8    1    ")
    print("7            2")
    print("              ")
    print("6            3")
    print("    5    4    ")
    print("--------------")

    print("Żeby wpisać komende wpisz najpierw numer a potem po spacji akcje")
    print("Pamiętaj że czas rzucania czaru nie jest znowu taki długi! Masz tylko " + str(reaction_time) + " sekund na reakcje!")
    print("\nŻeby zacząć kliknij [Enter]")
    input()

    action_dict = {
        "Δ":"odskok",
        "Γ":"złap",
        "ϴ":"schowaj",
        "Λ":"unik",
        "Π":"atak"
    }
    spot_values = [" "," "," "," "," "," "," "," "]
    marks = ("Δ","Γ","ϴ","Λ","Π")
    while True:
        start = time.time()
        print("# # # # # # # # # # # # # # # ")
        get_health_bar(player)
        get_health_bar(enemy)
        mage_location = random.randrange(1,8)
        mark_selected = random.choice(marks)
        spot_values[mage_location-1] = mark_selected
        location_correct = " "
        answer_correct = " "
        print("--------------")
        print("    "+spot_values[7]+"    "+spot_values[0]+"    ")
        print(spot_values[6]+"            "+spot_values[1])
        print("              ")
        print(spot_values[5]+"            "+spot_values[2])
        print("    "+spot_values[4]+"    "+spot_values[3]+"    ")
        print("--------------")

        #print(action_dict[mark_selected])
        #print(mage_location)

        command = input()
        try:
            direction = int(command.split(' ', 1)[0].lower())
            command = include.stringify(command.split(' ', 1)[1:])
        except:
            direction = "2137"
            command = "leżysz i umirosz"
        #print(direction)
        #print(command.lower())

        if direction == mage_location:
            location_correct = "YES"

        if hasattr(player,"weapon") and player.weapon == item_list.itwp_sword_silver and command.lower() == "tnij":
            answer_correct = "YES"
        elif command.lower() == action_dict[mark_selected]:
            answer_correct = "YES"

        elapsed = time.time()
        if elapsed > start + reaction_time:
            answer_correct = "NO"
            location_correct = "NO"

        if answer_correct == "YES" and location_correct == "YES":
            if action_dict[mark_selected] == "atak":
                enemy.hp -= 100
                if enemy.hp < 0:
                    enemy.hp = 0
                print("Trafiony!")
            else:
                print("Unik!")
        else:
            if action_dict[mark_selected] == "atak":
                print("Mag teleportował się")
            else:
                print("Trafił cie!")
                player.hp -= 20
                if player.hp < 0:
                    player.hp = 0

        spot_values[mage_location-1] = " "

        if player.hp == 0:
            get_health_bar(player)
            get_health_bar(enemy)
            input()
            return "FAILURE"
        if enemy.hp == 0:
            get_health_bar(player)
            get_health_bar(enemy)
            input()
            return "SUCCESS"
