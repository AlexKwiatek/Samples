import hero
import npc_list
import map
import item_list
import vob_list
import journal
import pickle

def save_game(saveslot):
    save_list = [
        hero.PC_HERO,
        map.LOC_CAVE,
        map.LOC_RIVERSIDE,
        map.LOC_WAYSHRINE,
        map.LOC_BOATMAKER,
        map.LOC_GATE,
        map.LOC_HIGHWAY_CH1,
        map.LOC_CHAPTER2_BOAT,
        map.LOC_PRIORY_OUTSIDE,
        map.LOC_PRIORY_DOCK,
        map.LOC_PRIORY,
        map.LOC_PRIORY_WOOD,
        map.LOC_PRIORY_BASEMENT,
        map.LOC_PRIORY_GARDEN,
        map.LOC_PRIORY_GATE,
        map.LOC_TOWER,
        map.LOC_UNBURIED,
        map.LOC_BASTARDS_HOME,
        map.LOC_FARM_ALLEY,
        map.LOC_FARM_WOOD,
        map.LOC_FARM,
        map.LOC_ORACLE,
        map.LOC_GRAVEDIGGER_HUT,
        map.LOC_FRESH_GRAVES,

        # Save Characters
        npc_list.PC_ANTIOCHUS,
        npc_list.VLK_100_Boatmaker,
        npc_list.VLK_101_Phrixos,
        npc_list.VLK_102_Blacksmith,
        npc_list.VLK_103_Slave,
        npc_list.VLK_104_Wiseman,
        npc_list.VLK_105_Fisherman,
        npc_list.KDF_202_Oracle_Voice,
        npc_list.KDF_201_Oracle,
        npc_list.KDF_200_Seer,
        npc_list.BDT_300_Bastard_Lantern,
        npc_list.BDT_300_Bastard,
        npc_list.BDT_301_Gravedigger,
        npc_list.BDT_302_Keeper,
        npc_list.BDT_303_Hunter,
        npc_list.BDT_304_Vince,
        npc_list.BDT_305_Nico,
        npc_list.BDT_306_Fang,
        npc_list.BDT_307_Sly,
        npc_list.BDT_308_Bandit,
        npc_list.BDT_309_Bandit,
        npc_list.PC_ANTIOCHUS_Lantern,
        npc_list.NOV_400_Gateguard,
        npc_list.NOV_401_Acolyte,
        npc_list.NOV_402_Acolyte,

        # Save Quests
        journal.MQ01,
        journal.MQ_Oracle,
        journal.MQ_Bastard,
        journal.SQ_Boatmaker_01,
        journal.SQ_Boatmaker_02,
        journal.SQ_Sly,
        journal.SQ_Gatekeeper,
        journal.SQ_Bastards_Man,
        journal.SQ_Death_Within_Death,

        # Save EQ
        item_list.itwp_sword_0,
        item_list.itwp_sword_1,
        item_list.itwp_sword_2,
        item_list.itwp_sword_silver,
        item_list.itar_bdt_l,
        item_list.itar_grd_l,
    ]
    print(saveslot)
    with open(saveslot, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(save_list, output, pickle.HIGHEST_PROTOCOL)

def load_game(saveslot):
    with open(saveslot, 'rb') as input:  # Overwrites any existing file.
        save_list = pickle.load(input)

        hero.PC_HERO = save_list[0]
        map.LOC_CAVE = save_list[1]
        map.LOC_RIVERSIDE = save_list[2]
        map.LOC_WAYSHRINE = save_list[3]
        map.LOC_BOATMAKER = save_list[4]
        map.LOC_GATE = save_list[5]
        map.LOC_HIGHWAY_CH1 = save_list[6]
        map.LOC_CHAPTER2_BOAT = save_list[7]
        map.LOC_PRIORY_OUTSIDE = save_list[8]
        map.LOC_PRIORY_DOCK = save_list[9]
        map.LOC_PRIORY = save_list[10]
        map.LOC_PRIORY_WOOD = save_list[11]
        map.LOC_PRIORY_BASEMENT = save_list[12]
        map.LOC_PRIORY_GARDEN = save_list[13]
        map.LOC_PRIORY_GATE = save_list[14]
        map.LOC_TOWER = save_list[15]
        map.LOC_UNBURIED = save_list[16]
        map.LOC_BASTARDS_HOME = save_list[17]
        map.LOC_FARM_ALLEY = save_list[18]
        map.LOC_FARM_WOOD = save_list[19]
        map.LOC_FARM = save_list[20]
        map.LOC_ORACLE = save_list[21]
        map.LOC_GRAVEDIGGER_HUT = save_list[22]
        map.LOC_FRESH_GRAVES = save_list[23]

        # Save Characters
        npc_list.PC_ANTIOCHUS = save_list[24]
        npc_list.VLK_100_Boatmaker = save_list[25]
        npc_list.VLK_101_Phrixos = save_list[26]
        npc_list.VLK_102_Blacksmith = save_list[27]
        npc_list.VLK_103_Slave = save_list[28]
        npc_list.VLK_104_Wiseman = save_list[29]
        npc_list.VLK_105_Fisherman = save_list[30]
        npc_list.KDF_202_Oracle_Voice = save_list[31]
        npc_list.KDF_201_Oracle = save_list[32]
        npc_list.KDF_200_Seer = save_list[33]
        npc_list.BDT_300_Bastard_Lantern = save_list[34]
        npc_list.BDT_300_Bastard = save_list[35]
        npc_list.BDT_301_Gravedigger = save_list[36]
        npc_list.BDT_302_Keeper = save_list[37]
        npc_list.BDT_303_Hunter = save_list[38]
        npc_list.BDT_304_Vince = save_list[39]
        npc_list.BDT_305_Nico = save_list[40]
        npc_list.BDT_306_Fang = save_list[41]
        npc_list.BDT_307_Sly = save_list[42]
        npc_list.BDT_308_Bandit = save_list[43]
        npc_list.BDT_309_Bandit = save_list[44]
        npc_list.PC_ANTIOCHUS_Lantern = save_list[45]
        npc_list.NOV_400_Gateguard = save_list[46]
        npc_list.NOV_401_Acolyte = save_list[47]
        npc_list.NOV_402_Acolyte = save_list[48]

        # Save Quests
        journal.MQ01 = save_list[49]
        journal.MQ_Oracle = save_list[50]
        journal.MQ_Bastard = save_list[51]
        journal.SQ_Boatmaker_01 = save_list[52]
        journal.SQ_Boatmaker_02 = save_list[53]
        journal.SQ_Sly = save_list[54]
        journal.SQ_Gatekeeper = save_list[55]
        journal.SQ_Bastards_Man = save_list[56]
        journal.SQ_Death_Within_Death = save_list[57]

        # Save EQ
        item_list.itwp_sword_0 = save_list[58]
        item_list.itwp_sword_1 = save_list[59]
        item_list.itwp_sword_2 = save_list[60]
        item_list.itwp_sword_silver = save_list[61]
        item_list.itar_bdt_l = save_list[62]
        item_list.itar_grd_l = save_list[63]
        print(hero.PC_HERO.name)

def load_item(item, saveslot):
    with open(saveslot, 'rb') as input:  # Overwrites any existing file.
        item = pickle.load(input)
        return item