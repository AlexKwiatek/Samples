import include
from hero import PC_HERO
import time
import math

def AI_Output(speaker,data):
    print(speaker.name + ": " + str(data))
    #time.sleep((len(data)/15)+1) #Diabled for now, it's kinda neat on paper, but it makes dialogues jump and irritates player

def init_dialogue(npc, inside):
    if npc.is_dead() == 1:
        print(npc.name + " jest martwy.")
        input("Kontynuuj...")
        return
    if inside == 0:
        npc.dialogue_hello(npc)
        PC_HERO.knowndialogue.append(npc.dialogue_hello)
    dia_ids = []
    dia_names = []
    print(" ")
    for topic in npc.dialogues:
        if not hasattr(topic,"condition"):
            dia_ids.append(topic)
            dia_names.append(topic.description)

            print("# " + topic.description)
        elif topic.condition() == 1:
            dia_ids.append(topic)
            dia_names.append(topic.description)

            print("# " + topic.description)
    dialogue_topics = dict(zip(dia_names, dia_ids))
    if hasattr(npc,"dialogue_trade"):
        print("# HANDEL")
    if not "forbid_exit" in PC_HERO.flags:
        print("# KONIEC")
    while True:
        command = input()
        if command in dialogue_topics:
            command = dialogue_topics[command]
            if hasattr(command, "info"):
                command.info(npc)
                input()
            PC_HERO.knowndialogue.append(command)
            if command.permanent == 0:
                npc.dialogues.remove(command)

            if npc.hp > 0:
                init_dialogue(npc, 1)
            break
        if command.lower() in include.trade_set:
            npc.dialogue_trade(npc)
            break
        if not "forbid_exit" in PC_HERO.flags:
            if command.lower() in include.end_set:
                break