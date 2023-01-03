import include
import random
import inventory
import math
import dialogue
import leveling

monster_attack_loc = (
    "[Uderza!]",
    "[Drapie!]",
    "[Gryzie!]"
)
human_attack_loc = (
    "[Tnie!]",
    "[Atakuje!]",
    "[Rąbie!]"
)
legion_attack_loc = (
    "[Tnie!]",
    "[Atakuje!]",
    "[Rąbie!]",
    "Legion Pany!!!"
)


MonsterKilledLoc = (
    "Kolejne bydle załatwione!",
    "No! Koniec z tobą bestio!",
    "I jeszcze jeden parszywy stwór załatwiony",
    "Jedna bestia mniej!"
)
HumanKilledLoc = (
    "[Zaczyna jeść truchło]",
    "[Grzebie w trupie łapką]"
)
EnemyKilledLoc = (
    "I po sprawie...",
    "Zasłużyłeś sobie na to, bydlaku!",
    "Tyle na ten temat..."
)
human_guilds = ["hoplite","peltist","companion","legion","commoner","bandit"]
monster_guilds = ["monster"]

def choose_attack_loc(NPC):
    if NPC.guild in monster_guilds:
        return monster_attack_loc
    if NPC.guild == "legion":
        return legion_attack_loc
    if NPC.guild in human_guilds:
        return human_attack_loc

def choose_finisher_loc(winner,loser):
    if winner.guild in human_guilds and loser.guild in monster_guilds:
        return MonsterKilledLoc
    elif winner.guild in human_guilds and loser.guild in human_guilds:
        return EnemyKilledLoc
    elif winner.guild in monster_guilds and loser.guild in human_guilds:
        return HumanKilledLoc

def choose_fighting_pattern(NPC):
    if NPC.guild in monster_guilds:
        return stances_monster
    if NPC.guild in human_guilds:
        return stances_human
    else: #Fallback
        return stances

def get_health_bar(NPC):
    bar_length = 20
    percentage = math.floor(NPC.hp / NPC.hp_max * bar_length)
    print(NPC.name + ": " + str(NPC.hp) + "/" + str(NPC.hp_max) + " - [" + percentage * "=" + (bar_length-percentage) * "-" + "]")

stances_monster = ["left","right","up","up","up","down"]
stances_human = ["left","right","up","down"]
stances = ["left","right","up","down"] #Fallback

def startfight(player,enemy): # Combat Placeholder
    print("# # # # # # # # # # # # # # # ")
    get_health_bar(player)
    get_health_bar(enemy)
    # Setup Armor and Weapon
    if hasattr(player,"weapon"):
        player_weapon_dmg = player.weapon.dmg
    else:
        player_weapon_dmg = 0
    if hasattr(player,"armor"):
        player_armor = player.armor.armor
    else:
        player_armor = 0
    if hasattr(enemy,"weapon"):
        enemy_weapon_dmg = enemy.weapon.dmg
    else:
        enemy_weapon_dmg = 0
    if hasattr(enemy,"armor"):
        enemy_armor = enemy.armor.armor
    else:
        enemy_armor = 0
    # Fight!
    combo = 0
    stance = " "
    print("Lewo;Prawo;Góra;Dół")
    while True:
        # Events
        shield_player = 0
        shield_enemy = 0
        bonus = 0
        carnage = 1
        result = " "
        prev_stance = stance
        while True:
            stance = input("Wybierz postawe: ")
            if stance.lower() == "help" or stance.lower() == "pomoc":
                print(include.help_fight_loc)
            elif stance.lower() in include.left_set:
                stance = "left"
                break
            elif stance.lower() in include.right_set:
                stance = "right"
                break
            elif stance.lower() in include.up_set:
                stance = "up"
                break
            elif stance.lower() in include.down_set:
                stance = "down"
                break
            else:
                stance = "none"
                break
        enemy_stance = random.choice(choose_fighting_pattern(enemy))
        # Special
        if stance == enemy_stance:
            result = " - BLOK!"
            shield_player = 1
            shield_enemy = 1
        if stance == "left" and enemy_stance == "right" or stance == "right" and enemy_stance == "left":
            result = " - RZEŹ! x2 Obrażenia!"
            carnage = 2
        if stance == "up" and enemy_stance == "down" or stance == "down" and enemy_stance == "up":
            result = " - RZEŹ! x2 Obrażenia!"
            carnage = 2
        # Left
        if stance == "left" and enemy_stance == "up":
            result = " - SUKCES! +10 Atak"
            bonus = 10
        if stance == "left" and enemy_stance == "down":
            result = " - PORAŻKA! -10 Atak"
            bonus = -10
        # Up
        if stance == "up" and enemy_stance == "right":
            result = " - SUKCES! +10 Atak"
            bonus = 10
        if stance == "up" and enemy_stance == "left":
            result = " - PORAŻKA! -10 Atak"
            bonus = -10
        # Right
        if stance == "right" and enemy_stance == "down":
            result = " - SUKCES! +10 Atak"
            bonus = 10
        if stance == "right" and enemy_stance == "up":
            result = " - PORAŻKA! -10 Atak"
            bonus = -10
        # Down
        if stance == "down" and enemy_stance == "left":
            result = " - SUKCES! +10 Atak"
            bonus = 10
        if stance == "down" and enemy_stance == "right":
            result = " - PORAŻKA! -10 Atak"
            bonus = -10
        # Combo
        if stance == "left" and prev_stance == "right":
            combo += 1
        elif stance == "right" and prev_stance == "left":
            combo += 1
        elif stance == "up" and prev_stance == "up":
            combo += 1
        else:
            combo = 0
        print(" ")
        print("# # # # # " + include.stance_dict[stance] + " vs " + include.stance_dict[enemy_stance]+ result)

        player_initiative_roll = player.dex + random.randrange(1,20) + bonus + combo
        enemy_initiative_roll = enemy.dex + random.randrange(1,20)
        if player_initiative_roll > enemy_initiative_roll:
            print("  # # " + player.name + ": " + str(player_initiative_roll) + " [!]")
            print("  # # " + enemy.name + ": " + str(enemy_initiative_roll))
            print("# # # # # # # # # # # # # # # ")
            dialogue.AI_Output(player,random.choice(choose_attack_loc(player)))
            dmg = player.str + player_weapon_dmg - enemy_armor + random.randrange(1,10) * carnage
            if shield_enemy == 1:
                print("Cios sparowany!")
            else:
                if dmg < 1:
                    dmg = 1
                enemy.hp -= dmg
                print("Obrażenia: " + str(dmg))
        elif player_initiative_roll == enemy_initiative_roll:
            print("  # # # " + player.name + ": " + str(player_initiative_roll) + " Unik!")
            print("  # # # " + enemy.name + ": " + str(enemy_initiative_roll) + " Unik!")
        else:
            print("  # # # " + player.name + ": " + str(player_initiative_roll))
            print("  # # # " + enemy.name + ": " + str(enemy_initiative_roll) + " [!]")
            print("# # # # # # # # # # # # # # # ")
            dialogue.AI_Output(enemy,random.choice(choose_attack_loc(enemy)))
            dmg = enemy.str + enemy_weapon_dmg - player_armor + random.randrange(1,10) * carnage
            if shield_player == 1:
                print("Cios sparowany!")
            else:
                if dmg < 1:
                    dmg = 1
                player.hp -= dmg
                print("Obrażenia: " + str(dmg))
        if player.hp < 0:
            player.hp = 0
        if enemy.hp < 0:
            enemy.hp = 0
        print("# # # # # # # # # # # # # # # ")
        get_health_bar(player)
        get_health_bar(enemy)

        if player.hp == 0:
            print(" ")
            dialogue.AI_Output(enemy,random.choice(choose_finisher_loc(enemy,player)))
            input("Kontynuuj...")
            return "FAILURE"
        if enemy.hp == 0:
            print(" ")
            dialogue.AI_Output(player,random.choice(choose_finisher_loc(player,enemy)))
            leveling.give_exp(player,enemy.level*10)
            loot(enemy, player)
            kill(enemy,0)
            input("Kontynuuj...")
            return "SUCCESS"




def kill(NPC,player):
    if player == 1:
        include.printimportanttext("KONIEC GRY")
        if "loop" in NPC.flags:
            print("Opiekun zesłał cię do kolejnej pętli")
        elif "elysium" in NPC.flags:
            print("Opiekun pozwolił ci ruszyć dalej - na Pola Elizejskie")
        elif "tartaros" in NPC.flags:
            print("Opiekun strącił cię do Tartaru na wieczne męki")
        elif "escape" in NPC.flags:
            print("Uciekłeś Opiekunom. Jesteś teraz ściganym człowiekiem. Ale za to przynajmniej wolnym.")
        else:
            print("Umarłeś. Zgodnie z prawami Hadesu wrócisz dopiero gdy ktoś złoży za ciebie ofiare.\nTo może zając pare ładnych lat...")
        print(" # Zdobyty poziom: " + str(NPC.level))
        print(" # Zdobyte doświadczenie: " + str(NPC.exp))
        while True:
            exitbool = input("Napisz KONIEC by wyjść z gry ")
            if exitbool.lower() in include.end_set:
                exit()
    else:
        NPC.hp = 0

def loot(NPC, killer):
    if hasattr(NPC,"loot"):
        for item in NPC.loot:
            inventory.add_to_inventory(killer,item)
            NPC.loot.remove(item)
        if hasattr(NPC, "gold"):
            inventory.add_gold(killer, NPC.gold)
            NPC.gold = 0
        input("Kontynuuj...")
    elif hasattr(NPC,"gold"):
        inventory.add_gold(killer,NPC.gold)
        NPC.gold = 0
        input("Kontynuuj...")