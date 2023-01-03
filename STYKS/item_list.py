import include
import journal

itke_lockpick = include.ITEM(
    "Wytrych",
    "key",
    "Używany do otwierania zamków"
)
itke_lockpick.value = 10

itmi_bait = include.ITEM(
    "Przynęta",
    "miscelanous",
    "Używana do łowienia ryb"
)
itmi_bait.value = 5

itmi_arrow = include.ITEM(
    "Strzała",
    "miscelanous",
    "Używana do polowania"
)
itmi_arrow.value = 5

## Boatmaker's Key
itke_boatmaker_key = include.ITEM(
    "Klucz do chaty Szkutnika",
    "key",
    "Prosty żelazny klucz"
)
itke_boatmaker_key.id = "itke_boatmaker_key"
def itke_boatmaker_key_effect():
    if journal.SQ_Boatmaker_01.status == "RUNNING":
        journal.SQ_Boatmaker_01.queststage = 20
        print("## Nowy wpis w dzienniku...")

itke_boatmaker_key.effect = itke_boatmaker_key_effect

## Loot
itmi_lurker_skin = include.ITEM(
    "Skóra Topielca",
    "miscelanous",
    "Solidna skóra, bylyby z niej dobre buty!"
)
itmi_lurker_skin.value = 25


## Lighhouse Key
itke_lighthouse_key = include.ITEM(
    "Klucz do Wieży Latarnika",
    "key",
    "Zdobiony złoty kluczyk"
)
itke_lighthouse_key.id = "itke_lighthouse_key"

## Gravedigger's Pendant
itmi_gravedigger_pendant = include.ITEM(
    "Amulet Grabarza",
    "miscelanous",
    "Złoty amulet pełen różnych ozdób i wyrytych bardzo cienkim rylcem napisów. W jego centrum znajduje się ogromny krwisty rubin.\nWygląda jakby pulsował delikatnym światłem. Wyryte napisy mówią: 'HADES NHEK THANATOS MORKUL'"
)
def itmi_gravedigger_pendant_effect():
    if journal.SQ_Sly.status == "RUNNING":
        journal.SQ_Sly.queststage = 30
        print("## Nowy wpis w dzienniku...")

itmi_gravedigger_pendant.effect = itmi_gravedigger_pendant_effect

###
### ### FOOD
###
itfo_booze = include.ITEM(
    "Wódka",
    "food",
    "Brzydko pachnie, fujka"
)
def itfo_booze_effect():
    if journal.SQ_Boatmaker_01.status == "RUNNING":
        journal.SQ_Boatmaker_01.queststage = 20
        print("## Nowy wpis w dzienniku...")

itfo_booze.value = 10
itfo_booze.effect = itfo_booze_effect

# # #
itfo_wine = include.ITEM(
    "Wino",
    "food",
    "Nasz grecki napój, pyszny w smaku"
)
def itfo_wine_eateffect(character,item):
    character.hp += 10
    if character.hp > character.hp_max:
        character.hp = character.hp_max
    character.inventory.remove(item)

itfo_wine.value = 15
itfo_wine.eateffect = itfo_wine_eateffect

# # #
itfo_superwine = include.ITEM(
    "Wino Rossosa",
    "food",
    "Słynne na cały hellenistyczny świat wino z winnicy której założycielem był legendarny Karzeł Rossus. Niebywale pyszne."
)
def itfo_superwine_eateffect(character,item):
    character.hp += 50
    if character.hp > character.hp_max:
        character.hp = character.hp_max
    character.inventory.remove(item)

itfo_superwine.value = 50
itfo_superwine.eateffect = itfo_superwine_eateffect

# # #
itfo_bread = include.ITEM(
    "Chleb",
    "food",
    "Podstawa żywienia."
)
def itfo_bread_eateffect(character,item):
    character.hp += 5
    if character.hp > character.hp_max:
        character.hp = character.hp_max
    character.inventory.remove(item)

itfo_bread.value = 5
itfo_bread.eateffect = itfo_bread_eateffect

# # #
itfo_wurst = include.ITEM(
    "Kiełbasa",
    "food",
    "Pyszna kiełbasa z barana"
)
def itfo_wurst_eateffect(character,item):
    character.hp += 5
    if character.hp > character.hp_max:
        character.hp = character.hp_max
    character.inventory.remove(item)

itfo_wurst.value = 5
itfo_wurst.eateffect = itfo_wurst_eateffect

# # #
itfo_fish = include.ITEM(
    "Ryba",
    "food",
    "Ryby ze Styksu wyglądają... niepokojąco. Jest zupełnie ślepa, nie ma oczu i wygląda na zdeformowaną.\nNiedobrze ci na myśl że mógłbyś tu zostać na zawsze i musieć to jeść"
)
def itfo_fish_eateffect(character,item):
    character.hp += 10
    if character.hp > character.hp_max:
        character.hp = character.hp_max
    character.inventory.remove(item)

itfo_fish.value = 5
itfo_fish.eateffect = itfo_fish_eateffect

# # #
itfo_venison = include.ITEM(
    "Dziczyzna",
    "food",
    "Fani legendy o dumnym jeleniu Bambusionie byliby bardzo smutni widząc co zrobiłeś"
)
def itfo_venison_eateffect(character,item):
    character.hp += 20
    if character.hp > character.hp_max:
        character.hp = character.hp_max
    character.inventory.remove(item)

itfo_venison.value = 5
itfo_venison.eateffect = itfo_venison_eateffect




###
### ### QUEST ITEMS
###
itmi_oars = include.ITEM(
    "Wiosło",
    "miscelanous",
    "Długi kij służący do odpychania promu. Nie wiesz do końca czy to nazywa się wiosło ale pochodzisz z Anatolii, tam nie ma promów."
)
itmi_bastard_amulet = include.ITEM(
    "Wisiorek",
    "miscelanous",
    "Mały amulecik z napisem Alexis"
)
### LETTERS
itwr_antiochus_letter = include.ITEM(
    "Pergamin",
    "book",
    "Stary pergamin który był zakopany w ziemii w ogrodzie Wyroczni"
)
def itwr_antiochus_letter_eateffect(character,item):
    print("Próbuję się z tobą skontaktować. Tak, z tobą. To trudniejsze niż myślisz.")
    print("Nie ufaj synowi Filipa. Macedończyk nie istnieje, już dawno został strącony do Tartaru")
    print("To nie jest on")
    print("Srebro rani czarnoksięznika")
    input()

itwr_antiochus_letter.eateffect = itwr_antiochus_letter_eateffect


### WEAPONS
itwp_sword_0 = include.ITEM(
    "Nóż na Wilki",
    "weapon",
    "Twój stary wysłużony nożyk"
)
itwp_sword_0.dmg = 5
itwp_sword_0.value = 25

itwp_sword_1 = include.ITEM(
    "Krótki Miecz",
    "weapon",
    "Krótkie żelazne ostrze"
)
itwp_sword_1.dmg = 10
itwp_sword_1.value = 50

itwp_sword_2 = include.ITEM(
    "Khopesh",
    "weapon",
    "Wygięty miecz którym walczą niektórzy wojowniczy Ptolemeuszy. Cenna i zabójcza broń."
)
itwp_sword_2.dmg = 15
itwp_sword_2.value = 50

itwp_sword_silver = include.ITEM(
    "Srebrny Miecz",
    "weapon",
    "Srebrna broń raczej nie ma sensu do zastosowania w zwykłej walce. Wygląda na to że miecz jest czysto paradny"
)
itwp_sword_silver.dmg = 1
itwp_sword_silver.value = 200

itar_grd_l = include.ITEM(
    "Zniszczona Zbroja",
    "armor",
    "Twoja stara dobra zbroja"
)
itar_grd_l.armor = 5
itar_grd_l.value = 50

itar_bdt_l = include.ITEM(
    "Lekka Zbroja Bandyty",
    "armor",
    "Lekka zbroja bandytów Bękarta z Koryntu"
)
itar_bdt_l.armor = 20
itar_bdt_l.value = 150