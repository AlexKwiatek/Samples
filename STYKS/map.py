import include


### CHAPTER 1
##################################################
LOC_RIVERSIDE = include.CELL(
    "Przyrzecze", "unlocked"
)
LOC_CAVE = include.CELL(
    "Jaskinia", "unlocked"
)

LOC_WAYSHRINE = include.CELL(
    "Kapliczka", "unlocked"
)
LOC_BOATMAKER = include.CELL(
    "Warsztat Szkutnika", "locked"
)
LOC_BOATMAKER.locked_reason = "Drzwi są zamknięte!"
LOC_GATE = include.CELL(
    "Furta", "unlocked"
)
LOC_HIGHWAY_CH1 = include.CELL(
    "Gościniec", "locked"
)
LOC_HIGHWAY_CH1.locked_reason = "To nie ma sensu. Na piechote podróż zajęłaby tygodnie albo i miesiące. Musisz zdobyć prom."
REGION_CHAPTER1 = include.REGION(
    "Górny Krąg", [LOC_WAYSHRINE,LOC_CAVE,LOC_RIVERSIDE,LOC_BOATMAKER,LOC_GATE]
)
LOC_RIVERSIDE.connected = ["loc_wayshrine","loc_cave","loc_boatmaker","loc_gate"]
LOC_CAVE.connected = ["loc_riverside"]
LOC_WAYSHRINE.connected = ["loc_riverside"]
LOC_BOATMAKER.connected = ["loc_riverside"]
LOC_GATE.connected = ["loc_riverside","loc_highway_ch1"]
LOC_HIGHWAY_CH1.connected = ["loc_gate"]



### CHAPTER 2
##################################################
LOC_PRIORY = include.CELL(
    "Świątynia", "unlocked"
)
LOC_PRIORY_BASEMENT = include.CELL(
    "Krypta", "unlocked"
)
LOC_PRIORY_BASEMENT.locked_reason = "Mithrydates is watching"
LOC_PRIORY_OUTSIDE = include.CELL(
    "Dziedziniec", "locked"
)
LOC_PRIORY_OUTSIDE.locked_reason = "Brama jest zamknięta. Może poproś strażnika o otwarcie?"
LOC_ORACLE = include.CELL(
    "Komnata", "locked"
)
LOC_ORACLE.locked_reason = "Anthimos obserwuje..."
LOC_PRIORY_GARDEN = include.CELL(
    "Ogród", "unlocked"
)
LOC_PRIORY_DOCK = include.CELL(
    "Wioska Rybacka", "unlocked"
)
LOC_PRIORY_GATE = include.CELL(
    "Bramy Świątyni", "unlocked"
)
LOC_PRIORY_WOOD = include.CELL(
    "Las","unlocked"
)
LOC_CHAPTER2_BOAT = include.CELL(
    "Prom", "unlocked"
)
REGION_CHAPTER2 = include.REGION(
    "Wyrocznia", [LOC_CHAPTER2_BOAT,LOC_PRIORY_DOCK,LOC_PRIORY_GATE,LOC_PRIORY_OUTSIDE,LOC_PRIORY_GARDEN,LOC_PRIORY,LOC_ORACLE,LOC_PRIORY_BASEMENT]
)
LOC_CHAPTER2_BOAT.connected = ["loc_priory_dock"] # Location disabled!!!
LOC_PRIORY_DOCK.connected = ["loc_priory_gate","loc_priory_wood"]
LOC_PRIORY_GATE.connected = ["loc_priory_outside","loc_priory_dock"]
LOC_PRIORY_OUTSIDE.connected = ["loc_priory_gate","loc_priory_garden","loc_priory"]
LOC_PRIORY_GARDEN.connected = ["loc_priory_outside"]
LOC_PRIORY.connected = ["loc_priory_outside","loc_priory_basement","loc_oracle"]
LOC_ORACLE.connected = ["loc_priory"]
LOC_PRIORY_BASEMENT.connected = ["loc_priory"]
LOC_PRIORY_WOOD.connected = ["loc_priory_dock"]

### CHAPTER 3
##################################################
LOC_UNBURIED = include.CELL(
    "Świeże Groby", "unlocked"
)
LOC_GRAVEDIGGER_HUT = include.CELL(
    "Chata Grabarza", "pickable"
)
LOC_GRAVEDIGGER_HUT.locked_reason = "Potrzebujesz wytrycha albo klucza"
LOC_GRAVEDIGGER_HUT.combination = "LLPLP"
LOC_FRESH_GRAVES = include.CELL(
    "Stare Groby", "unlocked"
)
LOC_TOWER = include.CELL(
    "Latarnia", "locked"
)
LOC_TOWER.locked_reason = "Drzwi są zamknięte!"
LOC_FARM = include.CELL(
    "Wioska", "unlocked"
)
LOC_FARM_ALLEY = include.CELL(
    "Alejka", "unlocked"
)
LOC_BASTARDS_HOME = include.CELL(
    "Dom Bękarta", "unlocked"
)
LOC_FARM_WOOD = include.CELL(
    "Zaniedbany Las", "unlocked"
)

REGION_CHAPTER3 = include.REGION(
    "Field of Unburied", [LOC_UNBURIED,LOC_GRAVEDIGGER_HUT,LOC_FRESH_GRAVES,LOC_TOWER,LOC_FARM,LOC_BASTARDS_HOME]
)
LOC_UNBURIED.connected = ["loc_farm","loc_fresh_graves","loc_farm_alley"]
LOC_GRAVEDIGGER_HUT.connected = ["loc_farm"]
LOC_FARM.connected = ["loc_gravedigger_hut","loc_unburied","loc_bastards_home","loc_farm_wood","loc_farm_alley"]
LOC_TOWER.connected = ["loc_farm_alley"]
LOC_FRESH_GRAVES.connected = ["loc_unburied"]
LOC_BASTARDS_HOME.connected = ["loc_farm","loc_farm_alley"]
LOC_FARM_WOOD.connected = ["loc_farm"]
LOC_FARM_ALLEY.connected = ["loc_farm","loc_unburied","loc_bastards_home","loc_tower"]


loc_objects_dict = {
    "loc_riverside":LOC_RIVERSIDE,
    "loc_cave":LOC_CAVE,
    "loc_wayshrine":LOC_WAYSHRINE,
    "loc_boatmaker":LOC_BOATMAKER,
    "loc_gate":LOC_GATE,
    "loc_highway_ch1":LOC_HIGHWAY_CH1,
    "loc_priory":LOC_PRIORY,
    "loc_priory_basement":LOC_PRIORY_BASEMENT,
    "loc_priory_outside":LOC_PRIORY_OUTSIDE,
    "loc_oracle":LOC_ORACLE,
    "loc_priory_garden":LOC_PRIORY_GARDEN,
    "loc_priory_dock":LOC_PRIORY_DOCK,
    "loc_priory_gate":LOC_PRIORY_GATE,
    "loc_priory_wood":LOC_PRIORY_WOOD,
    "loc_chapter2_boat":LOC_CHAPTER2_BOAT,
    "loc_unburied":LOC_UNBURIED,
    "loc_gravedigger_hut":LOC_GRAVEDIGGER_HUT,
    "loc_fresh_graves":LOC_FRESH_GRAVES,
    "loc_tower":LOC_TOWER,
    "loc_farm":LOC_FARM,
    "loc_farm_alley":LOC_FARM_ALLEY,
    "loc_bastards_home":LOC_BASTARDS_HOME,
    "loc_farm_wood":LOC_FARM_WOOD
}