import include
import npc_list
import journal
import item_list
import leveling
import inventory
import haggle
import enemy_list
import map
from hero import PC_HERO
from dialogue import AI_Output
import fight


def DIA_Bastard_First_Hello(other):
    print("Bękart z Koryntu siedzi na ganku swojej chaty i powoli dokańcza śniadanie. Gdy wziął kęs bekonu, tłuszcz spłynął mu po gęstej brodzie. Trzeba przyznać że jest on pokaźnym mężem.\nSiedzi więc trudno oszacować dokładnie, ale ma blisko sześć i pół stopy wzrostu. Szeroki w barach i z mocarnymi ramionami.\nNa sobie nosi zwyczajne spodnie i lnianą koszule, ale oburęczny miecz leży oparty o schody. Brzydka broń.\n")
    AI_Output(other,"Kim jesteś i co robisz na mojej farmie?")
    AI_Output(PC_HERO,"Jeśli jesteś tak blisko i nie wiesz gdzie zmierzam, musisz być głupcem.")
    AI_Output(other,"[Bękart uśmiechnął się paskudnie] A więc w tym rzecz. Tak spieszno ci by nas opuszczać? Rozsądny człowiek może się tu całkiem nieźle ułożyć")
    if PC_HERO.npcknowsinfo(DIA_Phrixos_First_Hello):
        AI_Output(other,"A skoro mowa o rozsądnych ludziach, to widziałem jak rozmawiałeś z moimi niewolnikami. Zwyczaj nakazuje spytać pana przed czymś takim")
        AI_Output(PC_HERO,"To nie są twoi niewolnicy. To Grecy jak ty i ja. Pojmałeś ich przemocą i wbrew prawu.")
        AI_Output(other,"Każdy niewolnik jest trzymany przemocą. A prawo? Rozejrzyj się. Prawa tutaj nie ma. Jest tylko takie jakie silny narzuci słabym.")
    AI_Output(other,"A ty wyglądasz mi na kogoś kto przydałby mi się do małej pracy")
    AI_Output(other,"Zainteresowany? Dobrze płace takim jak ty.")
    other.dialogue_hello = DIA_Bastard_Post_Hello

def DIA_Bastard_Post_Hello(other):
    AI_Output(other,"Mów co masz do powiedzenia. Byle szybko. Nie należe do cierpliwych ludzi.")

npc_list.BDT_300_Bastard.dialogue_hello = DIA_Bastard_First_Hello



### SHADOWBEAST quest
####################################
def DIA_Bastard_Quest_Info(other):
    AI_Output(PC_HERO,"Jaką masz dla mnie prace?")
    AI_Output(other,"Niedaleko moich pól zalęgła się bestia. Cieniostwór. Groźne bydle. Wysłałem do niego dwóch z moich chłopców.")
    AI_Output(other,"Znaleźliśmy ich kilka dni później. Musiałem prosić Alexis by ich odratowała. Paskudna sprawa. Grabarz pozszywał ich jak mógł, ale Vince i Nico do dzisiaj kuleją.")
    AI_Output(other,"Nie zamierzam posłać kolejnych chłopaków na śmierć, ale nie moge pozwolić by ta bestia grasowała w okolicy mojego obejścia.")
    PC_HERO.bastards_reward = 100
    PC_HERO.bastard_information = 0
    journal.SQ_Bastards_Man.status = "RUNNING"
    journal.SQ_Bastards_Man.queststage = 10
    print("## Nowy wpis w dzienniku...")

def DIA_Bastard_Quest_Condition():
    return 1

DIA_Bastard_Quest = include.DIALOGUE(
    npc_list.BDT_300_Bastard,
    DIA_Bastard_Quest_Info,
    DIA_Bastard_Quest_Condition,
    0,
    "Praca"
)

def DIA_Bastard_Doubt_Info(other):
    AI_Output(PC_HERO,"Mam uwierzyć że nagle zależy na bezpieczeństwie twoich więźniów?")
    AI_Output(other,"Słuchaj no. Nie wiem za jakiego masz mnie chuja, ale martwi chłopi mniej pracują")
    if PC_HERO.int >= 10:
        AI_Output(PC_HERO,"Wszyscy jesteśmy martwi.")
        AI_Output(other,"Patrzcie, jaki bystrzak się znalazł. Moge ci łatwo udowodnić że niektórzy z nas są bardziej martwi niż inni")
    AI_Output(other,"A im więcej bestia zeżre, tym trudniej jest przywrócić idiote do życia.")

def DIA_Bastard_Doubt_Condition():
    if PC_HERO.npcknowsinfo(DIA_Bastard_Quest) and journal.SQ_Bastards_Man.status == "RUNNING":
        return 1

DIA_Bastard_Doubt = include.DIALOGUE(
    npc_list.BDT_300_Bastard,
    DIA_Bastard_Doubt_Info,
    DIA_Bastard_Doubt_Condition,
    0,
    "Bezpieczeństwo Więźniów"
)


def DIA_Bastard_Kys_Info(other):
    AI_Output(PC_HERO,"Dlaczego sam nie zapolujesz na tego potwora?")
    AI_Output(other,"Pewnie bym dał rade. Gdybym mógł stąd pójść")
    AI_Output(other,"W momencie w którym znikne z widoku, połowa moich niewolników będzie próbowała włamać się do wieży")
    AI_Output(other,"Wole żeby kilku więcej zginęło, niż by mieć na głowie bunt gdy wróce")
    AI_Output(PC_HERO,"Prawdziwy z ciebie altruista, naprawde")

def DIA_Bastard_Kys_Condition():
    if PC_HERO.npcknowsinfo(DIA_Bastard_Doubt) and journal.SQ_Bastards_Man.status == "RUNNING":
        return 1

DIA_Bastard_Kys = include.DIALOGUE(
    npc_list.BDT_300_Bastard,
    DIA_Bastard_Kys_Info,
    DIA_Bastard_Kys_Condition,
    0,
    "Sam zapoluj"
)

def DIA_Bastard_Alexis_Info(other):
    AI_Output(PC_HERO,"Kim jest Alexis?")
    AI_Output(other,"Zadajesz dużo pytań, i zupełnie nie na temat. A gdzie pytania z serii 'Gdzie grasuje bestia?', 'Jak ją wytropić?', 'Ile ma w kłębie?'...")
    AI_Output(PC_HERO,"Odpowiesz na pytanie?")
    if PC_HERO.cha >= 10:
        AI_Output(other,"Masz jaja by tak do mnie mówić. Powiedzmy że mam dobry humor.")
        AI_Output(other,"Alexis jest moją kapłanką. Obawiam się że jej nie spotkasz.")
        if PC_HERO.npcknowsinfo(DIA_Phrixos_Bastard):
            AI_Output(PC_HERO,"Słyszałem o niej. Podobno mieliście wspólną przeszłość.")
            AI_Output(other,"A ja słyszałem że ktoś na farmie gada za dużo.")
            AI_Output(other,"Ale tak, ja i Alexis byliśmy razem zanim ten sukinsyn Uphel... Nieważne. To i tak nie jest temat o którym gadam z byle przybłędą.")
        else:
            AI_Output(PC_HERO,"Czemu, nie żyje?")
            AI_Output(other,"Wręcz przeciwnie.")
            AI_Output(PC_HERO,"W takim razie w jaki sposób...")
            AI_Output(other,"Czasem bezpieczniej jest nie wiedzieć zbyt wiele.")
    else:
        AI_Output(other,"Nie tym tonem, przybłędo.")
    AI_Output(other,"Skończyliśmy rozmawiać na ten temat.")

def DIA_Bastard_Alexis_Condition():
    if PC_HERO.npcknowsinfo(DIA_Bastard_Quest):
        return 1

DIA_Bastard_Alexis = include.DIALOGUE(
    npc_list.BDT_300_Bastard,
    DIA_Bastard_Alexis_Info,
    DIA_Bastard_Alexis_Condition,
    0,
    "Alexis"
)


def DIA_Bastard_Accept_Info(other):
    AI_Output(PC_HERO,"Zapoluje na tego twojego potwora.")
    AI_Output(other,"Świetnie. Masz, zjedz coś przed walką.")
    AI_Output(other,"Może i nie umieramy z głodu, ale na pewno wygodniej walczyć po solidnym śniadaniu.")

def DIA_Bastard_Accept_Condition():
    if PC_HERO.npcknowsinfo(DIA_Bastard_Quest) and not journal.SQ_Bastards_Man.status == "COMPLETED":
        return 1

DIA_Bastard_Accept = include.DIALOGUE(
    npc_list.BDT_300_Bastard,
    DIA_Bastard_Accept_Info,
    DIA_Bastard_Accept_Condition,
    0,
    "Zapoluje"
)

def DIA_Bastard_Price_Info(other):
    AI_Output(PC_HERO,"Porozmawiajmy o mojej nagrodzie.")
    AI_Output(other,"Jeszcze nic nie zrobiłeś. Za co chcesz nagrode?")
    AI_Output(PC_HERO,"Chce wiedzieć za ile nadstawiam skóre")
    AI_Output(other,"No dobrze. Czego chcesz?")
    if PC_HERO.int >= 20:
        AI_Output(PC_HERO,"Informacji.")
        AI_Output(other,"Sprytnie, chytrze. Ale za wskazanie drogi do Bramy musiałbyś zrobić coś więcej niż zasiec przerośniętego lwa")
        AI_Output(PC_HERO,"Nie mówiłem że to o tą informacje mi chodzi.")
        AI_Output(other,"W takim razie o co ci chodzi?")
        AI_Output(PC_HERO,"A to już też jest informacja, a one jak widzisz mają swoją cene.")
        AI_Output(other,"Ha ha! Chcesz zagrać w prawde za prawde? Zgoda.")
        AI_Output(other,"Zabij Bestie a zamienie z tobą jeden sekret na drugi.")
        AI_Output(other,"Ale cokolwiek o bramie jest wykluczone.")
        PC_HERO.bastard_information = 1
        PC_HERO.bastards_reward = 0
    elif PC_HERO.cha >= 15:
        PC_HERO.bastards_reward = haggle.haggle(PC_HERO,other,100)
        AI_Output(other,"Obyś był wart tych " + str(PC_HERO.bastards_reward) + " Oboli")
    else:
        AI_Output(PC_HERO,"200 Oboli")
        AI_Output(other,"Moge dać 100")
        AI_Output(PC_HERO,"150")
        AI_Output(other,"110 to moje ostatnie słowo. Bierz albo wynocha.")
        PC_HERO.bastards_reward = 110

def DIA_Bastard_Price_Condition():
    if PC_HERO.npcknowsinfo(DIA_Bastard_Quest) and not PC_HERO.npcknowsinfo(DIA_Bastard_Accept):
        return 1

DIA_Bastard_Price = include.DIALOGUE(
    npc_list.BDT_300_Bastard,
    DIA_Bastard_Price_Info,
    DIA_Bastard_Price_Condition,
    0,
    "Nagroda"
)


def DIA_Bastard_QuestDone_Info(other):
    AI_Output(PC_HERO,"Zabiłem twoją bestie")
    if PC_HERO.bastard_information == 0:
        AI_Output(other,"Oto twoje Obole, zasłużyłeś na nie")
        inventory.add_gold(PC_HERO,PC_HERO.bastards_reward)
    else:
        AI_Output(other,"I pewnie teraz chcesz zadać swoje pytanie. Pytaj.")

    journal.SQ_Bastards_Man.status = "COMPLETED"
    leveling.give_exp(PC_HERO,200)
    journal.SQ_Bastards_Man.queststage = 100
    print("## New Journal Entry...")

def DIA_Bastard_QuestDone_Condition():
    if enemy_list.mst_shadowbeast.hp == 0 and journal.SQ_Bastards_Man.status == "RUNNING":
        return 1

DIA_Bastard_QuestDone = include.DIALOGUE(
    npc_list.BDT_300_Bastard,
    DIA_Bastard_QuestDone_Info,
    DIA_Bastard_QuestDone_Condition,
    0,
    "Cieniostwór"
)


def DIA_Bastard_Pendant_Info(other):
    if PC_HERO.npcknowsinfo(DIA_Bastard_Doubt):
        AI_Output(PC_HERO,"Okłamałeś mnie. Nie chodziło ci o bezpieczeństwo więźnów")
        AI_Output(PC_HERO,"Ta bestia strzegła czegoś co należało do ciebie")
        AI_Output(other,"Trzeba wiele odwagi by zarzucić mi kłamstwo.")
        AI_Output(other,"Ale masz racje. Okłamałem cie. A teraz daj mi to.")
    else:
        AI_Output(PC_HERO,"Zdaje się że to należy do ciebie.")
        AI_Output(other,"No prosze. Przydajesz się bardziej niż cie o to posądzałem")

    PC_HERO.inventory.remove(item_list.itmi_bastard_amulet)
    leveling.give_exp(PC_HERO,50)

def DIA_Bastard_Pendant_Condition():
    if item_list.itmi_bastard_amulet in PC_HERO.inventory:
        return 1

DIA_Bastard_Pendant = include.DIALOGUE(
    npc_list.BDT_300_Bastard,
    DIA_Bastard_Pendant_Info,
    DIA_Bastard_Pendant_Condition,
    0,
    "Wisiorek"
)

## Gra w "Prawde" z Bękartem
# Gracz może dostać info o kluczu skracające 3 rozdział do 1 questa albo info które demaskuje prawdziwy rok
# Opcja ze śmiercią Bękarta nic nie daje
def DIA_Bastard_Wish_Death_Info(other):
    AI_Output(PC_HERO,"W jaki sposób umarłeś?")
    AI_Output(other,"Tyle zachodu, całe negocjacje i marnujesz swoją runde na tak błahe pytanie?")
    AI_Output(other,"Nie wiem na co ta informacja, ale słowo się rzekło. Odpowiem.")
    AI_Output(other,"Tigranocerta. Zabił mnie partyjski najemnik, Naphav Uphel. Miał szczęście. Teraz moja kolej.")
    PC_HERO.bastard_information = 0
    AI_Output(other,"Kiedy TY umarłeś?")
    AI_Output(PC_HERO,"Najpierw sarkasz na to że ja zadałem ci to pytanie, a teraz ty zadajesz je mi?")
    AI_Output(other,"Nie obchodzi mnie to. Gadaj kiedy umarłeś.")
    if PC_HERO.npcknowsinfo(DIA_Phrixos_First_Hello):
        AI_Output(other,"Wiem że ty i Phrixos znacie się z czasów jak jeszcze żył.") # Bękart też jest poddawany próbie. Hades w jego historii jest w roli Grabarza. Stąd miejsce w którym osiedlił się Bękart
    AI_Output(other,"Widziałem z kim przyszedłeś na farme. Gadaj.") # Bękart wie że to nie Antiochus bo spotkał jego prawdziwego ducha, nie wiem czy będę miał czas rozwinąć ten wątek
    AI_Output(PC_HERO,"Magnezja, 143 lata po Issos")
    AI_Output(other,"Więc to prawda. Jesteśmy przeklęci.")
    AI_Output(PC_HERO,"O co ci chodzi?")
    AI_Output(other,"A to już drugie pytanie. Wyjdź. Chce pobyć sam.")

def DIA_Bastard_Wish_Death_Condition():
    if journal.SQ_Bastards_Man.status == "COMPLETED" and PC_HERO.bastard_information == 1:
        return 1

DIA_Bastard_Wish_Death = include.DIALOGUE(
    npc_list.BDT_300_Bastard,
    DIA_Bastard_Wish_Death_Info,
    DIA_Bastard_Wish_Death_Condition,
    0,
    "Jak umarłeś?"
)


def DIA_Bastard_Wish_Success_Info(other):
    AI_Output(PC_HERO,"Co ktoś taki jak ty osiągnął największego w życiu?")
    AI_Output(other,"Tigranocerta. Trzy cale od szyi Lucullusa.")
    AI_Output(PC_HERO,"Co?")
    AI_Output(other,"Nie zrozumiesz. Moja kolej.")
    PC_HERO.bastard_information = 0
    AI_Output(other,"Kiedy umarłeś?")
    AI_Output(PC_HERO,"Naprawde zużywasz swoje pytanie na coś tak nieistotnego?")
    AI_Output(other,"Nie obchodzi mnie twoja opinia. Gadaj kiedy umarłeś.")
    if PC_HERO.npcknowsinfo(DIA_Phrixos_First_Hello):
        AI_Output(other,"Wiem że ty i Phrixos znacie się z czasów jak jeszcze żył.") # Bękart też jest poddawany próbie. Hades w jego historii jest w roli Grabarza. Stąd miejsce w którym osiedlił się Bękart
    AI_Output(other,"Widziałem z kim przyszedłeś na farme. Gadaj.") # Bękart wie że to nie Antiochus bo spotkał jego prawdziwego ducha, nie wiem czy będę miał czas rozwinąć ten wątek
    AI_Output(PC_HERO,"Magnezja, 143 lata po Issos")
    AI_Output(other,"Więc to prawda. Jesteśmy przeklęci.")
    AI_Output(PC_HERO,"O co ci chodzi?")
    AI_Output(other,"A to już drugie pytanie. Wyjdź. Chce pobyć sam.")

def DIA_Bastard_Wish_Success_Condition():
    if journal.SQ_Bastards_Man.status == "COMPLETED" and PC_HERO.bastard_information == 1:
        return 1

DIA_Bastard_Wish_Success = include.DIALOGUE(
    npc_list.BDT_300_Bastard,
    DIA_Bastard_Wish_Success_Info,
    DIA_Bastard_Wish_Success_Condition,
    0,
    "Największe osiągnięcie?"
)


def DIA_Bastard_Wish_Key_Info(other):
    AI_Output(PC_HERO,"Klucz do wieży Latarnika")
    AI_Output(other,"To nie jest pytanie")
    AI_Output(PC_HERO,"Gdzie on jest?")
    AI_Output(other,"Chcesz umrzeć?")
    AI_Output(PC_HERO,"Dałeś słowo. Nie pytam o droge do Bramy ani o nic związanego z nią. Powtarzam pytanie. Gdzie trzymasz klucz do wieży?")
    AI_Output(other,"Wiesz że wystarczy że krzykne a będzie tu pół tuzina moich chłopców?")
    AI_Output(PC_HERO,"Tracisz twarz. Klucz.")
    input()
    AI_Output(other,"Brawo. Dobrze. Dałem słowo. Oddałem klucz Grabarzowi. Wątpie by ci go oddał.")
    AI_Output(other,"Jeśli jednak to zrobi, wiedz jedno. Wejdziesz do wieży - nie żyjesz")
    AI_Output(other,"Nie, więcej niż nie żyjesz. Wypruje ci jelita i powiesze cie na haku. A następnie powiem Alexis by składała za ciebie ofiare. Codziennie.")
    AI_Output(PC_HERO,"Tracisz twarz. Teraz twoje pytanie.")
    PC_HERO.bastard_information = 0
    AI_Output(other,"Kiedy umarłeś?")
    AI_Output(PC_HERO,"Naprawde zużywasz swoje pytanie na coś tak nieistotnego?")
    AI_Output(other,"Nie obchodzi mnie twoja opinia. Gadaj kiedy umarłeś.")
    if PC_HERO.npcknowsinfo(DIA_Phrixos_First_Hello):
        AI_Output(other,"Wiem że ty i Phrixos znacie się z czasów jak jeszcze żył.") # Bękart też jest poddawany próbie. Hades w jego historii jest w roli Grabarza. Stąd miejsce w którym osiedlił się Bękart
    AI_Output(other,"Widziałem z kim przyszedłeś na farme. Gadaj.") # Bękart wie że to nie Antiochus bo spotkał jego prawdziwego ducha, nie wiem czy będę miał czas rozwinąć ten wątek
    AI_Output(PC_HERO,"Magnezja, 143 lata po Issos")
    AI_Output(other,"Więc to prawda. Jesteśmy przeklęci.")
    AI_Output(PC_HERO,"O co ci chodzi?")
    AI_Output(other,"A to już drugie pytanie. Wyjdź. Chce pobyć sam.")

def DIA_Bastard_Wish_Key_Condition():
    if journal.SQ_Bastards_Man.status == "COMPLETED" and PC_HERO.npcknowsinfo(DIA_Phrixos_Lighthouse) and PC_HERO.bastard_information == 1:
        return 1

DIA_Bastard_Wish_Key = include.DIALOGUE(
    npc_list.BDT_300_Bastard,
    DIA_Bastard_Wish_Key_Info,
    DIA_Bastard_Wish_Key_Condition,
    0,
    "Gdzie jest klucz?"
)

### THE TRUTH chain
####################################
def DIA_Bastard_Lucullus_Info(other):
    AI_Output(PC_HERO,"Lucullus to imie rzymskie")
    AI_Output(other,"Lucius Licinius Lucullus, no i? Nie chce o tym gadać.")
    AI_Output(PC_HERO,"Phrixos mówił że walczyłeś po naszej stronie w wojnach których nie znałem")
    AI_Output(other,"Więc? Nadużywasz mojej cierpliwości chłopcze")
    AI_Output(PC_HERO,"Nasze wojny z Rzymem zaczęły się 30 lat temu, gdy Filip Piąty wsparł Hannibala")
    AI_Output(other,"[Uśmiecha się enigmatycznie] Zaczynasz rozumieć")
    AI_Output(PC_HERO,"Wątpie by Phrixos nazywał dzikusów z Epiru i Illyrii naszą stroną. Zresztą tamte wojny też znam. Żadnego Mithrydatesa")
    AI_Output(other,"Blisko.")
    AI_Output(PC_HERO,"Kiedy umarłeś?")
    AI_Output(other,"Naginasz zasady chłopcze. Miała być jedna prawda za prawde. To już drugie pytanie")
    AI_Output(PC_HERO,"Nie gramy a mi skończyła się cierpliwość do gry. Wiesz o co pytam. Wiesz czemu o to pytam. I wiem że ty też o tym myślisz")
    AI_Output(other,"Tigranocerta. 264 lata po bitwie pod Issos.")
    AI_Output(PC_HERO,"To znaczy...")
    AI_Output(other,"121 lat po bitwie pod Magnezją")
    AI_Output(PC_HERO,"Czyli teraz jest...")
    AI_Output(other,"Teraz już wiesz czemu interesowało mnie kiedy umarłeś")

def DIA_Bastard_Lucullus_Condition():
    if PC_HERO.npcknowsinfo(DIA_Bastard_Wish_Success) and PC_HERO.int > 40:
        return 1

DIA_Bastard_Lucullus = include.DIALOGUE(
    npc_list.BDT_300_Bastard,
    DIA_Bastard_Lucullus_Info,
    DIA_Bastard_Lucullus_Condition,
    0,
    "Lucullus"
)


def DIA_Bastard_Antiochus_Info(other):
    AI_Output(PC_HERO,"Gdy zadawałeś mi pytanie wspomniałeś o księciu...")
    AI_Output(other,"Wspomniałem.")
    AI_Output(PC_HERO,"Dlaczego?")
    AI_Output(other,"Coraz więcej pytań...")
    AI_Output(other,"Grób pod wierzbą, cmentarz. Znajdź tam odpowiedź na swoje pytanie.")
    PC_HERO.antiochus_grave = 1

def DIA_Bastard_Antiochus_Condition():
    if PC_HERO.npcknowsinfo(DIA_Bastard_Lucullus) and PC_HERO.int > 40:
        return 1

DIA_Bastard_Antiochus = include.DIALOGUE(
    npc_list.BDT_300_Bastard,
    DIA_Bastard_Antiochus_Info,
    DIA_Bastard_Antiochus_Condition,
    0,
    "Antiochus"
)


def DIA_Bastard_AntiochusDead_Info(other):
    AI_Output(PC_HERO,"Widziałem grób. Zabiłeś go.")
    AI_Output(other,"Tak. To było z rok temu, może dwa.")
    AI_Output(PC_HERO,"Dlaczego?")
    AI_Output(other,"Czy jeśli powiem że dlatego że zadawał zbyt wiele pytań, zaakceptujesz tą odpowiedź i pójdziesz precz?")
    AI_Output(PC_HERO,"Nie mam nastroju do żartów. Dlaczego zabiłeś Antiochusa? Kim jest człowiek który mnie prowadzi? Mów")
    AI_Output(other,"Przyszedł tu wtedy. Miał na sobie piękny płaszcz, zdobiony miecz przy boku. To było jakoś trzy lata po tym jak powiedziałem Grabarzowi że to koniec")
    AI_Output(other,"Szukaliśmy razem Bramy, ale już wtedy zacząłem widzieć prawde. Spotykałem ludzi którzy mnie znali, mimo że ja ich nie pamiętałem")
    AI_Output(other,"Twój książe przyjechał tu, w pięknej zbroi, z mieczem u boku. Z początku wydawał się być dobrym kompanem.")
    AI_Output(other,"Mówił że przed kimś ucieka. Gdy dowiedział się o mojej więzi z Alexis, wręcz błagał mnie bym pozwolił mu z nią porozmawiać")
    AI_Output(other,"Ale Grabarz mu nie ufał. Pewnej nocy powiedział mi że Antiochus i moi niewolnicy szykują spisek by zabić mnie i Latarnika")
    AI_Output(other,"Uwierzyłem mu. Dlaczego miałbym nie? Był moim towarzyszem przez cały czas odkąd się tu obudziłem. Zabiłem twojego księcia. To była dobra walka.")
    AI_Output(other,"Miesiąc temu, gdy zacząłem coś podejrzewać, próbowałem przekazać Alexis wiadomość. Prośbe by przywróciła twojego księcia")
    AI_Output(PC_HERO,"Więc dlaczego dalej jest martwy?")
    AI_Output(other,"Gdy wyciągnąłem z ognia kawałek pergaminu, to nie było jej pismo. Mam to dalej przy sobie. Zobacz sam.")
    print(" ")
    print("Zwitek pergaminu który podał ci Bękart ma na sobie zapisane kilka zdań niemożliwie drobną, cienką linią. Jakby nie było wyryte przez człowieka")
    print("TO JEDYNE I OSTATNIE OSTRZEŻENIE BĘKARCIE \nMASZ WŁADZE NAD SWOIM 'KRÓLESTWEM'\nCIESZ SIĘ NIM, I NIGDY WIĘCEJ NIE POŻĄDAJ ODPOWIEDZI NA TO GDZIE JESTEŚ")

def DIA_Bastard_AntiochusDead_Condition():
    if PC_HERO.antiochus_grave == 2:
        return 1

DIA_Bastard_AntiochusDead = include.DIALOGUE(
    npc_list.BDT_300_Bastard,
    DIA_Bastard_AntiochusDead_Info,
    DIA_Bastard_AntiochusDead_Condition,
    0,
    "Antiochus"
)


def DIA_Bastard_AntiochusDie_Info(other):
    AI_Output(PC_HERO,"Kimkolwiek jesteś, kimkolwiek *on* jest, przysięgałem prawdziwemu Antiochusowi na swój honor")
    AI_Output(other,"I co zamierzasz z tym zrobić?")
    AI_Output(PC_HERO,"Zabije cie")
    AI_Output(other,"Jestem nieśmiertelny, wiesz o tym.")
    AI_Output(other,"Ale niech będzie. Oboje jesteśmy mu to winni. Wyciągaj żelazo.")
    fightresult = fight.startfight(PC_HERO,other)
    if fightresult == "SUCCESS":
        print("Bękart upadł wykrawiając się z potężnej rany na szyi. Pare sekund później szczyt Wieży Latarnika rozbłysł płomieniem")
        if PC_HERO.npcknowsinfo(DIA_Phrixos_Lighthouse):
            print("Alexis już wie.")


def DIA_Bastard_AntiochusDie_Condition():
   #if PC_HERO.npcknowsinfo(DIA_Bastard_AntiochusDead):
    return 0 #Scene disabled from final cut. Sorry.

DIA_Bastard_AntiochusDie = include.DIALOGUE(
    npc_list.BDT_300_Bastard,
    DIA_Bastard_AntiochusDie_Info,
    DIA_Bastard_AntiochusDie_Condition,
    0,
    "Zginiesz za to"
)






def DIA_Bastard_Lantern_Hello(other):
    if "i_choose_violence" in PC_HERO.flags:
        AI_Output(other,"[Bękart nie wygląda dobrze po waszej poprzedniej walce, wciąż jest ubrudzony krwią]")
        AI_Output(other,"Zatłuke. Zakope. Zabije!")
        AI_Output(other,"[Bękart rzucił się na ciebie]")
    else:
        AI_Output(other,"Powinienem był cie zabić gdy tylko tu przyszedłeś")
        if PC_HERO.npcknowsinfo(DIA_Bastard_AntiochusDead) == 1:
            AI_Output(other,"I to wszystko wiedząc że tkwimy w tym razem...")
        else:
            AI_Output(PC_HERO,"Wtedy byłeś nieśmiertelny. Teraz mamy równe szanse")
        AI_Output(other,"Na zewnątrz czeka pół tuzina moich chłopców. Jeśli nie ja, to oni cie wykończą")
        AI_Output(PC_HERO,"Albo będą chcieli dostać z powrotem swoich przyjaciół. Kończmy to")
    input()
    result = fight.startfight(PC_HERO,other)
    if result == "SUCCESS":
        print("\nBękart upadł na ziemie wykrwawiając się z potężnej rany w szyi. Ostatkami sił próbował wczołgać się na schody")
        print("Mechanicznie wręcz obróciłeś miecz i przebiłeś nim bandyte. Drzwi jednak otworzyły się. Dziwne. Przysiągłbyś że Bękart je zamknął")
        print("Przez drzwi wszedł do środka Książe Antiochus")
        map.LOC_TOWER.npc.append(npc_list.PC_ANTIOCHUS_Lantern)
    else:
        fight.kill(PC_HERO,1)



npc_list.BDT_300_Bastard_Lantern.dialogue_hello = DIA_Bastard_Lantern_Hello
