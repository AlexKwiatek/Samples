import include
import random
import pickle

### Example player char
PC_HERO = include.NPC(
    "TestChar", # Name
    "companion", # Class
    1, # Level
    0, 100, # XP
    100,100, # HP
    100,50,50,50,0 # Attributes
)
PC_HERO.inventory = []
PC_HERO.questlog = []
PC_HERO.knowndialogue = []
PC_HERO.gold = 0


def create_new_character():
    def print_skills():
        print("\nAttributes: ")
        print("Siła: " + str(PC_HERO.str))
        print("Zręczność: " + str(PC_HERO.dex))
        print("Inteligencja: " + str(PC_HERO.int))
        print("Charyzma: " + str(PC_HERO.cha))
        print("Punkty Nauki: " + str(PC_HERO.lp))

    print("Jeśli importujesz postać, wpisz nazwe pliku. Jeżeli chcesz zrobić nową postać wpisz 'Nowa'")
    command = input()
    if command.lower() != "nowa":
        command += ".dat"
        print(command)
        save_game = open(command, "rb")
        PC_HERO_SAVED = pickle.load(save_game)
        PC_HERO.name = PC_HERO_SAVED.name
        PC_HERO.guild = PC_HERO_SAVED.guild
        PC_HERO.hp = PC_HERO_SAVED.hp_max
        PC_HERO.hp_max = PC_HERO_SAVED.hp_max
        PC_HERO.str = PC_HERO_SAVED.str
        PC_HERO.dex = PC_HERO_SAVED.dex
        PC_HERO.int = PC_HERO_SAVED.int
        PC_HERO.cha = PC_HERO_SAVED.cha
        PC_HERO.lp = PC_HERO_SAVED.lp
        PC_HERO.printcharactersheet()

    else:
        ### WYBÓR IMIENIA I KLASY
        character_name = input("Imie: ")
        print(include.guilds["peltist"], include.guilds_desc["peltist"])
        print(include.guilds["hoplite"], include.guilds_desc["hoplite"])
        print(include.guilds["companion"], include.guilds_desc["companion"])
        PC_HERO.name = character_name
        while True:
            character_class = str(input("Wybierz klase postaci: "))

            if character_class.lower() == include.guilds["peltist"].lower():
                character_class = "peltist"
                break
            elif character_class.lower() == include.guilds["hoplite"].lower():
                character_class = "hoplite"
                break
            elif character_class.lower() == include.guilds["companion"].lower():
                character_class = "companion"
                break
            else:
                print("Error, type again")

        PC_HERO.guild = character_class
        print("Klasa: " + include.guilds[character_class])
        if character_class == "peltist":
            # hp_dice = 6
            hp_dice = [100,100,100,100]
            PC_HERO.str = 5
            PC_HERO.dex = 10
            PC_HERO.int = 5
            PC_HERO.cha = 0
        elif character_class == "hoplite":
            # hp_dice = 10
            hp_dice = [200,200,200,200]
            PC_HERO.str = 15
            PC_HERO.dex = 5
            PC_HERO.int = 0
            PC_HERO.cha = 0
        else:  # companion
            # hp_dice = 8
            hp_dice = [150,150,150,150]
            PC_HERO.str = 5
            PC_HERO.dex = 5
            PC_HERO.int = 0
            PC_HERO.cha = 10

        ### LOSOWANIE PUNKTÓW HP
        # print("Kość HP K" + str(hp_dice))
        # print("Losowanie HP... \n")
        # input("Kontynuuj...")
        # dice1 = random.randrange(1, hp_dice)
        # dice2 = random.randrange(1, hp_dice)
        # dice3 = random.randrange(1, hp_dice)
        # dice4 = random.randrange(1, hp_dice)

        # PC_HERO.hp_max = 50 + 5*(dice1 + dice2 + dice3 + dice4 - min(dice1, dice2, dice3, dice4))

        # Otusz - losowanie HP z poziomu tworzenia postaci (i jakiejkolwiek gry z zapisami) jest fundamentalnie zle.
        # Kusi to gracza by przerwać tworzenie postaci i zacząć je od początku aż wylosuje odpowiednio wysoką ilość HP.
        # Powyższy kod przedstawia co możnaby zrobić gdybym nie miał sumienia i będąc świadomym powyższego zrobił losowanie postaci
        # Ale ja zdążyłem się już przywiązać do tej gry. I nie będę tolerować w niej tak oczywistego design flaw
        # A zatem przedstawiam poniższe:
        # Tak, jest to funkcja random.choice, jest to LOSOWANIE, w 100% zgodne z wymaganiami kreatora postaci.
        # Fakt że losuje to z listy w której są 4 takie same liczby nie ma absolutnie żadnego znaczenia. To dalej jest losowanie.
        # Odbywa się poniżej losowanie punktów HP.
        # Może i jest ono uczciwe jak referendum na Krymie ale z punktu widzenia kodu to dalej jest losowanie i nikt mi nie wmówi że nie.

        PC_HERO.hp_max = random.choice(hp_dice)
        PC_HERO.hp = PC_HERO.hp_max

        print("Przyznane maksymalne HP: " + str(PC_HERO.hp_max))

        ### ROZDANIE STATYSTYK
        PC_HERO.lp = 10

        while PC_HERO.lp > 0:
            print_skills()
            print("\nWpisz 'auto' by rozdać automatycznie \n")
            print("\nAby rozdać wiecej punktów w daną ceche, napisz jej nazwe a potem liczbe punktów\n")
            invest_skill = input("Cecha: ")
            invest_skill = invest_skill.split()
            try:
                int(invest_skill[-1])
                invest_skill.append(int(invest_skill[-1]))
            except:
                invest_skill.append(1)
            if invest_skill[-1] > PC_HERO.lp:
                invest_skill[-1] = PC_HERO.lp
            if invest_skill[0].lower() == "auto":
                if character_class == "peltist":
                    PC_HERO.str = 10
                    PC_HERO.dex = 15
                    PC_HERO.int = 5
                    PC_HERO.cha = 0
                    PC_HERO.lp = 0
                elif character_class == "hoplite":
                    PC_HERO.str = 20
                    PC_HERO.dex = 10
                    PC_HERO.int = 0
                    PC_HERO.cha = 0
                    PC_HERO.lp = 0
                else:  # companion
                    PC_HERO.str = 5
                    PC_HERO.dex = 10
                    PC_HERO.int = 5
                    PC_HERO.cha = 10
                    PC_HERO.lp = 0
            elif invest_skill[0].lower() in include.str_set:
                PC_HERO.str += invest_skill[-1]
                PC_HERO.lp -= invest_skill[-1]
            elif invest_skill[0].lower() in include.dex_set:
                PC_HERO.dex += invest_skill[-1]
                PC_HERO.lp -= invest_skill[-1]
            elif invest_skill[0].lower() in include.int_set:
                PC_HERO.int += invest_skill[-1]
                PC_HERO.lp -= invest_skill[-1]
            elif invest_skill[0].lower() in include.cha_set:
                PC_HERO.cha += invest_skill[-1]
                PC_HERO.lp -= invest_skill[-1]

        print("\n")

        PC_HERO.printcharactersheet()
        PC_HERO_SAVED = PC_HERO
        char_slot = PC_HERO.name + ".dat"
        save_character = open(char_slot, "wb")
        # Save Characters
        pickle.dump(PC_HERO_SAVED, save_character)

def load_character(temp):
    PC_HERO.name = temp.name
    PC_HERO.guild = temp.guild
    PC_HERO.flags = temp.flags
    PC_HERO.level = temp.level
    PC_HERO.exp = temp.exp
    PC_HERO.exp_next = temp.exp_next
    PC_HERO.str = temp.str
    PC_HERO.dex = temp.dex
    PC_HERO.int = temp.int
    PC_HERO.cha = temp.cha
    PC_HERO.lp = temp.lp
    PC_HERO.hp = temp.hp
    PC_HERO.hp_max = temp.hp_max
    PC_HERO.antiochus_grave = temp.antiochus_grave
    PC_HERO.current_cell = temp.current_cell
    PC_HERO.inventory = temp.inventory
    PC_HERO.questlog = temp.questlog
    PC_HERO.knowndialogue = temp.knowndialogue
    PC_HERO.gold = temp.gold