import include
import npc_list
import journal
import item_list
import inventory
import map
import leveling
from hero import PC_HERO
from dialogue import AI_Output

def DIA_Gatekeeper_First_Hello(other):
    AI_Output(npc_list.PC_ANTIOCHUS,"Witaj dobry człowieku, może otworzyłbyś brame?")
    AI_Output(other,"[Odźwierny przeciągnął się i oparł na halabardzie] Niestety panowie, mam rozkazy od zarządcy by sprawdzać nowoprzybyłych")
    AI_Output(PC_HERO,"Więc sprawdzaj")
    AI_Output(other,"Kto, ja? Oj nie nie, miałem na myśli że to zarządca wyjdzie i sprawdzi")
    AI_Output(npc_list.PC_ANTIOCHUS,"To go zawołaj?")
    AI_Output(other,"Ja? Panowie, żarty sobie stroicie, zarządca wielki pan, ja tu tylko furty pilnuje.")
    AI_Output(other,"Moge przekazać wieść że nowi ludzie chcą audiencji u Wyroczni ale wyjdzie on w swoim czasie")
    AI_Output(PC_HERO,"A ile to może potrwać?")
    AI_Output(other,"Bo ja wiem... z reguły tydzień, czasem dwa...")
    AI_Output(npc_list.PC_ANTIOCHUS,"Dwa tygodnie?!")
    AI_Output(other,"Jak mówie. Wielki pan, a wyrocznia ważna sprawa. Mówił żeby tych no... miętkich duchem odsiać.")
    AI_Output(PC_HERO,"'Miętkich duchem'...")

    other.dialogue_hello = DIA_Gatekeeper_Post_Hello

def DIA_Gatekeeper_Post_Hello(other):
    AI_Output(other,"Noooo...?")

npc_list.NOV_400_Gateguard.dialogue_hello = DIA_Gatekeeper_First_Hello

def DIA_Gatekeeper_Quest_Info(other):
    AI_Output(PC_HERO,"Może zrobisz wyjątek? Jak już będziemy w środku to sami przekonamy zarządce że jesteśmy w porządku")
    AI_Output(other,"No nie wiem... To wbrew regułom... Wpuszczam tylko jak wieśniacy z wsi z rybami albo mięsem...")
    AI_Output(PC_HERO,"O widzisz! To powiedzmy że przyszedłem z rybami.")
    AI_Output(other,"Przecież nie przyszedłeś")
    AI_Output(npc_list.PC_ANTIOCHUS,"[Antiochus podrapał się w skroń zrezygnowany]")
    journal.SQ_Gatekeeper.status = "RUNNING"
    journal.setstage(journal.SQ_Gatekeeper,10)

def DIA_Gatekeeper_Quest_Condition():
    return 1

DIA_Gatekeeper_Quest = include.DIALOGUE(
    npc_list.NOV_400_Gateguard,
    DIA_Gatekeeper_Quest_Info,
    DIA_Gatekeeper_Quest_Condition,
    0,
    "Wyjątek"
)

def DIA_Gatekeeper_Fish_Info(other):
    AI_Output(PC_HERO,"Prosze, oto ryby. A teraz wpuść mnie.")
    AI_Output(other,"No dobrze. Mam nadzieje że nie będę tego żałować")
    AI_Output(other,"Yhym... OOOO JAKA PIĘKNA RYBA. CHYBA MUSZE WAM OTWORZYC BRAME")
    AI_Output(PC_HERO,"DZIĘKUJEMY DOBRY CZŁOWIEKU. PROSZE, OTO NASZA RYBA")
    inventory.destroy_item(PC_HERO,item_list.itfo_fish)
    journal.SQ_Gatekeeper.status = "COMPLETED"
    journal.setstage(journal.SQ_Gatekeeper,100)
    leveling.give_exp(PC_HERO,50)
    map.LOC_PRIORY_OUTSIDE.locked = "unlocked"

def DIA_Gatekeeper_Fish_Condition():
    if item_list.itfo_fish in PC_HERO.inventory and PC_HERO.npcknowsinfo(DIA_Gatekeeper_Quest) and journal.SQ_Gatekeeper.status == "RUNNING":
        return 1

DIA_Gatekeeper_Fish = include.DIALOGUE(
    npc_list.NOV_400_Gateguard,
    DIA_Gatekeeper_Fish_Info,
    DIA_Gatekeeper_Fish_Condition,
    0,
    "Ryby"
)

def DIA_Gatekeeper_Meat_Info(other):
    AI_Output(PC_HERO,"Prosze, oto mięso. A teraz wpuść mnie.")
    AI_Output(other,"No dobrze. Mam nadzieje że nie będę tego żałować")
    AI_Output(other,"Yhym... OOOO JAKI PIĘKNY KAWAL DZICZYZNY. CHYBA MUSZE WAM OTWORZYC BRAME")
    AI_Output(PC_HERO,"DZIĘKUJEMY DOBRY CZŁOWIEKU. PROSZE, OTO NASZA DZICZYZNA")
    inventory.destroy_item(PC_HERO,item_list.itfo_venison)
    journal.SQ_Gatekeeper.status = "COMPLETED"
    journal.setstage(journal.SQ_Gatekeeper,100)
    leveling.give_exp(PC_HERO,50)
    map.LOC_PRIORY_OUTSIDE.locked = "unlocked"

def DIA_Gatekeeper_Meat_Condition():
    if item_list.itfo_venison in PC_HERO.inventory and PC_HERO.npcknowsinfo(DIA_Gatekeeper_Quest) and journal.SQ_Gatekeeper.status == "RUNNING":
        return 1

DIA_Gatekeeper_Meat = include.DIALOGUE(
    npc_list.NOV_400_Gateguard,
    DIA_Gatekeeper_Meat_Info,
    DIA_Gatekeeper_Meat_Condition,
    0,
    "Dziczyzna"
)

