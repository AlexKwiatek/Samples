import include
import map
import journal
import inventory
import dialogue
import fight
import item_list
import leveling
import character_creation
import startup
import os.path
import prologue
import lockpicking
import pickle
import npc_list
import save_game
import dialogues
from dialogues import *
from hero import PC_HERO
import hero

help_loc = """
    -- By pójść gdzieś, wpisz nazwe lokacji
    -- By porozmawiać z NPC, wpisz imie NPC
    -- By użyć obiektu, wpisz jego nazwe
    -- By uzyskać dostęp do interfejsów wpisz: Dziennik; Ekwipunek; Postać
"""


def game():
    while True:
        vob_ids = []
        vob_names = []
        npc_ids = []
        npc_names = []
        location_npcs = {}
        location_vobs = {}
        location_ids = []
        location_names = []
        for cell in include.CELL.get_instances():
            location_ids.append(cell)
            location_names.append(cell.name.lower())

        location_locs = dict(zip(location_names, location_ids))
        print("\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ")
        print("\n####" + "#" * len(PC_HERO.current_cell.name) + "####")
        print("### " + PC_HERO.current_cell.name + " ###")
        print("[Ekwipunek][Postać][Dziennik][Opis][Pomoc]")
        fight.get_health_bar(PC_HERO)
        print("Kierunki: ")
        for location in PC_HERO.current_cell.connected:
            location = map.loc_objects_dict[location]
            print("# " + location.name)
        print("\n##################")
        if hasattr(PC_HERO.current_cell, "npc") and PC_HERO.current_cell.npc:
            print("# Postaci: ")
            for npc in PC_HERO.current_cell.npc:
                if npc.is_dead() == 1:
                    print(npc.name + " -- [MARTWY]")
                else:
                    print(npc.name)

                npc_ids.append(npc)
                npc_names.append(npc.name.lower())
            location_npcs = dict(zip(npc_names, npc_ids))
            print(" ")
        if hasattr(PC_HERO.current_cell, "vob") and PC_HERO.current_cell.vob:
            print("# Przedimoty: ")
            for vob in PC_HERO.current_cell.vob:
                vob_ids.append(vob)
                vob_names.append(vob.name.lower())
                if hasattr(vob,"illegal") and vob.illegal == 1:
                    print(vob.name + " -- [KRADZIEŻ]")
                else:
                    print(vob.name)

            location_vobs = dict(zip(vob_names, vob_ids))
        command = input()
        connectlist = [] #map.loc_objects_dict[PC_HERO.current_cell.connected]
        for x in PC_HERO.current_cell.connected:
            connection = map.loc_objects_dict[x]
            connectlist.append(connection)
        if command.lower() in include.end_set:
            command = input("Czy jesteś pewien? ").lower()
            if command in include.yes_set:
                exit()
        if command.lower() in include.save_set:
            print("Wybież numer zapisu")
            while True:
                saveslot = input()
                try:
                    saveslot = int(saveslot)
                    saveslot = "saveslot" + str(saveslot) + ".dat"
                    break
                except:
                    pass
            save_game.save_game(saveslot)
        ## HELP
        elif command.lower() == "pomoc":
            print(help_loc)
        ## JOURNAL
        elif command.lower() == "dziennik":
            journal.showjournal()
        ## INVENTORY
        elif command.lower() == "ekwipunek":
            inventory.showinv()
        ## CHARACTER
        elif command.lower() == "postać":
            leveling.showleveling(PC_HERO)
        ## LOC DESC
        elif command.lower() == "opis":
            PC_HERO.current_cell.show_loc_desc()
            input()
        ## MOVEMENT
        elif command.lower() in location_locs:
            command = location_locs[command.lower()]
            if command in connectlist:
                if command.locked == "locked" and hasattr(command, "locked_key") and command.locked_key in PC_HERO.inventory:
                    command.locked = "unlocked"
                elif command.locked == "pickable" and item_list.itke_lockpick in PC_HERO.inventory:
                    unlock = lockpicking.lockpick(command.combination)
                    if unlock == "SUCCESS":
                        command.locked = "unlocked"

                if command.locked == "locked" or command.locked == "pickable":
                    try:
                        print(command.locked_reason)
                        input("Kontynuuj...")
                    except:
                        print("Nie możesz tędy przejść!")
                        input("Kontynuuj...")
                elif hasattr(command, "monster"):
                    if hasattr(command,"monster_loc"):
                        print(command.monster_loc)
                    else:
                        print("Na drodze stoi " + command.monster.name)
                    yesno = input("Czy idziesz dalej? ")
                    if yesno.lower() in include.yes_set:
                        fightresult = fight.startfight(PC_HERO, command.monster)
                        if fightresult == "SUCCESS":
                            delattr(command, "monster")
                            PC_HERO.current_cell = command
                        if fightresult == "FAILURE":
                            fight.kill(PC_HERO, 1)
                            pass
                else:
                    PC_HERO.current_cell = command
        ## VOB USE
        elif command.lower() in location_vobs:
            command = location_vobs[command.lower()]
            print("\n\n" + command.name)
            print(command.desc)
            if hasattr(command, "item"):
                inventory.add_to_inventory(PC_HERO,command.item)
                PC_HERO.current_cell.vob.remove(command)
                input("Kontynuuj...")
            elif hasattr(command, "effect"):
                command.effect(PC_HERO)

        ## NPC USE
        elif command.lower() in location_npcs:
            command = location_npcs[command.lower()]
            dialogue.init_dialogue(command, 0)


def new_game():
    character_creation.new_character()
    input("Kontynuuj...")
    PC_HERO.current_cell = map.LOC_WAYSHRINE
    startup.startup()
    prologue.prologue_cutscene(PC_HERO)
    PC_HERO.inventory.append(item_list.itwp_sword_0)
    PC_HERO.weapon = item_list.itwp_sword_0
    PC_HERO.weapon.used = 1
    PC_HERO.inventory.append(item_list.itar_grd_l)
    PC_HERO.armor = item_list.itar_grd_l
    PC_HERO.armor.used = 1
    PC_HERO.hp = PC_HERO.hp_max
    input("")
    game()


def test_game():
    PC_HERO.current_cell = map.LOC_PRIORY_GARDEN
    startup.startup()
    PC_HERO.inventory.append(item_list.itwp_sword_1)
    #PC_HERO.weapon = item_list.itwp_sword_1
    PC_HERO.inventory.append(item_list.itfo_booze)
    PC_HERO.inventory.append(item_list.itmi_oars)
    PC_HERO.inventory.append(item_list.itke_lockpick)
    PC_HERO.inventory.append(item_list.itfo_fish)
    PC_HERO.inventory.append(item_list.itmi_arrow)
    PC_HERO.inventory.append(item_list.itmi_arrow)
    PC_HERO.inventory.append(item_list.itmi_arrow)
    PC_HERO.inventory.append(item_list.itmi_arrow)
    PC_HERO.inventory.append(item_list.itmi_arrow)
    PC_HERO.gold = 200
    PC_HERO.lp += 5
    game()

def initgame():
    while True:
        print("""
    #### #### #### #### #### #### #### #### #### #### ####
    ςανπ αωελ δρυγ ιγωα λξιλ μαλε δζιε ξιςα νπαω ελδρ υγιγ 
                          S T Y K S
    ωαλξ ιλμα λεδζ ιεξι ςανπ αωελ δρυγ ιγωα λξιλ μαλε δζιε
    #### #### #### #### #### #### #### #### #### #### ####    
        """)
        print("#### ")
        print("#### MENU GŁÓWNE")
        print("#### ")
        print("# Nowa Gra")
        command = input()
        if command.lower() == "nowa gra":
            new_game()
        if command.lower() == "test":
            test_game()

initgame()