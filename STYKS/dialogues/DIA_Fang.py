import include
import npc_list
import journal
import item_list
import leveling
import inventory
import haggle
import enemy_list
import trade
from hero import PC_HERO
from dialogue import AI_Output
import fight


def DIA_Fang_First_Hello(other):
    print("Przechodzisz obok chaty przy której siedzi bardzo gruby bandyta. Przy nim stoi długi stół na którym są różne przedmioty.")
    AI_Output(other,"Hej! Ty tam!")
    AI_Output(PC_HERO,"Kto? Ja?")
    AI_Output(other,"Nie! Twoja Babcia! Jasne że ty! Chcesz coś kupić?")
    other.dialogue_hello = DIA_Fang_Post_Hello

def DIA_Fang_Post_Hello(other):
    AI_Output(other,"Witaj! Przyszedłeś coś kupić? A może chcesz coś sprzedać?")

npc_list.BDT_306_Fang.dialogue_hello = DIA_Fang_First_Hello



def DIA_Fang_Trade_Info(other):
    AI_Output(PC_HERO,"Chciałbym kupić kilka drobiazgów")
    AI_Output(other,"Mam tu kilka drobiazgów na sprzedaż")
    trade.trade(PC_HERO,other)

npc_list.BDT_306_Fang.dialogue_trade = DIA_Fang_Trade_Info