import include
import item_list

mst_cerberus = include.NPC(
    "Cerber", # Name
    "monster", # Class
    20, # Level
    0, 100, # XP
    100,100, # HP
    15,15,0,0,0 # Attributes
)
mst_bloodhound = include.NPC(
    "Ogar", # Name
    "monster", # Class
    5, # Level
    0, 100, # XP
    75,75, # HP
    10,10,0,0,0 # Attributes
)
mst_lurker = include.NPC(
    "Topielec", # Name
    "monster", # Class
    3, # Level
    0, 100, # XP
    50,50, # HP
    10,10,0,0,0 # Attributes
)
mst_lurker.loot = [item_list.itmi_lurker_skin]
mst_shadowbeast = include.NPC(
    "Cieniostwór", # Name
    "monster", # Class
    15, # Level
    0, 100, # XP
    200,200, # HP
    20,20,0,0,0 # Attributes
)

LGN_legionnaire_1 = include.NPC(
    "Legionista", # Name
    "legion", # Class
    5, # Level
    0, 100, # XP
    50,50, # HP
    5,5,0,0,0 # Attributes
)
LGN_legionnaire_2 = include.NPC(
    "Legionista", # Name
    "legion", # Class
    5, # Level
    0, 100, # XP
    50,50, # HP
    10,10,0,0,0 # Attributes
)
LGN_legionnaire_3 = include.NPC(
    "Legionista", # Name
    "legion", # Class
    5, # Level
    0, 100, # XP
    50,50, # HP
    10,10,0,0,0 # Attributes
)
LGN_Centurion = include.NPC(
    "Centurion", # Name
    "legion", # Class
    20, # Level
    900, 1000, # XP
    500,500, # HP
    20,20,0,0,0 # Attributes
)