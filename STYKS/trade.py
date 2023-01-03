import include
import inventory
from hero import PC_HERO
import item_list
import random
import math

buy_set = ["kup","buy","dej","gib","b"]
sell_set = ["sprzedaj","sell","s"]
haggle_set = ["targowanie","haggle"]

def trade(character,trader):
    trader_discount = [character.cha,character.cha,character.cha] # Lista z totalnie niezależnymi wynikami #TODO: jak już oddasz do oceny to wyrzuć to. Losowość = HIV
    trader_price = 2-(random.choice(trader_discount)/100) # Zupełnie uczciwy i losujący (powtarzam - losujący. Element losowości) kod

    while True: # I guess it has to be updated each time to avoid exploits
        trader_ids = []
        trader_names = []
        item_ids = []
        item_names = []
        include.printimportanttext("HANDEL")
        print("\n# # # # # # # # # # # # # # # # # # # # # # # # # ")
        print("PRZEDMIOTY HANDLARZA: ")
        for item in trader.goods:
            if hasattr(item,"value"):
                print(item.name + " -- " + inventory.item_type_dict[item.type] + " - " + str(math.ceil(item.value*trader_price)))

                trader_ids.append(item)
                trader_names.append(item.name.lower())
        trader_items = dict(zip(trader_names, trader_ids))

        print("\n# # # # # # # # # # # # # # # # # # # # # # # # # ")
        print("TWOJE OBOLE: " + str(character.gold))
        print("TWOJE PRZEDMIOTY: ")
        for item in character.inventory:
            if hasattr(item,"value") and not hasattr(item,"used"):
                print(item.name + " -- " + inventory.item_type_dict[item.type] + " - " + str(item.value))

                item_ids.append(item)
                item_names.append(item.name.lower())
        char_items = dict(zip(item_names, item_ids))

        print("\nBy kupić item wpisz 'Kup' i jego nazwe. By go sprzedać wpisz 'Sprzedaj' i jego nazwe")
        command = input("Wybierz: ")
        if command in include.back_set:
            return
        #command = command.split() # Use first element as a designate what to do #TODO: Rework it properly. Create two separate vars from command
        action = command.split(' ', 1)[0].lower()
        ## Bit of quality of life improvement - if player/trader is the only char in here that has item, game will get what you're trying to do even if you forget buy/sell command
        if action in buy_set or action in sell_set:
            thing = include.stringify(command.split(' ', 1)[1:])
        elif command.lower() in trader_items and not command.lower() in char_items:
            action = "buy"
            thing = command
        elif command.lower() in char_items and not command.lower() in trader_items:
            action = "sell"
            thing = command
        #print(action)
        #print(thing)
        if action.lower() in buy_set:
            if thing.lower() in trader_items:
                traded_good = trader_items[thing.lower()]
                if math.ceil(traded_good.value*trader_price) > character.gold:
                    print("Nie masz dość Oboli")
                    input()
                else:
                    character.gold -= math.ceil(traded_good.value*trader_price)
                    character.inventory.append(traded_good)
                    trader.goods.remove(traded_good)
                    print("Kupiono " + traded_good.name + " za " + str(traded_good.value))
        if action.lower() in sell_set:
            if thing.lower() in char_items:
                traded_good = char_items[thing.lower()]
                character.gold += traded_good.value
                trader.goods.append(traded_good)
                character.inventory.remove(traded_good)
                print("Sprzedano " + traded_good.name + " za " + str(traded_good.value))
