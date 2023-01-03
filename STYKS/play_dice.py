import random

def throw_dice(player,enemy):
    while True:
        enemy_throw = random.randrange(1,6)
        enemy_throw2 = random.randrange(1,6)
        enemy_total = enemy_throw + enemy_throw2
        print(enemy.name + " wyrzucił " + str(enemy_total) + " z kośćmi " + str(enemy_throw) + " i " + str(enemy_throw2))
        command = input("# Rzuć albo pas ")
        if command.lower() == "pas":
            return 0
        if command.lower() == "rzuć":
            player_throw = random.randrange(1,6)
            player_throw2 = random.randrange(1,6)
            player_total = player_throw + player_throw2
            print(player.name + " wyrzucił " + str(player_total) + " z kośćmi " + str(player_throw) + " i " + str(player_throw2))
        if player_total > enemy_total:
            return 1
        if player_total < enemy_total:
            return 0
        else:
            print("REMIS! Powtórka:\n")
