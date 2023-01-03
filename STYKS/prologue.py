import include
import enemy_list
import fight
from hero import PC_HERO
from dialogue import AI_Output
from npc_list import PC_ANTIOCHUS

## Spoilery, lore primery:
# Protag: ugrzązł w pętli, bo za każdym razem jest bezwzględny i krzywdzi innych by dostać się do Bramy
# Bękart: był w pętli 50 lat, za ostatnim razem zaczął czuć że coś jest nie tak i zamiast dotrzeć do Bramy zoorganizował swoją osade blisko Bramy i odmawia ruszenia się dalej
# Antiochus Młodszy: ugrzązł w pętli, ale zostawiał sobie wskazówki, za ostatnim razem udało mu się uciec od swojego Opiekuna. Dotarł do osady Bękarta ale Opiekun Bękarta przekonał go by zabić Antiochusa
# Opiekun Bękarta: Grabarz
# Opiekun Antiochusa: Alexander Macedoński
# Opiekun Protaga: fAntiochus
# Obole: każdy zmarły idzie do piekła z jednym obolem który trafia do Charona. Później Charon puszcza je w rynek.
# Alexis: TODO, zdecyduj czy jest już bardzo stara czy już nie żyje i to Grabarz wysyła te pergaminy

# TODO: redo writing
def prologue_cutscene(hero):
    while True:
        print(" ")
        print("### 143 lata po bitwie pod Issos ###")
        print("############# Magnezja #############")

        print("Antiochus rzucił jeszcze jedno spojrzenie na swoich żołnierzy i krzyknął")
        print("'HERAKLES Z NAMI!'")
        input(" ")
        print("Dowódcy zgromadzonych falang krzyknęli komende i wszyscy hoplici prawie jednocześnie zbili swoje tarcze i opuścili włócznie")
        print("Zgromadzone wojska przypominały piękny kwiat z kolcami na czubkach włóczni. Zagrzmiały trąby i żołnierze regularnym krokiem ruszyli")
        print("Naprzeciwko was stały wojska Rzymian. Dużo mniej liczne, wiesz jednak że ci żołnierze żeby dotrzeć tutaj musieli przejść po trupach Antygonidów")
        print("Antygonidzi zawsze byli słabi. Dziś pod dowództwem waszego króla i księcia Rzymianie przekonają się kto jest prawdziwym dziedzicem Alexandra")
        input()
        print("W końcu zbliżyliście się na odległość rzutu włóczni. Rzymski pillum przeleciał tuż obok twojej głowy. Drugi ugrzązł w tarczy żołnierza po twojej lewej")
        print("Dwie ściany tarcz zderzyły się ze sobą. Przez moment wyglądało to jak patowa sytuacja. Dwie ogromne chmary ludzi napierające na siebie z całej siły")
        print("Nie trwało to jednak wiecznie. Gdy pierwsi ludzi zaczęli umierać, szeregi przerzedziły się. Dobyłeś ostrza.")
        print("Przykułeś swoją uwage do jednego z Legionistów. Stanęliście naprzeciwko siebie, miecze w dłoniach")
        input("NIKE!")
        fightresult = fight.startfight(hero, enemy_list.LGN_legionnaire_1)
        if fightresult == "FAILURE":
            break
        if fightresult == "SUCESS":
            pass
        print("Ocierasz swój miecz z krwi o tunike zabitego przeciwnika. To dobry dzień. Atena musi spoglądać na was łaskawie.")
        print("W czasie gdy walczyłeś szeregi rozluźniły się jeszcze bardziej. Być może Rzymianie ustępują pola?")
        print("Rozglądasz się dookoła siebie. Wygląda jednak jakby to twoje szeregi odeszły pare kroków w tył. \nCo się stało? Czy opuścił ich zapał do walki?")
        print("Nie masz czasu się zastanawiać. \nTym razem było ich dwóch. Lysy rzymianin, który zgubił gdzieś hełm, i drugi, z wyrazem furii na twarzy")
        input()
        print("Nim zdążyli cię jednak dopaść, Antiochus natarł konno na jednego z nich i odepchnął włócznią drugiego")
        print("'Orientuj się " + hero.name + "!' krzyknął")
        print("Podnosisz pillum upadłego żołnierza i rzucasz nim w nadchodzącego legioniste")
        print("Ten jednak zrobił unik. Znaleźliście się w zasięgu mieczy")
        input("'HERAKLES!'")
        fightresult = fight.startfight(hero, enemy_list.LGN_legionnaire_2)
        if fightresult == "FAILURE":
            break
        if fightresult == "SUCESS":
            pass
        print("Czujesz ogłuszające zmęczenie dwóch poprzednich walk. Zbroja zaczyna ci ciążyć. Kątem oka zauważasz twojego dowódce")
        print("Antiochus musiał zejść z konia, albo został z niego zrzucony. \nWalczył pieszo, razem z dwójką Towarzyszy przeciwko kilku legionistów.")
        print("Nagle uderza cie myśl 'Gdzie są wszyscy jeźdźcy?'. Jedyne konie jakie były wokół ciebie są martwe. Nagle uderzyło cię")
        print("Przegrywamy.")
        print("Nie masz czasu przyjrzeć się oddalającemu się tumanowi kurzu. \nNie masz czasu by rozpoznać czy to uciekająca z pola bitwy jazda, czy po prostu twój zmęczony wzrok odmawia posłuszeństwa")
        print("Nagle czujesz coś przy swoich plecach. Grupa żołnierzy Antiochusa cofając się, znalazła się już przy tobie. \nNie masz czasu myśleć. Kolejny żołnierz Scypiona znalazł się przed tobą")
        input("'N... NIKEEE!!!'")
        fightresult = fight.startfight(hero, enemy_list.LGN_legionnaire_3)
        if fightresult == "FAILURE":
            break
        if fightresult == "SUCESS":
            pass
        print("Ciało legionisty leży pod twoimi stopami. Szukasz wzrokiem swojego dowódcy i reszty szeregów. \nMoże uda wam się jakoś wydostać z tego piekła. Gdzieś muszą być rezerwy, może któraś flanka dalej się trzyma, to niemożliwe byście przegrali")
        print("Myśli przerywa coś ciężkiego upadającego na twoje ramie. To twój dowódca, Antiochus Młodszy Seleucyd. Ranny. \nPróbuje coś do ciebie powiedzieć, coś co brzmi bardzo podobnie do 'Uważaj!'")
        input()
        print("Gdy dostrzegasz kąte oka błysk gladiusa, wiesz co miał na myśli.")
        print("Żołnierz który zamachnął się w twoim kierunku, chybił o włos. Nosił on wyraźnie odznaczający się piuropusz centuriona")
        print("Gdy dołączałeś do armii w obozie krążyły plotki o tym jak funkcjonuje armia rzymska. \nNajwięksi i najbardziej brutalni żołnierze dostają komende nad 80 towarzyszami i prowadzą ich do bitwy")
        print("To musi być jeden z nich. Bydlak miał co najmniej 6 stóp wzrostu i ponad dwa cetnary wagi. Bierzesz wdech w oczekiwaniu na walke.")
        input("Nike.")
        fightresult = fight.startfight(hero, enemy_list.LGN_Centurion)
        if fightresult == "FAILURE":
            break
        if fightresult == "SUCESS":
            pass
        print("Trudno jest ci w to uwierzyć, ale wygląda na to że bogowie nie pozwolą ci dzisiaj umrzeć. \nOlbrzymi żołnierz padł martwy obok ciebie a jego legioniści cofnęli się o krok")
        print("Wstajesz opierając się na swoim mieczu. Może uda ci się wykorzystać ten moment.")
        print("Pillum który uderzył cie w czoło był ostatnią rzeczą jaką zobaczyłeś")
        break
    #input()
    print("Ciemność.")
    print("Budzisz się. Dookoła ciebie panuje lekki półmrok. Czyżbyś był w jakiejś jaskini? Ale... jak przeżyłeś bitwe? \nOstatni cios wyglądał jakby na pewno miał cie wykończyć")
    print("Niedaleko, koło promyka światła wydostającego się nieśmiało z sufitu siedzi znajoma sylwetka.")
    AI_Output(PC_ANTIOCHUS,"Hej, nareszcie sie obudziłeś")
    AI_Output(PC_HERO,"Co... gdzie ja jestem?")
    AI_Output(PC_ANTIOCHUS,"Wygląda na to że w zaświatach")
    AI_Output(PC_HERO,"Co, jak to? Mus... wasza miłość musi żartować, prawda?")
    AI_Output(PC_ANTIOCHUS,"Darujmy sobie konwenanse. Wygląda na to że w tym miejscu wszyscy jesteśmy równi, więc możesz mi mówić po imieniu")
    input()
    print("\nNie tak wyobrażałeś sobie królestwo Hadesa. W tym momenie jesteście w jaskini, ale na zewnątrz wygląda jak prawie normalny świat")
    print("Prawie. Niebo przesłaniaja gęste chmury, jak w ciemny burzowy dzień a rzeka wygląda jakby była wypełniona czarnym atramentem\n")
    AI_Output(PC_HERO,"Ile czasu minęło zanim się obudziłem?")
    AI_Output(PC_ANTIOCHUS,"Nie wiem. Sam obudziłem się w tej jaskini więc obaj nie mamy pojęcia ile czasu minęło nim ja się obudziłem.")
    AI_Output(PC_ANTIOCHUS,"Ale zdążyłem rozejrzeć się po okolicy. Wiem gdzie jesteśmy.")
    AI_Output(PC_HERO,"Tak, jak rozumiem jesteśmy w królestwie Hadesa...")
    AI_Output(PC_ANTIOCHUS,"Nie. Mam na myśli gdzie dokładnie jesteśmy. Widzisz tą kapliczkę na zewnątrz?")
    AI_Output(PC_ANTIOCHUS,"To Kapliczka Styenu. Dopływu Styksu. Powiedz mi znasz legende o Orfeuszu i Eurydyce?")
    AI_Output(PC_HERO,"Orfeusz wszedł w zaświaty po swoją ukochaną.")
    AI_Output(PC_HERO,"Hades pozwolił mu wyjść z nią pod warunkiem że nie będzie na nią patrzeć podczas dopóki nie dotrą do wyjścia")
    AI_Output(PC_ANTIOCHUS,"Kiedyś na dwór mojego ojca przyszła trójka wędrownych starców. Opowiedzieli mi tą historie, ze szczegółami.")
    AI_Output(PC_ANTIOCHUS,"Opowiedzieli mi wiele szczegółów dotyczących tego miejsca. Opowiedzieli mi o żyjących tu stworzeniach, nakreślili pare map...")
    AI_Output(PC_ANTIOCHUS,"Gdy pytałem się ich skąd mają tyle wiedzy o tej historii zbywali mnie najuprzejmiej jak potrafili.")
    AI_Output(PC_HERO,"Z całym szacunkiem, ale życie nauczyło mnie by nie wierzyć we wszystkie baśnie które opowiadają nam do...")
    AI_Output(PC_ANTIOCHUS,"Nie rozumiesz. Kiedy spałeś rozejrzałem się po tym miejscu. Wszystko co mówili się zgadza. Co do jednego szczegółu.")
    AI_Output(PC_HERO,"Chcesz powiedzieć mi że...")
    AI_Output(PC_ANTIOCHUS,"Oni tu byli.")
    input()
    AI_Output(PC_HERO,"Błagam, powiedz mi że pamiętasz gdzie...")
    AI_Output(PC_ANTIOCHUS,"To nie takie proste. Nigdy nie powiedzieli mi gdzie jest wyjście. Ale opisali mi kilka znaczących miejsc.")
    AI_Output(PC_ANTIOCHUS,"Mówili o wyroczni która zna odpowiedź na każde pytanie. Która jest związana paktem by odpowiedzieć każdemu na jego pytanie")
    AI_Output(PC_ANTIOCHUS,"I mówili gdzie jest jej siedziba. W miejscu w którym Styen wpływa do Styksu.")
    AI_Output(PC_ANTIOCHUS,"Nie zamierzam zostawić mojego ojca i mojego ludu na pastwe Rzymian. Wyjdziemy stąd " + PC_HERO.name)
    AI_Output(PC_ANTIOCHUS,"A gdy wyjdziemy, zbierzemy armie i wyzwolimy nasz kraj.")
    AI_Output(PC_HERO,"Dwójka ludzi którzy przezwyciężyli śmierć... to potężny przekaz. Jestem z tobą Książe")
    AI_Output(PC_ANTIOCHUS,"Ruszajmy")
