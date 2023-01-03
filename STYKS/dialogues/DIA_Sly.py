import include
import npc_list
import journal
import item_list
import leveling
import inventory
import fight
import map
import enemy_list
from hero import PC_HERO
from dialogue import AI_Output


def DIA_Sly_First_Hello(other):
    print("''Sądząc po ubraniu jest to jeden z ludzi Bękarta. Ma czarne włosy i krótko przystrzyżoną brodę.\nNie wygląda na bardzo silnego czy postawnego, jednak ma coś w oczach co sugeruje że nie jest to człowiek z którym chciałoby się zadzierać.\n''\n")
    AI_Output(other,"Hej, widze cie tu pierwszy raz. Jesteś tu nowy, co?")
    AI_Output(PC_HERO,"Nie planuję zagrzać tu miejsca")
    AI_Output(other,"Tym lepiej. Jestem 'Zły' i mam robote dla kogoś kto nie zamierza tu zostać na dłużej")
    other.dialogue_hello = DIA_Sly_Post_Hello

def DIA_Sly_Post_Hello(other):
    if journal.SQ_Sly.queststage == "254":
        AI_Output(other,"TY OFIARO. KAZAŁEM CI TRZYMAĆ JĘZYK ZA ZĘBAMI!")
        AI_Output(other,"Zabiję cie!")
        print("\n[Zły wyciąga miecz i rzuca się na ciebie]")
        result = fight.startfight(PC_HERO,other)
        if result == "FAILURE":
            fight.kill(PC_HERO,1)
    else:
        AI_Output(other,"Z czym przychodzisz?")

npc_list.BDT_307_Sly.dialogue_hello = DIA_Sly_First_Hello


### Quest
#############
def DIA_Sly_Quest_Info(other):
    AI_Output(PC_HERO,"Jaką prace masz na myśli?")
    AI_Output(other,"Poznałeś może naszego Grabarza?")
    if PC_HERO.npcknowsinfo(DIA_Gravedigger_First_Hello):
        AI_Output(PC_HERO,"Tak")
        AI_Output(other,"A zatem wiesz że nie jest najostrzejszym mieczem w koszarach")
        AI_Output(other,"Połowe czasu wpatruje się jak sroka w gnat, drugą połowe spędza na krążeniu między grobami")
    else:
        AI_Output(PC_HERO,"Nie")
        AI_Output(other,"Zajmuje się u nas kopaniem grobów. Nikt istotny, naprawde")
    AI_Output(other,"Możnaby powiedzieć że to taki nasz wioskowy głupek")
    AI_Output(other,"Tym bardziej nie rozumiem jak wszedł w posiadanie tego czegoś")
    AI_Output(PC_HERO,"Co masz na myśli?")
    AI_Output(other,"Widziałem kiedyś w jego posiadaniu piękny amulet. Był pełen grawerowań i cudnych symboli a w jego środku - rubin wielkości... Eh...")
    AI_Output(other,"Chciałem go od niego odkupić, ale ten szaleniec nie chce mi go sprzedać.")
    AI_Output(PC_HERO,"Chcesz żebym go okradł")
    AI_Output(other,"Zrobiłbym to sam, ale nie chcę żeby staruch poszedł z płaczem do Bękarta")
    AI_Output(other,"Gdyby jednak amulet zniknął gdy ja będę cały dzień pił i grał kości z Nico...")
    AI_Output(PC_HERO,"Jeśli chcesz bym go pobił i okradł to...")
    AI_Output(other,"Nie sądze by to było konieczne. Przycisnąłem jednego z chłopków który pomagał Grabarzowi wnosić dzbany z winem do chaty")
    AI_Output(other,"Mówił, że widział że starzec trzyma amulet w domu, przy łóżku")
    AI_Output(other,"Wyceniam go na sto Oboli. Zastanów się dobrze. Ja myśle że pójdę dziś wieczorem zagrać z Nico w kości.")
    journal.SQ_Sly.status = "RUNNING"
    journal.SQ_Sly.queststage = 10
    print("## Nowy wpis w dzienniku...")

def DIA_Sly_Quest_Condition():
    return 1

DIA_Sly_Quest = include.DIALOGUE(
    npc_list.BDT_307_Sly,
    DIA_Sly_Quest_Info,
    DIA_Sly_Quest_Condition,
    0,
    "Praca"
)


def DIA_Sly_Amulet_Info(other):
    AI_Output(PC_HERO,"Mam twój amulet")
    AI_Output(other,"'Mój amulet' he he, lubie dźwięk tego słowa. Dobrze się spisałeś. Pewnie teraz chcesz swoją nagrodę?")
    journal.SQ_Sly.status = "COMPLETED"
    journal.SQ_Sly.queststage = 100
    leveling.give_exp(PC_HERO,50)
    PC_HERO.karma -= 1
    PC_HERO.flags.append("stolen_amulet")
    PC_HERO.inventory.remove(item_list.itmi_gravedigger_pendant)
    print("## Nowy wpis w dzienniku...")

def DIA_Sly_Amulet_Condition():
    if item_list.itmi_gravedigger_pendant in PC_HERO.inventory and journal.SQ_Sly.status == "RUNNING":
        return 1

DIA_Sly_Amulet = include.DIALOGUE(
    npc_list.BDT_307_Sly,
    DIA_Sly_Amulet_Info,
    DIA_Sly_Amulet_Condition,
    0,
    "Amulet"
)


def DIA_Sly_Reward_Info(other):
    AI_Output(PC_HERO,"Byłoby miło otrzymać obiecane sto Oboli")
    if "sly_angry" in PC_HERO.flags:
        AI_Output(other,"Ty to chyba jesteś głupi. WYNOŚ SIĘ.")
    else:
        AI_Output(other,"Bierz, dobrze się spisałeś!")
        inventory.add_gold(PC_HERO,100)
    PC_HERO.flags.append("sly_reward")

def DIA_Sly_Reward_Condition():
    if PC_HERO.npcknowsinfo(DIA_Sly_Amulet) and not "sly_reward" in PC_HERO.flags:
        return 1

DIA_Sly_Reward = include.DIALOGUE(
    npc_list.BDT_307_Sly,
    DIA_Sly_Reward_Info,
    DIA_Sly_Reward_Condition,
    0,
    "Pieniądze"
)


def DIA_Sly_Favor_Info(other):
    AI_Output(PC_HERO,"Zamiast pieniędzy, wolałbym przysługe")
    AI_Output(other,"No proszę mamy tu człowieka interesu widze")
    AI_Output(other,"Czego chcesz?")
    AI_Output(PC_HERO,"Latarnik ostatnio trenuje rzucanie nożami. Chcę byś zadbał by w następnej dostawie był nóż. Ostry.")
    AI_Output(other,"Ciekawa prośba. Rozmawiałeś z nim? Sam?")
    if PC_HERO.cha >= 15:
        AI_Output(PC_HERO,"Być może. Zawsze możemy udać że poprosił cie o to jeden z poprzednich pomocników")
        AI_Output(other,"Zgoda. Zrzucę wine na Nisosa, sukinsyn i tak gryzie ziemie")
        PC_HERO.flags.append("sly_reward")
        PC_HERO.flags.append("sly_knife")
    else:
        AI_Output(PC_HERO,"Nie. Przecież nie wpuściliby mnie do jego wieży.")
        AI_Output(other,"Tak myślałem. Nie wolałbyś jednak pieniędzy kolego?")

def DIA_Sly_Favor_Condition():
    #if PC_HERO.npcknowsinfo(DIA_Sly_Amulet) and not "sly_reward" in PC_HERO.flags:
     #   return 1
    return 0

DIA_Sly_Favor = include.DIALOGUE(
    npc_list.BDT_307_Sly,
    DIA_Sly_Favor_Info,
    DIA_Sly_Favor_Condition,
    0,
    "Przysługa"
)


def DIA_Sly_Blackmail_Info(other):
    AI_Output(PC_HERO,"Właściwie to chciałbym cie zaszantażować")
    AI_Output(other,"COOO...?")
    AI_Output(PC_HERO,"Masz się zgłosić na następnego dostawce towarów do Wieży")
    AI_Output(other,"W co ty grasz?")
    AI_Output(PC_HERO,"Masz to zrobić albo Bękart dowie się o twojej kradzieży")
    AI_Output(other,"To TWOJA kradzież, kolego")
    AI_Output(PC_HERO,"To ty masz amulet")
    AI_Output(other,"Zawsze mogę go schować albo wyrzucić")
    if PC_HERO.int > 10:
        AI_Output(PC_HERO,"Możesz. Ale jeśli dobrze pamiętam, próbowałeś go wcześniej kupić. Czy tego chcesz czy nie, jesteś podejrzany.")
        AI_Output(other,"Ty psie! Nie ośmielisz się...")
        AI_Output(PC_HERO,"Jeśli dorzucę do tego swoje zeznania...")
        AI_Output(other,"Dobra, DOBRA! Ale nie gwarantuje że się zgodzą na mój udział")
        AI_Output(PC_HERO,"Zrobisz to tak by się zgodzili. Inaczej Bękart się o wszystkim dowie.")
        PC_HERO.flags.append("sly_reward")
        PC_HERO.flags.append("sly_blackmail")
        map.LOC_TOWER.locked = "unlocked"
    else:
        AI_Output(other,"Wtedy to TY będziesz mieć kłopoty")
        AI_Output(other,"Dobrze ci radze chłopcze. Przemyśl to.")
        PC_HERO.flags.append("sly_angry")

def DIA_Sly_Blackmail_Condition():
    if PC_HERO.npcknowsinfo(DIA_Sly_Amulet) and not "sly_reward" in PC_HERO.flags:
        return 1

DIA_Sly_Blackmail = include.DIALOGUE(
    npc_list.BDT_307_Sly,
    DIA_Sly_Blackmail_Info,
    DIA_Sly_Blackmail_Condition,
    0,
    "Szantaż"
)



