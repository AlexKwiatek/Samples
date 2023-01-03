import include
import npc_list
import journal
import item_list
import leveling
import armwrestling
from hero import PC_HERO
from dialogue import AI_Output


def DIA_Vince_First_Hello(other):
    print("Mężczyzna o twarzy tępego osiłka siedzi na ławce. Bandaże wskazują na niedawne rany. Mimo nich, wygląda na bardzo zdrowego i silnego. Przez twarz biegnie mu okrutna blizna.\n")
    AI_Output(PC_HERO,"Witaj")
    AI_Output(other,"Witaj. Jestem Vince. Musisz być tutaj nowy. Tutejsi raczej się mnie boją")
    AI_Output(PC_HERO,"A mają powody?")
    AI_Output(other,"Nieeee... jestem łagodny jak baranek! Chodzi o moją morde!")
    other.dialogue_hello = DIA_Vince_Post_Hello

def DIA_Vince_Post_Hello(other):
    AI_Output(PC_HERO,"Witaj Vince")
    AI_Output(other,"Witaj. Masz coś do żarcia? Głodny jestem.")

npc_list.BDT_304_Vince.dialogue_hello = DIA_Vince_First_Hello


### Armwrestling Game
#############
def DIA_Vince_Armwrestling_Info(other):
    AI_Output(PC_HERO,"Widze że siedzisz tu cały czas. Nie nudzi ci się?")
    AI_Output(other,"Prawde mówiąc, troche tak. Nie chciałbyś sprawdzić się ze mną na rękę? Nikt z wieśniaków nie chce bo...")
    AI_Output(PC_HERO,"Bo się ciebie boją, wiem, mówiłeś.")
    AI_Output(other,"To jak będzie?")
    AI_Output(PC_HERO,"Nie sądzisz że to byłoby nieuczciwe w twoim stanie?")
    AI_Output(other,"Eee nie. Chyba że tchórzysz?")

def DIA_Vince_Armwrestling_Condition():
    return 1

DIA_Vince_Armwrestling = include.DIALOGUE(
    npc_list.BDT_304_Vince,
    DIA_Vince_Armwrestling_Info,
    DIA_Vince_Armwrestling_Condition,
    0,
    "Nudy"
)
def DIA_Vince_Play_Info(other):
    AI_Output(PC_HERO,"Sprawdźmy się")
    AI_Output(other,"To właśnie chciałem usłyszeć! Podwijaj rękawy!")
    result = armwrestling.armwrestling(PC_HERO,other)
    if result == "SUCCESS":
        AI_Output(other,"Arrr! Masz krzepe! Ale dasz się odegrać, prawda?")
        if "won_wrestling" in PC_HERO.flags:
            leveling.give_exp(PC_HERO,25)
        PC_HERO.flags.append("won_wrestling")
    else:
        AI_Output(other,"Ha! Jak widzisz nawet poturbowany, jestem silny jak tur!")

def DIA_Vince_Play_Condition():
    if PC_HERO.npcknowsinfo(DIA_Vince_Armwrestling):
        return 1

DIA_Vince_Play = include.DIALOGUE(
    npc_list.BDT_304_Vince,
    DIA_Vince_Play_Info,
    DIA_Vince_Play_Condition,
    1,
    "Sprawdźmy się"
)