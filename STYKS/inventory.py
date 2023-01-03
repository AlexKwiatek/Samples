import include
import item_list
from hero import PC_HERO

item_type_dict = {
    "key":"Klucz",
    "weapon":"Broń",
    "armor":"Zbroja",
    "miscelanous":"Różne",
    "food":"Żywność",
    "book":"Słowo Pisane"
}

def showinv():
    item_ids = []
    item_names = []
    while True:
        include.printimportanttext("EKWIPUNEK")
        print("OBOLE: " + str(PC_HERO.gold))
        if hasattr(PC_HERO,"armor"):
            print("Używana zbroja: " + PC_HERO.armor.name)
        else:
            print("Używana zbroja: BRAK")
        if hasattr(PC_HERO,"weapon"):
            print("Używana broń: " + PC_HERO.weapon.name)
        else:
            print("Używana broń: BRAK")

        print("\nTORBA: ")
        for item in PC_HERO.inventory:
            print(item.name + " -- " + item_type_dict[item.type])

            item_ids.append(item)
            item_names.append(item.name)
        char_items = dict(zip(item_names, item_ids))
        print("Wpisz przedmiot którego chcesz użyć. Jeśli chcesz wrócić wpisz POWRÓT")
        command = input()
        action = command.split(' ', 1)[0].lower()
        if action in include.destroy_set:
            command = include.stringify(command.split(' ', 1)[1:])

        #print(action)
        #print(command)
        if command in char_items:
            command = char_items[command]
            if action in include.destroy_set:
                if hasattr(command,"used"):
                    print("Nie możesz wyrzucić itemu którego właśnie używasz!")
                else:
                    destroy_item(PC_HERO,command)
                    input()
            elif command.type == "weapon":
                print(command.desc)
                print("Obrażenia: " + str(command.dmg))
                if hasattr(command,"used"):
                    print("Używasz tej broni")
                    yes_no_bool = input("Odłożyć? ")
                    if yes_no_bool.lower() in include.yes_set:
                        delattr(PC_HERO.weapon,"used")
                else:
                    if hasattr(PC_HERO,"weapon"):
                        print("Obecna broń: " + str(PC_HERO.weapon.dmg))
                    else:
                        print("Obecna broń: BRAK")
                    yes_no_bool = input("Użyć? ")
                    if yes_no_bool.lower() in include.yes_set:
                        if hasattr(PC_HERO,"weapon"):
                            delattr(PC_HERO.weapon,"used")
                        PC_HERO.weapon = command
                        PC_HERO.weapon.used = 1

            elif command.type == "armor":
                print(command.desc)
                print("Ochrona: " + str(command.armor))
                if hasattr(command,"used"):
                    print("Używasz tej zbroi")
                    yes_no_bool = input("Odłożyć? ")
                    if yes_no_bool.lower() in include.yes_set:
                        delattr(PC_HERO.armor,"used")
                else:
                    if hasattr(PC_HERO,"armor"):
                        print("Obecna zbroja: " + str(PC_HERO.armor.armor))
                    else:
                        print("Obecna zbroja: BRAK")
                    yes_no_bool = input("Użyć? ")
                    if yes_no_bool.lower() in include.yes_set:
                        if hasattr(PC_HERO,"armor"):
                            delattr(PC_HERO.armor,"used")
                        PC_HERO.armor = command
                        PC_HERO.armor.used = 1
            elif hasattr(command,"eateffect"):
                command.eateffect(PC_HERO,command)
            else:
                print(command.desc)
        elif command.lower() in include.back_set:
            break

def add_to_inventory(character,item):
    character.inventory.append(item)
    print("Otrzymano przedmiot: " + item.name)
    if hasattr(item,"effect"):
        item.effect()

def add_gold(character,amount):
    character.gold += amount
    print("Zdobywasz " + str(amount) + " Obole")

def remove_gold(character,amount):
    character.gold -= amount
    print("Tracisz " + str(amount) + " Obole")

def destroy_item(character,item):
    character.inventory.remove(item)
    print("Wyrzucono przedmiot: " + item.name)