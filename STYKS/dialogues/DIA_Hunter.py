import include
import npc_list
import journal
import item_list
import leveling
from hero import PC_HERO
from dialogue import AI_Output


def DIA_Hunter_First_Hello(other):
    print("Ubrany w lekką skórzaną zbroje, z emblematem Bękarta mężczyzna, mający agresywny wściekły wyraz twarzy\n")
    AI_Output(PC_HERO,"Witaj. Czym się tutaj zajmujesz?")
    AI_Output(other,"Biciem wieśniaków którzy zadają zbyt wiele pytań")
    AI_Output(PC_HERO,"Wyglądam ci na wieśniaka?")
    AI_Output(other,"Wyglądasz mi na idiote. Wypad!")
    other.dialogue_hello = DIA_Hunter_Post_Hello

def DIA_Hunter_Post_Hello(other):
    AI_Output(PC_HERO,"Jeszcze jedno...")
    AI_Output(other,"Mówiłem ci, spadaj!")

npc_list.BDT_303_Hunter.dialogue_hello = DIA_Hunter_First_Hello

def DIA_Hunter_Skill_Info(other):
    AI_Output(PC_HERO,"Czy możesz mnie czegoś nauczyć?")
    AI_Output(other,"Tak. Wypierdalania. WYPAD")

def DIA_Hunter_Skill_Condition():
    return 1

DIA_Hunter_Skill = include.DIALOGUE(
    npc_list.BDT_303_Hunter,
    DIA_Hunter_Skill_Info,
    DIA_Hunter_Skill_Condition,
    0,
    "Nauka Polowania"
)