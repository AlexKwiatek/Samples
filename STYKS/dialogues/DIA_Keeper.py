import include
import npc_list
import journal
import item_list
import leveling
import inventory
import vob_list
import fight
import map
import enemy_list
from hero import PC_HERO
from dialogue import AI_Output


def DIA_Keeper_First_Hello(other):
    if "i_choose_violence" in PC_HERO.flags:
        AI_Output(other,"Sukinsynu zostaw mnie!!! Ratunkuuu!")
        map.LOC_TOWER.vob.append(vob_list.VOB_TowerFire)
        npc_list.BDT_302_Keeper.dialogue_hello = DIA_Keeper_Post_Hello
        return
    if "sly_blackmail" in PC_HERO.flags:
        print("Weszliście ze Złym do środka Latarni. Zły odłożył towary przy wejściu i zwrócił się do ciebie")
        AI_Output(npc_list.BDT_307_Sly,"Dobra, masz pare minut, bierz co chcesz zabrać i wynośmy się stąd.")
    print("Latarnik zszedł po schodach głośno mówiąc")
    AI_Output(other,"Witajcie, macie dla mnie zapasy? W samą porę. Zostaniecie chwile? Nudno tu, chciałbym z kimś pogadać")
    AI_Output(other,"[Gdy zobaczył cie stanął jak wryty]")
    AI_Output(other,"Ty... stój gdzie jesteś, nie zbliżaj się do mnie! Alexis... Alexis ostrzegała mnie przed tobą!")
    if "sly_blackmail" in PC_HERO.flags:
        AI_Output(npc_list.BDT_307_Sly,"Nie zamierzam się w to mieszać. Idę po Bękarta")
        print("\nNim zdążyłeś zareagować, wyszedł i zamknął cie w Latarni")
    else:
        AI_Output(other,"POMOCY! Zawołajcie Koryntczyka! Ratunku!")
    map.LOC_FARM_ALLEY.locked = "locked"
    map.LOC_FARM_ALLEY.locked_reason = "To nie jest dobry pomysł"
    map.LOC_TOWER.vob.append(vob_list.VOB_TowerFire)
    npc_list.BDT_302_Keeper.dialogue_hello = DIA_Keeper_Post_Hello

def DIA_Keeper_Post_Hello(other):
    AI_Output(other,"POMOCYY!!!")

npc_list.BDT_302_Keeper.dialogue_hello = DIA_Keeper_First_Hello


def DIA_Keeper_Attack_Info(other):
    AI_Output(PC_HERO,"Zamknij się!")
    print("Latarnik nie bronił się. Upadł martwy po pierwszym ciosie.")
    other.HP = 0
    PC_HERO.flags.append("killed_keeper")
    PC_HERO.karma -= 1
    fight.kill(other,0)

def DIA_Keeper_Attack_Condition():
    return 1

DIA_Keeper_Attack = include.DIALOGUE(
    npc_list.BDT_302_Keeper,
    DIA_Keeper_Attack_Info,
    DIA_Keeper_Attack_Condition,
    0,
    "Zaatakuj"
)

