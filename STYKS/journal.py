import include
from hero import PC_HERO

MQ01 = include.QUEST(
    "Ucieczka",
    10,
    "RUNNING",
    {
        "desc": """
Umarłem w bitwie pod Magnezją i wygląda na to że obudziłem się w zaświatach. Razem ze mną umarł książe Antiochus. 
Był przy mnie gdy zadano mi finalny cios. Być może to sprawiło że nasze dusze są teraz połączone. Mam szczęście że jest przy mnie.
Opowiedział mi on starą legende o Orfeuszu, Cerberze i wyjściu z piekła. Być może tu jest nasza szansa. Żeby to zrobić, musimy podążać śladami legend.
Nasz pierwszy przystanek to Wyrocznia Dusz. Jej siedziba znajduje się na widłach Styksu i jednego z jego dopływów. Potrzebujemy łódki albo promu by tam dopłynąć. 
Być może uda nam się dostać od niej informacje gdzie jest wyjście. O ile nie jest ono tylko legendą.
""",
        "10": "Zdobądź prom",
        "20": "Spotkaj się z Wyrocznią",
        "30": "Znajdź sposób na wejście do Latarni",
        "100": "REDACTED",
        "255": "SPOILERS"
    }
)
SQ_Boatmaker_01 = include.QUEST(
    "Klucz Szkutnika",
    0,
    "NONE",
    {
        "desc": """
Spotkałem Szkutnika na przyrzeczu. Być może będzie w stanie mi pomóc dopłynąć do Wyroczni.
Powiedział mi że jego wszystkie narzędzia i wiosła znajdują się w środku chaty, a klucz do niej zgubił w pijanym widzie w jaskini niedaleko.
Podobno uciekał tam przed jakimiś zwierzętami. Mówił że to może być Ogar albo Topielec.        
        """,
        "10": "Idź do Jaskini",
        "20": "Oddaj klucz Szkutnikowi",
        "100": "Oddałem klucz Szkutnikowi. Bardzo ucieszył się na jego widok",
        "255": "Zignorowałem prośby Szkutnika. Mam na głowie ważniejsze zadanie niż pijany starzec"
    }
)
SQ_Boatmaker_02 = include.QUEST(
    "Szemrane Typy",
    0,
    "NONE",
    {
        "desc": """
Szkutnik z Przyrzecza zgodził się mnie przetransportować do Świątyni, jeśli pomoge mu przepędzić dwóch bandytów kręcących się w okolicy       
        """,
        "10": "Porozmawiaj z Bandytami",
        "20": "Przekonałeś bandytów by odeszli, wróć do Szkutnika",
        "25": "Przepędziłeś bandytów siłą, wróć do Szkutnika",
        "30": "Zabiłeś bandytów, wróć do Szkutnika",
        "100": "Przekonałem bandytów by sobie poszli. Szkutnik był bardzo zadowolony",
        "101": "Zabiłem jednego z bandytów i pozwoliłem drugiemu uciec. Szkutnik był przerażony, ale nie wygląda jakby chciał złamać dane słowo",
        "102": "Zabiłem bandytów. Szkutnik był przerażony, ale nie wygląda jakby chciał złamać dane słowo",
        "255": "Zignorowałem prośby Szkutnika. Mam na głowie ważniejsze zadanie niż pijany starzec"
    }
)

MQ_Oracle = include.QUEST(
    "Wyrocznia",
    0,
    "NONE",
    {
        "desc": """
Dotarłem w końcu do kompleksu Świątyni. Nie mogę się jednak spotkać z Wyrocznią Zagubionych Dusz, gdyż jej zarządca, Anthimos, nie chce mnie wpuścić.
        """,
        "10": "Przekonaj Anthimosa by cie wpuścił",
        "50": "Zabiłeś Anthimosa. Czas spotkać się z Wyrocznią",
        "100": "Spotkałeś się z Wyrocznią. Jej przepowiednie trudno zrozumieć, ale jednak wyznaczyła ci cel. \nMusisz iść w strone trzech wyraźnie widocznych gór na wschodzie.\nTam znajdziesz Brame. 'Jednak klucz do niej znajduje się sześć stóp pod ziemią'. \nCokolwiek to znaczy.",
        "255": "Code Unreachable"
    }
)

SQ_Gatekeeper = include.QUEST(
    "Brama do Wyroczni",
    0,
    "NONE",
    {
        "desc": """
Dotarłem pod mury Świątyni, jednak odźwierny nie chce mnie wpuścić. Mówi że zarządca ma mnie ocenić sam a może to potrwać nawet i pare tygodni. 
Zdradził nam jednak że wpuszcza chłopów z żywnością. Gdybym zdobył ryby albo upolował dziczyzne...
        """,
        "10": "Zdobądź ryby, mięso albo przekonaj odźwiernego",
        "100": "Odźwierny wpuścił cie na teren świątyni.",
        "255": "Code Unreachable"
    }
)

SQ_Death_Within_Death = include.QUEST(
    "Śmierć po śmierci",
    0,
    "NONE",
    {
        "desc": """
Rozmawiając z Prixosem dowiedziałem się o tym co się dzieje gdy ktoś umrze w Hadesie. Mówił że umarli leżą jak martwi dopóki ktoś z żywych nie złoży za nich ofiary.
Mówił że ichni Cieśla jest jednym z ludzi których to spotkało. Mam wrażenie że powinienem porozmawiać z tym Cieślą.
        """,
        "10": "Porozmawiaj z Cieślą",
        "100": " PLACEHOLDER ",
        "255": "Kwestia śmierci po śmierci musi poczekać na następną śmierć. Dzisiaj planuje wyjść z Hadesu."
    }
)
MQ_Bastard = include.QUEST(
    "Bękart z Koryntu",
    0,
    "NONE",
    {
        "desc": """
Gdy dotarłem na Farme na Rozdrożu spotkałem tam mojego starego druha, Phrixosa. Wygląda na to że umarli którzy zapuszczą się w te okolice są łapani i zmuszani do niewolniczej pracy przez niejakiego Bękarta z Koryntu.
Pojmał Phrixosa i zabił moich przyjaciół - Apolodorusa i Nisosa. To wymaga krwi. Zanim wybiore gdzie pójść dalej, musze rozprawić się z tym Bękartem.
        """,
        "10": "Porozmawiaj z Grabarzem",
        "20": "Znajdź słabe ogniwo wśród ludzi Bękarta",
        "100": " PLACEHOLDER ",
        "255": "Kwestia śmierci po śmierci musi poczekać na następną śmierć. Dzisiaj planuje wyjść z Hadesu."
    }
)
SQ_Bastards_Man = include.QUEST(
    "Chłopak Bękarta",
    0,
    "NONE",
    {
        "desc": """
Bękart z Koryntu chce wynająć mnie do zabicia bestii atakującej chłopów. Nie wiem czy podjąć się tego zadania. Bękart obiecuje dobrą płace, a Cieniostwór atakuje więźniów...
        """,
        "10": "Zabij Cieniostwora",
        "20": "   ",
        "100": " PLACEHOLDER ",
        "255": "Kwestia śmierci po śmierci musi poczekać na następną śmierć. Dzisiaj planuje wyjść z Hadesu."
    }
)
SQ_Sly = include.QUEST(
    "Amulet Grabarza",
    0,
    "NONE",
    {
        "desc": """
Jeden z ludzi Bękarta chce mi zapłacić za ukradnięcie amuletu który trzyma w swoim domu Grabarz. Zły nie wydaje się być godnym zaufania człowiekiem, ale być może właśnie kogoś takiego potrzebuję?
        """,
        "10":"Włam się do chaty Grabarza",
        "20":"Ukradnij Amulet ",
        "30":"Oddaj Amulet Złemu",
        "100":"Oddałem Amulet Złemu",
        "254":"Doniosłem Grabarzowi o planie Złego. Podejrzewam że Bandyta nie będzie zadowolony.",
        "255":"Zdecydowałem że nie mam czasu bawić się w drobne kradzieże dla bandytów. Brama czeka na mnie."
    }
)

def setstage(quest,stage):
    quest.queststage = stage
    print("## Nowy wpis w dzienniku...")

def showjournal():
    include.printimportanttext("DZIENNIK")
    while True:
        print("Wybierz rozdział:")
        print("Aktywne")
        print("Zakończone")
        print("Zepsute")
        print("Glosariusz")
        running_set = ["aktywne","running"]
        completed_set = ["zakończone","completed"]
        failed_set = ["zepsute","failed"]
        glossary_set = ["glosariusz","glossary"]
        journal_dict = {
            "glosariusz":"glossary",
            "glossary":"glossary",
            "zepsute":"failed",
            "failed":"failed",
            "zakończone":"completed",
            "completed":"completed",
            "aktywne":"running",
            "running":"running"
        }

        command = input()
        if command.lower() in running_set or command.lower() in completed_set or command.lower() in failed_set or command.lower() in glossary_set:
            command = journal_dict[command.lower()]
            showjournal_book(command)
        elif command.lower() in include.back_set:
            break

def showjournal_book(book):
    if book == "running":
        include.printimportanttext("AKTYWNE")
    elif book == "completed":
        include.printimportanttext("ZAKOŃCZONE")
    elif book == "failed":
        include.printimportanttext("ZEPSUTE")
    elif book == "glossary":
        include.printimportanttext("GLOSARIUSZ")
    questpages = []
    questids = []
    for quest in include.QUEST.get_instances():
        if quest.status == book.upper():
            print(quest.name + " -- " + quest.get_current_objective())
            #print("-- " + quest.get_current_objective())
            questpages.append(quest.name)
            questids.append(quest)
            quest_zip = dict(zip(questpages,questids))

    while True:
       command = input("\nDla szczegółów, wpisz nazwe zadania. By wrócić wpisz POWRÓT ")
       if command in questpages:
           questpage = quest_zip[command]
           print(questpage.name)
           print(" ")
           print(questpage.get_quest_description())
           print("-- " + questpage.get_current_objective())
       if command.lower() in include.back_set:
           break


def B_Kapitelwechsel(chapter):
    PC_HERO.hp = PC_HERO.hp_max
    if chapter == 2:
        MQ01.queststage = 20
        if SQ_Boatmaker_01.status == "RUNNING":
            SQ_Boatmaker_01.status = "FAILED"
            SQ_Boatmaker_01.queststage = 255
    if chapter == 3:
        MQ01.queststage = 30