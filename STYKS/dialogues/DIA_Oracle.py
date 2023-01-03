import include
import npc_list
import journal
import fight
import map
import vob_list
import leveling
from hero import PC_HERO
from dialogue import AI_Output

def DIA_Oracle_First_Hello(other):
    print("Wyrocznia, nie wygląda tak jak to sobie wyobrażałeś.")
    print("Wiele greckich Polis ma swoje wyrocznie. W większości są to kobiety, w różnym wieku, u których odkryto za młodu dar rozmawiania z bogami")
    print("Istota którą widzisz możliwe że jest kobietą. Lecz nie jesteś nawet pewien czy jest człowiekiem. \nIstota ma co prawda humanoidalny kształt, jednak różni się od człowieka ważnym elementem")
    print("Nie ma twarzy")
    print("Stworzenie nie ma ust, w ich miejscu jest jednolita warstwa skóry. Skóra również pokrywa jej oczodoły i nos. Jak gdyby była makabryczną drewnianą lalką.")
    input()
    print("W przerażeniu nie usłyszałeś nawet kiedy do Świątyni wszedł Książe Antiochus\n")
    if journal.MQ_Oracle.queststage == 50:
        AI_Output(npc_list.PC_ANTIOCHUS,"Pobiegłem do ciebie jak tylko zobaczyłem światła z wnętrza. Rozumiem że pokojowa opcja jest przerekla...")
    elif journal.MQ_Oracle.queststage == 51:
        AI_Output(npc_list.PC_ANTIOCHUS,"Anthimos zawołał mnie gdy pozwolił ci wejść...")
    AI_Output(npc_list.PC_ANTIOCHUS,"Na diabły i demony a co to za monstrum?!")
    AI_Output(PC_HERO,"Rozumiem że legendy nie mówiły jak wygląda nasza wyrocznia?")
    AI_Output(npc_list.PC_ANTIOCHUS,"Ona nie ma ust.")
    AI_Output(npc_list.KDF_202_Oracle_Voice,"[Nagle w komnacie rozległ się spokojny kobiecy głos] Ale słyszy...")
    AI_Output(other,"[W reakcji na głos istota zaczęła się szarpać, jakby czuła ogromny ból i była przerażona]")
    AI_Output(PC_HERO,"Czy to ty jesteś wyrocznią?")
    AI_Output(npc_list.KDF_202_Oracle_Voice,"Jestem tym czym jestem. Zadawajcie swoje pytania przybysze...")
    AI_Output(other,"[Ruchy rzuchwy wyglądały jakby istota chciała wrzasnąć z bólu. Nie miała ust]")
    other.dialogue_hello = DIA_Oracle_Post_Hello

def DIA_Oracle_Post_Hello(other):
    AI_Output(other,"[Istota wyraźnie wyczerpana zwisa na łańcuchach ze ściany]")
    AI_Output(PC_HERO,"Wyrocznio...")
    AI_Output(other,"[Gdy tylko usłyszała twój głos zaczęła się szarpać w strachu]")

npc_list.KDF_201_Oracle.dialogue_hello = DIA_Oracle_First_Hello


def DIA_Oracle_Prophecy_Info(other):
    AI_Output(npc_list.PC_ANTIOCHUS,"Wyrocznio, zaklinam cie, wyjaw nam gdzie znajduje się wyjście z Hadesu!")
    AI_Output(other,"[Kobieta zaczęła ruszać bezoką twarzą po pokoju, jakby w panice chciała znaleźć mówiącego]")
    AI_Output(npc_list.KDF_202_Oracle_Voice,"Dlaczego miałabym wam pomóc...?")
    AI_Output(PC_HERO,"To jest twoja rola. Legendy mówią...")
    AI_Output(npc_list.PC_ANTIOCHUS,"Mówią że nie masz wyboru. Twój strażnik przepuścił nas. Musisz dać nam przepowiednie.")
    AI_Output(other,"[Istota jakby w ogromnym bólu i nienawiści próbowała sięgnąć rękami w strone Antiochusa. Wygląda na to że każde pytanie, każda interakcja sprawia jej ból]")
    AI_Output(npc_list.KDF_202_Oracle_Voice,"Ahhh... [zamiast niej odpowiedział głos] muszę. W istocie.")
    input()
    AI_Output(npc_list.KDF_202_Oracle_Voice,"Posłuchajcie mnie więc")
    AI_Output(other,"[Przykuta istota zaczęła szarpać się z jeszcze większą agresją, wbijając swoje palce w puste zaciągnięte skórą oczodoły i bijąc głową o ściane]")
    AI_Output(npc_list.KDF_202_Oracle_Voice,"Trzy góry w strone wschodzącego słońca, trzech wędrowców i trzech opiekunów, krew królów, krew bękartów, krew bestii")
    AI_Output(npc_list.KDF_202_Oracle_Voice,"Brama jest zamknięta na klucz, tam gdzie śmierć jest gorsza niż śmierć a śmierć traci swe znaczenie")
    AI_Output(npc_list.KDF_202_Oracle_Voice,"Odpowiedź jest sześć stóp pod ziemią, światło latarni wskaże ci kres twej wędrówki")
    AI_Output(other,"[Istota przestała się szarpać. Zawisła bez siły na łańcuchach i tylko delikatnie drży jakby rażona piorunem]")
    AI_Output(npc_list.KDF_202_Oracle_Voice,"A teraz odejdźcie. Jestem już zmęczona.")
    if journal.MQ_Oracle.queststage == 50:
        fight.kill(npc_list.NOV_400_Gateguard,0)
        fight.kill(npc_list.NOV_401_Acolyte,0)
        fight.kill(npc_list.NOV_402_Acolyte,0)
    journal.MQ_Oracle.status = "COMPLETED"
    journal.setstage(journal.MQ_Oracle,100)
    leveling.give_exp(PC_HERO,100)
    map.LOC_PRIORY_OUTSIDE.locked = "unlocked"
    map.LOC_PRIORY_OUTSIDE.vob.append(vob_list.VOB_Horses)

def DIA_Oracle_Prophecy_Condition():
    return 1

DIA_Oracle_Prophecy = include.DIALOGUE(
    npc_list.KDF_201_Oracle,
    DIA_Oracle_Prophecy_Info,
    DIA_Oracle_Prophecy_Condition,
    0,
    "Brama"
)

def DIA_Oracle_FreeHer_Info(other):
        AI_Output(PC_HERO,"Musimy ją... musimy to uwolnić")
        AI_Output(npc_list.PC_ANTIOCHUS,"Nie. Musimy udać się w strone trzech gór. Wiem gdzie to jest")
        AI_Output(PC_HERO,"To stworzenie cierpi!")
        AI_Output(npc_list.PC_ANTIOCHUS,"Wydawała mi się całkiem spokojna gdy mówiła. Chodź.")
        AI_Output(PC_HERO,"To nie ona mówiła. Przecież widziałeś... to jakiś głos...")
        AI_Output(npc_list.PC_ANTIOCHUS,PC_HERO.name + ". Nie próbuj zrozumieć tego miejsca.")
        AI_Output(npc_list.PC_ANTIOCHUS,"Nawet jeśli ona cierpi... jej obecność tutaj jest wymagana by przepowiednia się spełniła.")

def DIA_Oracle_FreeHer_Condition():
    if npc_list.KDF_200_Seer.hp == 0 and PC_HERO.npcknowsinfo(DIA_Oracle_Prophecy):
        return 1

DIA_Oracle_FreeHer = include.DIALOGUE(
    npc_list.KDF_201_Oracle,
    DIA_Oracle_FreeHer_Info,
    DIA_Oracle_FreeHer_Condition,
    0,
    "Uwolnienie"
)

def DIA_Oracle_BreakerOfChains_Info(other):
    AI_Output(PC_HERO,"Nie. [Wyciągasz broń i uderzasz w kajdany] jesteś. wolna.")
    AI_Output(npc_list.PC_ANTIOCHUS,"[Książe uchylił lekko usta. Jego mina bardziej niż zdziwienie wskazuje jakby... pozytywne zaskoczenie?]")
    AI_Output(npc_list.PC_ANTIOCHUS,"[Nie masz jednak czasu się nad tym zastanawiać]")
    AI_Output(other,"[Gdy tylko została uwolniona, pchnęła cie z siłą wściekłego konia na ścianie. Ogromny ból pleców zwala cie z nóg]")
    AI_Output(npc_list.PC_ANTIOCHUS,"[Dobył miecza]")
    input()
    AI_Output(other,"[Istota jednak nie chciała z nim walczyć. Wyszarpała mu zza pasa sztylet i wbiła go sobie w gardło, po czym z głośnym bulgotem przecięła sobie krtań]")
    AI_Output(npc_list.PC_ANTIOCHUS,"[Wziął pare głębokich wdechów i otworzył usta jakby chciał coś powiedzieć. Jednak odczekał chwile i spojrzał na ciebie] Widzimy się za tylną furtą.")
    AI_Output(PC_HERO,"[Wstajesz. Wciąż ciężko ci się otrząsnąć po tym co sie stało]")
    AI_Output(PC_HERO,"[Spoglądasz w góre i próbujesz odezwać się do tego głosu z którym rozmawiałeś]")
    AI_Output(PC_HERO,"Wyrocznio...?")
    AI_Output(other,"[Cisza]")
    other.hp = 0
    PC_HERO.karma += 2
    PC_HERO.flags.append("mercy_oracle")
    fight.kill(other,0)

def DIA_Oracle_BreakerOfChains_Condition():
    if PC_HERO.npcknowsinfo(DIA_Oracle_FreeHer):
        return 1

DIA_Oracle_BreakerOfChains = include.DIALOGUE(
    npc_list.KDF_201_Oracle,
    DIA_Oracle_BreakerOfChains_Info,
    DIA_Oracle_BreakerOfChains_Condition,
    0,
    "Uwolnij"
)

