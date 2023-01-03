import include
import npc_list
import journal
import item_list
import leveling
import vob_list
from hero import PC_HERO
from dialogue import AI_Output


def DIA_Boatmaker_First_Hello(other):
    AI_Output(other,"Witaj. Jesteś tu nowy? Nigdy wcześniej cie tu nie widziałem")
    AI_Output(PC_HERO,"Nic dziwnego. Masz racje, dopiero tu trafiłem. Na imie mi " + PC_HERO.name)
    AI_Output(other,"Jestem szkutnikiem. A to mój warsztat")
    AI_Output(PC_HERO,"Tak się składa że potrzebuję łodzi, albo promu")
    AI_Output(other,"Może będę ci w stanie pomóc... gdybym tylko miał mój klucz...")
    other.dialogue_hello = DIA_Boatmaker_Post_Hello

def DIA_Boatmaker_Post_Hello(other):
    AI_Output(PC_HERO,"Witaj Szkutniku")
    AI_Output(other,"Witaj " + PC_HERO.name)

npc_list.VLK_100_Boatmaker.dialogue_hello = DIA_Boatmaker_First_Hello

###
### First Quest
###

def DIA_Boatmaker_Quest_Info(other):
    AI_Output(PC_HERO,"Wspominałeś coś o kluczu")
    AI_Output(other,"Tak, wspominałem. Widzisz " + PC_HERO.name + " zdarza ci się czasem pić?")
    response = input()
    AI_Output(PC_HERO,response)
    AI_Output(other,"W tym cholernym miejscu nie jest wiele do roboty")
    AI_Output(other,"Kilka dni temu wracałem od mojego przyjaciela, Kotylona i tak się złożyło że zawędrowałem do jaskini coś sprawdzić...")
    AI_Output(PC_HERO,"Sprawdzić? Co takiego?")
    AI_Output(other,"Ach, nie w tym rzecz, nieważne. Słuchaj. Wygląda na to że w jaskini zalęgło się jakieś poskudztwo. Ogar albo Topielec")
    AI_Output(other,"Gdy wyskoczył na mnie z ciemności, musiałem upuścić swój klucz")
    AI_Output(other,"Teraz nie mam jak wejść do mojej chaty. Mam tam wszystkie narzędzia i pare innych cennych rzeczy")
    journal.SQ_Boatmaker_01.status = "RUNNING"
    journal.SQ_Boatmaker_01.queststage = 10
    print("## Nowy wpis w dzienniku...")
    if item_list.itke_boatmaker_key in PC_HERO.inventory:
        journal.SQ_Boatmaker_01.queststage = 20
        print("## Nowy wpis w dzienniku...")

def DIA_Boatmaker_Quest_Condition():
    return 1

DIA_Boatmaker_Quest = include.DIALOGUE(
    npc_list.VLK_100_Boatmaker,
    DIA_Boatmaker_Quest_Info,
    DIA_Boatmaker_Quest_Condition,
    0,
    "Klucz"
)

def DIA_Boatmaker_Key_Info(other):
    AI_Output(PC_HERO,"Mam twój klucz")
    AI_Output(other,"Naprawde? Pokaż!")
    AI_Output(other,"Nie wierze, a co z Topielcem?")
    AI_Output(PC_HERO,"Nie żyje.")
    AI_Output(other,"Piękne dzięki chłopcze!")
    AI_Output(other,"Wychylisz ze mną jednego?")
    response = input()
    if response in include.yes_set:
        AI_Output(PC_HERO,response)
        AI_Output(other,"Tak myślałem! No to do dna!")
        AI_Output(other,"[Pije]")
        AI_Output(PC_HERO,"[Pije]")
    elif response in include.no_set:
        AI_Output(PC_HERO,response)
        AI_Output(other,"Ah... no, to może innym razem!")
    journal.SQ_Boatmaker_01.status = "COMPLETED"
    leveling.give_exp(PC_HERO,100)
    journal.SQ_Boatmaker_01.queststage = 100
    PC_HERO.inventory.remove(item_list.itke_boatmaker_key)
    print("## New Journal Entry...")

def DIA_Boatmaker_Key_Condition():
    if journal.SQ_Boatmaker_01.status == "RUNNING" and item_list.itke_boatmaker_key in PC_HERO.inventory:
        return 1
    else:
        return 0

DIA_Boatmaker_Key = include.DIALOGUE(
    npc_list.VLK_100_Boatmaker,
    DIA_Boatmaker_Key_Info,
    DIA_Boatmaker_Key_Condition,
    0,
    "Klucz"
)


def DIA_Boatmaker_Food_Info(other):
    if PC_HERO.npcknowsinfo(DIA_Boatmaker_Key):
        AI_Output(PC_HERO,"Mówisz że nie mogłeś wejść do chaty przez kilka dni")
        AI_Output(other,"To prawda. Dziękuje że mi pomogłeś")
    else:
        AI_Output(PC_HERO,"Mówisz że nie możesz wejść do chaty od kilku dni")
        AI_Output(other,"To prawda")
    AI_Output(PC_HERO,"Co w takim razie jadłeś? Kilka dni bez jedzenia brzmi...")
    AI_Output(other,"Ah. Zapomniałem że jesteś tu nowy. Po tej stronie świat wygląda troche inaczej. Nie potrzebujemy jeść żeby żyć. Co nie znaczy że nie czujemy głodu. Głód nas tylko osłabia, ale nie jest w stanie zabić")
    AI_Output(PC_HERO,"Rozumiem...")

def DIA_Boatmaker_Food_Condition():
    if PC_HERO.npcknowsinfo(DIA_Boatmaker_Quest):
        return 1
    else:
        return 0

DIA_Boatmaker_Food = include.DIALOGUE(
    npc_list.VLK_100_Boatmaker,
    DIA_Boatmaker_Food_Info,
    DIA_Boatmaker_Food_Condition,
    0,
    "Głód"
)

def DIA_Boatmaker_Monsters_Info(other):
    AI_Output(PC_HERO,"Topielec? Ogar? Znaczy, wiem co to ogar ale...")
    AI_Output(other,"Topielce to takie duże gady. Żyją w Styksie i jego dopływach...")
    AI_Output(PC_HERO,"To swoją drogą. Bardziej mnie zastanawiało skąd tu w ogóle są potwory. Spytałbym czy one też trafiają do zaświatów po śmierci ale pierwsze słysze o tych Topielcach")
    AI_Output(other,"Nie wiem. Może i tak jest, a może to Hades wysyła je by nas poddać próbie")
    AI_Output(other,"Prawde mówiąc nie mamy pojęcia czy Topielce nie żyją gdzieś tam skąd przyszliśmy. Kto wie co leży hen za Partią albo na północy")

def DIA_Boatmaker_Monsters_Condition():
    if PC_HERO.npcknowsinfo(DIA_Boatmaker_Quest):
        return 1
    else:
        return 0

DIA_Boatmaker_Monsters = include.DIALOGUE(
    npc_list.VLK_100_Boatmaker,
    DIA_Boatmaker_Monsters_Info,
    DIA_Boatmaker_Monsters_Condition,
    0,
    "Potwory"
)
def DIA_Boatmaker_Name_Info(other):
    AI_Output(PC_HERO,"Domyślam się że Szkutnik to nie jest twoje prawdziwe imie?")
    AI_Output(other,"Żadna matka nie nazwałaby dziecka Szkutnik, więc myśle że masz racje")
    AI_Output(PC_HERO,"Więc...?")
    AI_Output(other,"Co 'Więc'?")
    AI_Output(PC_HERO,"Więc jakie jest twoje prawdziwe imie?")
    AI_Output(other,"Moje imie...")
    AI_Output(other,"Imie... Ja nie...")
    AI_Output(other,"Nie pamiętam")
    AI_Output(PC_HERO,"Nie pamiętasz swojego imienia?")
    AI_Output(other,"Jestem Szkutnikiem. Buduje łodzie które płyną po Styksie i jego dopływach. Tyle musi nam wystarczeć przyjacielu.")
    AI_Output(other,"Obawiam się że dla mnie jest już za późno na własne imie")

def DIA_Boatmaker_Name_Condition():
        return 1

DIA_Boatmaker_Name = include.DIALOGUE(
    npc_list.VLK_100_Boatmaker,
    DIA_Boatmaker_Name_Info,
    DIA_Boatmaker_Name_Condition,
    0,
    "Imie"
)

### Main Quest
##########
def DIA_Boatmaker_Boat_Info(other):
    AI_Output(PC_HERO,"Czy możesz przeprawić nas do Wyroczni Zagubionych Dusz?")
    AI_Output(other,"Masz na myśli tą świątynie na rozwidleniu rzeki?")
    AI_Output(PC_HERO,"Tak")
    if not PC_HERO.npcknowsinfo(DIA_Boatmaker_Key):
        AI_Output(other,"Nie ma takiej możliwości chłopcze. Będę potrzebował do tego tyczki, wioseł i wielu innych narzędzi")
        AI_Output(other,"A wszystkie są zamknięte na klucz w moim domu")
    elif not journal.SQ_Boatmaker_02.status == "COMPLETED":
        AI_Output(other,"Pomogłeś mi, ale martwi mnie jedna sprawa. Od jakiegoś czasu koło kapliczki kręci się dwóch typów w ciemnych płaszczach.")
        AI_Output(PC_HERO,"Coś z nimi nie tak?")
        AI_Output(other,"Znam takich jak oni. Może i są to zaświaty ale sukinsyny za życia pozostają sukinsynami po śmierci")
        AI_Output(other,"Są tutaj miejsca przejęte przez uzbrojonych obwiesiów i ludzie którzy żyją pod ich batem")
        if not journal.SQ_Boatmaker_02.status == "RUNNING" and not journal.SQ_Boatmaker_02.status == "COMPLETED":
            AI_Output(PC_HERO,"Zajmę się tym")
            journal.SQ_Boatmaker_02.status = "RUNNING"
            journal.SQ_Boatmaker_02.queststage = 10
            print("## Nowy wpis w dzienniku...")
    elif journal.SQ_Boatmaker_02.queststage == 101 or journal.SQ_Boatmaker_02.queststage == 102:
        AI_Output(other,"Uhm... tak panie... dobrze...")
        AI_Output(other,"W-wejdźcie na prom... Zaraz dołącze...")
        delattr(vob_list.VOB_Boat,"illegal")
    else:
        AI_Output(other,"W porządku. W końcu bardzo mi pomogłeś")
        AI_Output(other,"Ty i twój przyjaciel pakujcie się na prom, ja zaraz przyniose tyczke!")
        delattr(vob_list.VOB_Boat,"illegal")

def DIA_Boatmaker_Boat_Condition():
        return 1

DIA_Boatmaker_Boat = include.DIALOGUE(
    npc_list.VLK_100_Boatmaker,
    DIA_Boatmaker_Boat_Info,
    DIA_Boatmaker_Boat_Condition,
    1,
    "Transport"
)


def DIA_Boatmaker_Bandits_Info(other):
    AI_Output(PC_HERO,"Rozwiązałem twój problem z bandytami")
    AI_Output(other,"Świetnie! Czyli poszli sobie?")
    if journal.SQ_Boatmaker_02.queststage == 25:
        AI_Output(PC_HERO,"Jeden poszedł. Drugi został.")
        AI_Output(other,"Ale skoro został...")
        AI_Output(PC_HERO,"Został na zawsze.")
        AI_Output(other,"Jak to na zaw... O Hero o cholera...")
        AI_Output(PC_HERO,"Coś nie tak?")
        AI_Output(other,"Nie chciałem byś nikogo zabijał!")
        AI_Output(PC_HERO,"Myślałem że taką mieliśmy umowe. Przy okazji umowy - czy przetransportujesz nas teraz swoim promem?")
        AI_Output(other,"T-tak...")
        journal.SQ_Boatmaker_02.status = "COMPLETED"
        journal.SQ_Boatmaker_02.queststage = 101
        leveling.give_exp(PC_HERO,75)
    elif journal.SQ_Boatmaker_02.queststage == 30:
        AI_Output(PC_HERO,"Powiedzmy że zmusiłem ich do zejścia do podziemia.")
        AI_Output(other,"W jakim sensie... O Hero o cholera...")
        AI_Output(PC_HERO,"Coś nie tak?")
        AI_Output(other,"Nie chciałem byś nikogo zabijał!")
        AI_Output(PC_HERO,"Myślałem że taką mieliśmy umowe. Przy okazji umowy - czy przetransportujesz nas teraz swoim promem?")
        AI_Output(other,"T-tak...")
        journal.SQ_Boatmaker_02.status = "COMPLETED"
        journal.SQ_Boatmaker_02.queststage = 102
        leveling.give_exp(PC_HERO,75)
    else:
        AI_Output(PC_HERO,"Tak. Przekonałem ich że nie warto tutaj czekać")
        AI_Output(other,"Świetnie! Ty i twój kompan przygotujcie się do drogi, jutro z rana ruszamy!")
        journal.SQ_Boatmaker_02.status = "COMPLETED"
        journal.SQ_Boatmaker_02.queststage = 100
        leveling.give_exp(PC_HERO,100)

def DIA_Boatmaker_Bandits_Condition():
    if journal.SQ_Boatmaker_02.queststage == 20:
        return 1
    elif journal.SQ_Boatmaker_02.queststage == 25:
        return 1
    elif journal.SQ_Boatmaker_02.queststage == 30:
        return 1

DIA_Boatmaker_Bandits = include.DIALOGUE(
    npc_list.VLK_100_Boatmaker,
    DIA_Boatmaker_Bandits_Info,
    DIA_Boatmaker_Bandits_Condition,
    0,
    "Bandyci"
)