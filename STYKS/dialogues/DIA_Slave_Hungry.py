import include
import npc_list
import journal
import item_list
import leveling
import inventory
from hero import PC_HERO
from dialogue import AI_Output


def DIA_Slave_Hungry_First_Hello(other):
    print("Pod jedną z chat w wiosce leży brudny obszarpany człowiek. Jest bardzo wychudzony i ubrany w łachmany")
    AI_Output(other,"Khyyy...")
    AI_Output(PC_HERO,"A tobie co się stało człowieku?")
    AI_Output(other,"[Biedak z wyraźnym trudem dźwignął się do pozycji siedzącej] Wpadłem w niełaske Bękarta... lepiej ode mnie odejdź...")
    AI_Output(PC_HERO,"Dlaczego?")
    AI_Output(other,"Żeby mnie ukarać, zakazał swoim ludziom i niewolnikom dawać mi jedzenia. Mówił że mam głodować przez miesiąc za to co zrobiłem...")
    AI_Output(PC_HERO,"To nieludzkie...")
    AI_Output(PC_HERO,"Na twoje szczęście ja nie jestem ani jednym, ani drugim")
    other.dialogue_hello = DIA_Slave_Hungry_Post_Hello

def DIA_Slave_Hungry_Post_Hello(other):
    if "helped_slave" in PC_HERO.flags:
        AI_Output(other,"Dziękuję za twoją pomoc...")
    else:
        AI_Output(other,"[Wiezień leży pod chatą. Gdyby nie ruch gałek ocznych możnaby pomyśleć że nie żyje]")

npc_list.VLK_103_Slave.dialogue_hello = DIA_Slave_Hungry_First_Hello


def DIA_Slave_Bread_Info(other):
    AI_Output(PC_HERO,"Prosze... weź to jedzenie")
    AI_Output(other,"Ale Bękart...")
    AI_Output(PC_HERO,"Sam mówiłeś. Nie jestem jego własnością, nie obchodzą mnie jego zakazy")
    AI_Output(other,"Dziękuję...")
    PC_HERO.flags.append("helped_slave")
    if "absolute_dick_to_slave" in PC_HERO.flags:
        PC_HERO.flags.remove("absolute_dick_to_slave")
        PC_HERO.karma += 1
    PC_HERO.inventory.remove(item_list.itfo_bread)
    leveling.give_exp(PC_HERO,10)
    PC_HERO.karma += 1

def DIA_Slave_Bread_Condition():
    if item_list.itfo_bread in PC_HERO.inventory:
        return 1

DIA_Slave_Bread = include.DIALOGUE(
    npc_list.VLK_103_Slave,
    DIA_Slave_Bread_Info,
    DIA_Slave_Bread_Condition,
    0,
    "Daj chleb"
)


def DIA_Slave_Extort_Info(other):
    AI_Output(PC_HERO,"Pomogę ci, ale za cene. Przebyłem długą droge by gdzieś dojść. I to jest ostatni przystanek.")
    AI_Output(other,"Zrobie wszystko...")
    AI_Output(PC_HERO,"Brama do wyjścia z Hadesu. Chce wiedzieć jak do niej dotrzeć.")
    AI_Output(other,"Kilka miesięcy temu... [wyszeptał] był tu człowiek... Mówił że szukał Bramy Hadesu... i że 'zrozumiał'...")
    AI_Output(PC_HERO,"Co zrozumiał? Gdzie jest ten człowiek?")
    AI_Output(other,"Nie wiem co... człowiek nie żyje... Bękart go zabił")
    PC_HERO.flags.append("absolute_dick_to_slave") # Extorting guy is bad enough but if you do not help him now, you're dickest dick of the dicks, absolute dick with a crown, Duke Dick the First of Cockenheim Dynasty. Flag is removed on giving him bread
    PC_HERO.flags.append("extorted_slave")
    PC_HERO.karma -= 3

def DIA_Slave_Extort_Condition():
    if not "helped_slave" in PC_HERO.flags:
        return 1

DIA_Slave_Extort = include.DIALOGUE(
    npc_list.VLK_103_Slave,
    DIA_Slave_Extort_Info,
    DIA_Slave_Extort_Condition,
    0,
    "Jedzenie za przysługe"
)

