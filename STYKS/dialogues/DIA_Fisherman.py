import include
import npc_list
import journal
import item_list
import inventory
import map
import trade
from hero import PC_HERO
from dialogue import AI_Output


def DIA_Fisherman_First_Hello(other):
    AI_Output(PC_HERO,"Witaj dobry człowieku")
    AI_Output(other,"Chcesz coś kupić? A może chcesz coś sprzedać?")

npc_list.VLK_105_Fisherman.dialogue_hello = DIA_Fisherman_First_Hello


def DIA_Fisherman_Info(other):
    AI_Output(PC_HERO,"Pokaż co tam masz")
    #other.goods.append(itmi_bait)
    trade.trade(PC_HERO,other)

npc_list.VLK_105_Fisherman.dialogue_trade = DIA_Fisherman_Info