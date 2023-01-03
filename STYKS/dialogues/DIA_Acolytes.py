import journal
from hero import PC_HERO
import npc_list
from dialogue import AI_Output


def DIA_Novice_First_Hello(other):
    AI_Output(other,"Proszę zostaw mnie. Muszę się skupić na moich studiach")

npc_list.NOV_401_Acolyte.dialogue_hello = DIA_Novice_First_Hello
