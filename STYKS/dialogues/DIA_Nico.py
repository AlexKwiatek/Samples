import include
import npc_list
import journal
import item_list
import leveling
import inventory
import play_dice
import enemy_list
from hero import PC_HERO
from dialogue import AI_Output


def DIA_Nico_First_Hello(other):
    print("''Siedzi przed tobą młodo wyglądający mężczyzna w wytartej skórzanej zbroi. Do ramienia ma przypiętą blaszke z wyrytym symbolem chłopaków Bękarta.\nObok niego na stole leżą dwa kubeczki i skórzany woreczek. Ani chybi z kośćmi do gry.\nBandaż na czole sugeruje niedawno odniesione rany''\n")
    AI_Output(other,"Hej! Nowa twarz!")
    AI_Output(other,"Jestem Nico. Nie wyglądasz mi na kogoś kto szuka pracy w polu. Co tutaj robisz?")
    AI_Output(PC_HERO,"Jestem tu tylko przejazdem. Podróżuję do miejsca które jest niedaleko.")
    AI_Output(other,"Rozumiem że masz jakieś imie, tak? [spytał z uśmiechem]")
    AI_Output(PC_HERO,PC_HERO.name)
    AI_Output(other,"W takim razie miło mi cię poznać " + PC_HERO.name)
    other.dialogue_hello = DIA_Nico_Post_Hello

def DIA_Nico_Post_Hello(other):
    AI_Output(other,"''Kalimera'' przyjacielu")
    AI_Output(PC_HERO,"''Kalimera''")

npc_list.BDT_305_Nico.dialogue_hello = DIA_Nico_First_Hello



### Dice Game
#############
def DIA_Nico_Dice_Info(other):
    AI_Output(PC_HERO,"Widze że grywasz w kości")
    AI_Output(other,"Dobrze widzisz! Jeśli chcesz ze mną zagrać mów śmiało!")
    AI_Output(other,"Ale ostrzegam. Gram tylko na pieniądze! Bez stawki jest nudno")

def DIA_Nico_Dice_Condition():
    return 1

DIA_Nico_Dice = include.DIALOGUE(
    npc_list.BDT_305_Nico,
    DIA_Nico_Dice_Info,
    DIA_Nico_Dice_Condition,
    0,
    "Kości"
)


def DIA_Nico_DiceSecret_Info(other):
    AI_Output(PC_HERO,"Grywasz też o fanty?")
    AI_Output(other,"To zależy jakie")
    if PC_HERO.cha > 20:
        AI_Output(other,"Chyba nie chcesz mi zaoferować gry o ubrania? [śmieje się]")
    AI_Output(PC_HERO,"Myślałem o grze na sekrety")
    AI_Output(other,"Chcesz żebym ci wygadał brudne sekreciki naszych chłopców?")
    AI_Output(PC_HERO,"Albo kto ma pewien przedmiot.")
    AI_Output(other,"[Uśmiech natychmiast znikł z twarzy łotrzyka] Nie. Domyślam się czego szukasz. Nie chcę się w to mieszać.")

def DIA_Nico_DiceSecret_Condition():
    if PC_HERO.npcknowsinfo(DIA_Nico_Dice) and PC_HERO.npcknowsinfo(DIA_Phrixos_Lighthouse):
        return 1

DIA_Nico_DiceSecret = include.DIALOGUE(
    npc_list.BDT_305_Nico,
    DIA_Nico_DiceSecret_Info,
    DIA_Nico_DiceSecret_Condition,
    0,
    "Gra o sekrety"
)


def DIA_Nico_LetsPlay_Info(other):
    AI_Output(PC_HERO,"Chcę zagrać w kości")
    if other.gold == 0:
        AI_Output(other,"Przykro mi " + PC_HERO.name + " ograłeś mnie już z wszystkiego co mam!")
        return
    else:
        pass
    AI_Output(other,"W porządku!")
    AI_Output(other,"O ile gramy?")
    amount = input()
    try:
        amount = int(amount)
    except:
        return
    AI_Output(PC_HERO,str(amount) + " Oboli")
    if amount > other.gold:
        AI_Output(other,"Przykro mi przyjacielu, mam tylko " + str(other.gold))
        AI_Output(PC_HERO,"Dobrze, możemy zagrać o tyle")
        amount = other.gold
    if amount > PC_HERO.gold:
        AI_Output(other,"Pokaż najpierw pieniądze przyjacielu")
        if PC_HERO.gold == 0:
            AI_Output(PC_HERO,"Zapomniałem ich wziąć ze sobą. Zaraz wróce")
            AI_Output(other,"To wróć jak będziesz miał przyjacielu.")
            return
        else:
            AI_Output(other,"Wygląda na to że brakuje ci trochę!")
            AI_Output(other,"Zagrajmy o to ile masz")
            amount = PC_HERO.gold
    AI_Output(other,"To gramy?")
    command = input()
    AI_Output(PC_HERO,command)
    if command.lower() in include.yes_set:
        pass
    else:
        AI_Output(other,"Nie, to nie! Może innym razem!")
        return
    if play_dice.throw_dice(PC_HERO, other) == 1:
        AI_Output(other,"Nieźle, wygrałeś pierwszą runde!")
        input()
        if play_dice.throw_dice(PC_HERO, other) == 1:
            AI_Output(other,"A niech cie! Wygrałeś!")
            input()
            other.gold -= amount
            inventory.add_gold(PC_HERO,amount)
        else:
            AI_Output(other,"Ha! Są emocje! Pora na finał!")
            input()
            if play_dice.throw_dice(PC_HERO, other) == 1:
                AI_Output(other,"A niech cie! Wygrałeś!")
                input()
                other.gold -= amount
                inventory.add_gold(PC_HERO,amount)
            else:
                AI_Output(other,"Nie masz szczęścia przyjacielu! Może uda ci sie następnym razem!")
                input()
                other.gold += amount
                inventory.remove_gold(PC_HERO,amount)
    else:
        AI_Output(other,"Pierwsza runda moja! Ale masz jeszcze szanse!")
        input()
        if play_dice.throw_dice(PC_HERO, other) == 0:
            AI_Output(other,"Druga również! Nie masz szczęścia przyjacielu")
            input()
            other.gold += amount
            inventory.remove_gold(PC_HERO,amount)
        else:
            AI_Output(other,"Ha! Są emocje! Pora na finał!")
            input()
            if play_dice.throw_dice(PC_HERO, other) == 1:
                AI_Output(other,"A niech cie! Wygrałeś!")
                input()
                other.gold -= amount
                inventory.add_gold(PC_HERO,amount)
            else:
                AI_Output(other,"Nie masz szczęścia przyjacielu! Może uda ci sie następnym razem!")
                input()
                other.gold += amount
                inventory.remove_gold(PC_HERO,amount)


def DIA_Nico_LetsPlay_Condition():
    if PC_HERO.npcknowsinfo(DIA_Nico_Dice):
        return 1

DIA_Nico_LetsPlay = include.DIALOGUE(
    npc_list.BDT_305_Nico,
    DIA_Nico_LetsPlay_Info,
    DIA_Nico_LetsPlay_Condition,
    1,
    "Zagrajmy"
)

### Shadowbeast Quest
#####################
def DIA_Nico_Shadowbeast_Info(other):
    AI_Output(PC_HERO,"Słyszałem że walczyłeś z bestią z pobliskiego lasu")
    AI_Output(other,"'Walczyłem' pha... to dużo powiedziane. Koryntczyk wysłał nas byśmy ją zabili, ale nie spodziewaliśmy się że będzie taka wielka")
    AI_Output(PC_HERO,"Co to za potwór?")
    AI_Output(other,"Cieniostwór. Wielki włochaty kot, z łapami jak świńskie półtusze i pazurami jak sztylety.")
    if journal.SQ_Death_Within_Death.status == "RUNNING":
        AI_Output(PC_HERO,"Bękart wspominał też że musiał prosić swoją wiedźme by was wskrzesiła")
        AI_Output(other,"Jeśli tak mówił to pewnie tak było")
        AI_Output(PC_HERO,"A jaka jest twoja wersja?")
        AI_Output(other,"Nie mam wersji. Gdy potwór na mnie skoczył straciłem przytomność. Odzyskałem ją na stole w chacie Koryntczyka")
        AI_Output(PC_HERO,"Więc mogłeś po prostu stracić przytomność od utraty krwii?")
        AI_Output(other,"Możliwe. Wiedźmy i wskrzeszenia nie są na moją głowe przyjacielu.")
    AI_Output(other,"Czemu właściwie cie to interesuje?")
    AI_Output(PC_HERO,"Bękart chce mi zapłacić za pozbycie się jej")
    AI_Output(other,"Pracujesz dla Koryntczyka? No prosze. Może za niedługo będziesz jednym z nas!")

def DIA_Nico_Shadowbeast_Condition():
    if PC_HERO.npcknowsinfo(DIA_Bastard_Quest) and journal.SQ_Bastards_Man.status == "RUNNING":
        return 1

DIA_Nico_Shadowbeast = include.DIALOGUE(
    npc_list.BDT_305_Nico,
    DIA_Nico_Shadowbeast_Info,
    DIA_Nico_Shadowbeast_Condition,
    0,
    "Cieniostwór"
)


def DIA_Nico_ShadowbeastDead_Info(other):
    AI_Output(PC_HERO,"Pamiętasz bestie która cie zaatakowała w lesie?")
    AI_Output(other,"Coś takiego trudno zapomnieć przyjacielu")
    AI_Output(PC_HERO,"Nie żyje")
    AI_Output(other,"No prosze. Jesteś ulepiony z twardej gliny.")

def DIA_Nico_ShadowbeastDead_Condition():
    if enemy_list.mst_shadowbeast.hp == 0:
        return 1

DIA_Nico_ShadowbeastDead = include.DIALOGUE(
    npc_list.BDT_305_Nico,
    DIA_Nico_ShadowbeastDead_Info,
    DIA_Nico_ShadowbeastDead_Condition,
    0,
    "Cieniostwór"
)

