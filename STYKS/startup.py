import map
import npc_list
import enemy_list
import vob_list
import item_list

def startup():
    map.LOC_WAYSHRINE.npc = [npc_list.PC_ANTIOCHUS,npc_list.BDT_308_Bandit,npc_list.BDT_309_Bandit]
    map.LOC_BOATMAKER.vob = [vob_list.VOB_Booze_Stash]
    map.LOC_BOATMAKER.vob = [vob_list.VOB_Oars]
    map.LOC_CAVE.vob = [vob_list.VOB_Key_Boatmaker,vob_list.VOB_Riverside_Corpse]
    map.LOC_CAVE.monster = enemy_list.mst_lurker
    map.LOC_CAVE.monster_loc = """
W środku jaskini dostrzegasz wiele szczątków, zarówno ludzi jak i zwierząt. Twoje myśli nawiedza pytanie "Co stanie się z duszą jeśli umrze w zaświatach?"
Z rozważań wyciąga cie widok potwora. Jest to Topielec, łuskowata bestia potężnej postury i wzrostu. Warczy na ciebie a jego ślepia świecą w ciemności.
Wygląda na to że ktoś zadał bestii kilka ran zanim przyszedłeś...
    """
    map.LOC_RIVERSIDE.npc = [npc_list.VLK_100_Boatmaker]
    map.LOC_RIVERSIDE.vob = [vob_list.VOB_Boat]
    map.LOC_BOATMAKER.locked_key = item_list.itke_boatmaker_key
    map.LOC_GATE.npc = [npc_list.VLK_104_Wiseman]

    map.LOC_PRIORY_DOCK.vob = [vob_list.VOB_Fishing_Hole]
    map.LOC_PRIORY_DOCK.npc = [npc_list.VLK_105_Fisherman]
    map.LOC_PRIORY_GARDEN.vob = [vob_list.VOB_Dig_Site]
    map.LOC_PRIORY_GARDEN.npc = [npc_list.NOV_401_Acolyte]
    map.LOC_PRIORY_OUTSIDE.npc = [npc_list.NOV_402_Acolyte]
    map.LOC_PRIORY_OUTSIDE.vob = []
    map.LOC_PRIORY_GATE.npc = [npc_list.NOV_400_Gateguard]
    map.LOC_PRIORY.npc = [npc_list.KDF_200_Seer]
    map.LOC_PRIORY_BASEMENT.vob = [vob_list.VOB_Silver_Sword]
    map.LOC_ORACLE.npc = [npc_list.KDF_201_Oracle]
    map.LOC_PRIORY_WOOD.vob = [vob_list.VOB_Hunting_Spot]

    map.LOC_FARM.npc = [
        #npc_list.PC_ANTIOCHUS,
        npc_list.VLK_101_Phrixos,
        npc_list.BDT_303_Hunter,
        npc_list.VLK_103_Slave,
        npc_list.BDT_304_Vince
    ]
    map.LOC_FARM.vob = [vob_list.VOB_Usable_Sharpening_Stone]
    map.LOC_BASTARDS_HOME.npc = [npc_list.BDT_300_Bastard]
    map.LOC_FRESH_GRAVES.vob = [vob_list.VOB_Grave_Willow]
    map.LOC_UNBURIED.npc = [npc_list.BDT_301_Gravedigger]
    map.LOC_GRAVEDIGGER_HUT.vob = [vob_list.VOB_Gravedigger_Pendant]
    map.LOC_FARM_WOOD.vob = [vob_list.VOB_Wood_Pendant]
    map.LOC_FARM_WOOD.monster = enemy_list.mst_shadowbeast
    map.LOC_FARM_WOOD.monster_loc = """
Oddalasz się dość daleko od farmy, idąc w kierunku lasu. Cisza i brak żywych stworzeń zaczynają cię powoli niepokoić. Nagle słyszysz szelest w krzakach i ciche warknięcie.
Cieniostwór cicho przemyka się między drzewami. Masz jeszcze czas, możesz jeszcze odejść, powoli wycofać się. Bestia skoczy lada moment.
    """
    map.LOC_FARM_ALLEY.npc = [npc_list.BDT_305_Nico,npc_list.BDT_306_Fang,npc_list.BDT_307_Sly]
    map.LOC_FARM_ALLEY.vob = [vob_list.VOB_Tower_Door]
    map.LOC_TOWER.npc = [npc_list.BDT_302_Keeper]
    map.LOC_TOWER.vob = []
