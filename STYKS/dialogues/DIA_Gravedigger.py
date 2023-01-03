import include
import npc_list
import journal
import item_list
import leveling
import inventory
import haggle
import enemy_list
import armwrestling
from hero import PC_HERO
from dialogue import AI_Output
import fight


def DIA_Gravedigger_First_Hello(other):
    print("Obok grobów, na murku siedzi krzepki starzec w brudnej szacie. Obok niego oparta jest łopata a on sam w dłoniach trzyma dziwny drewniany przyrząd wypełniony płonącymi liśćmi\n Od razu przyszły ci na myśl rośliny sprowadzane przez Seleucydów z Indii. Starzec zdaje się nie przejmować twoją obecnością. Świeża ziemia na grobach sugeruje że właśnie skończył prace.")
    AI_Output(PC_HERO,"Witaj grabarzu")
    AI_Output(other,"Witaj " + PC_HERO.name)
    AI_Output(PC_HERO,"Nie podałem ci swojego imienia")
    if PC_HERO.npcknowsinfo(DIA_Phrixos_First_Hello):
        AI_Output(other,"Ale słyszałem jak rozmawiałeś z Phrixosem chłopcze.")
    else:
        AI_Output(other,"[Starzec wzruszył ramionami] Ale masz na farmie przyjaciół.")
        AI_Output(PC_HERO,"Przyjaciół?")
        AI_Output(other,"Porozmawiaj z Phrixosem. Myśle że się ucieszy na twój widok")
        AI_Output(PC_HERO,"Phrixos jest tutaj?!")
        AI_Output(other,"[Starzec zignorował twoje pytanie]")
    other.dialogue_hello = DIA_Gravedigger_Post_Hello

def DIA_Gravedigger_Post_Hello(other):
    AI_Output(other,"[Starzec zdaje się nie dostrzegać twojej obecności]")

npc_list.BDT_301_Gravedigger.dialogue_hello = DIA_Gravedigger_First_Hello


def DIA_Gravedigger_WhoAreYou_Info(other):
    AI_Output(PC_HERO,"Czym się tutaj zajmujesz?")
    AI_Output(other,"Jestem Grabarzem synu. Pomagam Bękartowi z obowiązkiem chowania zmarłych")
    AI_Output(PC_HERO,"Widze świeże groby. Co ich dopadło?")
    AI_Output(other,"Bękart jest człowiekiem niecierpliwym i porywczym.")
    AI_Output(PC_HERO,"Rozumiem")

def DIA_Gravedigger_WhoAreYou_Condition():
    return 1

DIA_Gravedigger_WhoAreYou = include.DIALOGUE(
    npc_list.BDT_301_Gravedigger,
    DIA_Gravedigger_WhoAreYou_Info,
    DIA_Gravedigger_WhoAreYou_Condition,
    0,
    "Kim jesteś?"
)


def DIA_Gravedigger_Bastard_Info(other):
    AI_Output(PC_HERO,"Nie czujesz się źle służąc takiemu panu?")
    AI_Output(other,"Czy powietrze czuje się źle bo oddychają nim złoczyńcy?")
    AI_Output(PC_HERO,"Powietrze nie ma wyboru. Człowiek ma")
    AI_Output(other,"A jeśli wybiore odejście, co będzie ze zmarłymi? Kto zapewni im pochówek?")
    AI_Output(other,"Jeśli odejde, w najlepszym razie Bękart zagoni kogoś innego do mojej pracy")
    AI_Output(other,"Czy w takim wypadku nie powinienem czuć się źle, uciekając od służby takiemu panu?")
    AI_Output(PC_HERO,"Dziwna logika.")
    AI_Output(other,"[Grabarz nie odpowiedział]")

def DIA_Gravedigger_Bastard_Condition():
    if PC_HERO.npcknowsinfo(DIA_Gravedigger_WhoAreYou):
        return 1

DIA_Gravedigger_Bastard = include.DIALOGUE(
    npc_list.BDT_301_Gravedigger,
    DIA_Gravedigger_Bastard_Info,
    DIA_Gravedigger_Bastard_Condition,
    0,
    "Bękart"
)

### Quest Grabarza
##################
def DIA_Gravedigger_Friends_Info(other):
    AI_Output(PC_HERO,"Phrixos mówił mi że pogrzebałeś Apolodorusa i Nisosa")
    AI_Output(other,"Zajmuję się pochówkiem wszystkich w Wiosce")
    AI_Output(PC_HERO,"Apolodorus miał czarne włosy i...")
    AI_Output(other,"Wiem którzy to byli. Nisos pracował przy obsłudze młyna. Silny człowiek. Często wyręczał innych niewolników Bękarta, gdy ci byli zbyt wycieńczeni")
    AI_Output(other,"Apolodorus zaczął od pomocy ludziom Bękarta przy polowaniach. Był pracowity ale i ambitny. Z czasem przyjęli go do swojej drużyny.")
    AI_Output(PC_HERO,"Apolodorus służył Bękartowi?")
    AI_Output(other,"Wszyscy w wiosce służymy mu na swój sposób. Wiem, nie musisz wyjaśniać. Pytasz czemu służył mu jako żołnierz, nie jako niewolnik")
    AI_Output(other,"Każdy człowiek jest inny i ma inne motywacje. To prawda, część z tych którzy przysięgają Bękartowi robi to dlatego że wierzą w to że silniejszy ma prawo rządzić słabszymi")
    AI_Output(other,"Bękart jest podobnego zdania i bardzo sobie ceni takich ludzi.")
    AI_Output(other,"Innych zachęciły dodatkowe racje, a jeszcze inni służyli jako żołnierze za życia i nie odnajdują się w innej pracy.")
    AI_Output(PC_HERO,"Mówisz więc że jedni są dobrzy a drudzy źli?")
    AI_Output(other,"Nie powiedziałem nic z tych rzeczy. Mówie tylko, że wszyscy są ludźmi.")
    AI_Output(PC_HERO,"Nie łap mnie za słówka. Chcę wiedzieć którzy z nich są ludźmi honoru a którzy to szelmy")
    AI_Output(other,"Nie słyszałem by którykolwiek człowiek był tylko jednym lub drugim. Cokolwiek chcesz o nich wiedzieć, dowiedz się tego sam. Porozmawiaj z nimi")
    journal.MQ_Bastard.status = "RUNNING"
    journal.MQ_Bastard.queststage = 20

def DIA_Gravedigger_Friends_Condition():
    if journal.MQ_Bastard.status == "RUNNING":
        return 1

DIA_Gravedigger_Friends = include.DIALOGUE(
    npc_list.BDT_301_Gravedigger,
    DIA_Gravedigger_Friends_Info,
    DIA_Gravedigger_Friends_Condition,
    0,
    "Przyjaciele"
)

### Klucz
#########
def DIA_Gravedigger_StealKey_Info(other):
    AI_Output(PC_HERO,"Opowiedz mi o tym jak umarli ostatni")
    AI_Output(other,"Nie ma o czym mówić. Słyszeli historie o tym jak Bękart stał się nieśmiertelny")
    AI_Output(other,"Liczyli na to że kradnąc mu pewien amulet który nosi przy sobie zerwą czar i będą mogli się go pozbyć")
    AI_Output(other,"Spiskowcy zerwali mu z paska talizman a następnie zadźgali go. Chłopcy Bękarta szybko pojmali dwóch z nich, a trzeci zdaje się uciekł z amuletem w strone lasu")
    AI_Output(PC_HERO,"[Wysuwasz Grabarzowi klucz z kieszeni]")
    AI_Output(other,"Bękart obudził się godzine później. Osobiście zabił pojmaną dwójke a za trzecim wysłał pościg do lasu")
    AI_Output(PC_HERO,"Czyli talizman nie był źródłem jego połączenia z Alexis")
    AI_Output(other,"Nie synu. To była tylko pamiątka wysłana mu przez starą miłość")
    AI_Output(other,"To nigdy nie jest bezpieczne, odbierać szaleńcowi jedyną rzecz która daje mu ukojenie.")
    AI_Output(PC_HERO,"Zapamiętam to. Dziękuję za historie")
    AI_Output(other,"Pozdrów Alexis gdy będziesz miał okazję.")
    inventory.add_to_inventory(PC_HERO,item_list.itke_lighthouse_key)
    leveling.give_exp(PC_HERO,50)

def DIA_Gravedigger_StealKey_Condition():
    if PC_HERO.npcknowsinfo(DIA_Bastard_Wish_Key) and PC_HERO.dex > 20:
        return 1

DIA_Gravedigger_StealKey = include.DIALOGUE(
    npc_list.BDT_301_Gravedigger,
    DIA_Gravedigger_StealKey_Info,
    DIA_Gravedigger_StealKey_Condition,
    0,
    "Ukradnij Klucz"
)



def DIA_Gravedigger_GiveKey_Info(other):
    AI_Output(PC_HERO,"Bękart powiedział mi że to ty masz klucz do Wieży Latarnika")
    AI_Output(other,"Musiałeś naprawdę przycisnąć tego starego łotra by zdradził ci tą tajemnice")
    AI_Output(PC_HERO,"Jak widać nawet najgorsze szelmy czują czasem potrzebę by dotrzymać danego słowa.")
    AI_Output(PC_HERO,"Czy możesz mi dać ten klucz? Potrzebuję porozmawiać z jego wiedźmą.")
    AI_Output(other,"Mogę. Ale czy to zrobie?")
    AI_Output(other,"Co z tym zrobisz jeśli ci go dam?")
    if PC_HERO.cha >= 20:
        AI_Output(PC_HERO,"Przypomnij sobie twarze ludzi których musiałeś tu zakopać. Ilu z nich zasługiwało na ten los?")
        AI_Output(PC_HERO,"Spójrz na ludzi w wiosce. Ilu z nich znajdzie się tu za rok? Za dwa?")
        AI_Output(PC_HERO,"Myślę że dobrze wiesz co musimy zrobić. To coś co powinieneś zrobić już dawno temu.")
        AI_Output(other,"[Starzec długo nie odpowiada, gdy chcesz już przerwać cisze, w dokładnie tym samym momencie odzywa się]")
        AI_Output(other,"Pięć lat... to już się ciągnie tak długo... tak. Myśle że masz racje. To chyba już koniec podróży Bękarta.")
        AI_Output(PC_HERO,"Daj mi klucz.")
        AI_Output(other,"Weź go. Ale pamiętaj... Cokolwiek robił Bękart tu na dole, Latarnik nie brał w tym udziału.")
        AI_Output(other,"To dobry człowiek. Nie każdy rodzi się bohaterem.")
        inventory.add_to_inventory(PC_HERO,item_list.itke_lighthouse_key)
        leveling.give_exp(PC_HERO,50)
    else:
        AI_Output(PC_HERO,"Czy to nie oczywiste? Wyeliminuje Latarnika, zabije Bękarta a wiedźme przekonam by wskrzesiła Apolodorusa i Nisosa")
        AI_Output(other,"A co z Chłopcami Bękarta, tu na dole? Mogą stawiać opór.")
        AI_Output(PC_HERO,"Oni wydali na siebie wyrok już dawno temu. Jeśli staną mi na drodze, zabiję ich")
        AI_Output(other,"Twój plan to krew")
        AI_Output(PC_HERO,"Krew winnych")
        AI_Output(other,"Nie. Słyszałem już podobne słowa od kogoś kogo znałem. Nie zwiastowały sprawiedliwości, tylko zemste.")
        AI_Output(PC_HERO,"Nie jestem tym do kogo mnie porównujesz. Daj mi klucz.")
        AI_Output(other,"Doprawdy? Moja odpowiedź wciąż brzmi - nie.") # Tak, Grabarz słyszał te słowa od Protaga w jednej z poprzednich Pętli
        AI_Output(PC_HERO,"Jesteś głupcem")
        AI_Output(other,"[Starzec nie odpowiedział]")

def DIA_Gravedigger_GiveKey_Condition():
    if PC_HERO.npcknowsinfo(DIA_Bastard_Wish_Key):
        return 1

DIA_Gravedigger_GiveKey = include.DIALOGUE(
    npc_list.BDT_301_Gravedigger,
    DIA_Gravedigger_GiveKey_Info,
    DIA_Gravedigger_GiveKey_Condition,
    0,
    "Klucz"
)



### THE TRUTH chain
####################################
def DIA_Gravedigger_AntiochusDead_Info(other):
    AI_Output(PC_HERO,"Kim jesteś?")
    if PC_HERO.npcknowsinfo(DIA_Gravedigger_WhoAreYou):
        AI_Output(other,"Mówiłem ci już synu.")
    AI_Output(other,"Jestem grabarzem, chowam tych których Bękart i jego ludzie kładą trupem")
    AI_Output(PC_HERO,"Wiesz że nie o to pytam.")
    AI_Output(other,"[Uśmiecha się enigmatycznie]")
    AI_Output(PC_HERO,"Bękart powiedział mi że byłeś przy nim od momentu jak obudził się w Hadesie i podążasz razem z nim od tego czasu. Ten schemat brzmi znajomo.")
    AI_Output(PC_HERO,"Ten kto towarzyszył mi, nie żyje. Więc pytam - czym jesteście?")
    input()
    AI_Output(other,"Widze że nie dasz się przekonać byś zapomniał o tej rozmowie i podążał dalej za swoim celem")
    AI_Output(PC_HERO,"Mój cel to kłamstwo, tak jak ten kto mi go nadał")
    AI_Output(PC_HERO,"Wiem że trzymacie mnie tu już od wielu dziesiątek lat. Wiem że na zewnątrz minęło już 120 lat.")
    AI_Output(other,"Tak naprawde minęło 173 lata synu")
    PC_HERO.flags.append("forbid_exit")
    PC_HERO.flags.append("truth_prompt")
    other.dialogues = [DIA_Gravedigger_Truth_Alexis, DIA_Gravedigger_Truth_Form, DIA_Gravedigger_Truth_Antiochus, DIA_Gravedigger_Truth_End]


def DIA_Gravedigger_AntiochusDead_Condition():
    if PC_HERO.npcknowsinfo(DIA_Bastard_AntiochusDead):
        return 1

DIA_Bastard_AntiochusDie = include.DIALOGUE(
    npc_list.BDT_301_Gravedigger,
    DIA_Gravedigger_AntiochusDead_Info,
    DIA_Gravedigger_AntiochusDead_Condition,
    0,
    "Czym jesteś?"
)


def DIA_Gravedigger_Truth_Alexis_Info(other):
    AI_Output(PC_HERO,"Kłamiesz, Bękart i Alexis byli razem za życia, jeśli od jego śmierci minęło...")
    AI_Output(other,"Dziewczyna dalej żyje. Ma 73 lata, jest starszą kapłanką w zakonie Persefony. Nie mogła uwierzyć gdy zaczęliśmy jej przesyłać wiadomości od Bękarta")
    AI_Output(PC_HERO,"Dlaczego...")
    AI_Output(other,"Liczyliśmy że jej wpływ może zmiękczyć jego serce. Uczynić je lepszym. Pozwoliliśmy mu na naprawe krzywd które wyrządzał, na przywracanie swoich ofiar do życia. To dar.")
    AI_Output(other,"Lecz on wykorzystał go dla swojej nieśmiertelności i dla torturowania ofiar. Niektórzy ludzie rzeczywiście są niereformowalni.")
    AI_Output(other,"A on jak widać nie zamierza kończyć swojej pętli. Siedzi tu już od pięciu lat i trzyma się tak daleko od Bramy jak tylko może.")

def DIA_Gravedigger_Truth_Alexis_Condition():
    if "truth_prompt" in PC_HERO.flags:
        return 1

DIA_Gravedigger_Truth_Alexis = include.DIALOGUE(
    npc_list.BDT_301_Gravedigger,
    DIA_Gravedigger_Truth_Alexis_Info,
    DIA_Gravedigger_Truth_Alexis_Condition,
    0,
    "Alexis"
)

def DIA_Gravedigger_Truth_Form_Info(other):
    AI_Output(PC_HERO,"Dlaczego przybrałeś tą forme?")
    AI_Output(other,"Przybieramy formę ludzi których podziwialiście za życia. W przypadku Bękarta to był trudny wybór. Ten człowiek nie miał za grosz szacunku ani za grosz honoru")
    AI_Output(other,"Ty służyłeś swojemu księciu, książe podziwiał watażke z przeszłości któremu zawdzięczali swoje królestwo")
    AI_Output(other,"Bękart służył tylko pieniądzu. Ale pewnego dnia spotkał starca który podążał za wojskiem. Był grabarzem.")
    AI_Output(other,"Ale nie robił tego dla szabrowania zwłok. Wręcz przeciwie. Bał się że martwi żołnierze nie będą godnie pochowani.")
    AI_Output(other,"Obraz tego człowieka zapadł na długo w myślach Bękarta. Dlatego gdy przyszedł na niego czas, przybrałem jego wygląd i zwyczaje")

def DIA_Gravedigger_Truth_Form_Condition():
    if "truth_prompt" in PC_HERO.flags:
        return 1

DIA_Gravedigger_Truth_Form = include.DIALOGUE(
    npc_list.BDT_301_Gravedigger,
    DIA_Gravedigger_Truth_Form_Info,
    DIA_Gravedigger_Truth_Form_Condition,
    0,
    "Grabarz"
)

def DIA_Gravedigger_Truth_Antiochus_Info(other):
    AI_Output(PC_HERO,"Mam uwierzyć twoje dobre intencje? Wiem że to ty kazałeś Bękartowi zabić Księcia Antiochusa")
    AI_Output(other,"Ach tak. Książe Antiochus. Niektórzy wciąż wierzą w jego szlachetność i dobre serce")
    AI_Output(PC_HERO,"Będziesz próbować obrócić mnie przeciwko niemu tak jak Bękarta? Nie jest ci dość że go zabiłeś, chcesz by jego ludzie go nienawidzili?")
    AI_Output(other,"Twój książe był łotrem który deptał innych pod swoimi stopami, patrzył na nich z góry i traktował jak środek do celu")
    AI_Output(other,"Nim zdecydowaliśmy się zesłać go do Tartaru próbowaliśmy go naprostować przez wiele dziesiątek lat. Tak jak i ciebie.")
    AI_Output(other,"Trzeba przyznać że był sprytny. Zostawiał sobie wskazówki na późniejsze pętle. Za ostatnim razem gdy uciekł od swojego opiekuna bardzo trudno było go złapać.")
    AI_Output(PC_HERO,"Więc gdy zauważyliście że was rozgryzł zdecydowaliście się go zabić na zawsze. I to samo zrobicie teraz ze mną, tak? Niedoczekanie")
    AI_Output(other,"Synu. To jest już szósty raz gdy toczymy tą rozmowę.")


def DIA_Gravedigger_Truth_Antiochus_Condition():
    if "truth_prompt" in PC_HERO.flags:
        return 1

DIA_Gravedigger_Truth_Antiochus = include.DIALOGUE(
    npc_list.BDT_301_Gravedigger,
    DIA_Gravedigger_Truth_Antiochus_Info,
    DIA_Gravedigger_Truth_Antiochus_Condition,
    0,
    "Antiochus"
)

def DIA_Gravedigger_Truth_End_Info(other):
    AI_Output(PC_HERO,"Mam już dość twoich tłumaczeń")
    AI_Output(other,"W porządku")
    AI_Output(other,"Spokojnie, nie poczujesz żadnego bólu, dotknę po prostu twojego czoła i zakończe to wszystko")
    AI_Output(other,"[Grabarz wyciągnął rękę w twoim kierunku...]")
    if PC_HERO.str > 20:
        AI_Output(PC_HERO,"Nie. [Odpowiedziałeś i chwyciłeś jego ramie. Utkwiliście w starciu na zwykłą prymitywną siłę]")
        result = armwrestling.armwrestling(PC_HERO,other)
        if result == "SUCCESS":
            print("\nByć może Grabarz był wysłannikiem Hadesa. Możliwe że nawet jego aspektem. Jednak w tej formie nie był w stanie ci się oprzeć")
            print("Odepchnąłeś jego ramie i uderzyłeś z całej siły w twarz. Raz. I jeszcze raz. I kolejny raz. Wyglądało na to że spróbuje cie chwycić jeszcze raz.")
            print("Wtedy przypomniałeś sobie o swoim mieczu. Dobyłeś go z prędkością błyskawicy i odciąłeś wyciągniętą w twoim kierunku ręke")
            print("Grabarz upadł na ziemie. Dało ci to wystarczająco czasu. Udało ci się dobiec do wioski i złapać swojego konia")
            PC_HERO.flags.append("loop")
            leveling.give_exp(PC_HERO, 500)
            fight.kill(PC_HERO,1)
    else:
        PC_HERO.flags.append("loop")
        leveling.give_exp(PC_HERO, 200)
        fight.kill(PC_HERO,1)

def DIA_Gravedigger_Truth_End_Condition():
    if "truth_prompt" in PC_HERO.flags:
        return 1

DIA_Gravedigger_Truth_End = include.DIALOGUE(
    npc_list.BDT_301_Gravedigger,
    DIA_Gravedigger_Truth_End_Info,
    DIA_Gravedigger_Truth_End_Condition,
    0,
    "Kończmy to"
)
