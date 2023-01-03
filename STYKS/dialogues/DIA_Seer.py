import include
import npc_list
import journal
import item_list
import leveling
import fight
import fight_mage
import map
from hero import PC_HERO
from dialogue import AI_Output

def DIA_Seer_First_Hello(other):
    print("Weszliście we dwójke razem z Antiochusem do wyglądającej na wpół zrujnowanej katedry. Powitał was na oko czterdziestoletni mężczyzna ubrany w bogato zdobioną czerwoną szate.")
    print("Najdziwniejsze były jednak jego oczy. Były zupełnie białe, jak mleko. Pełny zanik tęczówek i źrenic. Jednak widać było że poruszają się i reagują na otoczenie.")
    print("Być może to tylko wrażenie ale jego spojrzenie zdawało się widzieć więcej niż zwykłe oczy. Jakby widziało dusze, myśli i emocje\n")
    AI_Output(other,"Witaj panie [zignorował zupełnie ciebie i zwrócił się od razu do Księcia Antiochusa]")
    AI_Output(other,"Kto dziś przyszedł mnie odwiedzić?")
    AI_Output(npc_list.PC_ANTIOCHUS,"Ja. Książe Antiochus Młodszy. A ze mną mój towarzysz " + PC_HERO.name)
    AI_Output(other,"[Na moment oczy mężczyzny zrobiły się prawie normalne. Prawie - okazało się że ma on krwistoczerwone tęczówki. Po chwili jednak wróciły do pełnej bieli] Ah, teraz widze")
    AI_Output(other,"Z czym do mnie przychodzicie?")
    AI_Output(PC_HERO,"Czy to ty jesteś wyrocznią?")
    AI_Output(other,"Wyrocznią? Nie. Na imie mi Anthimos. Jestem jej opiekunem. Możnaby rzec - obrońcą. W zaświatach jest wiele dusz o różnych zamiarach.")
    AI_Output(other,"Ja mam tylko odsiać ziarno od plew i pozwalać na spotkanie tylko tym którzy mają prawdziwie ważną sprawę do Wyroczni")
    AI_Output(npc_list.PC_ANTIOCHUS,"Wyjaśnij mu o co chodzi. Ja rozejrze się po dziedzińcu.")
    print("Książe z typową dla siebie nonszalancją wyszedł z katedry bez pożegnania")
    other.dialogue_hello = DIA_Seer_Post_Hello

def DIA_Seer_Post_Hello(other):
    AI_Output(other,"Z czym do mnie przychodzisz?")

npc_list.KDF_200_Seer.dialogue_hello = DIA_Seer_First_Hello


def DIA_Seer_Quest_Info(other):
    AI_Output(PC_HERO,"Poszukujemy Bramy. Wyjścia z zaświatów do świata żywych. To chyba dość ważna sprawa?")
    AI_Output(other,"[Mężczyzna pogładził spiczastą czarno-siwą brodę i uśmiechnął się ironicznie] A więc jedna dusza z milionów chcę stać się na powrót żywa")
    AI_Output(other,"Zaprawde, wielkiej trzeba arogancji by uważać to za ważną sprawe. A co z resztą dusz? Z wszystkimi tutaj zebranymi? W czym twoje życie jest ważniejsze od innych?")
    AI_Output(PC_HERO,"Ale...")
    AI_Output(other,"A jeśli mielibyśmy wskazać drogę do Bramy tobie to dlaczego nie mielibyśmy jej wskazać każdemu? Tak byłoby sprawiedliwie, czyż nie?")
    AI_Output(other,"Ale wtedy, po co miałoby w ogóle istnieć to miejsce? Dlaczego ludzie nie mieliby być nieśmiertelni jeśli z Hadesu możnaby tak po prostu wyjść?")
    AI_Output(PC_HERO,"W takim razie poddaj mnie próbie.")
    AI_Output(other,"Nie.")
    journal.MQ_Oracle.status = "RUNNING"
    journal.setstage(journal.MQ_Oracle,10)

def DIA_Seer_Quest_Condition():
    return 1

DIA_Seer_Quest = include.DIALOGUE(
    npc_list.KDF_200_Seer,
    DIA_Seer_Quest_Info,
    DIA_Seer_Quest_Condition,
    0,
    "Brama"
)


def DIA_Seer_Threat_Info(other):
    AI_Output(PC_HERO,"W takim razie zejdź mi z drogi")
    AI_Output(other,"A więc przeszliśmy z próśb do gróźb? Szybko. Z reguły zajmuje to więcej czasu.")
    AI_Output(other,"[Jego oczy z bieli zmieniły kolor na w całości czerwone a ręka zapłonęła delikatnym płomieniem w kolorze purpury]")
    AI_Output(other,"Więc przyszedłeś tu z myślą że Wyrocznia Dusz jest bezzębną bestią?")
    AI_Output(other,"[Oczy wróciły do bieli a płomień zgasł] Zastanów się dobrze nad następnym czynem.")
    AI_Output(PC_HERO,"...")

def DIA_Seer_Threat_Condition():
    if PC_HERO.npcknowsinfo(DIA_Seer_Quest):
        return 1

DIA_Seer_Threat = include.DIALOGUE(
    npc_list.KDF_200_Seer,
    DIA_Seer_Threat_Info,
    DIA_Seer_Threat_Condition,
    0,
    "Zejdź mi z drogi"
)

def DIA_Seer_Fight_Info(other):
    AI_Output(PC_HERO,"[Wyciągasz miecz i tniesz. Szybko. By zabić zanim Anthimos zdąży rzucić zaklęcie]")
    AI_Output(other,"[Nie zdążyłeś. Jego oczy znów zmieniły kolor, tym razem na indygo a on sam rozproszył się jak mgła i złączył pare metrów w tył]")
    AI_Output(other,"[Westchnął niemal zrezygnowany, ale jego głos stopniowo zaczał zmieniać się na bardziej metaliczny] I znów jesteśmy w tym punkcie.")
    AI_Output(PC_HERO,"Stawaj do walki jak mężczyzna, zamiast chować się za zaklęciami!")
    AI_Output(other,"[Anthimos nie odpowiedział, wyciągnął w twoją strone wyprostowaną dłoń. Z jego palców wyskoczyły purpurowe płomienie]")
    if hasattr(PC_HERO,"weapon") and PC_HERO.weapon == item_list.itwp_sword_silver:
        AI_Output(PC_HERO,"[Odruchowo zasłoniłeś się ostrzem. W momencie gdy płomienie dotknęły srebrnej klingi, rozproszyły się w purpurową mgłe]")
        AI_Output(PC_HERO,"[Z miejsca zrozumiałeś co się stało. Srebro rozprasza jego zaklęcia]")
        AI_Output(other,"Widzę że przyszedłeś przygotowany. To nie ma znaczenia. Nie pójdziesz dalej.")
        AI_Output(PC_HERO,"Zobaczymy.")
    else:
        AI_Output(PC_HERO,"[W ostatniej chwili wykonałeś unik. Jednak Anthimos zdążył prznieść się już w inne miejsce. To będzie trudna walka]")

    input()
    fight_result = fight_mage.fight_mage(PC_HERO,other)
    if fight_result == "SUCCESS":
        print("Twój ostatni cios odseparował głowe maga od jego ciała. Upadł bezładnie z głuchym uderzeniem")
        print("Zabiłeś czarnoksiężnika. Prawdziwego. Wciąż nie jesteś w stanie w to uwierzyć")
        map.LOC_PRIORY_BASEMENT.locked = "unlocked"
        map.LOC_ORACLE.locked = "unlocked"
        map.LOC_PRIORY_OUTSIDE.locked = "locked"
        map.LOC_PRIORY_OUTSIDE.locked_reason = "Lepiej teraz tam nie wychodzić..."
        journal.setstage(journal.MQ_Oracle,50)
        fight.kill(other,0)
    else:
        print("Ostatkiem sił ruszyłeś z szarżą na Anthimosa. Mag jakby leniwie przeniósł się pół metra obok i przyłożył dłoń do twojej skroni")
        print("Nie poczułeś ostatniego zaklęcia")
        input()
        fight.kill(PC_HERO, 1)


def DIA_Seer_Fight_Condition():
    if PC_HERO.npcknowsinfo(DIA_Seer_Threat):
        return 1

DIA_Seer_Fight = include.DIALOGUE(
    npc_list.KDF_200_Seer,
    DIA_Seer_Fight_Info,
    DIA_Seer_Fight_Condition,
    0,
    "Zaatakuj"
)
