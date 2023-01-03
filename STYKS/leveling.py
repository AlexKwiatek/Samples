import include
import math

def give_exp(character,amount):
    character.exp += amount
    print("Doświadczenie +" + str(amount))
    if character.exp >= character.exp_next:
        character.exp_next += 100
        include.printimportanttext("KOLEJNY POZIOM!")
        character.level += 1
        character.lp += 5 + math.floor(character.int / 5)
        character.hp_max += 10
        character.hp += 10

def showleveling(NPC):
    NPC.printcharactersheet()
    while True:
        while NPC.lp > 0:
            print("\nKOLEJNY POZIOM!\n")
            print("Aby rozdać wiecej punktów w daną ceche, napisz jej nazwe a potem liczbe punktów")
            command = input("Nazwij atrybut do ulepszenia: ")
            command = command.split()
            try:
                int(command[-1])
                command.append(int(command[-1]))
            except:
                command.append(1)
            if command[-1] > NPC.lp:
                command[-1] = NPC.lp
            if command[0].lower() in include.str_set:
                NPC.lp -= command[-1]
                NPC.str += command[-1]
            elif command[0].lower() in include.dex_set:
                NPC.lp -= command[-1]
                NPC.dex += command[-1]
            elif command[0].lower() in include.int_set:
                NPC.lp -= command[-1]
                NPC.int += command[-1]
            elif command[0].lower() in include.cha_set:
                NPC.lp -= command[-1]
                NPC.cha += command[-1]
            elif command[0].lower() in include.back_set:
                NPC.printcharactersheet()
                return
            else:
                print("Nieznana komenda")
            print(" ")
            NPC.printcharactersheet()

        command = input("\nWpisz POWRÓT by wyjść... ")
        if command.lower() == "marvin":
            NPC.marvinmode = 1
        if command.lower() in include.back_set:
            return
