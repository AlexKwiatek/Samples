from collections import defaultdict
import weakref
import math
import time
import os

# TODO: Class-Container i skrzynki. Ale to jak już oddam projekt
class NPC:
    def __init__(self, name, guild, level, exp, exp_next, hp_max, hp, str, dex, int, cha, lp, ):
        self.name = name
        self.guild = guild
        self.level = level
        self.exp = exp
        self.exp_next = exp_next
        self.hp_max = hp_max
        self.hp = hp
        self.str = str
        self.dex = dex
        self.int = int
        self.cha = cha
        self.lp = lp
        self.knowndialogue = []
        self.dialogues = []
        self.flags = []
        self.inventory = []
        self.antiochus_grave = 0
        self.karma = 0

    def printcharactersheet(self):
        printimportanttext("KARTA POSTACI")
        print("Imie: " + self.name)
        print("Klasa: " + guilds[self.guild])
        print("Poziom: " + str(self.level))
        print("Doświadczenie: " + str(self.exp) + "/" + str(self.exp_next))
        print("Punkty Nauki: " + str(self.lp))
        print(" ")
        print("Zdrowie: " + str(self.hp) + "/" + str(self.hp_max))
        print("Siła: " + str(self.str))
        print("Zręczność: " + str(self.dex))
        print("Inteligencja: " + str(self.int))
        print("Charyzma: " + str(self.cha))
        print(" ")
        if hasattr(self,"weapon"):
            print("Obrażenia broni: " + str(self.weapon.dmg))
        else:
            print("Obrażenia Broni: BRAK")
        if hasattr(self,"armor"):
            print("Ochrona przed bronią: " + str(self.armor.armor))
        else:
            print("Ochrona przed bronią: BRAK")

    def npcknowsinfo(self, info):
        if info in self.knowndialogue:
            return 1
        else:
            return 0

    def marvin(self):
        if hasattr(self,"marvinmode"):
            return 1
        else:
            return 0

    def is_dead(self):
        if self.hp == 0:
            return 1
        else:
            return 0

class VOB:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

class ITEM:
    def __init__(self, name, type, desc):
        self.name = name
        self.type = type
        self.desc = desc
        self.flags = []

class DIALOGUE:
    def __init__(self, NPC, info, condition, permanent, description):
        NPC.dialogues.append(self)
        self.description = description
        self.permanent = permanent
        self.info = info
        self.condition = condition


class QUEST:
    __refs__ = defaultdict(list)
    def __init__(self, name, queststage, status, dict):
        self.name = name # Name of quest
        self.queststage = queststage # Stage
        self.status = status # Completion status
        self.dict = dict
        self.__refs__[self.__class__].append(weakref.ref(self))

    @classmethod
    def get_instances(cls):
        for inst_ref in cls.__refs__[cls]:
            inst = inst_ref()
            if inst is not None:
                yield inst
    def get_current_objective(self):
        stage = str(self.queststage)
        return self.dict[stage]
    def get_quest_description(self):
        return self.dict["desc"]


class CELL:
    __refs__ = defaultdict(list)
    def __init__(self, name, locked):
        self.name = name # Name of location
        self.locked = locked # Locked Status
        # Non-inited: Connected Cells = [LIST]
        # Non-inited: NPCs
        # Non-inited: Hostile Mob Guardian (propably only one per location as my combat system do not include 2v1 fight) #TODO: Yet.
        self.__refs__[self.__class__].append(weakref.ref(self))

    def show_loc_desc(self):  # Show Cell's description, based on the ID
        loc_desc = os.path.dirname(__file__) + "/locations/" + self.name + ".txt"
        desc_file = open(loc_desc, 'r', encoding="utf-8")
        print(desc_file.read())

    @classmethod
    def get_instances(cls):
        for inst_ref in cls.__refs__[cls]:
            inst = inst_ref()
            if inst is not None:
                yield inst

class REGION:
    def __init__(self, name, cells):
        self.name = name
        self.name = cells

queststatus = {
    "RUNNING":"Active",
    "COMPLETED":"Finished",
    "FAILED":"Failed"
}
questname = {
    "MQ1":"Main Quest 1",
    "SQ1":"Side Quest 1",
    "SQ2":"Side Quest 2"
}

guilds = {
    "peltist":"Peltasta",
    "hoplite":"Hoplita",
    "companion":"Towarzysz"
}
guilds_desc = {
    "peltist":"- - - \nLekka piechota zajmująca się głównie zwiadem i krótkimi dystansowymi starciami, które mają dać czas na uformowanie się falangi\n",
    "hoplite":"- - - \nOsławiona Macedońska Falanga. Zawodowi żołnierze, zdyscyplinowani i nie do zatrzymania gdy maszerują w kierunku wroga\n",
    "companion":"- - - \nCiężka jazda złożona ze szlacheckich synów i macedońskiej śmietanki towarzyskiej. Szkoleni zarówno w walce jak i w dyplomacji i towarzyskim obyciu\n"
}
yes_set = (
    "yes", "tak", "da", "no raczej", "no kurwa", "można, jak najbardziej", "jeszcze jak", "sheet negro, that's all you had to say", "chętnie", "jak najbardziej", "można, jak najbardziej, jeszcze jak"
)
no_set = (
    "nie", "no", "nei", "oj nie nie byczq, -1", "nie, dziękuję"
)
maybe_set = (
    "może", "maybe", "chyba", "i'm not sure", "depends", "to zależy"
)
undecided_set = (
    "średnio", "troche", "kinda"
)
left_set = (
    "lewo", "left", "l", "a"
)
right_set = (
    "prawo", "right", "p", "d"
)
up_set = (
    "góra", "up", "offence", "ofensywa", "off", "w"
)
down_set = (
    "dół", "down", "defense", "defensywa", "obrona", "def", "s"
)
forward_set = (
    "forward","przód"
)
backward_set = (
    "backward","tył"
)
trade_set = (
    "handel", "trade"
)
save_set = (
    "zapis", "zapisz", "save"
)
load_set = (
    "wczytaj", "load"
)
stance_dict = {
    "left":"Lewo",
    "right":"Prawo",
    "up":"Góra",
    "down":"Dół",
    "none":"Brak"
}
str_set = (
    "str", "siła", "strength"
)
dex_set = (
    "dex", "zręczność", "dexterity"
)
int_set = (
    "int", "inteligencja", "intelligence"
)
cha_set = (
    "cha", "charyzma", "charisma"
)
back_set = (
    "back", "powrót", "tył", "take me home to the place i belong"
)
end_set = (
    "ende", "exit", "koniec", "wypierdalaj"
)
destroy_set = (
    "destroy","wyrzuć","zniszcz","rozpapież","wywojtyl","throw"
)

help_fight_loc = """
    -- Zręcznośc bohaterów liczy się do tego kto dał rade trafić przeciwnika, siła wlicza się do zadanych obrażeń
    -- Jakość broni liczy się do zadawanych obrażeń. Jakość pancerza zmniejsza otrzymane obrażenia
    -- W walce poza statystykami bohatera, liczy się też wybór postawy
    - Są cztery postawy. Lewo, Prawo, Góra, Dół
    - Postawa Lewo pokonuje postawe Dół, przegrywa z postawą Góra
    - Postawa Góra pokonuje postawe Lewo, przegrywa z postawą Prawo
    - Postawa Prawo pokonuje postawe Góra, przegrywa z postawą Dół
    - Postawa Dół pokonuje postawe Prawo, przegrywa z postawą Lewo
    - Jeśli walczący wybiorą tą samą postawe, nie zadadzą sobie obrażeń
    - Jeśli natomiast wybiorą przeciwną postawe (Lewo-Prawo, Góra-Dół) zadadzą sobie podwójne obrażenia
    - Różne istoty walczą w różny sposób. Ludzie wybierają style walki mniej więcej równo, natomiast zwierzęta mogą preferować konkretny, powtarzalny atak
"""

def printimportanttext(text):
    print("\n####" + "#" * len(text) + "####")
    print("# # " + text + " # #")
    print("####" + "#" * len(text) + "####\n")


def stringify(list):
    str = ""
    for element in list:
        str += element
    return str