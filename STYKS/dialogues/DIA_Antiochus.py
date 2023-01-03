import include
import npc_list
import journal
import item_list
import leveling
import vob_list
import fight
from hero import PC_HERO
from dialogue import AI_Output

def DIA_Antiochus_Hello(other):
    if journal.MQ01.queststage == 10:
        AI_Output(other,"Jak ci idzie zdobycie promu " + PC_HERO.name + "?")
    if journal.MQ01.queststage == 20:
        AI_Output(other,"Musimy dostać się do Wyroczni")
    if journal.MQ01.queststage == 30:
        AI_Output(other,"Wygląda na to że znaleźliśmy naszą Latarnie.")


npc_list.PC_ANTIOCHUS.dialogue_hello = DIA_Antiochus_Hello

def DIA_Antiochus_Boat_Info(other):
    AI_Output(PC_HERO,"Masz jakiś pomysł jak dostać się na tą wyspe?")
    AI_Output(other,"Moglibyśmy iść wzdłóż Styenu aż wpłynie. Ale ta podróż to byłoby samobójstwo")
    AI_Output(other,"Wody Styenu deprawują zwierzęta które z nich piją. Podróż na piechote zajęłaby wiele tygodni")
    AI_Output(other,"Wiele tygodni bez snu i odpoczynku - w takim momencie bylibyśmy najbardziej narażeni")
    AI_Output(other,"Niedaleko widziałem małą wioske rybacką. Być może któryś z wieśniaków pożyczy nam swoją łódź.")

def DIA_Antiochus_Boat_Condition():
    if journal.MQ01.queststage == 10:
        return 1

DIA_Antiochus_Boat = include.DIALOGUE(
    npc_list.PC_ANTIOCHUS,
    DIA_Antiochus_Boat_Info,
    DIA_Antiochus_Boat_Condition,
    0,
    "Świątynia"
)

def DIA_Antiochus_Boatmaker_Info(other):
    AI_Output(PC_HERO,"Szkutnik pomoże nam dostać się na drugi brzeg ale musimy mu pomóc")
    AI_Output(PC_HERO,"Chce byśmy odstraszyli bandytów od jego chaty")
    AI_Output(other,"Tych dwóch tutaj? To nie będzie trudne")

def DIA_Antiochus_Boatmaker_Condition():
    if journal.SQ_Boatmaker_02.status == "RUNNING":
        return 1

DIA_Antiochus_Boatmaker = include.DIALOGUE(
    npc_list.PC_ANTIOCHUS,
    DIA_Antiochus_Boatmaker_Info,
    DIA_Antiochus_Boatmaker_Condition,
    0,
    "Szkutnik"
)

def DIA_Antiochus_BoatmakerKey_Info(other):
    AI_Output(PC_HERO,"Mam klucz do chaty szkutnika. Możemy mu ukraść prom")
    AI_Output(other,"Jest to jakaś opcja. Będę obserwował wioske, jak zobacze że włamujesz mu się do chaty, pójde w strone promu")

def DIA_Antiochus_BoatmakerKey_Condition():
    if item_list.itke_boatmaker_key in PC_HERO.inventory:
        return 1

DIA_Antiochus_BoatmakerKey = include.DIALOGUE(
    npc_list.PC_ANTIOCHUS,
    DIA_Antiochus_BoatmakerKey_Info,
    DIA_Antiochus_BoatmakerKey_Condition,
    0,
    "Klucz"
)


def DIA_Antiochus_Lantern(other):
    AI_Output(PC_HERO,"Chodź, rozumiem już jak korzystać z płomienia, teraz tylko musimy znaleźć tutaj klucz")
    if npc_list.BDT_302_Keeper.hp == 0:
        AI_Output(other,"[Antiochus zdaje się ciebie nie słuchać. Spojrzał tylko na ciało Latarnika i westchnął]")
    AI_Output(other,"Niestety " + PC_HERO.name + " nie mogę ci pomóc. Nie musisz już szukać klucza")
    input()
    if PC_HERO.antiochus_grave == 2:
        AI_Output(other,"Przyszedłem tu żeby...")
        AI_Output(PC_HERO,"Wiem, nie jesteś prawdziwym Antiochusem, a teraz zamknij się i pomóż mi szukać klucza")
        AI_Output(other,"[Antiochus był dość zdziwiony odpowiedzią]")
        AI_Output(other,"To chyba pierwszy raz jak zamiast uciekać albo walczyć... po prostu to zignorowałeś")
        AI_Output(PC_HERO,"Antiochus walczył. Wygląda na to że nie ma tu przed tobą ucieczki.")
        PC_HERO.karma += 1
        AI_Output(PC_HERO,"Rozumiem że brama nie istnieje")
        AI_Output(other,"Dobrze rozumiesz")
        AI_Output(PC_HERO,"Po co w takim razie cała ta intryga?")
        AI_Output(other,"Tutaj nad Styksem jest tylko pierwszy przystanek na drodze każdego umarłego")
        AI_Output(other,"Zanim dowiemy się gdzie wysłać następnego zmarłego musimy sprawdzić na co zasłużył")
        AI_Output(PC_HERO,"Czy wszyscy ludzie których spotkałem byli częścią twojej gry?")
        AI_Output(other,"Nie wszyscy. Spora część.")
        AI_Output(other,"Część po prostu została tutaj. Odmówili testu, nie próbowali się wydostać, albo zwyczajnie odnaleźli tu swoje miejsce")
        AI_Output(PC_HERO,"Wiem że minęło wiele lat")
        AI_Output(other,"Hades być może jest bogiem śmierci, ale jest też łaskawy. Daje wiele szans. A ty wiele razy zawiodłeś")
        AI_Output(PC_HERO,"Trzymanie nas tutaj jak zwierzęta w klatce nie jest łaskawe")
        AI_Output(other,"Być może. Nie mi to oceniać.")
        AI_Output(PC_HERO,"Skoro mowa o ocenianiu... przejdźmy do rzeczy. Mów swoje.")
    else:
        AI_Output(other,"Przyszedłem porozmawiać. Klucz nie istnieje.")
        AI_Output(PC_HERO,"Co? Skąd wiesz? To niemożliwe, Wyrocznia powiedziała...")
        AI_Output(other,"Powiedziała że tu się zakończy twoja podróż. Zawsze wysyła ludzi w tą okolice")
        AI_Output(other,"Gdy wysłała tu Bękarta, stwierdził że nie ruszy się do miejsca które mu wybrała")
        AI_Output(other,"Zamiast pójść wytyczonym szlakiem oznajmił Grabarzowi że tutaj zostaje. Ty dotarłeś do końca. Spełniłeś dane ci zadanie")
        AI_Output(PC_HERO,"Co? O czym ty mówisz? Bękart widział się z Wyrocznią? O jaki szlak chodzi?")
        AI_Output(other,"Nie rozumiesz. Bramy nigdy nie było. To tylko próba. Test, któremu poddajemy każdego nowego")
        AI_Output(PC_HERO,"Jak to... Dlaczego...")
        input()
        AI_Output(other,"Tutaj trafiają różne dusze jedne są dobre, inne złe. Musimy zdecydować co z nimi zrobić.")
        AI_Output(other,"Zwykliśmy przybierać forme ludzi których nasz pacjent szanował za życia.")
        AI_Output(PC_HERO,"Pacjent?!")
        AI_Output(other,"Gdy ktoś nie przechodzi testu, cofamy pamięć o tym wydarzeniu i za pare lat przeprowadzamy go od nowa")
        AI_Output(PC_HERO,"Od nowa... ile lat jestem waszym więźniem? Ile razy mnie już 'Testowaliście'?!")
        AI_Output(other,"Gniew naprawde jest niepotrzebny, robimy to dla twojego dobra...")
        AI_Output(PC_HERO,"ILE. RAZY?!")
        input()
        AI_Output(other,"Sto siedemdziesiąt trzy lata, trzydzieści pięć pełnych cykli. Ten jest trzydziesty szósty")
        AI_Output(PC_HERO,"[Niemy szok]")
        AI_Output(other,"Za każdym razem zabijałeś, mordowałeś, szantażowałeś i kradłeś przez swoją droge, byleby tylko osiągnąć cel")
    if "extorted_slave" in PC_HERO.flags:
        AI_Output(other,"Wykorzystałeś głodnego więźnia by dowiedzieć się gdzie jest brama") #-1
    if "absolute_dick_to_slave" in PC_HERO.flags:
        AI_Output(other,"...po czym nawet nie dałęś mu obiecanego chleba") #-2
    if "killed_petty" in PC_HERO.flags:
        AI_Output(other,"Zabiłeś zwykłego drobnego złodzieja za to że wyglądał ci na groźnego") #-1
    if "killed_minion" in PC_HERO.flags:
        AI_Output(other,"...dobiłeś nawet rannego który się poddał") #-1
    if "killed_keeper" in PC_HERO.flags:
        AI_Output(other,"Zabiłeś Latarnika który nawet nie walczył. Bał sie ciebie i uciekał w panice") #-1
    if "stolen_ferry" in PC_HERO.flags:
        AI_Output(other,"Ukradłeś Szkutnikowi jego prom") #-1
    if "stolen_amulet" in PC_HERO.flags:
        AI_Output(other,"Ukradłeś amulet Grabarzowi") #-1
    #Karma:
    # Negative max = -8
    # Positive sources:
    # Riverside +1
    # Oracle +2
    # Bread +1
    if not "mercy_oracle" in PC_HERO.flags:
        AI_Output(other,"Pozwoliłeś cierpieć Wyroczni bo służyło to twoim celom")
    elif "mercy_oracle" in PC_HERO.flags:
        AI_Output(other,"Zaimponowało mi to że zlitowałeś się nad Wyrocznią. Mimo że wprost powiedziałem ci że możesz przez to zostać tu na zawsze")
    if "mountain_lion" in PC_HERO.flags:
        AI_Output(other,"Musze przyznać że to z Pumą było dobre.")
    if PC_HERO.karma == 4:
        AI_Output(other,"Jesteś dowodem na to że nie istnieją przypadki beznadziejne. Pozwolę ci przejść dalej. Na pola elizejskie")
        AI_Output(PC_HERO,"Nie wiem czy cie przekląć czy ci dziękować")
        AI_Output(other,"Nie musisz. Tej podróży też nie będziesz pamiętał")
        input()
        PC_HERO.flags.append("elysium")
        leveling.give_exp(PC_HERO, 300)
        fight.kill(PC_HERO,1)
    if PC_HERO.karma > 0:
        AI_Output(other,"Dobre uczynki nie równoważą złych.")
        AI_Output(other,"Czyniłeś zarówno dobro jak i zło. Nie jesteśmy pewni. Na szczęście mamy czas")
        AI_Output(PC_HERO,"Nie waż się! Nie waż się mieszać znowu w mojej głowie!!!")
        AI_Output(other,"Nie bój się. To potrwa tylko chwile")
        input()
        PC_HERO.flags.append("loop")
        leveling.give_exp(PC_HERO, 200)
        fight.kill(PC_HERO,1)
    elif PC_HERO.karma > -6:
        AI_Output(other,"Uczyniłeś wiele zła by się tutaj dostać")
        AI_Output(other,"Na szczęście mamy dość czasu. Całą wieczność")
        AI_Output(PC_HERO,"Nie waż się! Nie waż się mieszać znowu w mojej głowie!!!")
        AI_Output(other,"Nie bój się. To potrwa tylko chwile")
        input()
        PC_HERO.flags.append("loop")
        leveling.give_exp(PC_HERO, 100)
        fight.kill(PC_HERO,1)
    else:
        AI_Output(other,"Jesteś potworem w ludzkiej skórze. Minęło już 36 prób i wciąż żadnej poprawy.")
        AI_Output(PC_HERO,"Może to wasza próba psuje ludzi?")
        AI_Output(other,"Możę. Możesz być pewien że powtórze twoje słowa Hadesowi")
        AI_Output(other,"Ale do tej pory... przykro mi synu. Wiesz gdzie musisz teraz iść")
        AI_Output(PC_HERO,"Wymażesz mi pamięć i wrócisz mnie do tej przeklętej pętli")
        AI_Output(other,"Nie tym razem. Przykro mi to robić ale muszę. Niniejszym zsyłam cie do Tartaru")
        input()
        PC_HERO.flags.append("tartaros")
        fight.kill(PC_HERO,1)


npc_list.PC_ANTIOCHUS_Lantern.dialogue_hello = DIA_Antiochus_Lantern
