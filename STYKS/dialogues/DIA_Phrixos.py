import include
import npc_list
import journal
import item_list
import leveling
from hero import PC_HERO
from dialogue import AI_Output


def DIA_Phrixos_First_Hello(other):
    print("''Nie możesz uwierzyć swoim oczom. Minęło wiele czasu od twojej śmierci, ale do tej pory Książe Antiochus był jedyną znajomą ci twarzą. Do teraz. \nPhrixos zupełnie nie przypomina twojego przyjaciela, który stał obok ciebie w bitwie pod Magnezją. Wygląda bardzo mizernie, a z jego oczu bije zmęczenie.''\n")
    AI_Output(PC_HERO,"Phrixos! Druchu!")
    AI_Output(other,PC_HERO.name + "? Jesteś tutaj. Daleko zaszedłeś.")
    AI_Output(PC_HERO,"O czym mówisz Phrixos? Zresztą nieważne! Co się z tobą działo? Mam nadzieje że odpłaciłeś temu Rzymskiemu sukinsynowi z nawiązką!")
    AI_Output(other,"Rzyms... Tak... Zabiłem drania, nie martw się o to " + PC_HERO.name)
    AI_Output(PC_HERO,"To dobrze. Bałem się że będę musiał cie pomścić. Mam plan.")
    AI_Output(other,"Plan... tak...")
    print("''Nie umknęło twojej uwadze że Phrixos zdaje się dość nerwowo spoglądać na Antiochusa. Być może dopiero teraz dowiedział się o jego śmierci?''")
    other.dialogue_hello = DIA_Phrixos_Post_Hello

def DIA_Phrixos_Post_Hello(other):
    AI_Output(PC_HERO,"''Kalimera'' Phrixos")
    AI_Output(other,"''Kalimera'' " + PC_HERO.name)

npc_list.VLK_101_Phrixos.dialogue_hello = DIA_Phrixos_First_Hello


def DIA_Phrixos_Quest_Info(other):
    AI_Output(PC_HERO,"Nie spodziewałem się że zastane cie pracującego w polu. Gdzie się podział twój żołnierski duch?")
    AI_Output(other,"Cóż... wiele się zmieniło odkąd ostatnim razem się widzieliśmy")
    AI_Output(other,"Każdy z nas trafił do innego miejsca. Ja miałem pecha i natknąłem się na Bękarta z Koryntu")
    AI_Output(PC_HERO,"Skąd wiesz? Trafiłeś na reszte naszych towarzyszy? Gdzie oni są?")
    AI_Output(other,"Kilku było ze mną tu, na farmie. Apolodorus i Nisos. Wpadli w niełaske Bękarta. Grabarz powie ci, gdzie zakopał ich ciała.")
    journal.MQ_Bastard.status = "RUNNING"
    journal.MQ_Bastard.queststage = 10
    print("## Nowy wpis w dzienniku...")

def DIA_Phrixos_Quest_Condition():
    return 1

DIA_Phrixos_Quest = include.DIALOGUE(
    npc_list.VLK_101_Phrixos,
    DIA_Phrixos_Quest_Info,
    DIA_Phrixos_Quest_Condition,
    0,
    "Rola"
)

def DIA_Phrixos_Death_Info(other):
    AI_Output(PC_HERO,"Ciała? Phrixos, my jesteśmy już martwi. Nie da się nas bardziej zabić, czyż nie?")
    AI_Output(other,"To miejsce rządzi się swoimi prawami. W pewnym sensie jesteśmy nieśmiertelni, nie widziałem by czyjeś ciała gniły")
    AI_Output(other,"Lecz wciąż jeśli ktoś z nas zostanie 'zabity', jego ciało pada bez ruchu a oczy pozostają otwarte jak u nieboszczyka")
    AI_Output(other,"To nie jest nieodwracalne. Wystarczy że ktoś na górze o nas pamięta. Gdy złoży za nas ofiarę, wstajemy.")
    AI_Output(PC_HERO,"Ale skąd nasi bliscy mają wiedzieć o tym kto z nas padł? Co z tymi którzy zmarli dawno temu i ich bliscy mają swoje rodziny do opłakiwania?")
    AI_Output(other,"Wtedy zwłokami zajmuje się Grabarz.")
    AI_Output(PC_HERO,"Apolodorus i Nisos zmarli niedawno. Apo miał żone a Nisos dwóch braci. Dlaczego Grabarz zajął się nimi?")
    AI_Output(other,"Minie dość czasu nim ktoś się o nich upomni. A nawet jeśli to Bękart zabije ich znowu.")

def DIA_Phrixos_Death_Condition():
    if PC_HERO.npcknowsinfo(DIA_Phrixos_Quest):
        return 1
    else:
        return 0

DIA_Phrixos_Death = include.DIALOGUE(
    npc_list.VLK_101_Phrixos,
    DIA_Phrixos_Death_Info,
    DIA_Phrixos_Death_Condition,
    0,
    "Ciała?"
)


def DIA_Phrixos_Bastard_Info(other):
    AI_Output(PC_HERO,"Co to za jeden, ten 'Bękart'?")
    AI_Output(other,"Bękart z Koryntu. Zdaje się że za życia był najemnikiem. Walczył w wojnach Mithrydatesa po stronie naszych")
    AI_Output(PC_HERO,"Wojnach Mithrydatesa? Nie słyszałem o nich, to musiało być dawno temu")
    AI_Output(other,"Zasłynął wtedy szczególnym okrucieństwem a także sprawnością w walce. Teraz po śmierci umyślił sobie że będzie terroryzował nowych i zmuszał ich do pracy dla siebie")
    AI_Output(PC_HERO,"Podły typ. Nikt nie próbował mu się postawić? Było was trzech, trzech na jednego to dość by...")
    AI_Output(other,"Zabiliśmy go. Trzy razy.")
    AI_Output(PC_HERO,"Trzy razy?! Nie wiem co mnie bardziej dziwi. Że nie uciekliście, czy że ktoś trzy razy złożył ofiare za takiego łotra")
    AI_Output(other,"Mówią że jego kochanka wciąż żyje. Kapłanka Persefony.")
    print("''Phrixos pokazuje na wieże w na wzgórzu, koło farmy''")
    AI_Output(other,"Widzisz tą wieże? Za każdym razem gdy któryś z nas zbuntuje się przeciwko Bękartowi, Latarnik wysyła do niej wiadomość")

def DIA_Phrixos_Bastard_Condition():
    if PC_HERO.npcknowsinfo(DIA_Phrixos_Death):
        return 1
    else:
        return 0

DIA_Phrixos_Bastard = include.DIALOGUE(
    npc_list.VLK_101_Phrixos,
    DIA_Phrixos_Bastard_Info,
    DIA_Phrixos_Bastard_Condition,
    0,
    "Bękart"
)


def DIA_Phrixos_Lighthouse_Info(other):
    AI_Output(PC_HERO,"Kim jest Latarnik? To jakiś jego pomagier?")
    AI_Output(other,"Nie jestem pewien. Nie widujemy go zbyt często. Siedzi w wieży, na szczycie. Czasem ktoś z nas zostawia mu różne rzeczy w środku")
    AI_Output(other,"Na pewno musi być po jego stronie. Gdyby nie on, już dawno byśmy dopadli Bękarta. A jeśli nie my, to poprzedni więźniowie")
    AI_Output(PC_HERO,"Dlaczego nikt z was nie dopadł tego Latarnika? Brzmi prosto. Wyeliminuj Latarnika a dorwiesz Bękarta")
    AI_Output(other,"To nie takie proste. Zapasy zanosimy mu raz na tydzień, a i tak wpuszczają tam najwyżej jednego z nas. Jeśli w ogóle")
    AI_Output(other,"Właściwie, to to zadanie należy do Chłopaków Bękarta. Ale oni nie lubią ciężkiej pracy więc z reguły wysługują się nami")
    AI_Output(PC_HERO,"Jak rozumiem reszte czasu drzwi są zamknięte. Gdzie jest klucz?")
    AI_Output(other,"Nie wiemy. Ostatnim razem próbowaliśmy przeszukać kieszenie Bękarta gdy go powaliliśmy. Ale wstał i załatwił Nisosa")
    AI_Output(other,"Ale jestem pewien że gdyby nosił go przy sobie - znaleźlibysmy go")

def DIA_Phrixos_Lighthouse_Condition():
    if PC_HERO.npcknowsinfo(DIA_Phrixos_Bastard):
        return 1
    else:
        return 0


DIA_Phrixos_Lighthouse = include.DIALOGUE(
    npc_list.VLK_101_Phrixos,
    DIA_Phrixos_Lighthouse_Info,
    DIA_Phrixos_Lighthouse_Condition,
    0,
    "Latarnik"
)



def DIA_Phrixos_Gravedigger_Info(other):
    AI_Output(PC_HERO,"Kim jest Grabarz?")
    AI_Output(other,"Grabarz jest jednym z Chłopaków Bękarta. Z reguły trzyma się na uboczu. Nie należy do towarzyskich typów")
    AI_Output(other,"Ale nie mam nic do niego, nigdy nie widziałem by znęcał się nad którymś z nas. Albo zmuszał do pracy.")
    AI_Output(other,"Gdy Bękart kogoś zabije, to on dostaje zadanie by zakopać ciało. Nawet gdyby ktoś z nas wstał, ciężko byłoby mu wygrzebać się spod sześciu stóp ziemi i chyba o to właśnie chodzi")
    AI_Output(PC_HERO,"Gdzie znajde tego Grabarza?")
    AI_Output(other,"Powinien być przy grobach. Widzisz tamtą ścieżke? Ona prowadzi do zagajnika gdzie nas zakopują")

def DIA_Phrixos_Gravedigger_Condition():
    if PC_HERO.npcknowsinfo(DIA_Phrixos_Quest):
        return 1
    else:
        return 0


DIA_Phrixos_Gravedigger = include.DIALOGUE(
    npc_list.VLK_101_Phrixos,
    DIA_Phrixos_Gravedigger_Info,
    DIA_Phrixos_Gravedigger_Condition,
    0,
    "Grabarz"
)



def DIA_Phrixos_RezFriends_Info(other):
    AI_Output(PC_HERO,"Czy widziałeś by kiedyś wstał ktoś inny niż Bękart?")
    AI_Output(other,"Czasem słyszymy krzyki ze strony grobów. Z reguły szybko milkną. Pod ziemią nie ma zbyt wiele powietrza, nawet jeśli o kogoś z nas upominają się krewni, starcza to zaledwie na pare minut")
    AI_Output(PC_HERO,"Pare minut cierpienia.")
    AI_Output(other,"Pare razy Bękart potrzebował z powrotem kogoś kogo zdążył wcześniej zabić. Wtedy wysyłał Grabarza po ciało i dawał znać Latarnikowi")
    AI_Output(PC_HERO,"Ktoś taki jest tu teraz z nami?")
    AI_Output(other,"Cieśla. Właściwie to pomocnik Cieśli. Bękart go dopadł pare miesięcy temu za drobne kradzieże.")
    AI_Output(other,"Ale gdy stary Cieśla próbował zamordować Bękarta we śnie, potrzebowaliśmy nowego Cieśli")
    journal.SQ_Death_Within_Death.status = "RUNNING"
    journal.SQ_Death_Within_Death.queststage = 10
    print("## Nowy wpis w dzienniku...")

def DIA_Phrixos_RezFriends_Condition():
    if PC_HERO.npcknowsinfo(DIA_Phrixos_Lighthouse):
        return 1
    else:
        return 0


DIA_Phrixos_RezFriends = include.DIALOGUE(
    npc_list.VLK_101_Phrixos,
    DIA_Phrixos_RezFriends_Info,
    DIA_Phrixos_RezFriends_Condition,
    0,
    "Ożywianie"
)
