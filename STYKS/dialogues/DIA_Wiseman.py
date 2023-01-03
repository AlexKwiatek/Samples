import include
import npc_list
import item_list
import leveling
import inventory
import symulator_pumy
from hero import PC_HERO
from dialogue import AI_Output


def DIA_Wiseman_First_Hello(other):
    print("Przed furtą stoi starzec w wytartej szacie, opierający się o kostur. Patrzy na ciebie spode łba zainteresowanym spojrzeniem.")
    AI_Output(other,"Witaj wędrowcze. Czy przyszedłeś tu odbyć próbę?")
    AI_Output(PC_HERO,"Ja? Jaką próbe?")
    AI_Output(other,"Jeśli odpowiesz poprawnie na moje zagadki, przepuszcze cię przez furte i dam ci magiczny artefakt. Miecz zwany Kłem Basa.")
    other.dialogue_hello = DIA_Wiseman_Post_Hello

def DIA_Wiseman_Post_Hello(other):
    if "bamboozled" in PC_HERO.flags:
        AI_Output(other,"Ha ha ha! Za każdym razem bawi tak samo!")
    else:
        AI_Output(other,"Czekam na odpowiedź na moją zagadkę...")

npc_list.VLK_104_Wiseman.dialogue_hello = DIA_Wiseman_First_Hello


def DIA_Wiseman_Bamboozle_Info(other):
    AI_Output(PC_HERO,"Mów swoją zagadkę starcze.")
    bamboozled_var = symulator_pumy.puma(PC_HERO,other)
    if  bamboozled_var == "SUCCESS":
        AI_Output(other,"Ha ha ha! Za każdym razem bawi tak samo!") # Pomimo całej goofowatości to jedna z pierwszych wskazówek że gracz jest w pętli. Ten dziad siedzi tutaj i za każdym razem wkręca protaga w ten sam żart
        AI_Output(other,"Nie tak szybko wojowniku, twoja nagroda.")
        leveling.give_exp(PC_HERO,25)
        inventory.add_to_inventory(PC_HERO,item_list.itfo_wurst)
        PC_HERO.flags.append("mountain_lion")
        PC_HERO.flags.append("bamboozled")
    elif bamboozled_var == "YES":
        AI_Output(other,"Ale...")
        AI_Output(PC_HERO,"Co? No w sumie duże zwierze, dość niebezpieczne...")
        AI_Output(other,"Nie takiej odpowiedzi się spodziewałem...")
        AI_Output(PC_HERO,"Ale dostane swoją nagrodę?")
        AI_Output(other,"Um... tak. Później. A teraz odejdź. Musze przemyśleć sens swojego istnienia.")
        PC_HERO.flags.append("bamboozled")
    elif bamboozled_var == "NO":
        AI_Output(other,"Ale...")
        AI_Output(PC_HERO,"No niespecjalnie, to taki duży kociak. Lew to byłoby dopiero coś. Co tak zamilkłeś?")
        AI_Output(other,"Nie takiej odpowiedzi się spodziewałem...")
        AI_Output(PC_HERO,"Ale dostane swoją nagrodę?")
        AI_Output(other,"Um... tak. Później. A teraz odejdź. Musze przemyśleć sens swojego istnienia.")
        PC_HERO.flags.append("bamboozled")
    else:
        AI_Output(other, "Musisz się jeszcze wiele nauczyć... wróć do mnie gdy będziesz gotowy")

def DIA_Wiseman_Bamboozle_Condition():
    if not "bamboozled" in PC_HERO.flags:
        return 1

DIA_Wiseman_Bamboozle = include.DIALOGUE(
    npc_list.VLK_104_Wiseman,
    DIA_Wiseman_Bamboozle_Info,
    DIA_Wiseman_Bamboozle_Condition,
    1,
    "Test"
)

