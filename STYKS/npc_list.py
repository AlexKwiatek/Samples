import include
import item_list

### Create example npc

PC_ANTIOCHUS = include.NPC(
    "Antiochus",
    "companion", # Class
    20, # Level
    1900, 2000, # XP
    1000,1000, # HP
    50,50,20,100,0 # Attributes
)
PC_ANTIOCHUS_Lantern = include.NPC(
    "Antiochus",
    "companion", # Class
    20, # Level
    1900, 2000, # XP
    1000,1000, # HP
    50,50,20,100,0 # Attributes
)
VLK_100_Boatmaker = include.NPC(
    "Szkutnik",
    "commoner", # Class
    3, # Level
    200, 300, # XP
    60,60, # HP
    10,10,0,0,0 # Attributes
)
BDT_308_Bandit = include.NPC(
    "Bandzior",
    "bandit", # Class
    5, # Level
    400, 500, # XP
    100,100, # HP
    15,15,0,0,0 # Attributes
)
BDT_308_Bandit.gold = 50
BDT_309_Bandit = include.NPC(
    "Pomocnik Bandziora",
    "bandit", # Class
    3, # Level
    200, 300, # XP
    50,50, # HP
    10,10,0,0,0 # Attributes
)
BDT_308_Bandit.gold = 50
VLK_104_Wiseman = include.NPC(
    "Mędrzec",
    "commoner", # Class
    1, # Level
    0, 100, # XP
    50,50, # HP
    5,5,0,0,0 # Attributes
)

# CHAPTER 3
VLK_101_Phrixos = include.NPC(
    "Phrixos",
    "commoner", # Class
    5, # Level
    200, 300, # XP
    120,120, # HP
    10,10,0,0,0 # Attributes
)
VLK_102_Blacksmith = include.NPC(
    "Kowal",
    "commoner", # Class
    4, # Level
    200, 300, # XP
    150,150, # HP
    40,0,0,0,0 # Attributes
)
VLK_103_Slave = include.NPC(
    "Głodny Niewolnik",
    "commoner", # Class
    1, # Level
    0, 100, # XP
    10,50, # HP
    5,5,0,0,0 # Attributes
)
BDT_300_Bastard = include.NPC(
    "Bękart z Koryntu",
    "bandit", # Class
    20, # Level
    1900, 2000, # XP
    500,500, # HP
    30,20,0,0,0 # Attributes
)
BDT_300_Bastard_Lantern = include.NPC( # Copy for final boss
    "Bękart z Koryntu",
    "bandit", # Class
    20, # Level
    1900, 2000, # XP
    500,500, # HP
    30,20,0,0,0 # Attributes
)
BDT_301_Gravedigger = include.NPC(
    "Grabarz",
    "bandit", # Class
    20, # Level
    1900, 2000, # XP
    500,500, # HP
    40,40,0,0,0 # Attributes
)
BDT_302_Keeper = include.NPC(
    "Latarnik",
    "bandit", # Class
    10, # Level
    900, 1000, # XP
    50,50, # HP
    10,10,40,0,0 # Attributes
)
BDT_303_Hunter = include.NPC(
    "Myśliwy",
    "bandit", # Class
    5, # Level
    400, 500, # XP
    200,200, # HP
    10,20,0,0,0 # Attributes
)
BDT_304_Vince = include.NPC(
    "Vince",
    "bandit", # Class
    5, # Level
    400, 500, # XP
    250,150, # HP
    30,10,0,0,0 # Attributes
)
BDT_305_Nico = include.NPC(
    "Nico",
    "bandit", # Class
    5, # Level
    400, 500, # XP
    250,150, # HP
    10,10,0,0,0 # Attributes
)
BDT_305_Nico.gold = 500
BDT_306_Fang = include.NPC(
    "Kieł",
    "bandit", # Class
    6, # Level
    500, 600, # XP
    250,250, # HP
    10,15,0,0,0 # Attributes
)
BDT_306_Fang.goods = [
    item_list.itke_lockpick,
    item_list.itke_lockpick,
    item_list.itke_lockpick,
    item_list.itke_lockpick,
    item_list.itar_bdt_l,
    item_list.itwp_sword_2,
    item_list.itfo_wine,
    item_list.itfo_wine,
    item_list.itfo_superwine,
    item_list.itfo_bread,
    item_list.itfo_bread,
    item_list.itfo_bread
]
BDT_307_Sly = include.NPC(
    "Zły",
    "bandit", # Class
    6, # Level
    500, 600, # XP
    250,250, # HP
    10,15,0,0,0 # Attributes
)

### CHAPTER 2
KDF_200_Seer = include.NPC(
    "Anthimos",
    "mage", # Class
    10, # Level
    200, 300, # XP
    200,200, # HP
    10,10,40,0,0 # Attributes
)
KDF_201_Oracle = include.NPC(
    "Wyrocznia",
    "mage", # Class
    50, # Level
    4900, 5000, # XP
    500,500, # HP
    10,10,30,30,0 # Attributes
)
KDF_202_Oracle_Voice = include.NPC(
    "Głos",
    "mage", # Class
    50, # Level
    4900, 5000, # XP
    500,500, # HP
    10,10,30,30,0 # Attributes
)
NOV_400_Gateguard = include.NPC(
    "Strażnik",
    "hoplite", # Class
    5, # Level
    400, 500, # XP
    100,100, # HP
    15,15,0,0,0 # Attributes
)
NOV_401_Acolyte = include.NPC(
    "Akolita",
    "mage", # Class
    1, # Level
    0, 100, # XP
    50,50, # HP
    5,5,5,0,0 # Attributes
)
NOV_402_Acolyte = include.NPC(
    "Akolita",
    "mage", # Class
    1, # Level
    0, 100, # XP
    50,50, # HP
    5,5,5,0,0 # Attributes
)
VLK_105_Fisherman = include.NPC(
    "Kupiec",
    "commoner", # Class
    1, # Level
    0, 100, # XP
    50,50, # HP
    5,5,0,0,0 # Attributes
)
VLK_105_Fisherman.goods = [
    item_list.itmi_bait,
    item_list.itmi_bait,
    item_list.itmi_bait,
    item_list.itmi_bait,
    item_list.itmi_bait,
    item_list.itmi_bait,
    item_list.itmi_bait,
    item_list.itmi_arrow,
    item_list.itmi_arrow,
    item_list.itmi_arrow,
    item_list.itmi_arrow,
    item_list.itmi_arrow,
    item_list.itmi_arrow,
    item_list.itmi_arrow
]
