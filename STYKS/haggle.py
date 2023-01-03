import random
import include
from dialogue import AI_Output

far_too_much_list = ["Chyba cie rozum opuścił, ", "Chyba śnisz, ", "Oszalałeś, "]
no_more_list = [" i ani obola więcej", " więcej nie dam", " i to moje ostatnie słowo"]
too_much_list = ["Za dużo, ", "Nieee... raczej nie, ", "Może... nie. "]

def haggle(self,other,sum_min):
    accepted = int(random.randrange(sum_min,sum_min*2))
    heat = 0
    former_price = 9999
    haggle_skill = 1 + self.cha * 0.001
    #print("DEBUG MODE: " + str(haggle_skill))
    while heat <= 10:
        print("\nZniecierpliwienie: [" + heat * "=" + (10-heat) * "-" + "]")
        price = int(input("Podaj swoją cene: "))
        AI_Output(self,price)
        if price > former_price:
            AI_Output(other,"Targujesz w góre? Sukinsynu!" + str(sum_min) + "!" + random.choice(no_more_list))
            heat += 5 # Bid higher than previous bid results only in angering NPC
        #Price get's accepted
        elif price <= accepted:
            if price < sum_min and heat != 0:
                AI_Output(other,"Nie rozumiem czemu chcesz tak mało skoro oferuje ci więcej ale w porzadku.")
            elif heat > 5:
                AI_Output(other,"Na diabły i demony!")
            AI_Output(other,"Stoi!")
            return price
        #Price is far to high. NPC is angered twice as much. It is an indicator that player overbid by 50%
        elif price >= accepted * 1.5:
            sum_min = random.randrange(int(sum_min),int(accepted)) # NPC offers some amount between last bid and maximum price that he would accept
            AI_Output(other,random.choice(far_too_much_list) + str(sum_min) + "!" + random.choice(no_more_list))
            accepted *= haggle_skill # Depending on char's charisma, NPC accepts higher price after that
            if accepted > price:
                accepted = price
            heat += 2
        #Price is too high but it isn't 50% higher than the one that NPC has in mind
        else:
            sum_min = random.randrange(int(sum_min),int(accepted)) # NPC offers some amount between last bid and maximum price that he would accept
            AI_Output(other,random.choice(too_much_list) + str(sum_min) + random.choice(no_more_list))
            accepted *= haggle_skill # Depending on char's charisma, NPC accepts higher price after that
            if accepted > price:
                accepted = price
            heat += 1
        former_price = price
        #print("DEBUG MODE: " + str(accepted))
        #If NPC is angered too much it results in him
        if heat >= 10:
            AI_Output(other,"Dość. Bierzesz ile ci daje, albo zapomnij o nagrodzie")
            return sum_min

#TODO: make dialogues varied depending on NPCs character traits. Kind NPCs should be polite while bandits should be banditous