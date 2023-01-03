import include
import npc_list
import journal
import item_list
import leveling
import fight
import vob_list
from hero import PC_HERO
from dialogue import AI_Output
import map


def DIA_RiversideBandit_Hello(other):
    AI_Output(other,"A ty tu czego? Zostaw nas w spokoju")
    AI_Output(PC_HERO,"Co tutaj robicie?")
    AI_Output(other,"Czekamy na naszego kupca. Ale tobie nic do tego")
    other.dialogue_hello = DIA_RiversideBandit_Post_Hello

def DIA_RiversideBandit_Post_Hello(other):
    AI_Output(other,"Szukasz guza?")

npc_list.BDT_308_Bandit.dialogue_hello = DIA_RiversideBandit_Hello

### Annoying Quest Line
def DIA_Bandits_Quest_Info(other):
    AI_Output(PC_HERO,"Na jakiego kupca czekacie?")
    if not hasattr(PC_HERO,"bandits_annoyed"):
        PC_HERO.bandits_annoyed = 0
    if PC_HERO.bandits_annoyed == 0:
        AI_Output(other,"To nie twoja sprawa!")
        PC_HERO.bandits_annoyed = 1
    elif PC_HERO.bandits_annoyed == 1:
        AI_Output(other,"Mówiłem ci już! Spadaj!")
        PC_HERO.bandits_annoyed = 2
    elif PC_HERO.bandits_annoyed == 2:
        AI_Output(other,"Odwal się od nas!")
        PC_HERO.bandits_annoyed = 3
    elif PC_HERO.bandits_annoyed == 3:
        AI_Output(other,"Dobra, mam dość. Skasuje gnojka.")
        print("\nBandyta skoczył na ciebie z pięściami. Po krótkiej szamotaninie na podłodze rozdzieliliście się i łotr dobył broni. Zareagowałeś tak samo")
        print("\nJego pomocnik również próbował to zrobić ale został szarpnięty i obalony na ziemie przez Księcia Antiochusa który przyglądał się od początku całej rozmowie")
        result = fight.startfight(PC_HERO,other)
        if result == "SUCCESS":
            PC_HERO.karma -= 1
            PC_HERO.flags.append("killed_petty")
            fight.kill(other,0)
            print("\nPodczas walki bandyta padł martwy. Jego pomocnik, ranny i rozbrojony jest trzymany za głowe i włosy przez Antiochusa")
            print("Wygląda na przerażonego.")
            AI_Output(npc_list.BDT_309_Bandit,"Argh! Puszczaj mnie! O zeusie ty go zabiłeś, ja... przepraszam, zostawcie mnie!")
            AI_Output(PC_HERO,"Najpierw powiedz co naprawde tutaj robiliście.")
            AI_Output(npc_list.BDT_309_Bandit,"Chcieliśmy udać się na północ, mieliśmy się tam zaciągnąć u jednego watażki, prosze, pozwólcie mi odejść...")
            AI_Output(PC_HERO,"Kłamiesz, twój partner wspomniał kupca")
            AI_Output(npc_list.BDT_309_Bandit,"Kupiec... Tak, kupiec! Miał nam sprzedać mapy byśmy mogli dotrzeć do tamtej wioski! Mówie prawde, uwierzcie mi!")
            AI_Output(npc_list.PC_ANTIOCHUS,"Wierzysz mu?")
            print("[TAK/NIE]")
            while True:
                command = input()
                if command.lower() in include.yes_set:
                    AI_Output(PC_HERO,"Tak. Zostawmy go")
                    AI_Output(npc_list.BDT_309_Bandit,"Dziękuje! Już nigdy mnie nie zobaczycie obiecuje!")
                    map.LOC_WAYSHRINE.npc.remove(npc_list.BDT_309_Bandit)
                    journal.SQ_Boatmaker_02.queststage = 25
                    print("## Nowy wpis w dzienniku...")
                    break
                if command.lower() in include.no_set:
                    PC_HERO.karma -= 1
                    PC_HERO.flags.append("killed_minion")
                    AI_Output(PC_HERO,"Nie. To się nie trzyma kupy. Skończmy z nim.")
                    print("[Przecinasz gardło bandyty]")
                    fight.kill(npc_list.BDT_309_Bandit,0)
                    journal.SQ_Boatmaker_02.queststage = 30
                    print("## Nowy wpis w dzienniku...")
                    break
        else:
            fight.kill(PC_HERO, 1)
            pass

def DIA_Bandits_Quest_Condition():
    if journal.SQ_Boatmaker_02.status == "RUNNING":
        return 1

DIA_Bandits_Quest = include.DIALOGUE(
    npc_list.BDT_308_Bandit,
    DIA_Bandits_Quest_Info,
    DIA_Bandits_Quest_Condition,
    1,
    "Co tu robisz?"
)

### Peaceful quest line
def DIA_Bandits_Peaceful_Info(other):
    AI_Output(PC_HERO,"Lepiej idźcie stąd prędko")
    AI_Output(other,"Co? Niby czemu?")
    if PC_HERO.cha >= 10:
        if PC_HERO.npcknowsinfo(DIA_Boatmaker_Quest):
            AI_Output(PC_HERO,"Tropie niebezpieczne zwierze. Zdaje się że Ogara albo Topielca. Nocą wychodzą z jaskiń i rzek.")
        else:
            AI_Output(PC_HERO,"Widziałem w tej okolicy sporo niebezpiecznych zwierząt...")
            AI_Output(npc_list.BDT_309_Bandit,"Jakich? [Przestraszony]")
            AI_Output(other,"[Kompan zrugał go spojrzeniem]")
            AI_Output(PC_HERO,"Wilki i dziki...")
        AI_Output(other,"Nie boimy się zwierząt. Mówiłem ci już, czekamy na naszego kupca a wtedy...")
        AI_Output(PC_HERO,"Jak długo czekacie?")
        AI_Output(other,"A tobie... eh sześć dni")
        AI_Output(PC_HERO,"Nie chce wam psuć nastrojów chłopaki ale jeśli słyszał o problemach z potworami w tej okolicy, to raczej zmienił trase")
        AI_Output(npc_list.BDT_309_Bandit,"Ej myślisz że... Wiesz, on może mieć racje, te kości które mijaliśmy...")
        AI_Output(other,"W sumie... na gościńcu muszą być jakieś drogowskazy, poradzimy sobie bez map.")
        journal.SQ_Boatmaker_02.queststage = 20
        print("## Nowy wpis w dzienniku...")
        leveling.give_exp(PC_HERO,25)
        PC_HERO.karma += 1
    elif PC_HERO.int >= 10:
        AI_Output(PC_HERO,"Widzicie tam pod kapliczką? Ten człowiek to Książe Antiochus Młodszy. Jestem tylko jednym z jego żołnierzy")
        AI_Output(PC_HERO,"Nie wiem jaki szemrany interes tu knujecie, ale odradzam wam robienie tego za jego plecami")
        AI_Output(PC_HERO,"Mój pan bierze te tereny pod swoją opieke i jakiekolwiek interesy mają być załatwiane za jego zgodą")
        AI_Output(other,"[Bandyci zbici z tropu spoglądają na Księcia]")
        AI_Output(npc_list.BDT_309_Bandit,"Ej Mardo, on rzeczywiście wygląda jakby był kimś ważnym")
        AI_Output(other,"A co jeśli to blef?")
        AI_Output(npc_list.BDT_309_Bandit,"Może lepiej powiedzmy mu")
        AI_Output(PC_HERO,"Powiecie mi co?")
        AI_Output(other,"Słuchaj no... Eh")
        AI_Output(other,"No dobra. Czekamy tu na przemytników. Chcieliśmy przedostać się w góry na północy")
        AI_Output(other,"Słyszeliśmy że jest tam jakiś watażka który zbiera dookoła siebie takich jak my")
        AI_Output(npc_list.BDT_309_Bandit,"Czekaliśmy na kupca który miał nam sprzedać mapy jak tam dojść...")
        input()
        print("\nAntiochus nagle włączył się do rozmowy\n")
        AI_Output(npc_list.PC_ANTIOCHUS,"Wasz kupiec was oszukał. Gościniec za furtą jest nie do przejścia")
        AI_Output(npc_list.PC_ANTIOCHUS,"Jedyne co na was tam może czekać to zasadzka i szabrownicy. Zawróćcie stąd lepiej")
        AI_Output(PC_HERO,"Skąd...")
        AI_Output(npc_list.PC_ANTIOCHUS,"Sam powiedziałeś. Teraz to moje ziemie. Zawróćcie")
        print("\nBandyci jakby skurczyli się pod jego spojrzeniem. Wyglądało jakby się czuli przed nim nawet nie respekt, ale strach.\n")
        AI_Output(PC_HERO,"Oszuści, zasadzki, szabrownicy? Skąd tyle wiesz o tym miejscu?")
        AI_Output(npc_list.PC_ANTIOCHUS,"Kiedy byłeś nieprzytomny zasięgnąłem trochę języka o okolicy. Gościniec był pierwszą rzeczą jaka przyszła mi do głowy by sprawdzić.")
        journal.SQ_Boatmaker_02.queststage = 20
        print("## Nowy wpis w dzienniku...")
        leveling.give_exp(PC_HERO,25)
        PC_HERO.karma += 1
    else:
        AI_Output(PC_HERO,"Bo mam się was pozbyć i jeśli będzie trzeba, zrobie to siłą")
        AI_Output(other,"Tak? No to spróbuj szczęścia. Nie masz szans, szermierki uczył mnie sam Bernard Eudetos")

def DIA_Bandits_Peaceful_Condition():
    if journal.SQ_Boatmaker_02.queststage == 10:
        return 1

DIA_Bandits_Peaceful = include.DIALOGUE(
    npc_list.BDT_308_Bandit,
    DIA_Bandits_Peaceful_Info,
    DIA_Bandits_Peaceful_Condition,
    0,
    "Idźcie stąd"
)


### Fighting Quest Line
def DIA_Bandits_Fight_Info(other):
        print("\nWyciągasz miecz i idziesz w strone bandytów. Lider dwójki wyszarpał szybko swój miecz z pochwy")
        AI_Output(other,"Ani kroku dalej albo wypatrosze cie jak rybe!")
        print("\nJego pomocnik również próbował dobyć broni ale został szarpnięty i obalony na ziemie przez Księcia Antiochusa który przyglądał się od początku całej rozmowie")
        result = fight.startfight(PC_HERO, other)
        if result == "SUCCESS":
            PC_HERO.karma -= 1
            PC_HERO.flags.append("killed_petty")
            fight.kill(other,0)
            print("\nPodczas walki bandyta padł martwy. Jego pomocnik, ranny i rozbrojony jest trzymany za głowe i włosy przez Antiochusa")
            print("Wygląda na przerażonego.")
            AI_Output(npc_list.BDT_309_Bandit,"Argh! Puszczaj mnie! O zeusie ty go zabiłeś, ja... przepraszam, zostawcie mnie!")
            AI_Output(PC_HERO,"Najpierw powiedz co naprawde tutaj robiliście.")
            AI_Output(npc_list.BDT_309_Bandit,"Chcieliśmy udać się na północ, mieliśmy się tam zaciągnąć u jednego watażki, prosze, pozwólcie mi odejść...")
            AI_Output(PC_HERO,"Kłamiesz, twój partner wspomniał kupca")
            AI_Output(npc_list.BDT_309_Bandit,"Kupiec... Tak, kupiec! Miał nam sprzedać mapy byśmy mogli dotrzeć do tamtej wioski! Mówie prawde, uwierzcie mi!")
            AI_Output(npc_list.PC_ANTIOCHUS,"Wierzysz mu?")
            print("[TAK/NIE]")
            while True:
                command = input()
                if command.lower() in include.yes_set:
                    AI_Output(PC_HERO,"Tak. Zostawmy go")
                    AI_Output(npc_list.BDT_309_Bandit,"Dziękuje! Już nigdy mnie nie zobaczycie obiecuje!")
                    print("Bandyta uciekł")
                    map.LOC_WAYSHRINE.npc.remove(npc_list.BDT_309_Bandit)
                    journal.SQ_Boatmaker_02.queststage = 25
                    print("## Nowy wpis w dzienniku...")
                    break
                if command.lower() in include.no_set:
                    PC_HERO.karma -= 1
                    PC_HERO.flags.append("killed_minion")
                    AI_Output(PC_HERO,"Nie. To się nie trzyma kupy. Skończmy z nim.")
                    print("[Przecinasz gardło bandyty]")
                    fight.kill(npc_list.BDT_309_Bandit,0)
                    journal.SQ_Boatmaker_02.queststage = 30
                    print("## Nowy wpis w dzienniku...")
                    break
        else:
            fight.kill(PC_HERO, 1)
            pass


def DIA_Bandits_Fight_Condition():
    if journal.SQ_Boatmaker_02.queststage == 10:
        return 1


DIA_Bandits_Fight = include.DIALOGUE(
    npc_list.BDT_308_Bandit,
    DIA_Bandits_Fight_Info,
    DIA_Bandits_Fight_Condition,
    0,
    "Zaatakuj"
)

#################
# Bandit's helper
#################
def DIA_Bandit_Riverside_1_First_Hello(other):
    if not journal.SQ_Boatmaker_02.queststage == 20:
        AI_Output(other,"Szukasz kłopotów?")
    else:
        AI_Output(other,"Życz nam szerokiej drogi!")

npc_list.BDT_309_Bandit.dialogue_hello = DIA_Bandit_Riverside_1_First_Hello

