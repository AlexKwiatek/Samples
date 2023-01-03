import include
import item_list
import journal
import map
import sharpening
import digging_treasure
import leveling
import time
import fight
import boat_manouver
import fishing
import npc_list
import labirynth
import hunting
import spellbreaker
import inventory
from hero import PC_HERO

### Create example vobs
VOB_Key_Boatmaker = include.VOB(
    "Klucz",
    "Prosty żelazny klucz"
)
VOB_Key_Boatmaker.item = item_list.itke_boatmaker_key

VOB_Booze_Stash = include.VOB(
    "Booze",
    "It would seem that Boatmaker has his stash of booze. Aaand he is outside. Aaand stash is inside. If you know what i mean. \n I bet you know"
)
VOB_Booze_Stash.illegal = 1
VOB_Booze_Stash.item = item_list.itfo_booze

VOB_Oars = include.VOB(
    "Tyczka",
    "Ukradłem tyczke. Teraz moge użyć promu"
)
VOB_Oars.illegal = 1
VOB_Oars.item = item_list.itmi_oars

VOB_Boat = include.VOB(
    "Łódź", #TODO: Dowiedz się dlaczego polskie słowo "Prom" psuło skrypt
    "Prom Szkutnika. Wielka drewniana tratwa."
)
VOB_Boat.illegal = 1
def VOB_Boat_effect(user):
    if not hasattr(VOB_Boat,"illegal"): #Is not theft
        print("\nRazem ze szkutnikiem załadowaliście się na jego prom. Starzec przetransportował was w góre rzeki, ostrzegając przed niebezpieczeństwami i wybierając bezpieczne ścieżki")
    elif not item_list.itmi_oars in user.inventory:
        print("Nie masz kija by odepchnąć prom od wody!")
        input("Kontynuuj...")
        return
    else:
        print("\nKradniesz Szkutnikowi jego prom. Nim stary rzemieślnik zdążył zareagować byliście już na wodzie. \nPo chwili udaje wam się oddalić dość daleko by i jego krzyki i wyzwiska ucichły w oddali")
        print("Podróż trwa...")
        PC_HERO.karma -= 1
        PC_HERO.flags.append("stolen_ferry")
        time.sleep(5)
        print("W pewnym momencie dopływacie do rozwidlenia rzeki. Antiochus twierdzi że obie odnogi wpływają do Styksu i rzeki tworzą tutaj swoistą wyspe")
        print("Mówi jednak że prawa odnoga jest niebezpieczna. Mimo iż dużo szybciej dopłynęlibyśmy nią do Wyroczni")
        print("Którą odnoge wybierasz? [LEWO/PRAWO]")
        while True:
            command = input()
            if command.lower() in include.left_set: # Lewą
                print("Wybrałeś lewą odnogę... rozłóż się wygodnie na promie!")
                break
            elif command.lower() in include.right_set: # Prawą
                print("Wybrałeś prawą odnogę... i natychmiast zaczynasz tego żałować. Chwytasz mocno tyczke... będzie trzeba intensywnie manewrować by nie osiąść na mieliźnie!")
                result = boat_manouver.boat_manouver()
                if result == "SUCCESS":
                    print("Udało się wam dopłynąć na bezpieczne wody. Szczęśliwie, bez niespodzianek!")
                    leveling.give_exp(user,25)
                    break
                else:
                    print("Niestety osiedliście na mieliźnie. Ty i Antiochus spędziliście mase czasu by wyciągnąć z niej prom. W końcu się udało, jednak wyczerpała was ta praca")
                    user.hp -= 20
                    break
    journal.B_Kapitelwechsel(2)
    PC_HERO.current_cell = map.LOC_PRIORY_DOCK
    input("Kontynuuj...")

VOB_Boat.effect = VOB_Boat_effect

# # #
VOB_Fishing_Hole = include.VOB(
    "Łowienie Ryb",
    "W wiosce rybackiej jest molo przeznaczone specjalnie dla rybaków"
)
def VOB_Fishing_Hole_effect(user):
    print("Czy chcesz łowić ryby?")
    command = input()
    if command in include.yes_set:
        if item_list.itmi_bait in user.inventory:
            result = fishing.fishing()
            if result == "SUCCESS":
                inventory.add_to_inventory(user,item_list.itfo_fish)
            else:
                return
        else:
            print("Musisz zdobyć przynęte")
            input()
            return
    else:
        return
VOB_Fishing_Hole.effect = VOB_Fishing_Hole_effect

# # #
VOB_Hunting_Spot = include.VOB(
    "Polowanie",
    "W lesie obok wioski rybackiej można znaleźć dużo miejsc dobrych do polowania na zwierzęta"
)
def VOB_Hunting_Spot_effect(user):
    print("Czy chcesz zapolować?")
    command = input()
    if command in include.yes_set:
        if item_list.itmi_arrow in user.inventory:
            result = hunting.hunting(user)
            if result == "SUCCESS":
                inventory.add_to_inventory(user,item_list.itfo_venison)
            else:
                return
        else:
            print("Musisz zdobyć strzały")
            input()
            return
    else:
        return
VOB_Hunting_Spot.effect = VOB_Hunting_Spot_effect




VOB_Grave_Willow = include.VOB(
    "Grób pod Starą Wierzbą",
    "Stary grób. Wystaje z niego zdobiony miecz przybijający ciemnoniebieski płaszcz. Płaszcz wydaje ci się być dziwnie znajomy."
)
def VOB_Grave_Willow_effect(user):
    if hasattr(user,"antiochus_grave") and user.antiochus_grave == 1:
        print("Mimo że jesteś w Hadesie, czujesz jakby atmosfera była bardziej grobowa niż zwykle. Bierzesz łopate leżącą przy świeżych grobach i wbijasz ją w starą ziemie")
        print("Nie wiesz ile czasu zajęło ci kopanie w ziemii. W końcu dokopujesz się do ciała. Twarz. Zaczynasz pomagać sobie rękami by odsłonić jej rysy")
        print("Nie możesz złapać wdechu. Z miejsca rozumiesz o czym mówił Bękart.")
        print("Jesteś przeklęty. Nie może być innego wyjaśnienia na to co się dzieje.")
        print("")
        print("Z wnętrza grobu spogląda na ciebie martwo twarz Księcia Antiochusa Młodszego.")
        user.antiochus_grave = 2
        leveling.give_exp(user,500) #Odkryłeś że fAntiochus nie jest prawdziwym Antiochusem
    elif hasattr(user,"antiochus_grave") and user.antiochus_grave == 2:
        print("Z wnętrza grobu wystaje odsłonięta twarz Księcia Antiochusa")
    else:
        pass

VOB_Grave_Willow.effect = VOB_Grave_Willow_effect


VOB_Wood_Pendant = include.VOB(
    "Wisiorek w trawie",
    "Mały wisiorek z wygrawerowanym napisem 'Alexis'"
)
VOB_Wood_Pendant.item = item_list.itmi_bastard_amulet
VOB_Gravedigger_Pendant = include.VOB(
    "Naszyjnik",
    "Złoty amulet z wielkim rubinem zawieszony na kolumnie łóżka. Wygląda jakby emanował złą energią."
)
VOB_Gravedigger_Pendant.item = item_list.itmi_gravedigger_pendant


VOB_Dig_Site = include.VOB(
    "Oznaczona ziemia",
    "Za wierzbami w ogrodzie jest alejka idąca pod murkiem. Pod jednym ze drzew jest wbity patyk\nWygląda jakby coś tu było zakopane.\n"
)
def VOB_Dig_Site_effect(user):
    if not "Digged Parchment" in user.flags:
        command = input("Czy chcesz spróbować to wykopać? ")
        if command in include.yes_set:
            effect = digging_treasure.digging(user)
            if effect == "SUCCESS":
                print("Był tu zakopany zwinięty kawałek pergaminu")
                inventory.add_to_inventory(PC_HERO,item_list.itwr_antiochus_letter)
                input()
                user.flags.append("Digged Parchment")
                leveling.give_exp(PC_HERO,50)
    else:
        print("Wykopałeś już to co tu było zakopane")
VOB_Dig_Site.effect = VOB_Dig_Site_effect


VOB_Silver_Sword = include.VOB(
    "Katakumby",
    "Wygląda to na prawdziwy labirynt różnych magazynów, sarkofagów... Może jest w nim coś wartościowego?"
)
def VOB_Siver_Sword_Effect(user):
    if "labyrinth_done" in user.flags:
        print("Nie ma tam już nic ciekawego")
    else:
        print("Czy chcesz wejść do labiryntu?")
        while True:
            command = input()
            if command in include.yes_set:
                result = labirynth.labirynth()
                if result == "SUCCESS":
                    print("W końcu dotarłeś do zdobionej rzeźby trzymającej srebrny miecz. Wygląda na to że broń jest prawdziwa")
                    inventory.add_to_inventory(user,item_list.itwp_sword_silver)
                    user.flags.append("labyrinth_done")
                    break
                break
            else:
                break


VOB_Silver_Sword.effect = VOB_Siver_Sword_Effect
###


VOB_Horses = include.VOB(
    "Osiodłane Konie",
    "Antiochus stoi przy dwóch osiodłanych koniach. Wygląda na to że zdobył je gdy ty rozmawiałeś z Odźwiernym"
)
def VOB_Horses_effect(user):
    print("Wreszcie możecie opuścić to przeklęte miejsce. Wsiedliście na konie i podążaliście za śladem przepowiedni wyroczni")
    print("Trzy góry")
    print("Trzy góry, trzech wędrowców i trzech opiekunów")
    print("I klucz w latarni")
    input()
    PC_HERO.current_cell = map.LOC_FARM
    print("Jechaliście tak przez kilka dni, widząc wiele opustoszałych miejsc, lecz wciąż zaskakująco mało dusz")
    print("Jak to możliwe że miejsce do którego trafiły setki tysięcy zmarłych jest opustoszałe?")
    print("Co się dzieje z ludźmi których spotka śmierć tutaj? Czy jest jeszcze jakieś piekło do umarłych?")
    print("W końcu dojechaliście do małej wioski u podnóża gór. Jest tu zaskakujaco dużo ludzi. Wygląda na to że jest tu jakaś plantacja niewolnicza")
    print("A co ważniejsze - jest tu wieża z latarnią.")
    journal.B_Kapitelwechsel(3)
VOB_Horses.effect = VOB_Horses_effect


VOB_Tower_Door = include.VOB(
    "Włam do Latarni",
    "Nawet jeśli nie masz klucza są inne metody by wejść do środka..."
)
def VOB_Tower_Door_Effect(user):
    print("Czy chcesz przemocą wtargnąć do Latarni?")
    while True:
        command = input()
        if command.lower() in include.yes_set:
            print("Chwytasz pobliską siekiere i uderzasz nią w drzwi z całej siły. Po chwili powtarzasz")
            print("Bandyci Bękarta nie pozostali bierni, chwycili za broń i biegną w twoim kierunku!")
            input()
            result = fight.startfight(user,npc_list.BDT_303_Hunter)
            if result == "SUCCESS":
                result = fight.startfight(user,npc_list.BDT_307_Sly)
                if result == "SUCCESS":
                    result = fight.startfight(user,npc_list.BDT_305_Nico)
                    if result == "SUCCESS":
                        result = fight.startfight(user,npc_list.BDT_306_Fang)
                        if result == "SUCCESS":
                            print("W końcu przybiegł i sam Bękart zamachując się na ciebie ogromnym oburęcznym mieczem")
                            result = fight.startfight(user,npc_list.BDT_300_Bastard)
                            if result == "SUCCESS":
                                print("Nie minęły nawet sekundy a wieża buchnęła płomieniem. Alexis już wie.")
                                PC_HERO.flags.append("i_choose_violence")
                                PC_HERO.current_cell = map.LOC_TOWER
                                map.LOC_FARM_ALLEY.locked = "locked"
                                map.LOC_FARM_ALLEY.locked_reason = "To nie jest dobry pomysł"
                                break
                            else:
                                fight.kill(PC_HERO, 1)
                        else:
                            fight.kill(PC_HERO, 1)
                    else:
                        fight.kill(PC_HERO, 1)
                else:
                    fight.kill(PC_HERO, 1)
            else:
                fight.kill(PC_HERO, 1)
        else:
            break
VOB_Tower_Door.effect = VOB_Tower_Door_Effect

VOB_Riverside_Corpse = include.VOB(
    "Zwłoki",
    "Bardzo dobrze zachowane zwłoki. Co ciekawe nie mają krwi. Wygląda na to że ciała tutaj się nie rozkładają"
)
def VOB_Riverside_Corpse_effect(user):
    inventory.add_to_inventory(user,item_list.itwp_sword_1)
    inventory.add_gold(user,50)
    map.LOC_CAVE.vob.remove(VOB_Riverside_Corpse)

VOB_Riverside_Corpse.effect = VOB_Riverside_Corpse_effect

VOB_TowerFire = include.VOB(
    "Płomień Latarni",
    "Intensywnie czerwone płomienie zdają się bardziej pożerać ciepło z okolicy niż je oddawać"
)
def VOB_TowerFire_effect(user):
    print("Magia jest niemal wyczuwalna na odległość ręki. Masz wrażenie jakby była emitowana przez ogień zamiast ciepła")
    print("Instynktownie czujesz że tak jak dotykając ciepłego przedmiotu możesz zagrzać swoją dłoń, tak tutaj możesz dostroić się do magii płomienia")
    print("Czy chcesz spróbować?")
    command = input()
    if command in include.yes_set:
        result = spellbreaker.spellbreaking()
        print("Udało ci się. Twoja głowa, twoje myśli zdają się mieć bezpośrednie połączenie z ogniem")
        print("Jedyne co widzisz przed oczami to tańczące płomienie. Możesz się skupić i nadać wiadomość")
        print("Nie może być jednak zbyt długa. Z każdym słowem głowa boli cie coraz bardziej i tracisz koncentracje")
        print("Możesz użyć jedynie " + str(result) + " liter")
        while True:
            message = input()
            if len(message) > result:
                print("Wiadmość jest za długa...")
            else:
                print("Ogień buchnął płomieniem na pare stóp w góre. Wiadomość została przesłana.")
                print("Nagle słyszysz skrzypienie drzwi. Gdy spoglądasz ze schodów na dół widzisz że do wieży wszedł Bękart z Koryntu.")
                input()
                map.LOC_TOWER.npc.append(npc_list.BDT_300_Bastard_Lantern)
                map.LOC_TOWER.vob.remove(VOB_TowerFire)
                if npc_list.BDT_302_Keeper.hp != 0:
                    map.LOC_TOWER.npc.remove(npc_list.BDT_302_Keeper)
                break
VOB_TowerFire.effect = VOB_TowerFire_effect


### Common VOBs
VOB_Usable_Sharpening_Stone = include.VOB(
    "Kamień Szlifierski",
    "Mechanizm napędzany pedałem który wprawia ogromny kamień w ruch obrotowy. Można na nim ostrzyć miecze lub inne narzędzia"
)
def VOB_Usable_Sharpening_Stone_effect(user):
    if hasattr(user,"weapon") and not "sharpened" in user.weapon.flags:
        sharp_max = user.weapon.dmg
        command = input("Czy chcesz naostrzyć broń? ")
        if command in include.yes_set:
            sharpen = sharpening.sharpening()
            if sharpen > sharp_max:
                sharpen = sharp_max
            user.weapon.dmg = user.weapon.dmg + sharpen
            user.weapon.flags.append("sharpened")
            print("Ulepszyłeś swoją broń o " + str(sharpen) + " punktów!")
            print("Nowe obrażenia: " + str(user.weapon.dmg))
            input()
    elif not hasattr(user,"weapon"):
        print("Nie masz broni do naostrzenia")
        input()
    elif "sharpened" in user.weapon.flags:
        print("Twoja broń już jest naostrzona!")
        input()
VOB_Usable_Sharpening_Stone.effect = VOB_Usable_Sharpening_Stone_effect

